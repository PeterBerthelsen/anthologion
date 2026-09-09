"""
Typikon assembly for liturgical variables.

The JSON books hold raw hymns. Templates expect a 10-slot Lord I have Cried
list (index -10 = first inserted verse through -1 = last). This module:

1. Treats truncated PDF blobs as notes, not structured stichera.
2. Combines octoechos + menaion using the existing rank/weekday counts
   from service.py (duplicate early hymns when a book is short).
3. Left-pads to 10 so template negative indexes hit the right verses.
"""

from __future__ import annotations

import re
from typing import Any


STICHERA_SLOTS = 10

# Rank → (octoechos count, menaion count) for weekdays / Sundays.
# St. Sergius:
#   oktiochos/1-1.pdf Great Vespers: 7 Resurrection + 3 saint, or 4+6 if Polyeleos.
#   Emenaion/09-08.pdf Great Vespers: 8 stichera of the feast.
#   weekday oktiochos (e.g. 7-2.pdf): 3 repentance + menaion (or 3 angels).
_STICHERA_COUNTS = {
    1: {'weekday': (0, 8), 'sunday': (0, 8)},
    2: {'weekday': (0, 8), 'sunday': (4, 6)},
    3: {'weekday': (0, 6), 'sunday': (4, 6)},
    4: {'weekday': (3, 3), 'sunday': (7, 3)},
    5: {'weekday': (3, 3), 'sunday': (7, 3)},
    6: {'weekday': (3, 3), 'sunday': (7, 3)},
}


_BLOB_RE = re.compile(
    r'^\s*(?:\.\.\.|…)|Stichera from the|Oktoechos|Triodion|Pentecostarion',
    re.I,
)


def is_structured_hymn_list(value: Any) -> bool:
    """True if value is a list of individual hymn HTML/text strings."""
    if not isinstance(value, list) or not value:
        return False
    if not all(isinstance(x, str) for x in value):
        return False
    # A single truncated extractor blob stuffed in a 1-item list is not usable.
    if len(value) == 1 and _looks_like_blob(value[0]):
        return False
    return True


def _looks_like_blob(text: str) -> bool:
    if not text or not isinstance(text, str):
        return False
    stripped = text.strip()
    if stripped.startswith('...,') or stripped.startswith('…'):
        return True
    if 'Stichera from the' in stripped[:400]:
        return True
    if stripped.startswith('...,”') or '10 Stichera' in stripped[:200]:
        return True
    return bool(_BLOB_RE.match(stripped[:120]))


def as_hymn_list(value: Any) -> list[str]:
    """Coerce a field to a list of hymn strings; blobs/empty → []."""
    if value is None or value == '':
        return []
    if is_structured_hymn_list(value):
        return [v for v in value if v]
    if isinstance(value, str) and not _looks_like_blob(value):
        # A single complete hymn (or HTML block that is the hymn itself).
        if '<p>' in value and value.count('<p>') >= 2 and _looks_like_blob(value):
            return []
        if _looks_like_blob(value):
            return []
        return [value]
    return []


def blob_note(value: Any) -> str | None:
    """Return unstructured extractor text so it is not silently dropped."""
    if isinstance(value, str) and _looks_like_blob(value):
        return value
    if isinstance(value, list) and len(value) == 1 and _looks_like_blob(value[0]):
        return value[0]
    return None


def _repeat_to_count(hymns: list[str], needed: int) -> list[str]:
    """Duplicate earliest hymns when the book is short (service.py)."""
    if needed <= 0:
        return []
    if not hymns:
        return []
    if len(hymns) >= needed:
        return hymns[:needed]
    out: list[str] = []
    duplicates = needed - len(hymns)
    for i, s in enumerate(hymns):
        out.append(s)
        if i + 1 <= duplicates:
            out.append(s)
    # If still short (very small source lists), cycle.
    i = 0
    while len(out) < needed and hymns:
        out.append(hymns[i % len(hymns)])
        i += 1
    return out[:needed]


def assemble_stichera(rank: int, weekday: int,
                      oct_stichera: Any, men_stichera: Any,
                      fill_stichera: Any = None) -> list[str]:
    """
    Build Lord I have Cried stichera for a date.

    weekday: 0=Mon … 6=Sun (datetime.date.weekday)
    rank: 1–7 (7 = simple / octoechos only)
    """
    oct_list = as_hymn_list(oct_stichera)
    men_list = as_hymn_list(men_stichera)
    fill_list = as_hymn_list(fill_stichera)
    sunday = weekday == 6

    if rank == 7 or not (men_list or fill_list):
        if sunday:
            chosen = oct_list[:7]
        else:
            chosen = oct_list[:6]
        return pad_stichera(chosen)

    counts = _STICHERA_COUNTS.get(rank, _STICHERA_COUNTS[5])
    oct_needed, men_needed = counts['sunday' if sunday else 'weekday']

    oct_source = oct_list[:7] if sunday else oct_list[:3]
    men_source = list(men_list)
    if len(men_source) < men_needed:
        men_source = men_source + fill_list
    assembled = _repeat_to_count(oct_source, oct_needed) + _repeat_to_count(
        men_source, men_needed
    )
    return pad_stichera(assembled)


def pad_stichera(stichera: list[str], n: int = STICHERA_SLOTS) -> list[str]:
    """Left-pad with empty strings so template indexes [-n]…[-1] are safe."""
    items = [s for s in (stichera or []) if s is not None]
    if len(items) < n:
        return [''] * (n - len(items)) + items
    if len(items) > n:
        return items[-n:]
    return items


def first_nonempty(*values: Any) -> Any:
    for v in values:
        if v:
            return v
    return ''


def merge_service(service_type: str, *, rank: int, weekday: int,
                  period: str, oct_svc: dict | None, men_svc: dict | None,
                  tri_svc: dict | None, pent_svc: dict | None,
                  full_svc: dict | None = None) -> dict:
    """
    Merge one service's variables.

    Structured hymn lists are assembled. Extractor blobs become *_block notes
    so they cannot overwrite a good octoechos/menaion list.
    """
    oct_svc = oct_svc if isinstance(oct_svc, dict) else {}
    men_svc = men_svc if isinstance(men_svc, dict) else {}
    full_svc = full_svc if isinstance(full_svc, dict) else {}
    tri_svc = tri_svc if isinstance(tri_svc, dict) else {}
    pent_svc = pent_svc if isinstance(pent_svc, dict) else {}

    if period in ('lent', 'pre_lent'):
        moveable = tri_svc
        moveable_name = 'triodion'
    elif period == 'paschal':
        moveable = pent_svc
        moveable_name = 'pentecostarion'
    else:
        moveable = {}
        moveable_name = 'menaion' if men_svc else 'octoechos'

    merged: dict[str, Any] = {}

    # Start with octoechos scalars (tone markings, aposticha, etc.)
    for k, v in oct_svc.items():
        if k == 'stichera':
            continue
        if v:
            merged[k] = v

    # Menaion scalars overlay when present
    if rank != 7:
        for k, v in men_svc.items():
            if k == 'stichera':
                continue
            note = blob_note(v)
            if note:
                merged.setdefault(f'{k}_block', note)
                continue
            if v:
                merged[k] = v

    # Full Menaion (great feasts) overlays general
    if rank != 7:
        for k, v in full_svc.items():
            if k == 'stichera':
                continue
            if v:
                merged[k] = v

    # Moveable book scalars overlay; blobs become notes
    if rank != 7:
        for k, v in moveable.items():
            if k == 'stichera':
                continue
            note = blob_note(v)
            if note:
                merged[f'{k}_block'] = note
                continue
            structured = as_hymn_list(v)
            if structured:
                merged[k] = structured if k in ('stichera',) else v
            elif v and not isinstance(v, list):
                merged[k] = v

    has_full = bool(as_hymn_list(full_svc.get('stichera')))
    stichera = assemble_stichera(
        rank, weekday, oct_svc.get('stichera'),
        full_svc.get('stichera') if has_full else (men_svc.get('stichera') if rank != 7 else None),
        fill_stichera=men_svc.get('stichera') if has_full else None,
    )

    # Moveable structured stichera only when this is not a full great feast.
    moveable_stichera = as_hymn_list(moveable.get('stichera'))
    if rank != 7 and moveable_stichera and not has_full:
        stichera = assemble_stichera(
            rank, weekday, oct_svc.get('stichera'), moveable_stichera,
            fill_stichera=men_svc.get('stichera'),
        )
    elif not has_full:
        note = blob_note(moveable.get('stichera'))
        if note:
            merged['stichera_block'] = note

    if has_full:
        moveable_name = 'full_menaion'

    merged['stichera'] = stichera
    merged['_moveable_book'] = moveable_name
    return merged
