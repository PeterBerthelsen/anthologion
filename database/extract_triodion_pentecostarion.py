"""
Extract Triodion and Pentecostarion PDFs into structured JSON.

These are stored as a SINGLE COLLECTION indexed by pascha_offset,
since it's mathematically impossible for them to overlap:
  - Triodion:       ~day -70 to day -1 (Publican & Pharisee → Holy Saturday)
  - Pentecostarion: day 0 to day +56   (Pascha → All Saints Sunday)

CALENDAR DAY vs LITURGICAL DAY:
  Orthodox liturgical day begins at Vespers (sunset, evening before).
  So "Saturday Vespers" is liturgically SUNDAY.

  The PDFs from st-sergius.org are indexed by CALENDAR day.
  We convert to LITURGICAL day (pascha_offset) during extraction:
    - Vespers text from calendar day N → liturgical day N+1 (pascha_offset)
    - Matins/Liturgy from calendar day N → liturgical day N (pascha_offset)

RUN THIS AFTER downloading the PDFs:
    python3 database/extract_triodion_pentecostarion.py

Requires: pip install pymupdf
"""

import os
import re
import json

try:
    import fitz  # PyMuPDF
except ImportError:
    print("ERROR: PyMuPDF not installed. Run: pip install pymupdf")
    exit(1)

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TRIOD_DIR = os.path.join(SCRIPT_DIR, '..', 'services', 'triodion')
PENT_DIR = os.path.join(SCRIPT_DIR, '..', 'services', 'pentecostarion')
OUTPUT_DIR = os.path.join(SCRIPT_DIR, 'paschal_cycle')

ROMAN_TO_INT = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8}


# ============================================================
# TRIODION FILENAME → PASCHA OFFSET MAPPING
# ============================================================
# This maps the st-sergius filename convention to days-from-Pascha.
#
# Pre-Lenten Triodion (0-N.pdf):
#   The pre-Lenten period has 3 preparatory Sundays:
#     Publican & Pharisee = Pascha - 70
#     Prodigal Son        = Pascha - 63
#     Meatfare (Judgment) = Pascha - 56
#     Cheesefare (Forgiveness) = Pascha - 49
#   Then Clean Week begins at Pascha - 48
#
# Lenten Triodion (N.pdf):
#   Week 1 of Lent starts at Pascha - 48 (Clean Monday)
#   Week 1: days 1-7 → offsets -48 to -42
#   Week 2: days 8-14 → offsets -41 to -35
#   ...
#   Week 6: days 36-42 → offsets -13 to -7
#   Holy Week: days 43-49 → offsets -6 to 0
#
# The exact file-to-offset mapping needs verification after download,
# but we use the PDF content (titles, day names) to determine the
# actual liturgical day.

# Known mappings from search results:
KNOWN_TRIOD_MAPPINGS = {
    # Pre-Lenten
    '0-10.pdf': {'title': 'Sunday of Publican & Pharisee', 'approx_offset': -70},
    '0-14.pdf': {'title': 'Friday/Saturday stichera', 'approx_offset': -65},
    '0-37.pdf': {'title': 'Meatfare Sunday', 'approx_offset': -56},
    # Lenten
    '13.pdf': {'title': 'Week 1 Wednesday Matins', 'approx_offset': -46},
    '16.pdf': {'title': 'Week 1 Saturday Matins', 'approx_offset': -43},
    '36.pdf': {'title': 'Week 3 Saturday Matins', 'approx_offset': -29},
    '37.pdf': {'title': 'Week 3 Sunday (Cross)', 'approx_offset': -28},
    '74.pdf': {'title': 'Holy Thursday Matins', 'approx_offset': -3},
    '75.pdf': {'title': 'Holy Friday Matins', 'approx_offset': -2},
}

# Known Pentecostarion mappings:
KNOWN_PENT_MAPPINGS = {
    '42.pdf': {'title': 'Week 4 Tuesday', 'approx_offset': 23},
    '61.pdf': {'title': 'Week 6 Sunday Evening', 'approx_offset': 35},
    '64.pdf': {'title': 'Ascension (Week 6 Thursday)', 'approx_offset': 39},
    '82.pdf': {'title': 'Week 8 Tuesday', 'approx_offset': 51},
}


def detect_service_type(text_block):
    """Detect whether a text block is Vespers, Matins, or Liturgy"""
    upper = text_block[:500].upper()
    if 'AT VESPERS' in upper or 'VESPERS' in upper:
        return 'vespers'
    elif 'AT MATINS' in upper or 'MATINS' in upper:
        return 'matins'
    elif 'AT LITURGY' in upper or 'LITURGY' in upper:
        return 'liturgy'
    elif 'COMPLINE' in upper:
        return 'compline'
    elif 'HOURS' in upper:
        return 'hours'
    return 'unknown'


def detect_pascha_offset_from_content(text, filename):
    """
    Try to determine the pascha_offset from the PDF text content.
    Uses day/week references and known title patterns.
    """
    upper = text[:2000].upper()

    # Check known mappings first
    if filename in KNOWN_TRIOD_MAPPINGS:
        return KNOWN_TRIOD_MAPPINGS[filename]['approx_offset']
    if filename in KNOWN_PENT_MAPPINGS:
        return KNOWN_PENT_MAPPINGS[filename]['approx_offset']

    # Try to detect from week/day references in title
    # Pattern: "FIRST WEEK" / "SECOND WEEK" etc.
    week_words = {
        'FIRST': 1, 'SECOND': 2, 'THIRD': 3, 'FOURTH': 4,
        'FIFTH': 5, 'SIXTH': 6, 'SEVENTH': 7, 'EIGHTH': 8
    }
    day_words = {
        'SUNDAY': 0, 'MONDAY': 1, 'TUESDAY': 2, 'WEDNESDAY': 3,
        'THURSDAY': 4, 'FRIDAY': 5, 'SATURDAY': 6
    }

    detected_week = None
    detected_day = None

    for word, num in week_words.items():
        if f'{word} WEEK' in upper:
            detected_week = num
            break

    for word, num in day_words.items():
        if word in upper:
            detected_day = num
            break

    # For Triodion (Lenten): Week 1 Monday = offset -47
    # Week W, Day D → offset = -48 + (W-1)*7 + D
    if detected_week and detected_day is not None:
        if 'triod' in filename or any(k in upper for k in ['LENT', 'TRIODION', 'GREAT AND HOLY']):
            return -48 + (detected_week - 1) * 7 + detected_day

    # For Pentecostarion: Week 1 = Thomas week, Sunday = offset 7
    # Week W, Day D → offset = W*7 + D
    if detected_week and detected_day is not None:
        if 'pent' in filename or any(k in upper for k in ['PENTECOSTARION', 'PASCHA', 'BRIGHT']):
            return detected_week * 7 + detected_day

    # Holy Week detection
    if 'HOLY AND GREAT' in upper or 'GREAT AND HOLY' in upper:
        if 'MONDAY' in upper: return -6
        if 'TUESDAY' in upper: return -5
        if 'WEDNESDAY' in upper: return -4
        if 'THURSDAY' in upper: return -3
        if 'FRIDAY' in upper: return -2
        if 'SATURDAY' in upper: return -1

    # Bright Week detection
    if 'BRIGHT' in upper:
        if 'MONDAY' in upper: return 1
        if 'TUESDAY' in upper: return 2
        if 'WEDNESDAY' in upper: return 3
        if 'THURSDAY' in upper: return 4
        if 'FRIDAY' in upper: return 5
        if 'SATURDAY' in upper: return 6

    return None  # Could not determine


def extract_pdf_text(pdf_path):
    """Extract all text from a PDF"""
    doc = fitz.open(pdf_path)
    text = ''
    for page in doc:
        text += page.get_text()
    return text


def parse_stichera(text_section):
    """Extract stichera from a text section"""
    stichera = []
    parts = re.split(r'\*\*\s*', text_section)
    for i, part in enumerate(parts):
        cleaned = ' '.join(part.split()).strip()
        if len(cleaned) > 40:
            # Try to extract tone
            tone_match = re.search(r'[Tt]one\s+([IVXL]+)', cleaned[:100])
            tone = ROMAN_TO_INT.get(tone_match.group(1)) if tone_match else None

            stichera.append({
                'order': i + 1,
                'tone': tone,
                'text': cleaned
            })
    return stichera


def extract_service_sections(full_text):
    """
    Split a PDF's text into service sections (Vespers, Matins, Liturgy, etc.)
    and extract structured data from each.
    """
    sections = []

    # Find service boundaries
    service_markers = [
        (r'AT\s+(?:GREAT\s+)?VESPERS', 'vespers'),
        (r'AT\s+(?:SMALL\s+)?VESPERS', 'small_vespers'),
        (r'AT\s+COMPLINE', 'compline'),
        (r'AT\s+MATINS', 'matins'),
        (r'AT\s+(?:THE\s+)?LITURGY', 'liturgy'),
        (r'(?:THE\s+)?(?:ROYAL\s+)?HOURS', 'hours'),
    ]

    # Find positions of all service markers
    positions = []
    for pattern, svc_type in service_markers:
        for m in re.finditer(pattern, full_text, re.IGNORECASE):
            positions.append((m.start(), svc_type, m.group()))

    positions.sort()

    # Extract each service section
    for i, (pos, svc_type, marker) in enumerate(positions):
        next_pos = positions[i + 1][0] if i + 1 < len(positions) else len(full_text)
        section_text = full_text[pos:next_pos]

        section = {
            'service_type': svc_type,
            'marker': marker,
            'raw_length': len(section_text),
        }

        # Extract stichera on "Lord I have cried"
        lord_start = section_text.find('Lord')
        if lord_start > -1 and 'cried' in section_text[lord_start:lord_start + 100]:
            glory_pos = section_text.find('Glory', lord_start + 50)
            if glory_pos > lord_start:
                stichera_text = section_text[lord_start:glory_pos]
                section['stichera_lord_i_cried'] = parse_stichera(stichera_text)

        # Extract aposticha
        apost_start = section_text.find('Aposticha')
        if apost_start > -1:
            apost_end = section_text.find('Now lettest', apost_start)
            if apost_end == -1:
                apost_end = min(apost_start + 3000, len(section_text))
            apost_text = section_text[apost_start:apost_end]
            section['aposticha'] = parse_stichera(apost_text)

        # Extract troparion
        trop_match = re.search(
            r'Troparion.*?(?:[Ii]n Tone\s+([IVXL]+))?[:\s]+(.*?)(?=Kontakion|Glory|Dismissal|\Z)',
            section_text[-3000:], re.DOTALL
        )
        if trop_match:
            t = ROMAN_TO_INT.get(trop_match.group(1)) if trop_match.group(1) else None
            txt = ' '.join(trop_match.group(2).split())[:500]
            section['troparion'] = {'tone': t, 'text': txt}

        # Extract kontakion
        kont_match = re.search(
            r'Kontakion.*?(?:[Ii]n Tone\s+([IVXL]+))?[:\s]+(.*?)(?=Ikos|Oikos|Prokeimenon|Glory|\Z)',
            section_text, re.DOTALL
        )
        if kont_match:
            t = ROMAN_TO_INT.get(kont_match.group(1)) if kont_match.group(1) else None
            txt = ' '.join(kont_match.group(2).split())[:500]
            section['kontakion'] = {'tone': t, 'text': txt}

        sections.append(section)

    return sections


def process_pdf_file(pdf_path, source_type):
    """
    Process a single Triodion/Pentecostarion PDF.
    Returns structured data ready for database insertion.
    """
    filename = os.path.basename(pdf_path)
    text = extract_pdf_text(pdf_path)

    # Detect pascha offset
    pascha_offset = detect_pascha_offset_from_content(text, filename)

    # Extract title from first ~500 chars
    title_match = re.search(r'^(.+?)(?:\n|\r)', text[:500])
    title = title_match.group(1).strip() if title_match else filename

    # Extract service sections
    sections = extract_service_sections(text)

    return {
        'filename': filename,
        'source': source_type,  # 'triodion' or 'pentecostarion'
        'pascha_offset': pascha_offset,
        'title': title,
        'total_chars': len(text),
        'services': sections,
        'raw_text_preview': text[:500]
    }


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("=" * 65)
    print("TRIODION & PENTECOSTARION EXTRACTION")
    print("=" * 65)

    all_data = []

    # Process Triodion
    if os.path.exists(TRIOD_DIR):
        triod_files = sorted([f for f in os.listdir(TRIOD_DIR) if f.endswith('.pdf')])
        print(f"\nFound {len(triod_files)} Triodion PDFs")

        for pdf_file in triod_files:
            pdf_path = os.path.join(TRIOD_DIR, pdf_file)
            try:
                data = process_pdf_file(pdf_path, 'triodion')
                all_data.append(data)

                svc_count = len(data['services'])
                offset = data['pascha_offset']
                offset_str = f"P{offset:+d}" if offset is not None else "P???"
                print(f"  {pdf_file:12s} → {offset_str:6s} | {svc_count} services | {data['title'][:50]}")
            except Exception as e:
                print(f"  {pdf_file:12s} → ERROR: {e}")
    else:
        print(f"\nTriodion directory not found: {TRIOD_DIR}")
        print("  Run download_triodion_pentecostarion.py first!")

    # Process Pentecostarion
    if os.path.exists(PENT_DIR):
        pent_files = sorted([f for f in os.listdir(PENT_DIR) if f.endswith('.pdf')])
        print(f"\nFound {len(pent_files)} Pentecostarion PDFs")

        for pdf_file in pent_files:
            pdf_path = os.path.join(PENT_DIR, pdf_file)
            try:
                data = process_pdf_file(pdf_path, 'pentecostarion')
                all_data.append(data)

                svc_count = len(data['services'])
                offset = data['pascha_offset']
                offset_str = f"P{offset:+d}" if offset is not None else "P???"
                print(f"  {pdf_file:12s} → {offset_str:6s} | {svc_count} services | {data['title'][:50]}")
            except Exception as e:
                print(f"  {pdf_file:12s} → ERROR: {e}")
    else:
        print(f"\nPentecostarion directory not found: {PENT_DIR}")
        print("  Run download_triodion_pentecostarion.py first!")

    # Save all extracted data
    if all_data:
        output_path = os.path.join(OUTPUT_DIR, 'paschal_cycle.json')
        with open(output_path, 'w', encoding='utf-8') as f:
            # Don't save raw_text_preview in combined file
            clean_data = []
            for d in all_data:
                clean = {k: v for k, v in d.items() if k != 'raw_text_preview'}
                clean_data.append(clean)
            json.dump(clean_data, f, indent=2, ensure_ascii=False)

        print(f"\n{'=' * 65}")
        print(f"EXTRACTION COMPLETE")
        print(f"{'=' * 65}")
        print(f"  Total PDFs processed: {len(all_data)}")
        print(f"  Triodion:             {sum(1 for d in all_data if d['source'] == 'triodion')}")
        print(f"  Pentecostarion:       {sum(1 for d in all_data if d['source'] == 'pentecostarion')}")
        print(f"  With pascha_offset:   {sum(1 for d in all_data if d['pascha_offset'] is not None)}")
        print(f"  Output: {output_path}")

        # Show offset coverage
        offsets = sorted([d['pascha_offset'] for d in all_data if d['pascha_offset'] is not None])
        if offsets:
            print(f"\n  Pascha offset range: {offsets[0]} to {offsets[-1]}")
            print(f"  Days covered: {len(offsets)}")

            # Check for gaps
            full_range = set(range(offsets[0], offsets[-1] + 1))
            covered = set(offsets)
            gaps = sorted(full_range - covered)
            if gaps:
                print(f"  Gaps in coverage: {len(gaps)} days")
                if len(gaps) <= 10:
                    print(f"  Missing offsets: {gaps}")
            else:
                print(f"  Coverage: COMPLETE (no gaps!)")
    else:
        print("\nNo PDFs found to process.")
        print("Run download_triodion_pentecostarion.py first!")

    print(f"\nNext step: Import to database with import_paschal_cycle.py")


if __name__ == '__main__':
    main()
