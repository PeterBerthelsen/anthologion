"""
End-to-end test: render tonight's vespers from JSON data only.

No PDFs are read. All liturgical data comes from the pre-extracted JSON
via the unified resolver.

Usage:
    python3 test_render.py                  # today's date
    python3 test_render.py 2 26 2026        # specific date
"""

import os
import sys
from datetime import date, timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from jinja2 import Environment, FileSystemLoader
from resolver import resolve, resolve_service
from hymns import vespers_prokeimena
from kathisma import parse_kathisma

# Kathisma rubric: weekday → [vespers_kathisma, nocturns, [matins1, matins2]]
KATHISMA_RUBRIC = {
    0: [0, 17, [4, 5]],
    1: [6, 17, [7, 8]],
    2: [9, 17, [10, 11]],
    3: [12, 17, [13, 14]],
    4: [15, 17, [19, 20]],
    5: [18, 9, [16, 17]],
    6: [1, None, [2, 3]],
}


def render_vespers(month, day, year, calendar=1):
    """Render vespers for the given date, returning HTML string."""
    ctx = resolve(month, day, year, calendar)
    weekday = ctx['weekday']
    service_date = date(year, month, day)

    # Get merged vespers variables
    vs = resolve_service(month, day, year, 'vespers', calendar)

    # Add template-expected metadata
    link_date = service_date.strftime('%m%d%Y')
    vs['link'] = f'{link_date}-vespers'

    if calendar == 1:
        date_oc = service_date - timedelta(days=13)
        night = (service_date - timedelta(days=1))
        night_oc = night - timedelta(days=13)
        vs['night_date'] = night.strftime('%m/%d/%Y') + ' (' + night_oc.strftime('%m/%d/%Y') + ')'
    else:
        night = service_date - timedelta(days=1)
        vs['night_date'] = night.strftime('%m/%d/%Y')

    # Add kathisma
    vs['vespers_kathisma'] = parse_kathisma(KATHISMA_RUBRIC[weekday][0])

    # Add daily prokeimenon
    vs['prokeimenon'] = vs.get('prokeimenon') or vespers_prokeimena(weekday)

    # Ensure stichera is a list for template indexing
    stichera = vs.get('stichera', [])
    if isinstance(stichera, str):
        stichera = [stichera]
    vs['stichera'] = stichera

    # Fill in any missing keys the template expects
    for key in ['doxastichon', 'theotokion', 'readings', 'aposticha',
                'aposticha_theotokion', 'apolytichion']:
        if key not in vs:
            vs[key] = ''

    # Extract feast info
    feast = ctx.get('feast')
    name = feast['service_name'] if feast else None
    long_name = feast['long_name'] if feast else None

    # Set up Jinja
    env = Environment(
        loader=FileSystemLoader(os.path.join(BASE_DIR, 'static', 'html')),
        autoescape=False,
    )
    template = env.get_template('vespers.html')

    html = template.render(
        variables=vs,
        weekday=weekday,
        name=name,
        long_name=long_name,
    )

    return html, ctx


def main():
    if len(sys.argv) == 4:
        m, d, y = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    else:
        today = date.today()
        m, d, y = today.month, today.day, today.year

    print(f'Rendering vespers for {m}/{d}/{y}...')
    print('='*60)

    html, ctx = render_vespers(m, d, y)

    # Print context summary
    lit = ctx['liturgical']
    print(f'Date:    {ctx["date"]} ({ctx["weekday_name"]})')
    print(f'Period:  {ctx["period"]}')
    print(f'Sources: {ctx["sources"]}')
    print(f'Offset:  {lit["pascha_offset"]}, Tone: {lit["weekly_tone"]}')

    if ctx['triodion']:
        print(f'Triodion: {ctx["triodion"]["key"]} - {ctx["triodion"]["desc"]}')
    if ctx['pentecostarion']:
        print(f'Pent:     {ctx["pentecostarion"]["key"]} - {ctx["pentecostarion"]["desc"]}')
    if ctx['feast']:
        print(f'Feast:    rank={ctx["feast"]["rank"]} {ctx["feast"]["long_name"]}')

    # Write HTML output
    out_path = os.path.join(BASE_DIR, 'test_vespers_output.html')
    wrapper = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Vespers - {ctx['date']} ({ctx['weekday_name']})</title>
  <style>
    body {{ font-family: Georgia, serif; max-width: 800px; margin: 40px auto; padding: 0 20px; line-height: 1.6; }}
    h1 {{ color: #8B0000; }}
    h2 {{ color: #4a4a4a; }}
    h3, h4 {{ color: #666; }}
    .note {{ color: #888; font-style: italic; }}
    .name {{ font-weight: bold; color: #8B0000; }}
    hr {{ border: none; border-top: 1px solid #ccc; margin: 2em 0; }}
    .service {{ padding: 20px; }}
  </style>
</head>
<body>
  <div class="header">
    <p><b>Period:</b> {ctx['period']} | <b>Sources:</b> {', '.join(ctx['sources'])} | <b>Tone:</b> {lit['weekly_tone']}</p>
  </div>
  {html}
</body>
</html>"""

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(wrapper)

    print(f'\nHTML written to: {out_path}')
    print(f'HTML size: {len(html):,} characters')

    # Quick content check
    stichera_count = html.count('<p><i class="note">*')
    has_kathisma = 'Kathisma' in html
    has_prokeimenon = 'Prokeimenon' in html or 'prokeimenon' in html.lower()
    has_aposticha = 'Aposticha' in html

    print(f'\nContent check:')
    print(f'  Stichera markers: {stichera_count}')
    print(f'  Kathisma: {"Yes" if has_kathisma else "No"}')
    print(f'  Prokeimenon: {"Yes" if has_prokeimenon else "No"}')
    print(f'  Aposticha: {"Yes" if has_aposticha else "No"}')


if __name__ == '__main__':
    main()
