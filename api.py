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
    format    Output format: 'json' (default), 'html' (rendered service)
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
    if fmt not in ('json', 'html'):
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

    Optional `service` param filters to a single merged service type.
    Optional `rank` overrides feast rank (7 = simple/octoechos only).
    Optional `menaion` selects source: general, full, none.
    Optional `format` selects output: json (default), html.
    """
    m, d, y = _parse_date(request.args)
    calendar = request.args.get('calendar', 1, type=int)
    service = request.args.get('service', None)
    rank, menaion_source, fmt = _parse_options(request.args)

    try:
        date(y, m, d)  # validate
    except ValueError:
        return jsonify({'error': f'Invalid date: {m}/{d}/{y}'}), 400

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
            'format': 'json | html',
            'service': 'vespers | matins | liturgy | compline | nocturns | ...',
            'calendar': '0=new, 1=old (default)',
        },
    })


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', '1') == '1'
    app.run(host='0.0.0.0', port=port, debug=debug)
