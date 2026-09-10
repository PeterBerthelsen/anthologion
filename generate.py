#!/usr/bin/env python3
"""
Generate Anthologion day or month packs to disk.

Examples:
    python generate.py --date 2026-09-21 --calendar old
    python generate.py --date 2026-09-08 --calendar new --formats md,html,epub
    python generate.py --month 2026-09 --calendar old --formats md,epub
    python generate.py --date 2026-02-23 --calendar old --formats md,html
"""

from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

from export import (  # noqa: E402
    DEFAULT_SERVICES,
    _full_html,
    export_epub,
    export_markdown_day,
    export_markdown_month,
    export_pdf,
    render_day_html,
    render_month_html,
)


def _calendar(value: str) -> int:
    v = value.lower()
    if v in ('old', 'julian', '1'):
        return 1
    if v in ('new', 'gregorian', 'revised', '0'):
        return 0
    raise argparse.ArgumentTypeError(f'unknown calendar: {value}')


def _write(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(data, bytes):
        path.write_bytes(data)
    else:
        path.write_text(data, encoding='utf-8')
    return path


def generate_day(out: Path, m, d, y, calendar, formats, services):
    cal_name = 'old' if calendar == 1 else 'new'
    dest = out / cal_name / f'{y:04d}' / f'{m:02d}' / f'{d:02d}'
    written = []
    if 'md' in formats:
        md, _ = export_markdown_day(m, d, y, services, calendar)
        written.append(_write(dest / 'day.md', md))
    if 'html' in formats:
        body, ctx = render_day_html(m, d, y, services, calendar)
        title = f'Anthologion — {date(y, m, d).strftime("%B %d, %Y")}'
        written.append(_write(dest / 'day.html', _full_html(body, title)))
    if 'epub' in formats:
        written.append(_write(dest / 'day.epub',
                              export_epub(m, y, day=d, services=services,
                                          calendar=calendar)))
    if 'pdf' in formats:
        written.append(_write(dest / 'day.pdf',
                              export_pdf(m, y, day=d, services=services,
                                         calendar=calendar)))
    return dest, written


def generate_month(out: Path, m, y, calendar, formats, services):
    cal_name = 'old' if calendar == 1 else 'new'
    dest = out / cal_name / f'{y:04d}' / f'{m:02d}'
    written = []
    if 'md' in formats:
        md = export_markdown_month(m, y, services, calendar)
        written.append(_write(dest / 'month.md', md))
    if 'html' in formats:
        body = render_month_html(m, y, services, calendar)
        title = f'Anthologion — {date(y, m, 1).strftime("%B %Y")}'
        written.append(_write(dest / 'month.html', _full_html(body, title)))
    if 'epub' in formats:
        written.append(_write(dest / 'month.epub',
                              export_epub(m, y, day=None, services=services,
                                          calendar=calendar)))
    if 'pdf' in formats:
        written.append(_write(dest / 'month.pdf',
                              export_pdf(m, y, day=None, services=services,
                                         calendar=calendar)))
    return dest, written


def main(argv=None):
    p = argparse.ArgumentParser(description='Generate Anthologion packs')
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument('--date', help='YYYY-MM-DD')
    g.add_argument('--month', help='YYYY-MM')
    p.add_argument('--calendar', type=_calendar, default='old',
                   help='old (default) or new')
    p.add_argument('--formats', default='md,html,epub',
                   help='comma list: md,html,epub,pdf')
    p.add_argument('--out', default=str(BASE_DIR / 'out'))
    p.add_argument('--services', default=','.join(DEFAULT_SERVICES))
    args = p.parse_args(argv)

    formats = [f.strip() for f in args.formats.split(',') if f.strip()]
    services = [s.strip() for s in args.services.split(',') if s.strip()]
    out = Path(args.out)

    if args.date:
        y, m, d = (int(x) for x in args.date.split('-'))
        dest, written = generate_day(out, m, d, y, args.calendar, formats, services)
    else:
        y, m = (int(x) for x in args.month.split('-'))
        dest, written = generate_month(out, m, y, args.calendar, formats, services)

    print(f'Wrote {len(written)} file(s) under {dest}')
    for path in written:
        print(f'  {path} ({path.stat().st_size} bytes)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
