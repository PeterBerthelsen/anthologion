"""
Anthologion API — Liturgical service variable resolver.

Returns JSON or HTML for any date, sourced entirely from
pre-extracted JSON data. No PDF reads, no database.

Usage:
    python3 api.py                          # runs on port 5000
    PORT=8080 python3 api.py                # custom port

Endpoints:
    GET /api/resolve?m=2&d=26&y=2026
        Full liturgical context for a date.

    GET /api/resolve?m=2&d=26&y=2026&service=vespers
        Merged variables for a specific service type.

    GET /api/paschalion?m=2&d=26&y=2026
        Just the paschalion (liturgical calendar) data.

    GET /health
        Health check.

Query parameters (all optional — defaults to today):
    m         Month (1-12)
    d         Day (1-31)
    y         Year
    service   Filter to one service: vespers, matins, liturgy, compline, etc.
    calendar  0 = new calendar, 1 = old calendar (default)
    rank      Override feast rank (1-7). 7 = simple service (octoechos only).
    menaion   Menaion source: 'general' (default), 'full' (not yet available),
              'none' (skip menaion — same effect as rank=7 for menaion)
    format    Output format: 'json' (default), 'html', 'epub', 'pdf'
    scope     For epub/pdf: 'day' (default) or 'month'
"""

import os
from datetime import datetime, date, timedelta
from flask import Flask, request, jsonify, Response
from jinja2 import Environment, FileSystemLoader
from resolver import resolve, resolve_service, paschalion, RANK_NAMES

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

# Jinja env for HTML rendering (independent of Flask templates)
_jinja = Environment(
    loader=FileSystemLoader(os.path.join(BASE_DIR, 'static', 'html')),
    autoescape=False,
)

# Template map: service type → template file
_TEMPLATES = {
    'vespers': 'vespers.html',
    'matins': 'matins.html',
    'compline': 'smallCompline.html',
    'nocturns': 'nocturns.html',
    'typika': 'typika.html',
    'first_hour': 'first.html',
    'third_hour': 'third.html',
    'sixth_hour': 'sixth.html',
    'ninth_hour': 'ninth.html',
}


def _parse_date(args):
    """Extract month/day/year from request args, defaulting to today."""
    today = datetime.today()
    m = args.get('m', today.month, type=int)
    d = args.get('d', today.day, type=int)
    y = args.get('y', today.year, type=int)
    return m, d, y


def _parse_options(args):
    """Extract rank, menaion, format options from request args."""
    rank = args.get('rank', None, type=int)
    if rank is not None and not (1 <= rank <= 7):
        rank = None
    menaion_source = args.get('menaion', 'general')
    if menaion_source not in ('general', 'full', 'none'):
        menaion_source = 'general'
    fmt = args.get('format', 'json')
    if fmt not in ('json', 'html', 'epub', 'pdf'):
        fmt = 'json'
    return rank, menaion_source, fmt


def _serialize(obj):
    """Make an object JSON-safe (handle datetime, date, etc.)."""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    if isinstance(obj, dict):
        return {k: _serialize(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_serialize(i) for i in obj]
    return obj


# ---------------------------------------------------------------------------
# HTML rendering helpers
# ---------------------------------------------------------------------------
def _render_html(service_type, variables, ctx):
    """Render a service to HTML using the existing Jinja templates."""
    from hymns import vespers_prokeimena
    from kathisma import parse_kathisma

    KATHISMA_RUBRIC = {
        0: [0, 17, [4, 5]],   1: [6, 17, [7, 8]],
        2: [9, 17, [10, 11]], 3: [12, 17, [13, 14]],
        4: [15, 17, [19, 20]], 5: [18, 9, [16, 17]],
        6: [1, None, [2, 3]],
    }

    weekday = ctx['weekday']
    service_date = date.fromisoformat(ctx['date'])
    calendar = 1  # default, could be passed through ctx
    link_date = service_date.strftime('%m%d%Y')

    # Date strings
    if calendar == 1:
        night = service_date - timedelta(days=1)
        night_oc = night - timedelta(days=13)
        night_str = night.strftime('%m/%d/%Y') + ' (' + night_oc.strftime('%m/%d/%Y') + ')'
        date_oc = service_date - timedelta(days=13)
        day_str = service_date.strftime('%m/%d/%Y') + ' (' + date_oc.strftime('%m/%d/%Y') + ')'
    else:
        night_str = (service_date - timedelta(days=1)).strftime('%m/%d/%Y')
        day_str = service_date.strftime('%m/%d/%Y')

    feast = ctx.get('feast')
    name = feast['service_name'] if feast else None
    long_name = feast['long_name'] if feast else None
    tone = (ctx.get('liturgical') or {}).get('weekly_tone')

    vs = dict(variables)  # copy so we don't mutate

    tmpl_file = _TEMPLATES.get(service_type)
    if not tmpl_file:
        return f'<p>No template available for service type: {service_type}</p>'

    # Add template-expected metadata per service type
    vs['link'] = f'{link_date}-{service_type}'

    if service_type == 'vespers':
        vs['night_date'] = night_str
        vs['vespers_kathisma'] = parse_kathisma(KATHISMA_RUBRIC[weekday][0])
        vs.setdefault('prokeimenon', vespers_prokeimena(weekday))
        # Ensure stichera is a list
        stichera = vs.get('stichera', [])
        if isinstance(stichera, str):
            stichera = [stichera]
        vs['stichera'] = stichera

    elif service_type == 'matins':
        vs['date'] = day_str
        vs['kathisma1'] = parse_kathisma(KATHISMA_RUBRIC[weekday][2][0])
        vs['kathisma2'] = parse_kathisma(KATHISMA_RUBRIC[weekday][2][1])

    elif service_type == 'nocturns':
        vs['date'] = day_str
        kath = KATHISMA_RUBRIC[weekday][1]
        vs['kathisma'] = parse_kathisma(kath) if kath else {}

    elif service_type == 'compline':
        vs['night_date'] = night_str

    # Fill missing keys templates might reference
    for key in ['doxastichon', 'theotokion', 'readings', 'aposticha',
                'aposticha_theotokion', 'apolytichion', 'troparion',
                'exapostilarion', 'praises', 'canon', 'after50',
                'prokeimenon', 'session1', 'session2', 'session3']:
        vs.setdefault(key, '')

    template = _jinja.get_template(tmpl_file)
    return template.render(
        variables=vs,
        weekday=weekday,
        tone=tone,
        rank=ctx.get('rank', 7),
        name=name,
        long_name=long_name,
        service_type=(feast or {}).get('service_type'),
    )


def _wrap_html(body, ctx, service_type):
    """Wrap rendered service HTML in a full page."""
    feast = ctx.get('feast')
    tone = (ctx.get('liturgical') or {}).get('weekly_tone')
    return f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{service_type.title()} — {ctx['date']} ({ctx['weekday_name']})</title>
  <style>
    body {{ font-family: 'Palatino Linotype', Georgia, serif; max-width: 800px;
           margin: 40px auto; padding: 0 20px; line-height: 1.6;
           background: #FFFEF5; color: #2C1810; }}
    h1 {{ color: #8B0000; }} h2 {{ color: #4a4a4a; }} h3, h4 {{ color: #666; }}
    .note {{ color: #888; font-style: italic; }}
    .name {{ font-weight: bold; color: #8B0000; }}
    hr {{ border: none; border-top: 1px solid #ccc; margin: 2em 0; }}
    .service {{ padding: 20px; }}
    .info-bar {{ background: #F5F0E0; border-left: 4px solid #8B0000;
                 padding: 12px 16px; margin: 15px 0; font-size: 0.9em; }}
    .info-bar strong {{ color: #8B0000; }}
  </style>
</head>
<body>
  <div class="info-bar">
    <strong>Date:</strong> {ctx['date']} ({ctx['weekday_name']}) |
    <strong>Period:</strong> {ctx['period']} |
    <strong>Tone:</strong> {tone or 'N/A'} |
    <strong>Rank:</strong> {ctx.get('rank_name', 'Simple')} |
    <strong>Sources:</strong> {', '.join(ctx['sources'])}
    {f' | <strong>Feast:</strong> {feast["long_name"]}' if feast else ''}
  </div>
  {body}
</body>
</html>"""


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.route('/api/resolve')
def api_resolve():
    """
    Main endpoint: resolve all liturgical variables for a date.

    Params:
        service   Filter to one service type (vespers, matins, etc.)
        rank      Override feast rank (1-7, 7=simple)
        menaion   Source: general, full, none
        format    Output: json (default), html, epub, pdf
        scope     For epub/pdf: 'day' (default) or 'month'
    """
    m, d, y = _parse_date(request.args)
    calendar = request.args.get('calendar', 1, type=int)
    service = request.args.get('service', None)
    scope = request.args.get('scope', 'day')
    rank, menaion_source, fmt = _parse_options(request.args)

    try:
        date(y, m, d)  # validate
    except ValueError:
        return jsonify({'error': f'Invalid date: {m}/{d}/{y}'}), 400

    # --- EPUB export ---
    if fmt == 'epub':
        from export import export_epub
        if scope == 'month':
            data = export_epub(m, y, day=None, calendar=calendar,
                               rank=rank, menaion_source=menaion_source)
            fname = f'Anthologion-{y}-{m:02d}.epub'
        else:
            data = export_epub(m, y, day=d, calendar=calendar,
                               rank=rank, menaion_source=menaion_source)
            fname = f'Anthologion-{y}-{m:02d}-{d:02d}.epub'
        return Response(data, content_type='application/epub+zip',
                        headers={'Content-Disposition': f'attachment; filename="{fname}"'})

    # --- PDF export ---
    if fmt == 'pdf':
        from export import export_pdf
        if scope == 'month':
            data = export_pdf(m, y, day=None, calendar=calendar,
                              rank=rank, menaion_source=menaion_source)
            fname = f'Anthologion-{y}-{m:02d}.pdf'
        else:
            data = export_pdf(m, y, day=d, calendar=calendar,
                              rank=rank, menaion_source=menaion_source)
            fname = f'Anthologion-{y}-{m:02d}-{d:02d}.pdf'
        return Response(data, content_type='application/pdf',
                        headers={'Content-Disposition': f'attachment; filename="{fname}"'})

    # --- Single service (HTML or JSON) ---
    if service:
        merged = resolve_service(m, d, y, service, calendar,
                                 rank=rank, menaion_source=menaion_source)

        if fmt == 'html':
            ctx = resolve(m, d, y, calendar, rank=rank,
                          menaion_source=menaion_source)
            body = _render_html(service, merged, ctx)
            html = _wrap_html(body, ctx, service)
            return Response(html, content_type='text/html; charset=utf-8')

        return jsonify(_serialize({
            'date': f'{y}-{m:02d}-{d:02d}',
            'service': service,
            'calendar': 'old' if calendar == 1 else 'new',
            'rank': merged.get('_rank', 7),
            'rank_name': merged.get('_rank_name', 'Simple'),
            'menaion_source': merged.get('_menaion_source', 'general'),
            'variables': merged,
        }))

    # --- Full context (JSON) ---
    ctx = resolve(m, d, y, calendar, rank=rank, menaion_source=menaion_source)
    return jsonify(_serialize({
        'date': ctx['date'],
        'weekday': ctx['weekday'],
        'weekday_name': ctx['weekday_name'],
        'calendar': 'old' if calendar == 1 else 'new',
        'period': ctx['period'],
        'rank': ctx['rank'],
        'rank_name': ctx['rank_name'],
        'menaion_source': ctx['menaion_source'],
        'menaion_note': ctx.get('menaion_note'),
        'sources': ctx['sources'],
        'liturgical': ctx['liturgical'],
        'feast': ctx['feast'],
        'triodion': _summary(ctx['triodion']),
        'pentecostarion': _summary(ctx['pentecostarion']),
        'octoechos': _summary(ctx['octoechos']),
        'menaion': _menaion_summary(ctx['menaion']),
    }))


def _summary(entry):
    """Summarize a source entry (key, desc, available services) without full text."""
    if not entry:
        return None
    return {
        'key': entry.get('key'),
        'desc': entry.get('desc'),
        'tone': entry.get('tone'),
        'services': list(entry.get('services', {}).keys()),
    }


def _menaion_summary(entry):
    """Summarize menaion entry."""
    if not entry:
        return None
    return {
        'rank': entry.get('rank'),
        'service_type': entry.get('service_type'),
        'service_name': entry.get('service_name'),
        'long_name': entry.get('long_name'),
        'services': list((entry.get('services') or {}).keys()),
    }


# ---------------------------------------------------------------------------
# Home page UI
# ---------------------------------------------------------------------------
@app.route('/')
def home():
    """Interactive home page for testing the API."""
    return Response(_HOME_HTML, content_type='text/html; charset=utf-8')


_HOME_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Anthologion</title>
  <style>
    :root {
      --primary: #8B0000;
      --accent: #4B0082;
      --bg: #FFFEF5;
      --text: #2C1810;
      --border: #D4C5A9;
      --card-bg: #FFF;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Palatino Linotype', 'Book Antiqua', Georgia, serif;
      background: var(--bg); color: var(--text);
      line-height: 1.6; padding: 20px;
    }
    .container { max-width: 900px; margin: 0 auto; }
    h1 { color: var(--primary); text-align: center; font-size: 2em;
         letter-spacing: 3px; margin-bottom: 5px; }
    .subtitle { text-align: center; color: var(--accent); margin-bottom: 25px; }
    .card {
      background: var(--card-bg); border: 1px solid var(--border);
      border-radius: 8px; padding: 24px; margin-bottom: 20px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .card h2 { color: var(--primary); font-size: 1.1em; margin-bottom: 16px;
               border-bottom: 1px solid var(--border); padding-bottom: 8px; }
    .form-row { display: flex; flex-wrap: wrap; gap: 16px; margin-bottom: 12px; }
    .form-group { display: flex; flex-direction: column; min-width: 120px; }
    .form-group label { font-size: 0.85em; color: #666; margin-bottom: 4px; font-weight: bold; }
    .form-group select, .form-group input {
      padding: 8px 12px; border: 1px solid var(--border); border-radius: 4px;
      font-family: inherit; font-size: 0.95em; background: #FAFAF5;
    }
    .form-group select:focus, .form-group input:focus {
      outline: none; border-color: var(--primary);
    }
    .btn {
      display: inline-block; padding: 10px 24px; background: var(--primary);
      color: white; border: none; border-radius: 4px; font-family: inherit;
      font-size: 1em; cursor: pointer; letter-spacing: 1px;
    }
    .btn:hover { background: #6B0000; }
    .btn-row { display: flex; gap: 10px; margin-top: 8px; }
    .btn-secondary {
      background: var(--accent); padding: 10px 24px; color: white;
      border: none; border-radius: 4px; font-family: inherit;
      font-size: 1em; cursor: pointer;
    }
    .btn-secondary:hover { background: #350066; }
    .info-bar {
      background: #F5F0E0; border-left: 4px solid var(--primary);
      padding: 12px 16px; margin: 12px 0; font-size: 0.9em;
      border-radius: 0 4px 4px 0;
    }
    .info-bar strong { color: var(--primary); }
    #context-panel { display: none; }
    #result-panel { display: none; }
    #result-frame {
      width: 100%; border: 1px solid var(--border); border-radius: 4px;
      min-height: 400px; background: white;
    }
    pre {
      background: #2C1810; color: #F5F0E0; padding: 16px; border-radius: 4px;
      overflow-x: auto; font-size: 0.85em; line-height: 1.5;
      max-height: 500px; overflow-y: auto;
    }
    .tag { display: inline-block; background: #E8E0D0; color: var(--accent);
           padding: 2px 8px; border-radius: 3px; font-size: 0.8em; margin: 2px; }
    .tag-primary { background: var(--primary); color: white; }
    @media (max-width: 600px) {
      body { padding: 10px; }
      .form-row { flex-direction: column; }
      h1 { font-size: 1.5em; }
    }
  </style>
</head>
<body>
<div class="container">
  <h1>ANTHOLOGION</h1>
  <p class="subtitle">Liturgical Service Generator</p>

  <div class="card">
    <h2>Service Options</h2>
    <div class="form-row">
      <div class="form-group">
        <label>Month</label>
        <input type="number" id="month" min="1" max="12" value="">
      </div>
      <div class="form-group">
        <label>Day</label>
        <input type="number" id="day" min="1" max="31" value="">
      </div>
      <div class="form-group">
        <label>Year</label>
        <input type="number" id="year" min="1900" max="2200" value="">
      </div>
      <div class="form-group">
        <label>Calendar</label>
        <select id="calendar">
          <option value="1">Old Calendar</option>
          <option value="0">New Calendar</option>
        </select>
      </div>
    </div>
    <div class="form-row">
      <div class="form-group">
        <label>Service</label>
        <select id="service">
          <option value="vespers">Vespers</option>
          <option value="compline">Compline</option>
          <option value="nocturns">Nocturns</option>
          <option value="matins">Matins</option>
          <option value="first_hour">First Hour</option>
          <option value="third_hour">Third Hour</option>
          <option value="sixth_hour">Sixth Hour</option>
          <option value="ninth_hour">Ninth Hour</option>
          <option value="typika">Typika</option>
          <option value="liturgy">Liturgy</option>
        </select>
      </div>
      <div class="form-group">
        <label>Rank</label>
        <select id="rank">
          <option value="">Auto (from calendar)</option>
          <option value="1">1 — Great Feast</option>
          <option value="2">2 — Vigil</option>
          <option value="3">3 — Polyeleos</option>
          <option value="4">4 — Doxology</option>
          <option value="5">5 — Six Stichera</option>
          <option value="6">6 — Afterfeast</option>
          <option value="7">7 — Simple (Octoechos only)</option>
        </select>
      </div>
      <div class="form-group">
        <label>Menaion</label>
        <select id="menaion">
          <option value="general">General (24 classes)</option>
          <option value="full">Full (366 days) — coming soon</option>
          <option value="none">None (skip)</option>
        </select>
      </div>
      <div class="form-group">
        <label>Export Scope</label>
        <select id="scope">
          <option value="day">Single Day</option>
          <option value="month">Entire Month</option>
        </select>
      </div>
    </div>
    <div class="btn-row">
      <button class="btn" onclick="fetchContext()">Resolve Context</button>
      <button class="btn-secondary" onclick="fetchHTML()">Render HTML</button>
      <button class="btn-secondary" onclick="fetchJSON()">View JSON</button>
      <button class="btn-secondary" onclick="downloadEpub()" style="background:#2E7D32">Download EPUB</button>
      <button class="btn-secondary" onclick="downloadPDF()" style="background:#1565C0">Download PDF</button>
    </div>
  </div>

  <div class="card" id="context-panel">
    <h2>Liturgical Context</h2>
    <div id="context-body"></div>
  </div>

  <div class="card" id="result-panel">
    <h2 id="result-title">Result</h2>
    <div id="result-body"></div>
  </div>
</div>

<script>
  // Set defaults to today
  const now = new Date();
  document.getElementById('month').value = now.getMonth() + 1;
  document.getElementById('day').value = now.getDate();
  document.getElementById('year').value = now.getFullYear();

  function buildParams(extra) {
    const p = new URLSearchParams();
    p.set('m', document.getElementById('month').value);
    p.set('d', document.getElementById('day').value);
    p.set('y', document.getElementById('year').value);
    p.set('calendar', document.getElementById('calendar').value);
    const rank = document.getElementById('rank').value;
    if (rank) p.set('rank', rank);
    p.set('menaion', document.getElementById('menaion').value);
    p.set('scope', document.getElementById('scope').value);
    if (extra) Object.entries(extra).forEach(([k,v]) => p.set(k,v));
    return p.toString();
  }

  function downloadEpub() {
    window.location.href = '/api/resolve?' + buildParams({format: 'epub'});
  }

  function downloadPDF() {
    window.location.href = '/api/resolve?' + buildParams({format: 'pdf'});
  }

  async function fetchContext() {
    const r = await fetch('/api/resolve?' + buildParams());
    const d = await r.json();
    const panel = document.getElementById('context-panel');
    panel.style.display = 'block';

    let html = '<div class="info-bar">';
    html += '<strong>Date:</strong> ' + d.date + ' (' + d.weekday_name + ') | ';
    html += '<strong>Period:</strong> ' + d.period + ' | ';
    html += '<strong>Rank:</strong> ' + d.rank_name + ' (' + d.rank + ')';
    if (d.liturgical) html += ' | <strong>Tone:</strong> ' + (d.liturgical.weekly_tone || 'N/A');
    html += '</div>';

    if (d.menaion_note) {
      html += '<div class="info-bar"><strong>Note:</strong> ' + d.menaion_note + '</div>';
    }

    html += '<p style="margin:8px 0"><strong>Sources:</strong> ';
    d.sources.forEach(s => { html += '<span class="tag tag-primary">' + s + '</span> '; });
    html += '</p>';

    if (d.feast) {
      html += '<p><strong>Feast:</strong> ' + d.feast.long_name;
      html += ' <span class="tag">' + d.feast.service_type + '</span></p>';
    }

    if (d.triodion) {
      html += '<p><strong>Triodion:</strong> ' + d.triodion.desc;
      html += ' — services: ' + d.triodion.services.map(s => '<span class="tag">'+s+'</span>').join(' ') + '</p>';
    }
    if (d.pentecostarion) {
      html += '<p><strong>Pentecostarion:</strong> ' + d.pentecostarion.desc;
      html += ' — services: ' + d.pentecostarion.services.map(s => '<span class="tag">'+s+'</span>').join(' ') + '</p>';
    }
    if (d.octoechos) {
      html += '<p><strong>Octoechos:</strong> ' + d.octoechos.desc;
      html += ' — services: ' + d.octoechos.services.map(s => '<span class="tag">'+s+'</span>').join(' ') + '</p>';
    }
    if (d.menaion) {
      html += '<p><strong>Menaion:</strong> ' + d.menaion.long_name;
      html += ' (' + d.menaion.service_type + ')';
      html += ' — services: ' + d.menaion.services.map(s => '<span class="tag">'+s+'</span>').join(' ') + '</p>';
    }

    document.getElementById('context-body').innerHTML = html;
  }

  async function fetchHTML() {
    const svc = document.getElementById('service').value;
    const url = '/api/resolve?' + buildParams({service: svc, format: 'html'});
    const r = await fetch(url);
    const html = await r.text();
    const panel = document.getElementById('result-panel');
    panel.style.display = 'block';
    document.getElementById('result-title').textContent = svc.charAt(0).toUpperCase() + svc.slice(1) + ' (HTML)';
    document.getElementById('result-body').innerHTML =
      '<iframe id="result-frame" srcdoc="' + html.replace(/"/g, '&quot;') + '"></iframe>';
  }

  async function fetchJSON() {
    const svc = document.getElementById('service').value;
    const url = '/api/resolve?' + buildParams({service: svc, format: 'json'});
    const r = await fetch(url);
    const d = await r.json();
    const panel = document.getElementById('result-panel');
    panel.style.display = 'block';
    document.getElementById('result-title').textContent = svc.charAt(0).toUpperCase() + svc.slice(1) + ' (JSON)';
    document.getElementById('result-body').innerHTML = '<pre>' + JSON.stringify(d, null, 2) + '</pre>';
  }
</script>
</body>
</html>
"""


@app.route('/api/paschalion')
def api_paschalion():
    """Paschalion calculation for a date."""
    m, d, y = _parse_date(request.args)

    try:
        date(y, m, d)
    except ValueError:
        return jsonify({'error': f'Invalid date: {m}/{d}/{y}'}), 400

    result = paschalion(m, d, y)
    return jsonify(_serialize(result))


@app.route('/health')
def health():
    """Health check."""
    return jsonify({
        'status': 'ok',
        'version': '3.0.0',
        'data_sources': ['triodion', 'pentecostarion', 'octoechos', 'menaion'],
        'params': {
            'rank': '1-7 (7=simple)',
            'menaion': 'general | full (coming soon) | none',
            'format': 'json | html | epub | pdf',
            'scope': 'day | month (for epub/pdf)',
            'service': 'vespers | matins | liturgy | compline | nocturns | ...',
            'calendar': '0=new, 1=old (default)',
        },
    })


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', '1') == '1'
    app.run(host='0.0.0.0', port=port, debug=debug)
