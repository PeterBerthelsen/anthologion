"""Variable calculation and template-slot placement."""

import sys
from datetime import date
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from assembly import (  # noqa: E402
    assemble_stichera,
    is_structured_hymn_list,
    pad_stichera,
)
from resolver import paschalion, resolve, resolve_service  # noqa: E402


KNOWN_PASCHA = {
    2021: date(2021, 5, 2),
    2022: date(2022, 4, 24),
    2023: date(2023, 4, 16),
    2024: date(2024, 5, 5),
    2025: date(2025, 4, 20),
    2026: date(2026, 4, 12),
    2027: date(2027, 5, 2),
    2028: date(2028, 4, 16),
}


def _dt(p):
    return p.date() if hasattr(p, 'date') else p


@pytest.mark.parametrize('year,expected', list(KNOWN_PASCHA.items()))
def test_paschalion_known_orthodox_pascha(year, expected):
    p = paschalion(expected.month, expected.day, year)
    assert _dt(p['pascha']) == expected
    assert p['is_pascha'] is True
    assert p['pascha_offset'] == 0


def test_pad_stichera_left_pads_to_ten():
    padded = pad_stichera(['a', 'b', 'c'])
    assert len(padded) == 10
    assert padded[:7] == [''] * 7
    assert padded[-3:] == ['a', 'b', 'c']
    # Template uses negative indexes: last hymn at -1
    assert padded[-1] == 'c'
    assert padded[-10] == ''


def test_blob_is_not_structured():
    blob = '...,” 6 Stichera from the Oktoechos, in Tone II:'
    assert is_structured_hymn_list(blob) is False
    assert is_structured_hymn_list([blob]) is False
    assert is_structured_hymn_list(['<p>Receive our evening prayers</p>'] * 6) is True


def test_sunday_ordinary_is_seven_oct_plus_three_men():
    oct_h = [f'o{i}' for i in range(7)]
    men_h = [f'm{i}' for i in range(3)]
    out = assemble_stichera(5, 6, oct_h, men_h)
    sung = [x for x in out if x]
    assert sung == [f'o{i}' for i in range(7)] + ['m0', 'm1', 'm2']


def test_vigil_weekday_is_eight_menaion_only():
    oct_h = [f'o{i}' for i in range(6)]
    men_h = [f'm{i}' for i in range(3)]
    out = assemble_stichera(2, 0, oct_h, men_h)
    sung = [x for x in out if x]
    assert len(sung) == 8
    assert all(s.startswith('m') for s in sung)
    assert out[-10] == ''
    assert out[-9] == ''


def test_weekday_six_stichera_is_three_oct_plus_three_men():
    oct_h = [f'o{i}' for i in range(6)]
    men_h = [f'm{i}' for i in range(3)]
    # weekday Monday, rank 5
    out = assemble_stichera(5, 0, oct_h, men_h)
    assert len(out) == 10
    sung = [x for x in out if x]
    assert sung == ['o0', 'o1', 'o2', 'm0', 'm1', 'm2']
    assert out[-1] == 'm2'
    assert out[-4] == 'o2'
    assert out[-10] == ''


def test_old_calendar_nativity_theotokos_on_civil_sep_21_2026():
    ctx = resolve(9, 21, 2026, calendar=1)
    assert ctx['calendar'] == 1
    assert ctx['menaion_date'] == '09-08'
    assert ctx['feast']['long_name'] == 'The Nativity of the Mother of God'
    vs = resolve_service(9, 21, 2026, 'vespers', calendar=1)
    assert isinstance(vs['stichera'], list)
    assert len(vs['stichera']) == 10
    sung = [s for s in vs['stichera'] if s]
    assert len(sung) >= 6
    # Last slot must be a menaion hymn (name substituted), not an empty wrap.
    assert vs['stichera'][-1]
    assert '(name)' not in vs['stichera'][-1]
    joined = '\n'.join(sung)
    assert 'noetic thrones' in joined
    assert 'full_menaion' in vs['_sources']
    assert vs['_primary'] == 'full_menaion'


def test_ordinary_saint_does_not_use_full_menaion():
    ctx = resolve(9, 8, 2026, calendar=1)  # old cal → 08-26 Adrian
    assert ctx.get('full_menaion') in (None, {})
    assert ctx['menaion_source'] != 'full'


def test_new_calendar_nativity_theotokos_on_civil_sep_8_2026():
    ctx = resolve(9, 8, 2026, calendar=0)
    assert ctx['calendar'] == 0
    assert ctx['menaion_date'] == '09-08'
    assert ctx['feast']['long_name'] == 'The Nativity of the Mother of God'


def test_old_and_new_calendar_differ_on_same_civil_date():
    old = resolve(9, 8, 2026, calendar=1)
    new = resolve(9, 8, 2026, calendar=0)
    assert old['menaion_date'] == '08-26'
    assert new['menaion_date'] == '09-08'
    assert old['feast']['long_name'] != new['feast']['long_name']
    # Pascha math is civil/Julian-Pascha and does not flip with the menaion calendar.
    assert old['liturgical']['pascha_offset'] == new['liturgical']['pascha_offset']


def test_sunday_tone_cycle_has_octoechos_and_ten_slots():
    ctx = resolve(11, 8, 2026, calendar=0)
    assert ctx['weekday'] == 6
    assert ctx['octoechos'] is not None
    vs = resolve_service(11, 8, 2026, 'vespers', calendar=0)
    assert len(vs['stichera']) == 10
    assert vs['stichera'][-1]  # last verse has a hymn


def test_lent_does_not_replace_stichera_list_with_pdf_blob():
    # Clean Monday 2026 = Feb 23 (Pascha Apr 12, offset -48)
    ctx = resolve(2, 23, 2026, calendar=1)
    assert ctx['period'] in ('lent', 'pre_lent')
    assert ctx['triodion'] is not None
    vs = resolve_service(2, 23, 2026, 'vespers', calendar=1)
    assert isinstance(vs['stichera'], list)
    assert len(vs['stichera']) == 10
    assert not any(isinstance(s, str) and s.strip().startswith('...,') for s in vs['stichera'])
    # Blob preserved as a note, not as the verse list.
    if vs.get('stichera_block'):
        assert 'Stichera' in vs['stichera_block'] or '...' in vs['stichera_block'][:20]


def test_pascha_resolves_pentecostarion():
    ctx = resolve(4, 12, 2026, calendar=1)
    assert ctx['period'] == 'paschal'
    assert ctx['pentecostarion'] is not None
    assert ctx['pentecostarion']['key'] == '10'


def test_name_placeholder_substituted():
    vs = resolve_service(1, 7, 2026, 'vespers', calendar=1)  # Nativity on old calendar
    blob = ' '.join(s for s in vs['stichera'] if s)
    assert '(name)' not in blob
    for key, val in vs.items():
        if isinstance(val, str):
            assert '(name)' not in val
