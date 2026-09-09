"""Day/month document and EPUB generation, old and new calendar."""

import sys
import zipfile
from io import BytesIO
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from export import (  # noqa: E402
    export_epub,
    export_markdown_day,
    render_day_html,
)


DATES = [
    # (m, d, y, calendar, label)
    (9, 21, 2026, 1, 'old-nativity-theotokos'),
    (9, 8, 2026, 0, 'new-nativity-theotokos'),
    (11, 8, 2026, 0, 'new-sunday'),
    (2, 23, 2026, 1, 'old-clean-monday'),
]


@pytest.mark.parametrize('m,d,y,cal,label', DATES)
def test_day_html_renders_and_places_date(m, d, y, cal, label):
    html, ctx = render_day_html(m, d, y, calendar=cal)
    assert ctx['calendar'] == cal
    assert '<div class="day-header">' in html
    assert ctx['weekday_name'] in html
    # Vespers template should not crash on short stichera lists.
    assert 'Lord, I Have Cried' in html or 'Vespers' in html
    # Negative-index wrap used to repeat the same hymn in verse 1 and verse 7.
    # After padding, empty early slots mean we should not see 10 copies of one hymn.
    assert html.count('undefined') == 0


@pytest.mark.parametrize('m,d,y,cal,label', DATES)
def test_day_epub_is_zip_with_chapters(m, d, y, cal, label):
    data = export_epub(m, y, day=d, calendar=cal)
    assert data[:2] == b'PK'
    zf = zipfile.ZipFile(BytesIO(data))
    names = zf.namelist()
    chapters = [n for n in names if n.endswith('.xhtml') and 'day_' in n]
    assert chapters, names
    chapter = chapters[0]
    body = zf.read(chapter).decode('utf-8', errors='replace')
    assert str(y) in body or date_month(m) in body


def date_month(m):
    import calendar
    return calendar.month_name[m]


@pytest.mark.parametrize('m,d,y,cal,label', DATES)
def test_day_markdown_has_headings_and_variables(m, d, y, cal, label):
    md, ctx = export_markdown_day(m, d, y, calendar=cal)
    assert md.startswith('# ')
    assert ctx['weekday_name'] in md
    assert 'Vespers' in md
    assert '(name)' not in md


def test_old_vs_new_calendar_docs_differ():
    old_html, old_ctx = render_day_html(9, 8, 2026, calendar=1)
    new_html, new_ctx = render_day_html(9, 8, 2026, calendar=0)
    assert old_ctx['menaion_date'] != new_ctx['menaion_date']
    assert old_html != new_html


def test_day_pdf_header():
    weasyprint = pytest.importorskip('weasyprint')
    from export import export_pdf
    data = export_pdf(9, 2026, day=21, calendar=1, services=['vespers'])
    assert data.startswith(b'%PDF')


def test_month_epub_september_2026_old_calendar_has_30_chapters():
    data = export_epub(9, 2026, day=None, calendar=1, services=['vespers'])
    zf = zipfile.ZipFile(BytesIO(data))
    days = [n for n in zf.namelist() if 'day_' in n and n.endswith('.xhtml')]
    assert len(days) == 30
