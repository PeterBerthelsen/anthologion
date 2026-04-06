"""
Export services to epub and PDF formats.

Uses the resolver + Jinja templates to render HTML, then packages
into epub (via ebooklib) or PDF (via weasyprint).

Supports single-day and monthly scope.
"""

import os
import io
from datetime import date, timedelta
from calendar import monthrange

from ebooklib import epub

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Services to include in a full day's export, in liturgical order
DEFAULT_SERVICES = ['vespers', 'compline', 'nocturns', 'matins', 'liturgy']

# CSS for epub/PDF rendering
_STYLES = """
body {
  font-family: 'Palatino Linotype', 'Book Antiqua', Georgia, serif;
  line-height: 1.6; color: #2C1810; max-width: 100%;
}
h1 { color: #8B0000; font-size: 1.6em; margin-top: 1em; }
h2 { color: #4a4a4a; font-size: 1.3em; }
h3, h4 { color: #666; }
.note { color: #888; font-style: italic; }
.name { font-weight: bold; color: #8B0000; }
hr { border: none; border-top: 1px solid #ccc; margin: 1.5em 0; }
.service { page-break-before: always; padding: 10px; }
.service:first-child { page-break-before: avoid; }
.info-bar {
  background: #F5F0E0; border-left: 4px solid #8B0000;
  padding: 8px 12px; margin: 10px 0; font-size: 0.9em;
}
.info-bar strong { color: #8B0000; }
.day-header {
  text-align: center; padding: 15px 0; border-bottom: 2px solid #8B0000;
  margin-bottom: 15px; page-break-before: always;
}
.day-header:first-child { page-break-before: avoid; }
.day-header h1 { margin: 0; }
.day-header p { color: #666; margin: 4px 0; }
"""


def _render_service_html(m, d, y, service_type, calendar=1, rank=None,
                         menaion_source='general'):
    """Render a single service to HTML fragment (no <html> wrapper)."""
    # Import here to avoid circular imports at module level
    from resolver import resolve, resolve_service
    from api import _render_html

    ctx = resolve(m, d, y, calendar, rank=rank, menaion_source=menaion_source)
    merged = resolve_service(m, d, y, service_type, calendar,
                             rank=rank, menaion_source=menaion_source)
    body = _render_html(service_type, merged, ctx)
    return body, ctx


def render_day_html(m, d, y, services=None, calendar=1, rank=None,
                    menaion_source='general'):
    """Render all services for a single day into one HTML document."""
    from resolver import resolve

    services = services or DEFAULT_SERVICES
    ctx = resolve(m, d, y, calendar, rank=rank, menaion_source=menaion_source)

    feast = ctx.get('feast')
    tone = (ctx.get('liturgical') or {}).get('weekly_tone')

    header = f"""<div class="day-header">
      <h1>{ctx['weekday_name']}, {date(y, m, d).strftime('%B %d, %Y')}</h1>
      <p><strong>Period:</strong> {ctx['period']} |
         <strong>Tone:</strong> {tone or 'N/A'} |
         <strong>Rank:</strong> {ctx.get('rank_name', 'Simple')}</p>
      {'<p><strong>' + feast['long_name'] + '</strong></p>' if feast else ''}
    </div>"""

    bodies = [header]
    for svc in services:
        try:
            body, _ = _render_service_html(m, d, y, svc, calendar, rank,
                                           menaion_source)
            if body.strip():
                bodies.append(body)
        except Exception:
            pass  # Service not available for this day/period

    return '\n<hr/>\n'.join(bodies), ctx


def render_month_html(m, y, services=None, calendar=1, rank=None,
                      menaion_source='general'):
    """Render all days in a month into one HTML document."""
    days_in_month = monthrange(y, m)[1]
    parts = []
    for d in range(1, days_in_month + 1):
        day_html, _ = render_day_html(m, d, y, services, calendar, rank,
                                      menaion_source)
        parts.append(day_html)
    return '\n'.join(parts)


def _full_html(body, title):
    """Wrap body HTML in a complete document."""
    return f"""<!DOCTYPE html>
<html><head>
  <meta charset="utf-8">
  <title>{title}</title>
  <style>{_STYLES}</style>
</head><body>
{body}
</body></html>"""


# ---------------------------------------------------------------------------
# EPUB export
# ---------------------------------------------------------------------------
def export_epub(month, year, day=None, services=None, calendar=1,
                rank=None, menaion_source='general'):
    """
    Generate an epub file.

    If day is None, generates the full month.
    Returns bytes (the epub file content).
    """
    services = services or DEFAULT_SERVICES

    book = epub.EpubBook()
    book.set_identifier(f'anthologion-{year}-{month:02d}' +
                        (f'-{day:02d}' if day else ''))
    book.set_language('en')

    if day:
        dt = date(year, month, day)
        title = f'Anthologion — {dt.strftime("%B %d, %Y")}'
    else:
        title = f'Anthologion — {date(year, month, 1).strftime("%B %Y")}'

    book.set_title(title)
    book.add_author('Anthologion Service Generator')

    # Stylesheet
    style = epub.EpubItem(
        uid='style', file_name='style/main.css',
        media_type='text/css', content=_STYLES.encode('utf-8'),
    )
    book.add_item(style)

    chapters = []
    toc = []

    if day:
        days = [day]
    else:
        days = range(1, monthrange(year, month)[1] + 1)

    for d in days:
        dt = date(year, month, d)
        from resolver import resolve
        ctx = resolve(month, d, year, calendar, rank=rank,
                      menaion_source=menaion_source)

        feast = ctx.get('feast')
        tone = (ctx.get('liturgical') or {}).get('weekly_tone')

        day_title = f'{ctx["weekday_name"]}, {dt.strftime("%B %d")}'
        if feast:
            day_title += f' — {feast["long_name"]}'

        # Build HTML for this day
        day_html, _ = render_day_html(month, d, year, services, calendar,
                                      rank, menaion_source)

        chapter = epub.EpubHtml(
            title=day_title,
            file_name=f'day_{d:02d}.xhtml',
            lang='en',
        )
        chapter.content = f'<html><body>{day_html}</body></html>'.encode('utf-8')
        chapter.add_item(style)

        book.add_item(chapter)
        chapters.append(chapter)
        toc.append(chapter)

    book.toc = toc
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = ['nav'] + chapters

    buf = io.BytesIO()
    epub.write_epub(buf, book, {})
    return buf.getvalue()


# ---------------------------------------------------------------------------
# PDF export
# ---------------------------------------------------------------------------
def export_pdf(month, year, day=None, services=None, calendar=1,
               rank=None, menaion_source='general'):
    """
    Generate a PDF file.

    If day is None, generates the full month.
    Returns bytes (the PDF content).
    """
    services = services or DEFAULT_SERVICES

    if day:
        body, _ = render_day_html(month, day, year, services, calendar,
                                  rank, menaion_source)
        dt = date(year, month, day)
        title = f'Anthologion — {dt.strftime("%B %d, %Y")}'
    else:
        body = render_month_html(month, year, services, calendar, rank,
                                 menaion_source)
        title = f'Anthologion — {date(year, month, 1).strftime("%B %Y")}'

    html = _full_html(body, title)

    import weasyprint
    pdf_bytes = weasyprint.HTML(string=html).write_pdf()
    return pdf_bytes
