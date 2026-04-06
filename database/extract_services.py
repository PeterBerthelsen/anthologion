"""
Extract Triodion and Pentecostarion PDFs into structured Python data.

Processes all PDFs in services/triodion/ and services/pentecost/,
extracts liturgical text, splits into service sections (Vespers, Matins, etc.),
and parses key components (stichera, canons, kontakia, etc.).

Output: triodion_data.py and pentecostarion_data.py

Usage:
    python3 database/extract_services.py
    python3 database/extract_services.py --triodion-only
    python3 database/extract_services.py --pent-only
    python3 database/extract_services.py --test  # test on a few sample files
"""

import os
import re
import sys
import json
import fitz  # PyMuPDF

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRIOD_DIR = os.path.join(BASE_DIR, 'services', 'triodion')
PENT_DIR = os.path.join(BASE_DIR, 'services', 'pentecost')


# ============================================================
# PDF Text Extraction
# ============================================================

def extract_pdf_text(filepath):
    """Extract all text from a PDF using PyMuPDF."""
    text = ''
    with fitz.open(filepath) as doc:
        for page in doc:
            text += page.get_text()
    # Normalize whitespace: collapse multiple blank lines, strip trailing spaces
    text = re.sub(r'[ \t]+\n', '\n', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


# ============================================================
# Service Section Splitting
# ============================================================

# Patterns that mark the beginning of major service sections
SERVICE_HEADERS = [
    (r'(?:AT\s+)?(?:GREAT\s+)?VESPERS', 'vespers'),
    (r'(?:AT\s+)?(?:GREAT\s+)?COMPLINE', 'compline'),
    (r'(?:AT\s+)?NOCTURNS?', 'nocturns'),
    (r'(?:AT\s+)?MATINS', 'matins'),
    (r'(?:AT\s+)?(?:THE\s+)?(?:FIRST|1ST)\s+HOUR', 'first_hour'),
    (r'(?:AT\s+)?(?:THE\s+)?(?:THIRD|3RD)\s+HOUR', 'third_hour'),
    (r'(?:AT\s+)?(?:THE\s+)?(?:SIXTH|6TH)\s+HOUR', 'sixth_hour'),
    (r'(?:AT\s+)?(?:THE\s+)?(?:NINTH|9TH)\s+HOUR', 'ninth_hour'),
    (r'(?:AT\s+)?(?:THE\s+)?TYPIK[AO]', 'typika'),
    (r'(?:AT\s+)?(?:THE\s+)?(?:DIVINE\s+)?LITURGY', 'liturgy'),
    (r'(?:AT\s+)?(?:THE\s+)?PRESANCTIFIED', 'presanctified'),
]


def split_into_services(text):
    """
    Split full PDF text into service sections.
    Returns dict: {service_name: text_content}

    Handles three header styles:
    1. Standalone: "AT VESPERS" or "VESPERS" on its own line
    2. Inline with title: "FIRST WEEK OF LENT: WEDNESDAY MATINS"
    3. With trailing punctuation: "AT VESPERS:"
    """
    # Find all service header positions
    found = []

    # Pass 1: Standalone headers (on their own line, with optional trailing colon/space)
    for pattern, name in SERVICE_HEADERS:
        for m in re.finditer(
            r'^[\s]*' + pattern + r'[\s:]*$',
            text,
            re.MULTILINE | re.IGNORECASE
        ):
            found.append((m.start(), name, m.group()))

    # Pass 2: Inline headers (embedded in title lines like "WEEK 1: WEDNESDAY MATINS")
    # Only look in the first ~500 chars for title-embedded headers
    title_region = text[:500]
    for pattern, name in SERVICE_HEADERS:
        for m in re.finditer(pattern, title_region, re.IGNORECASE):
            # Check this position isn't already captured
            already_found = any(abs(m.start() - pos) < 20 for pos, _, _ in found)
            if not already_found:
                # Find the start of this line to use as the section start
                line_start = text.rfind('\n', 0, m.start())
                line_start = 0 if line_start == -1 else line_start + 1
                found.append((line_start, name, m.group()))

    # Pass 3: Headers elsewhere in the text that are on a line with minimal prefix
    for pattern, name in SERVICE_HEADERS:
        for m in re.finditer(pattern, text, re.IGNORECASE):
            already_found = any(abs(m.start() - pos) < 20 for pos, _, _ in found)
            if not already_found:
                line_start = text.rfind('\n', 0, m.start())
                prefix = text[line_start+1:m.start()].strip()
                # Allow lines like "Then the reader immediately begineth the first hour"
                # but also direct headers like "SIXTH HOUR"
                line_end = text.find('\n', m.end())
                full_line = text[line_start+1:line_end].strip() if line_end > 0 else text[line_start+1:].strip()
                # The line should be short (header-like) or the keyword at end of short line
                if len(full_line) < 80 and len(prefix) < 50:
                    found.append((m.start(), name, m.group()))

    if not found:
        return {'full_text': text}

    # Sort by position and deduplicate
    found.sort(key=lambda x: x[0])
    deduped = []
    seen = []  # list of (pos, name)
    for pos, name, header in found:
        # Skip if same service type found within 100 chars
        if any(abs(pos - sp) < 100 and sn == name for sp, sn in seen):
            continue
        # Skip if any service found within 20 chars (likely same header matched twice)
        if any(abs(pos - sp) < 20 for sp, sn in seen):
            continue
        deduped.append((pos, name, header))
        seen.append((pos, name))
    found = deduped

    # Build service sections
    services = {}
    for i, (pos, name, header) in enumerate(found):
        end_pos = found[i + 1][0] if i + 1 < len(found) else len(text)
        section_text = text[pos:end_pos].strip()

        if name in services:
            services[name] += '\n\n---\n\n' + section_text
        else:
            services[name] = section_text

    return services


# ============================================================
# Component Extraction within a Service Section
# ============================================================

def extract_stichera_block(text, start_pattern, end_patterns):
    """Extract a block of text between start and end patterns."""
    start_match = re.search(start_pattern, text, re.IGNORECASE)
    if not start_match:
        return None

    start_pos = start_match.end()

    end_pos = len(text)
    for ep in end_patterns:
        m = re.search(ep, text[start_pos:], re.IGNORECASE)
        if m:
            end_pos = min(end_pos, start_pos + m.start())

    return text[start_pos:end_pos].strip()


def parse_vespers(text):
    """Extract vespers components from a vespers section."""
    parts = {}

    # Stichera on "Lord I have cried"
    stichera_block = extract_stichera_block(
        text,
        r'(?:On\s+)?["\u201c]?Lord,?\s+I\s+have\s+cried',
        [r'\bGlory\s*\.\.\.', r'After\s+the\s+[Ee]ntrance', r'Prokeimenon']
    )
    if stichera_block:
        parts['stichera'] = clean_text(stichera_block)

    # Doxastichon (Glory...)
    glory_block = extract_stichera_block(
        text,
        r'Glory\s*(?:\.\.\.|…)',
        [r'Both\s+now\s*\.\.\.', r'Now\s+&\s+[Ee]ver', r'After\s+the\s+[Ee]ntrance',
         r'Prokeimenon', r'\bLitya\b', r'On\s+the\s+Aposticha']
    )
    if glory_block:
        parts['doxastichon'] = clean_text(glory_block)

    # Theotokion / Both now
    theotokion_block = extract_stichera_block(
        text,
        r'(?:Both\s+now|Now\s+&\s+[Ee]ver)\s*(?:\.\.\.|…)',
        [r'After\s+the\s+[Ee]ntrance', r'Prokeimenon', r'\bLitya\b',
         r'On\s+the\s+Aposticha', r'["\u201c]?O\s+Joyous\s+Light']
    )
    if theotokion_block:
        parts['theotokion'] = clean_text(theotokion_block)

    # Prokeimenon
    prok_block = extract_stichera_block(
        text,
        r'Prokeimenon',
        [r'On\s+the\s+Aposticha', r'\bLitya\b', r'(?:Vouchsafe|Then)',
         r'The\s+(?:Three\s+)?Lessons?', r'["\u201c]?Now\s+lettest']
    )
    if prok_block:
        parts['prokeimenon'] = clean_text(prok_block)

    # Litya (if present)
    litya_block = extract_stichera_block(
        text,
        r'(?:At\s+the\s+)?Litya',
        [r'On\s+the\s+Aposticha', r'Aposticha']
    )
    if litya_block:
        parts['litya'] = clean_text(litya_block)

    # Aposticha
    aposticha_block = extract_stichera_block(
        text,
        r'(?:On\s+the\s+|At\s+the\s+)?Aposticha',
        [r'["\u201c]?Now\s+lettest', r'Troparion', r'Dismissal',
         r'Then\s+in\s+Tone', r'Blessed\s+be\s+the\s+Name']
    )
    if aposticha_block:
        parts['aposticha'] = clean_text(aposticha_block)

    # Troparion / Apolytichion
    trop_block = extract_stichera_block(
        text,
        r'(?:The\s+)?Troparion',
        [r'Dismissal', r'Blessed\s+be\s+the\s+Name', r'$']
    )
    if trop_block:
        parts['troparion'] = clean_text(trop_block)

    return parts


def parse_matins(text):
    """Extract matins components from a matins section."""
    parts = {}

    # Troparion / "God is the Lord" or Alleluia section
    trop_block = extract_stichera_block(
        text,
        r'(?:On\s+["\u201c]?God\s+is\s+the\s+Lord|Alleluia|Troparion)',
        [r'(?:1st|first)\s+(?:chanting|reading|Kathisma)',
         r'Kathisma\s+[IVX]+', r'Psalm\s+50', r'ODE\s+I\b']
    )
    if trop_block:
        parts['troparion'] = clean_text(trop_block)

    # Sessional hymns (after kathisma readings)
    sessional_blocks = []
    for m in re.finditer(r'Sessional\s+Hymn', text, re.IGNORECASE):
        block = extract_stichera_block(
            text[m.start():],
            r'Sessional\s+Hymn',
            [r'(?:Then\s+)?(?:the\s+)?(?:\d+(?:st|nd|rd|th))?\s*(?:chanting|reading)',
             r'Psalm\s+50', r'ODE\s+', r'Katavasia', r'(?:Then|Followed\s+by)']
        )
        if block:
            sessional_blocks.append(clean_text(block))
    if sessional_blocks:
        parts['sessional_hymns'] = sessional_blocks

    # Polyeleos (if present)
    polyeleos_block = extract_stichera_block(
        text,
        r'Polyeleos',
        [r'Psalm\s+50', r'Magnification', r'Sessional\s+Hymn', r'ODE\s+']
    )
    if polyeleos_block:
        parts['polyeleos'] = clean_text(polyeleos_block)

    # After Psalm 50
    after50_block = extract_stichera_block(
        text,
        r'Psalm\s+50',
        [r'ODE\s+I\b', r'(?:The\s+)?[Cc]anon', r'(?:Followed|Then)\s+by\s+the\s+canons?']
    )
    if after50_block:
        parts['after50'] = clean_text(after50_block)

    # Canon(s) - extract the full canon block
    canon_start = None
    for m in re.finditer(r'(?:ODE\s+I\b|(?:The\s+)?(?:tri-ode\s+)?[Cc]anon)', text, re.IGNORECASE):
        # Make sure this is the start of the canon, not a reference
        if re.search(r'ODE\s+I\b', text[m.start():m.start()+20]):
            canon_start = m.start()
            break
        elif 'canon' in text[m.start():m.start()+30].lower():
            canon_start = m.start()
            break

    if canon_start:
        # Canon ends at exapostilarion, praises, or aposticha
        canon_end_patterns = [
            r'[Ee]xapostilarion', r'[Ee]xaposteilarion',
            r'(?:The\s+)?[Pp]raises', r'(?:On\s+the\s+)?Aposticha',
            r'(?:The\s+)?[Dd]oxology', r'(?:At\s+)?(?:THE\s+)?(?:FIRST|1ST)\s+HOUR'
        ]
        canon_end = len(text)
        for ep in canon_end_patterns:
            m = re.search(ep, text[canon_start:])
            if m:
                canon_end = min(canon_end, canon_start + m.start())
        parts['canon'] = clean_text(text[canon_start:canon_end])

    # Kontakion (usually after Ode VI)
    kontakion_block = extract_stichera_block(
        text,
        r'Kontakion',
        [r'(?:Synaxarion|Ikos\b)', r'ODE\s+VII']
    )
    if kontakion_block:
        parts['kontakion'] = clean_text(kontakion_block)

    # Ikos
    ikos_block = extract_stichera_block(
        text,
        r'\bIkos\b',
        [r'Synaxarion', r'ODE\s+VII', r'ODE\s+VIII']
    )
    if ikos_block:
        parts['ikos'] = clean_text(ikos_block)

    # Exapostilarion
    exap_block = extract_stichera_block(
        text,
        r'[Ee]xapost[ei]ilarion',
        [r'(?:The\s+)?[Pp]raises', r'(?:On\s+the\s+)?Aposticha',
         r'(?:The\s+)?[Dd]oxology', r'(?:AT\s+)?(?:THE\s+)?(?:FIRST|1ST)\s+HOUR',
         r'(?:AT\s+)?(?:THE\s+)?LITURGY']
    )
    if exap_block:
        parts['exapostilarion'] = clean_text(exap_block)

    # Praises / Lauds (Ainoi)
    praises_block = extract_stichera_block(
        text,
        r'(?:The\s+)?(?:Praises|Lauds|Ainoi)',
        [r'(?:The\s+)?(?:Great\s+)?[Dd]oxology', r'(?:On\s+the\s+)?Aposticha',
         r'(?:AT\s+)?(?:THE\s+)?(?:FIRST|1ST)\s+HOUR',
         r'(?:AT\s+)?(?:THE\s+)?LITURGY']
    )
    if praises_block:
        parts['praises'] = clean_text(praises_block)

    # Aposticha (at matins)
    aposticha_block = extract_stichera_block(
        text,
        r'(?:On\s+the\s+|At\s+the\s+)?Aposticha',
        [r'(?:The\s+)?(?:Great\s+)?[Dd]oxology', r'(?:AT\s+)?(?:THE\s+)?(?:FIRST|1ST)\s+HOUR',
         r'(?:AT\s+)?(?:THE\s+)?LITURGY', r'Troparion', r'Dismissal',
         r'(?:It\s+is\s+)?[Tt]ruly\s+meet']
    )
    if aposticha_block:
        parts['aposticha'] = clean_text(aposticha_block)

    return parts


def parse_hours(text):
    """Extract hours components (for Lenten hours)."""
    parts = {}

    # Troparion
    trop_block = extract_stichera_block(
        text,
        r'Troparion',
        [r'Kontakion', r'Prokeimenon', r'The\s+Reading']
    )
    if trop_block:
        parts['troparion'] = clean_text(trop_block)

    # Kontakion
    kont_block = extract_stichera_block(
        text,
        r'Kontakion',
        [r'Prokeimenon', r'The\s+Reading', r'(?:AT|THE)\s+']
    )
    if kont_block:
        parts['kontakion'] = clean_text(kont_block)

    # Prokeimenon
    prok_block = extract_stichera_block(
        text,
        r'Prokeimenon',
        [r'The\s+Reading', r'(?:AT|THE)\s+']
    )
    if prok_block:
        parts['prokeimenon'] = clean_text(prok_block)

    return parts


def parse_liturgy(text):
    """Extract liturgy/typika components."""
    parts = {}

    # Beatitudes
    beat_block = extract_stichera_block(
        text,
        r'[Bb]eatitudes?',
        [r'Troparion', r'Kontakion', r'Prokeimenon', r'[Ee]pistle', r'[Aa]postle']
    )
    if beat_block:
        parts['beatitudes'] = clean_text(beat_block)

    # Troparion
    trop_block = extract_stichera_block(
        text,
        r'Troparion',
        [r'Kontakion', r'Prokeimenon', r'[Ee]pistle']
    )
    if trop_block:
        parts['troparion'] = clean_text(trop_block)

    # Kontakion
    kont_block = extract_stichera_block(
        text,
        r'Kontakion',
        [r'Prokeimenon', r'[Ee]pistle', r'[Aa]postle', r'[Aa]lleluia']
    )
    if kont_block:
        parts['kontakion'] = clean_text(kont_block)

    # Prokeimenon
    prok_block = extract_stichera_block(
        text,
        r'Prokeimenon',
        [r'[Ee]pistle', r'[Aa]postle', r'[Aa]lleluia', r'[Gg]ospel']
    )
    if prok_block:
        parts['prokeimenon'] = clean_text(prok_block)

    # Readings (Epistle + Gospel)
    readings_block = extract_stichera_block(
        text,
        r'(?:[Ee]pistle|[Aa]postle|THE\s+READING|[Rr]eading)',
        [r'[Cc]ommunion\s+[Hh]ymn', r'[Dd]ismissal', r'$']
    )
    if readings_block:
        parts['readings'] = clean_text(readings_block)

    # Communion hymn
    comm_block = extract_stichera_block(
        text,
        r'[Cc]ommunion\s+[Hh]ymn',
        [r'[Dd]ismissal', r'$']
    )
    if comm_block:
        parts['communion_hymn'] = clean_text(comm_block)

    return parts


# ============================================================
# Text Cleaning
# ============================================================

def clean_text(text):
    """Clean extracted text: normalize whitespace, fix common issues."""
    if not text:
        return ''
    # Remove page numbers that appear as isolated numbers
    text = re.sub(r'\n\s*\d{1,3}\s*\n', '\n', text)
    # Normalize whitespace
    text = re.sub(r'[ \t]+', ' ', text)
    # Remove leading/trailing whitespace on each line
    lines = [line.strip() for line in text.split('\n')]
    text = '\n'.join(lines)
    # Collapse multiple blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


# ============================================================
# File-to-Day Mapping
# ============================================================

# Pre-Lenten file mapping to pascha offsets
# Based on the naming convention: 0-{group}{day}
# Group 1 = Publican & Pharisee week (10 weeks before Pascha)
# Group 2 = Prodigal Son week
# Group 3 = Meatfare week
# Group 4 = Cheesefare week

TRIODION_FILE_MAP = {
    # Common texts (shared across pre-Lenten period)
    '0-01': {'type': 'common', 'desc': 'Friday/Saturday Stichera in 8 Tones'},
    '0-02': {'type': 'common', 'desc': 'Saturday common texts pt 2'},
    '0-03': {'type': 'common', 'desc': 'Saturday common texts pt 3'},

    # Publican & Pharisee week (10 weeks before Pascha, offset -70 to -64)
    '0-10': {'offset': -70, 'desc': 'Sunday of the Publican & Pharisee'},
    '0-11': {'offset': -69, 'desc': 'Mon after Publican & Pharisee'},
    '0-12': {'offset': -68, 'desc': 'Tue after Publican & Pharisee'},
    '0-13': {'offset': -67, 'desc': 'Wed after Publican & Pharisee'},
    '0-14': {'offset': -66, 'desc': 'Thu after Publican & Pharisee'},
    '0-15': {'offset': -65, 'desc': 'Fri after Publican & Pharisee'},
    '0-16': {'offset': -64, 'desc': 'Sat after Publican & Pharisee'},
    '0-17': {'offset': -63, 'desc': 'Sunday of the Prodigal Son (alt key)'},
    '0-18': {'offset': -62, 'desc': 'Mon after Prodigal Son'},

    # Prodigal Son week
    '0-27': {'offset': -56, 'desc': 'Meatfare Sunday (Sunday before Meatfare?)'},

    # Meatfare week
    '0-36': {'offset': -50, 'desc': 'Meatfare Saturday (Souls Saturday)'},
    '0-36P': {'offset': -50, 'desc': 'Meatfare Saturday Presanctified', 'variant': 'presanctified'},
    '0-37': {'offset': -49, 'desc': 'Meatfare Sunday (Last Judgment)'},

    # Cheesefare week
    '0-41': {'offset': -55, 'desc': 'Cheesefare Mon'},
    '0-42': {'offset': -54, 'desc': 'Cheesefare Tue'},
    '0-43': {'offset': -53, 'desc': 'Cheesefare Wed'},
    '0-44': {'offset': -52, 'desc': 'Cheesefare Thu'},
    '0-45': {'offset': -51, 'desc': 'Cheesefare Fri'},
    '0-46': {'offset': -50, 'desc': 'Cheesefare Sat'},
    '0-47': {'offset': -49, 'desc': 'Forgiveness Sunday'},
}

def get_triodion_lenten_offset(filename):
    """
    Calculate pascha offset for a Lenten triodion file.
    Filename format: {W}{D}.pdf where W=week(1-7), D=day(1=Mon...7=Sun)
    Clean Monday (W=1, D=1) = -48 days before Pascha
    """
    base = filename.replace('.pdf', '').replace('A', '').replace('B', '')
    if len(base) == 2 and base.isdigit():
        week = int(base[0])
        day = int(base[1])
        # Clean Monday = -48, each day adds 1, each week adds 7
        offset = -48 + (week - 1) * 7 + (day - 1)
        return offset
    return None


def get_pent_offset(filename):
    """
    Calculate pascha offset for a Pentecostarion file.
    Filename format: {W}{D}.pdf or {W}{D}-2.pdf
    W=week(1-9), D=day(0=Sun, 1=Mon...6=Sat)
    Pascha Sunday (W=1, D=0) = offset 0
    """
    base = filename.replace('.pdf', '').replace('-2', '').replace('A', '')
    if len(base) == 2 and base.isdigit():
        week = int(base[0])
        day = int(base[1])
        offset = (week - 1) * 7 + day
        return offset
    return None


# ============================================================
# Day Name Mapping
# ============================================================

WEEKDAY_NAMES = {
    0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
    4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'
}


def get_day_description(filename, source='triodion'):
    """Get a human-readable description for a file."""
    base = filename.replace('.pdf', '')

    if source == 'triodion':
        if base in TRIODION_FILE_MAP:
            return TRIODION_FILE_MAP[base].get('desc', base)
        # Lenten period
        offset = get_triodion_lenten_offset(filename)
        if offset is not None:
            clean = base.replace('A', '').replace('B', '')
            week = int(clean[0])
            day = int(clean[1])
            suffix = ''
            if 'A' in base:
                suffix = ' (Part A)'
            elif 'B' in base:
                suffix = ' (Part B)'
            day_name = WEEKDAY_NAMES.get(day, f'Day {day}')
            if week == 7:
                return f'Holy Week {day_name}{suffix}'
            return f'Lent Week {week} {day_name}{suffix}'

    elif source == 'pentecostarion':
        offset = get_pent_offset(filename)
        if offset is not None:
            clean = base.replace('-2', '').replace('A', '')
            week = int(clean[0])
            day = int(clean[1])
            day_name = WEEKDAY_NAMES.get(day, f'Day {day}')
            return f'Pascha Week {week} {day_name}'

    return base


# ============================================================
# Main Processing
# ============================================================

def process_single_pdf(filepath, source='triodion'):
    """Process a single PDF and return structured data."""
    filename = os.path.basename(filepath)
    base = filename.replace('.pdf', '')

    print(f'  Processing {filename}...', end=' ')

    # Extract text
    text = extract_pdf_text(filepath)
    if not text:
        print('EMPTY')
        return None

    # Split into services
    services = split_into_services(text)

    # Parse each service section
    result = {
        'file': filename,
        'desc': get_day_description(filename, source),
    }

    # Add offset
    if source == 'triodion':
        if base in TRIODION_FILE_MAP:
            info = TRIODION_FILE_MAP[base]
            if 'offset' in info:
                result['offset'] = info['offset']
            if 'type' in info:
                result['type'] = info['type']
        else:
            offset = get_triodion_lenten_offset(filename)
            if offset is not None:
                result['offset'] = offset
    elif source == 'pentecostarion':
        offset = get_pent_offset(filename)
        if offset is not None:
            result['offset'] = offset

    parsed_services = {}
    for svc_name, svc_text in services.items():
        if svc_name == 'full_text':
            parsed_services['full_text'] = clean_text(svc_text)
            continue

        if svc_name == 'vespers':
            parsed = parse_vespers(svc_text)
        elif svc_name == 'matins':
            parsed = parse_matins(svc_text)
        elif svc_name in ('liturgy', 'presanctified', 'typika'):
            parsed = parse_liturgy(svc_text)
        elif svc_name in ('first_hour', 'third_hour', 'sixth_hour', 'ninth_hour'):
            parsed = parse_hours(svc_text)
        elif svc_name in ('compline', 'nocturns'):
            parsed = parse_matins(svc_text)  # similar structure
        else:
            parsed = {'text': clean_text(svc_text)}

        if parsed:
            parsed_services[svc_name] = parsed

    result['services'] = parsed_services

    component_count = sum(len(v) for v in parsed_services.values() if isinstance(v, dict))
    print(f'{len(parsed_services)} services, {component_count} components')

    return result


def process_all_triodion():
    """Process all triodion PDFs."""
    print('=' * 60)
    print('EXTRACTING TRIODION')
    print('=' * 60)

    results = {}
    files = sorted([f for f in os.listdir(TRIOD_DIR) if f.endswith('.pdf')])

    for filename in files:
        filepath = os.path.join(TRIOD_DIR, filename)
        data = process_single_pdf(filepath, source='triodion')
        if data:
            key = filename.replace('.pdf', '')
            results[key] = data

    return results


def process_all_pentecostarion():
    """Process all pentecostarion PDFs."""
    print('\n' + '=' * 60)
    print('EXTRACTING PENTECOSTARION')
    print('=' * 60)

    results = {}
    files = sorted([f for f in os.listdir(PENT_DIR) if f.endswith('.pdf')])

    for filename in files:
        filepath = os.path.join(PENT_DIR, filename)
        data = process_single_pdf(filepath, source='pentecostarion')
        if data:
            key = filename.replace('.pdf', '')
            results[key] = data

    return results


# ============================================================
# Output Generation
# ============================================================

def write_json_data(results, output_path):
    """Write extracted data as a JSON file."""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f'\nWrote {len(results)} entries to {output_path}')


def write_python_loader(json_path, output_path, var_name):
    """Write a Python file that loads the JSON data."""
    json_filename = os.path.basename(json_path)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f'"""\n{var_name.title()} - Auto-extracted from PDFs\n')
        f.write(f'Generated by database/extract_services.py\n')
        f.write(f'Data loaded from {json_filename}\n"""\n\n')
        f.write(f'import json\n')
        f.write(f'import os\n\n')
        f.write(f'_dir = os.path.dirname(os.path.abspath(__file__))\n')
        f.write(f"_json_path = os.path.join(_dir, 'database', '{json_filename}')\n\n")
        f.write(f'with open(_json_path, "r", encoding="utf-8") as _f:\n')
        f.write(f'    {var_name} = json.load(_f)\n')
    print(f'Wrote loader to {output_path}')


# ============================================================
# Entry Point
# ============================================================

def main():
    args = sys.argv[1:]

    if '--test' in args:
        # Test on a few sample files
        print('TEST MODE: Processing sample files\n')
        samples = [
            (os.path.join(TRIOD_DIR, '0-10.pdf'), 'triodion'),
            (os.path.join(TRIOD_DIR, '13.pdf'), 'triodion'),
            (os.path.join(TRIOD_DIR, '16.pdf'), 'triodion'),
            (os.path.join(TRIOD_DIR, '75.pdf'), 'triodion'),
            (os.path.join(PENT_DIR, '30.pdf'), 'pentecostarion'),
            (os.path.join(PENT_DIR, '32-2.pdf'), 'pentecostarion'),
        ]
        for filepath, source in samples:
            if os.path.exists(filepath):
                data = process_single_pdf(filepath, source)
                if data:
                    print(f'    Services: {list(data["services"].keys())}')
                    for svc, parts in data['services'].items():
                        if isinstance(parts, dict):
                            print(f'    {svc}: {list(parts.keys())}')
                    print()
        return

    triodion_data = None
    pent_data = None
    db_dir = os.path.join(BASE_DIR, 'database')

    if '--pent-only' not in args:
        triodion_data = process_all_triodion()
        json_path = os.path.join(db_dir, 'triodion_data.json')
        write_json_data(triodion_data, json_path)
        loader_path = os.path.join(BASE_DIR, 'triodion_data.py')
        write_python_loader(json_path, loader_path, 'triodion_data')

    if '--triodion-only' not in args:
        pent_data = process_all_pentecostarion()
        json_path = os.path.join(db_dir, 'pentecostarion_data.json')
        write_json_data(pent_data, json_path)
        loader_path = os.path.join(BASE_DIR, 'pentecostarion_data.py')
        write_python_loader(json_path, loader_path, 'pentecostarion_data')

    # Summary
    print('\n' + '=' * 60)
    print('EXTRACTION COMPLETE')
    print('=' * 60)
    if triodion_data:
        total_svc = sum(len(d.get('services', {})) for d in triodion_data.values())
        print(f'  Triodion:       {len(triodion_data)} days, {total_svc} service sections')
    if pent_data:
        total_svc = sum(len(d.get('services', {})) for d in pent_data.values())
        print(f'  Pentecostarion: {len(pent_data)} days, {total_svc} service sections')


if __name__ == '__main__':
    main()
