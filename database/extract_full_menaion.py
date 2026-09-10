"""
Extract St. Sergius Full Menaion (Emenaion) PDFs for the twelve Great Feasts.

Nine fixed feasts live in services/emenaion/MM-DD.pdf.
Three moveable feasts (Palm Sunday, Ascension, Pentecost) stay in
Triodion/Pentecostarion; they are catalogued here so the resolver can
prefer them the same way.

Usage:
    python3 database/extract_full_menaion.py
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE_DIR))

try:
    import fitz
except ImportError:
    print('ERROR: pymupdf required')
    raise SystemExit(1)


FIXED_GREAT_FEASTS = {
    '09-08': {
        'name': 'The Nativity of the Mother of God',
        'files': ['09-08.pdf'],
        'rank': 2,
    },
    '09-14': {
        'name': 'The Universal Exaltation of the Precious Cross',
        'files': ['09-14.pdf'],
        'rank': 1,
    },
    '11-21': {
        'name': 'The Entrance of the Theotokos into the Temple',
        'files': ['11-21.pdf'],
        'rank': 2,
    },
    '12-25': {
        'name': 'The Nativity of Our Lord Jesus Christ',
        'files': ['12-25.pdf'],
        'rank': 1,
    },
    '01-06': {
        'name': 'The Holy Theophany of our Lord Jesus Christ',
        'files': ['01-06.pdf'],
        'rank': 1,
    },
    '02-02': {
        'name': 'The Meeting of our Lord',
        'files': ['02-02.pdf'],
        'rank': 2,
    },
    '03-25': {
        'name': 'The Annunciation of the Theotokos',
        'files': ['03-25.pdf'],
        'rank': 2,
    },
    '08-06': {
        'name': 'The Transfiguration of our Lord',
        'files': ['08-06.pdf'],
        'rank': 2,
    },
    '08-15': {
        'name': 'The Dormition of the Theotokos',
        'files': ['08-15.pdf'],
        'rank': 2,
    },
}

MOVEABLE_GREAT_FEASTS = {
    'palm_sunday': {
        'name': 'Palm Sunday — The Entrance of the Lord into Jerusalem',
        'source': 'triodion',
        'rank': 1,
    },
    'ascension': {
        'name': 'The Ascension of our Lord',
        'source': 'pentecostarion',
        'rank': 1,
    },
    'pentecost': {
        'name': 'Pentecost — Holy Trinity Day',
        'source': 'pentecostarion',
        'rank': 1,
    },
}

RUBRIC_ONLY = re.compile(
    r'^(On [“"]Lord|Spec\.?\s*Mel|Verse:|The composition of|Glory|Both now|'
    r'After the Introductory|We chant|Entrance|Prokeimenon|Then |And |'
    r'At Litiya|At the blessing|Note:|N\.B\.)',
    re.I,
)


def pdf_text(path: Path) -> str:
    doc = fitz.open(path)
    text = '\n'.join(page.get_text() for page in doc)
    doc.close()
    text = text.replace('\u00ad', '')  # soft hyphen
    text = re.sub(r'-\n(?=[a-z])', '', text)  # dehyphenate
    return text


def split_services(text: str) -> dict[str, str]:
    markers = [
        (r'(?m)^[ \t]*AT\s+LITTLE\s+VESPERS', 'little_vespers'),
        (r'(?m)^[ \t]*AT\s+SMALL\s+VESPERS', 'little_vespers'),
        (r'(?m)^[ \t]*AT\s+GREAT\s+VESPERS', 'vespers'),
        (r'(?m)^[ \t]*AT\s+VESPERS', 'vespers'),
        (r'(?m)^[ \t]*AT\s+MATINS', 'matins'),
        (r'(?m)^[ \t]*AT\s+(?:THE\s+)?LITURGY', 'liturgy'),
        (r'(?m)^[ \t]*AT\s+COMPLINE', 'compline'),
    ]
    hits = []
    for pat, name in markers:
        for m in re.finditer(pat, text, re.I):
            hits.append((m.start(), name, m.group()))
    hits.sort()
    # First AT VESPERS after LITTLE should not overwrite GREAT if GREAT exists.
    sections: dict[str, str] = {}
    for i, (pos, name, _) in enumerate(hits):
        end = hits[i + 1][0] if i + 1 < len(hits) else len(text)
        chunk = text[pos:end]
        if name == 'vespers' and 'vespers' in sections:
            # Keep GREAT if we already stored it; replace only if current is GREAT.
            if re.match(r'AT\s+GREAT', chunk, re.I):
                sections['vespers'] = chunk
            continue
        if name not in sections:
            sections[name] = chunk
    return sections


def _paras(block: str) -> list[str]:
    block = re.sub(r'[ \t]+', ' ', block)
    block = re.sub(r'\n{2,}', '\n\n', block)
    # Join wrapped lines inside a paragraph
    paras = []
    for raw in re.split(r'\n\s*\n', block):
        p = ' '.join(raw.split()).strip()
        if p:
            paras.append(p)
    return paras


def _hymn_html(text: str) -> str:
    text = text.strip()
    text = re.sub(r'\s*\(Twice\)\s*$', '', text, flags=re.I)
    return f'<p><i class="note">*</i>{text}</p>'


def extract_stichera(section: str) -> tuple[str, list[str]]:
    """Return (tone_note, list of hymn HTML) from Lord I have Cried."""
    m = re.search(
        r'On\s.{0,8}Lord,?\s+I have cried.{0,700}?:',
        section, re.I | re.S,
    )
    if not m:
        m = re.search(
            r'(?:chant|sing)\s+.{0,80}Lord,?\s+I have cried.{0,400}',
            section, re.I | re.S,
        )
    if not m:
        return '', []
    tone_html = f'<p><i class="note">{" ".join(m.group(0).split())}</i></p>'
    rest = section[m.end():]
    end_m = re.search(
        r'(Glory\s*\.\.\.|Both now\s*\.\.\.|Entrance\.|At Litiya|'
        r'On the Aposticha|THE READING|A READING FROM|'
        r'Entrance with the Gospel)',
        rest, re.I,
    )
    body = rest[:end_m.start()] if end_m else rest[:6000]
    hymns = split_hymn_run(' '.join(body.split()))
    return tone_html, [_hymn_html(h) for h in hymns]


_STARTER = re.compile(
    r'(?<=[.!?])\s+(?=(?:Today|Come,|Come |When |What |Even though|'
    r'Tell us|Before Thy|The forerunner|Let us join|O wondrous|'
    r'Raised on high|Thy kingdom|Desiring to save|Having |'
    r'The currents|The Cross is|Moses |Who is |She who |'
    r'Joachim |This is the day))'
)


def _subsplit(chunk: str) -> list[str]:
    chunk = chunk.strip()
    chunk = re.sub(r'^The composition of[^:]+:\s*', '', chunk, flags=re.I)
    chunk = re.sub(
        r'The priest performeth.{0,250}?(?:usual|feast)\.?\s*',
        '', chunk, flags=re.I,
    )
    if not chunk or RUBRIC_ONLY.match(chunk) or len(chunk) < 40:
        return []
    parts = [p.strip() for p in _STARTER.split(chunk) if p.strip()]
    # re.split with capturing? _STARTER is lookaround so split keeps text
    parts = [p for p in parts if len(p) > 40]
    return parts or ([chunk] if len(chunk) > 40 else [])


def split_hymn_run(text: str) -> list[str]:
    text = re.sub(r'\s+', ' ', text).strip()
    parts = re.split(r'(\(\s*Twice\s*\))', text, flags=re.I)
    hymns: list[str] = []
    pending = ''
    for part in parts:
        if re.fullmatch(r'\(\s*Twice\s*\)', part.strip(), re.I):
            subs = _subsplit(pending)
            pending = ''
            if not subs:
                continue
            hymns.extend(subs[:-1])
            hymns.append(subs[-1])
            hymns.append(subs[-1])
        else:
            pending += part
    hymns.extend(_subsplit(pending))
    cleaned = []
    for h in hymns:
        h = re.sub(r'^In Tone [IVXL]+[:.]\s*', '', h, flags=re.I).strip()
        if len(h) >= 50 and not h.lower().startswith('from the triodion') \
                and not h.startswith(',') and 'choirs chant' not in h.lower() \
                and 'Stichera of the feast' not in h \
                and 'Idiomelon' not in h:
            cleaned.append(h)
    return cleaned


def extract_aposticha(section: str) -> str:
    m = re.search(r'On the Aposticha.{0,200}?:', section, re.I | re.S)
    if not m:
        return ''
    rest = section[m.end():]
    end_m = re.search(
        r'(Troparion|Now lettest|AT MATINS|Dismissal|At the blessing)',
        rest, re.I,
    )
    body = rest[:end_m.start()] if end_m else rest[:2500]
    parts = [_hymn_html(p) for p in _paras(body)
             if not RUBRIC_ONLY.match(p) and len(p) > 40]
    return '\n'.join(parts)


def extract_named(section: str, label: str) -> str:
    m = re.search(
        rf'{label}[^:]{{0,80}}:',
        section, re.I,
    )
    if not m:
        return ''
    rest = section[m.end():]
    end_m = re.search(
        r'(Kontakion|Ikos|Prokeimenon|Glory|Both now|Dismissal|'
        r'AT LITURGY|Troparion|Theotokion)',
        rest, re.I,
    )
    body = rest[:end_m.start()] if end_m else rest[:800]
    para = ' '.join(body.split()).strip()
    para = para[:1200]
    if not para:
        return ''
    return f'<p>{para}</p>'


def extract_file(path: Path) -> dict:
    text = pdf_text(path)
    sections = split_services(text)
    services = {}
    vespers_src = sections.get('vespers')
    if not vespers_src or not extract_stichera(vespers_src)[1]:
        # Nativity/Theophany start vespers without an AT GREAT VESPERS header.
        vespers_src = vespers_src or text
        if not extract_stichera(vespers_src)[1]:
            vespers_src = text
    if vespers_src:
        tone, stichera = extract_stichera(vespers_src)
        trop = extract_named(vespers_src, r'Troparion(?: of the feast)?')
        services['vespers'] = {
            'stichera_tone': tone,
            'stichera': stichera,
            'aposticha': extract_aposticha(vespers_src),
            'apolytichion': trop,
            'theotokion': '',
        }
    if 'matins' in sections:
        trop = extract_named(sections['matins'], r'Troparion(?: of the feast)?')
        kont = extract_named(sections['matins'], r'Kontakion(?: of the feast)?')
        services['matins'] = {
            'troparion': trop,
            'kontakion': kont,
            'apolytichion': trop,
        }
    if 'liturgy' in sections:
        trop = extract_named(sections['liturgy'], r'Troparion(?: of the feast)?')
        kont = extract_named(sections['liturgy'], r'Kontakion(?: of the feast)?')
        services['liturgy'] = {
            'troparion': trop,
            'kontakion': kont,
        }
    return services


def main():
    src_dir = BASE_DIR / 'services' / 'emenaion'
    out = {}
    print('=' * 60)
    print('EXTRACTING FULL MENAION — 9 fixed Great Feasts')
    print('=' * 60)
    for key, meta in FIXED_GREAT_FEASTS.items():
        fname = meta['files'][0]
        path = src_dir / fname
        print(f'  {key} {fname}...', end=' ')
        if not path.exists():
            print('MISSING')
            continue
        services = extract_file(path)
        ves = (services.get('vespers') or {}).get('stichera') or []
        print(f'vespers stichera={len(ves)} services={list(services)}')
        out[key] = {
            'date': key,
            'name': meta['name'],
            'rank': meta['rank'],
            'source': 'emenaion',
            'file': fname,
            'services': services,
        }

    json_path = BASE_DIR / 'database' / 'full_menaion_data.json'
    json_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'\nWrote {len(out)} feasts to {json_path}')

    catalog = {
        'fixed': FIXED_GREAT_FEASTS,
        'moveable': MOVEABLE_GREAT_FEASTS,
        'priority': ['full_menaion', 'general_menaion', 'octoechos'],
    }
    cat_path = BASE_DIR / 'database' / 'great_feasts.json'
    cat_path.write_text(json.dumps(catalog, indent=2) + '\n', encoding='utf-8')
    print(f'Wrote catalog {cat_path}')


if __name__ == '__main__':
    main()
