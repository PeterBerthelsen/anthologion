"""
Unified variable resolver for the Anthologion.

Given a date, determines the liturgical position and returns all variables
needed to assemble any service, sourced entirely from pre-extracted JSON data.

Priority chain:
  - Normal period:  Menaion (primary) → Octoechos (fill)
  - Lent/Pre-Lent:  Triodion (primary) → Menaion → Octoechos
  - Paschal period:  Pentecostarion (primary) → Menaion → Octoechos

Usage:
    from resolver import resolve
    ctx = resolve(2, 26, 2026)
    vespers = ctx['services']['vespers']
"""

import os
import json
from datetime import datetime, timedelta, date

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Load JSON data once at import
# ---------------------------------------------------------------------------
def _load(name):
    path = os.path.join(BASE_DIR, 'database', name)
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

_triodion = _load('triodion_data.json')
_pentecostarion = _load('pentecostarion_data.json')
_octoechos = _load('octoechos_data.json')
_menaion = _load('menaion_data.json')
try:
    _full_menaion = _load('full_menaion_data.json')
except FileNotFoundError:
    _full_menaion = {}

# Build pentecostarion offset→key lookup
_pent_by_offset = {}
for _k, _v in _pentecostarion.items():
    off = _v.get('offset')
    if off is not None:
        _pent_by_offset.setdefault(off, []).append(_k)


# ---------------------------------------------------------------------------
# Paschalion — copied from service.py to avoid circular imports
# ---------------------------------------------------------------------------
def paschalion(month, day, year):
    month = int(month) if isinstance(month, str) else month
    day = int(day) if isinstance(day, str) else day
    year = int(year) if isinstance(year, str) else year

    Y = year
    # Old-Calendar offset
    if Y <= 2099:
        O = 13
    elif Y <= 2199:
        O = 14
    elif Y <= 2299:
        O = 15
    else:
        O = 15

    a = Y % 4
    b = Y % 7
    c = Y % 19
    d = ((19 * c) + 15) % 30
    e = ((2 * a) + (4 * b) - d + 34) % 7
    f = d + e + 114
    M = f // 31
    D = (f % 31) + 1

    T = datetime(Y, month, day)
    this_pascha = datetime(Y, M, D) + timedelta(days=O)
    this_pentecost = this_pascha + timedelta(days=49)

    pascha_offset = (T - this_pascha).days

    last_pascha = last_pentecost = lent_week = pascha_week = weeks_after = weekly_tone = None

    if pascha_offset < -70:
        lp = paschalion(12, 31, Y - 1)
        last_pentecost = lp['pentecost']
        weeks_after = (((T - last_pentecost).days - 1) // 7) + 1
    elif -70 <= pascha_offset <= -49:
        lent_week = (pascha_offset + 48) // 7
    elif -49 < pascha_offset < 0:
        lent_week = ((pascha_offset + 48) // 7) + 1
    elif 0 <= pascha_offset <= 49:
        pascha_week = (pascha_offset // 7) + 1
    elif pascha_offset > 49:
        weeks_after = (((T - this_pentecost).days - 1) // 7) + 1

    # Tone
    if pascha_week:
        weekly_tone = None if pascha_week in (1, 8) else (pascha_week - 1)
    elif -7 <= pascha_offset < 0:
        weekly_tone = None
    elif pascha_offset > 0:
        weekly_tone = pascha_offset // 7
        weekly_tone = (weekly_tone % 8) if weekly_tone > 8 else weekly_tone
        weekly_tone = 8 if not weekly_tone else weekly_tone
    elif pascha_offset < 0:
        lp = paschalion(12, 31, Y - 1)
        last_pascha_dt = lp['pascha']
        lpo = (T - last_pascha_dt).days
        weekly_tone = lpo // 7
        weekly_tone = (weekly_tone % 8) if weekly_tone > 8 else weekly_tone
        weekly_tone = 8 if not weekly_tone else weekly_tone

    return {
        'pascha': this_pascha,
        'pentecost': this_pentecost,
        'pascha_offset': pascha_offset,
        'is_pascha': T == this_pascha,
        'is_pentecost': T == this_pentecost,
        'lent_week': lent_week,
        'pascha_week': pascha_week,
        'weeks_after': weeks_after,
        'weekly_tone': weekly_tone,
    }


# ---------------------------------------------------------------------------
# Triodion key mapping (pascha_offset → JSON key)
# ---------------------------------------------------------------------------

# Pre-Lenten explicit mapping: offset → key
_PRE_LENTEN = {
    -70: '0-10',  # Sunday of the Publican & Pharisee
    -69: '0-11', -68: '0-12', -67: '0-13',
    -66: '0-14', -65: '0-15', -64: '0-16',
    -63: '0-17',  # Sunday of the Prodigal Son
    -62: '0-18',  # Mon after Prodigal Son
    # Tue–Fri after Prodigal Son: no triodion content
    -57: '0-36',  # Meatfare Saturday (Souls Saturday)
    -56: '0-37',  # Meatfare Sunday (Last Judgment)
    -55: '0-41',  # Cheesefare Monday
    -54: '0-42', -53: '0-43', -52: '0-44',
    -51: '0-45', -50: '0-46',
    -49: '0-47',  # Forgiveness Sunday
}


def _triodion_key(pascha_offset):
    """Map pascha_offset to triodion JSON key, or None if not applicable."""
    if pascha_offset < -70 or pascha_offset >= 0:
        return None

    # Pre-Lenten period: offset -70 to -49
    if pascha_offset <= -49:
        return _PRE_LENTEN.get(pascha_offset)

    # Lent proper: offset -48 (Clean Monday) to -1 (Great Saturday)
    days_into_lent = pascha_offset + 48  # 0-based
    week = (days_into_lent // 7) + 1     # 1–7
    day_in_week = (days_into_lent % 7) + 1  # 1=Mon .. 7=Sun
    return f'{week}{day_in_week}'


def _pentecostarion_key(pascha_offset):
    """Map pascha_offset to pentecostarion JSON key, or None."""
    if pascha_offset < 0 or pascha_offset > 56:
        return None
    keys = _pent_by_offset.get(pascha_offset)
    if not keys:
        return None
    # Prefer the primary key (shorter, no suffix)
    keys_sorted = sorted(keys, key=len)
    return keys_sorted[0]


# ---------------------------------------------------------------------------
# Octoechos key mapping
# ---------------------------------------------------------------------------
def _octoechos_key(tone, weekday):
    """Map tone (1-8) and weekday (0=Mon .. 6=Sun) to octoechos JSON key."""
    if tone is None:
        return None
    # Sergius day mapping: Sat eve/Sun=1, Sun eve/Mon=2, ... Fri eve/Sat=7
    sergius_day = weekday + 2 if weekday < 6 else weekday - 5
    return f'{tone}-{sergius_day}'


# ---------------------------------------------------------------------------
# Fixed and relative feasts calendar (from service.py)
# ---------------------------------------------------------------------------
# Inlined from menaion.py to avoid pulling in PyMuPDF at runtime.
# Maps class ID → saint class name (matches menaion_data.json keys).
_menaion_class = {
    0: 'Master', 1: 'Theotokos', 2: 'Cross', 3: 'St John Baptist',
    4: 'Prophet', 5: 'Angels', 6: 'Apostle', 7: 'Apostles',
    8: 'Heirarch', 9: 'Heirarchs', 10: 'Hieromartyr', 11: 'Heiromartyrs',
    12: 'HieroConfessor', 13: 'MonasticMartyr', 14: 'MonasticMartyrs',
    15: 'Holy Fathers', 16: 'Martyr', 17: 'Martyrs', 18: 'Martyress',
    19: 'Martyresses', 20: 'Nun', 21: 'Nuns', 23: 'Fools', 24: 'Unmercenaries',
}

_RELATIVE_FEASTS = {
    '09-09': [6, 1, None, 'Nativity', 'Afterfeast of the Nativity of the Mother of God'],
    '09-10': [6, 1, None, 'Nativity', 'Afterfeast of the Nativity of the Mother of God'],
    '09-11': [6, 1, None, 'Nativity', 'Afterfeast of the Nativity of the Mother of God'],
    '09-15': [4, 2, None, 'Elevation', 'Afterfeast of the Elevation of the Cross'],
    '09-16': [4, 2, None, 'Elevation', 'Afterfeast of the Elevation of the Cross'],
    '09-17': [4, 2, None, 'Elevation', 'Afterfeast of the Elevation of the Cross'],
    '09-18': [4, 2, None, 'Elevation', 'Afterfeast of the Elevation of the Cross'],
    '09-19': [4, 2, None, 'Elevation', 'Afterfeast of the Elevation of the Cross'],
    '09-20': [4, 2, None, 'Elevation', 'Afterfeast of the Elevation of the Cross'],
    '10-11': [3, 15, 6, 'Holy Fathers', 'Our Holy Fathers of the Seventh Ecumenical Council'],
    '10-12': [3, 15, 6, 'Holy Fathers', 'Our Holy Fathers of the Seventh Ecumenical Council'],
    '10-13': [3, 15, 6, 'Holy Fathers', 'Our Holy Fathers of the Seventh Ecumenical Council'],
    '10-14': [3, 15, 6, 'Holy Fathers', 'Our Holy Fathers of the Seventh Ecumenical Council'],
    '10-15': [3, 15, 6, 'Holy Fathers', 'Our Holy Fathers of the Seventh Ecumenical Council'],
    '10-16': [3, 15, 6, 'Holy Fathers', 'Our Holy Fathers of the Seventh Ecumenical Council'],
    '10-17': [3, 15, 6, 'Holy Fathers', 'Our Holy Fathers of the Seventh Ecumenical Council'],
    '11-22': [6, 1, None, 'Entrance', 'The Afterfeast of the Entrance of the Most Holy Theotokos into the Temple'],
    '11-23': [6, 1, None, 'Entrance', 'The Afterfeast of the Entrance of the Most Holy Theotokos into the Temple'],
    '11-24': [6, 1, None, 'Entrance', 'The Afterfeast of the Entrance of the Most Holy Theotokos into the Temple'],
    '12-11': [4, 4, 6, 'Forefathers', 'Sunday of Our Holy Forefathers'],
    '12-12': [4, 4, 6, 'Forefathers', 'Sunday of Our Holy Forefathers'],
    '12-13': [4, 4, 6, 'Forefathers', 'Sunday of Our Holy Forefathers'],
    '12-14': [4, 4, 6, 'Forefathers', 'Sunday of Our Holy Forefathers'],
    '12-15': [4, 4, 6, 'Forefathers', 'Sunday of Our Holy Forefathers'],
    '12-16': [4, 4, 6, 'Forefathers', 'Sunday of Our Holy Forefathers'],
    '12-17': [4, 4, 6, 'Forefathers', 'Sunday of Our Holy Forefathers'],
    '12-18': [3, 0, 6, 'Nativity', 'Sunday Before Nativity'],
    '12-19': [3, 0, 6, 'Nativity', 'Sunday Before Nativity'],
    '12-20': [3, 0, 6, 'Nativity', 'Sunday Before Nativity'],
    '12-21': [3, 0, 6, 'Nativity', 'Sunday Before Nativity'],
    '12-22': [3, 0, 6, 'Nativity', 'Sunday Before Nativity'],
    '12-23': [3, 0, 6, 'Nativity', 'Sunday Before Nativity'],
    '12-24': [3, 0, 6, 'Nativity', 'Sunday Before Nativity'],
    '12-27': [6, 0, None, 'Nativity', 'The Afterfeast of the Nativity of our Lord'],
    '12-28': [6, 0, None, 'Nativity', 'The Afterfeast of the Nativity of our Lord'],
    '12-29': [6, 0, None, 'Nativity', 'The Afterfeast of the Nativity of our Lord'],
    '12-30': [6, 0, None, 'Nativity', 'The Afterfeast of the Nativity of our Lord'],
    '12-31': [4, 0, None, 'Nativity', 'The Leavetaking of the Nativity of our Lord'],
    '01-01': [4, 0, 6, 'Theophany', 'Sunday Before Theophany'],
    '01-02': [4, 0, 6, 'Theophany', 'Sunday Before Theophany'],
    '01-03': [4, 0, 6, 'Theophany', 'Sunday Before Theophany'],
    '01-04': [4, 0, 6, 'Theophany', 'Sunday Before Theophany'],
    '01-05': [4, 0, 6, 'Theophany', 'Sunday Before Theophany'],
    '01-08': [6, 0, None, 'Theophany', 'Afterfeast of Theophany'],
    '01-09': [6, 0, None, 'Theophany', 'Afterfeast of Theophany'],
    '01-10': [6, 0, None, 'Theophany', 'Afterfeast of Theophany'],
    '01-11': [6, 0, None, 'Theophany', 'Afterfeast of Theophany'],
    '01-12': [6, 0, None, 'Theophany', 'Afterfeast of Theophany'],
    '01-13': [6, 0, None, 'Theophany', 'Afterfeast of Theophany'],
    '01-22': [3, 17, 6, 'New Martyrs', 'Holy New Martyrs of Russia'],
    '01-23': [3, 17, 6, 'New Martyrs', 'Holy New Martyrs of Russia'],
    '01-24': [3, 17, 6, 'New Martyrs', 'Holy New Martyrs of Russia'],
    '01-25': [3, 17, 6, 'New Martyrs', 'Holy New Martyrs of Russia'],
    '01-26': [3, 17, 6, 'New Martyrs', 'Holy New Martyrs of Russia'],
    '01-27': [3, 17, 6, 'New Martyrs', 'Holy New Martyrs of Russia'],
    '01-28': [3, 17, 6, 'New Martyrs', 'Holy New Martyrs of Russia'],
    '02-03': [6, 0, None, 'Meeting', 'Afterfeast of the Meeting of Our Lord'],
    '02-04': [6, 0, None, 'Meeting', 'Afterfeast of the Meeting of Our Lord'],
    '02-05': [6, 0, None, 'Meeting', 'Afterfeast of the Meeting of Our Lord'],
    '02-06': [6, 0, None, 'Meeting', 'Afterfeast of the Meeting of Our Lord'],
    '02-07': [6, 0, None, 'Meeting', 'Afterfeast of the Meeting of Our Lord'],
    '02-08': [6, 0, None, 'Meeting', 'Afterfeast of the Meeting of Our Lord'],
    '07-13': [3, 15, 6, 'Holy Fathers', 'Our Holy Fathers of the Fourth Ecumenical Council'],
    '07-14': [3, 15, 6, 'Holy Fathers', 'Our Holy Fathers of the Fourth Ecumenical Council'],
    '07-15': [3, 15, 6, 'Holy Fathers', 'Our Holy Fathers of the Fourth Ecumenical Council'],
    '07-16': [3, 15, 6, 'Holy Fathers', 'Our Holy Fathers of the Fourth Ecumenical Council'],
    '07-17': [3, 15, 6, 'Holy Fathers', 'Our Holy Fathers of the Fourth Ecumenical Council'],
    '07-18': [3, 15, 6, 'Holy Fathers', 'Our Holy Fathers of the Fourth Ecumenical Council'],
    '07-19': [3, 15, 6, 'Holy Fathers', 'Our Holy Fathers of the Fourth Ecumenical Council'],
    '08-07': [6, 0, None, 'Transfiguration', 'Afterfeast of the Transfiguration'],
    '08-08': [6, 0, None, 'Transfiguration', 'Afterfeast of the Transfiguration'],
    '08-09': [6, 0, None, 'Transfiguration', 'Afterfeast of the Transfiguration'],
    '08-10': [6, 0, None, 'Transfiguration', 'Afterfeast of the Transfiguration'],
    '08-11': [6, 0, None, 'Transfiguration', 'Afterfeast of the Transfiguration'],
    '08-12': [6, 0, None, 'Transfiguration', 'Afterfeast of the Transfiguration'],
    '08-16': [6, 1, None, 'Dormition', 'Afterfeast of the Dormition of the Theotokos'],
    '08-17': [6, 1, None, 'Dormition', 'Afterfeast of the Dormition of the Theotokos'],
    '08-18': [6, 1, None, 'Dormition', 'Afterfeast of the Dormition of the Theotokos'],
    '08-19': [6, 1, None, 'Dormition', 'Afterfeast of the Dormition of the Theotokos'],
    '08-20': [6, 1, None, 'Dormition', 'Afterfeast of the Dormition of the Theotokos'],
    '08-21': [6, 1, None, 'Dormition', 'Afterfeast of the Dormition of the Theotokos'],
    '08-22': [6, 1, None, 'Dormition', 'Afterfeast of the Dormition of the Theotokos'],
}

_FIXED_FEASTS = {
    '09-01': [4, 16, 'Symeon', 'Our Venerable Father Symeon the Stylite'],
    '09-04': [4, 4, 'Moses and Aaron', 'Holy Prophets Moses and Aaron'],
    '09-05': [5, 4, 'Zacharias', 'Holy Prophet Zacharias'],
    '09-06': [4, 5, 'Michael', 'Archangel Michael'],
    '09-08': [2, 1, 'Nativity', 'The Nativity of the Mother of God'],
    '09-12': [4, 1, 'Nativity', 'Leavetaking of the Nativity of the Mother of God'],
    '09-13': [4, 0, 'Sepulcher', 'Consecration of the Holy Sepulcher'],
    '09-14': [1, 2, 'Elevation', 'Elevation of the Cross'],
    '09-20': [4, 16, 'Eustathius', 'Greatmartyr Eustathius'],
    '09-21': [4, 2, 'Elevation', 'Leavetaking of the Elevation of the Cross'],
    '09-23': [4, 3, 'Conception', 'Conception of the Forerunner and Baptist John'],
    '09-24': [5, 18, 'Thekla', 'Protomartyr Thekla'],
    '09-25': [3, 13, 'Sergius', 'Sergius of Radonezh'],
    '09-26': [3, 6, 'John', 'Holy Apostle John'],
    '09-28': [4, 12, 'Chariton', 'Chariton the Confessor'],
    '10-01': [3, 1, 'Protection', 'Protection of the Mother of God'],
    '10-06': [4, 6, 'Thomas', 'Holy Apostle Thomas'],
    '10-09': [4, 6, 'James', 'Holy Apostle James Alphaeus'],
    '10-12': [3, 13, 'Symeon', 'Symeon the New Theologian'],
    '10-18': [3, 6, 'Luke', 'Holy Apostle Luke'],
    '10-19': [3, 8, 'John', 'John of Kronstadt'],
    '10-23': [4, 6, 'James', 'Holy Apostle James, the Brother of the Lord'],
    '10-26': [2, 16, 'Demetrius', 'The Holy Great Martyr Demetrius'],
    '11-01': [5, 24, 'Cosmas and Damian', 'The Holy Cosmas and Damian, Unmercenary Physicians'],
    '11-03': [4, 16, 'George', 'The Consecration of the Church of the Great Martyr George'],
    '11-06': [5, 12, 'Paul', 'Paul the Confessor, Archbishop of Constantinople'],
    '11-08': [3, 5, 'Archangels', 'The Synaxis of the Angels'],
    '11-09': [3, 8, 'Nectarius', 'Nectarius, Bishop of Pentapolis'],
    '11-11': [4, 12, 'Theodore', 'Theodore the Studite'],
    '11-13': [3, 8, 'John Chrysostom', 'John Chrysostom, Archbishop of Constantinople'],
    '11-14': [4, 6, 'Philip', 'The Holy Apostle Philip'],
    '11-15': [5, 17, 'Shamuna, Guria, and Habib', 'The Holy Martyrs Shamuna, Guria, and Habib'],
    '11-16': [3, 6, 'Matthew', 'The Holy Apostle and Evangelist Matthew'],
    '11-21': [2, 1, 'Entrance', 'The Entrance of the Most Holy Theotokos into the Temple'],
    '11-24': [3, 18, 'Catherine', 'The Holy Great Martyr Catherine of Alexandria'],
    '11-25': [4, 1, 'Entrance', 'The Leavetaking of the Entrance of the Theotokos'],
    '11-30': [3, 6, 'Andrew', 'The Holy Apostle Andrew, The First-Called'],
    '12-04': [3, 18, 'Barbara', 'Holy Great-Martyr Barbara'],
    '12-05': [3, 13, 'Sabbas', 'Sabbas the Sanctified'],
    '12-06': [3, 8, 'Nicholas', 'Nicholas, Archbishop of Myra'],
    '12-07': [4, 8, 'Ambrose', 'Ambrose, Bishop of Milan'],
    '12-09': [3, 1, 'Conception', 'The Conception of the Most Holy Theotokos'],
    '12-12': [3, 8, 'Spyridon', 'Spyridon The Wonderworker'],
    '12-15': [4, 10, 'Eleutherius', 'The Holy Hieromartyr Eleutherius'],
    '12-17': [5, 4, 'Daniel', 'Holy Prophet Daniel'],
    '12-20': [5, 10, 'Ignatius', 'Holy Hieromartyr Ignatius The God-Bearer'],
    '12-25': [1, 0, 'Nativity', 'The Nativity of Our Lord Jesus Christ'],
    '01-01': [3, 8, 'Basil', 'Basil the Great'],
    '01-02': [3, 13, 'Seraphim', 'Seraphim of Sarov'],
    '01-06': [1, 0, 'Theophany', 'The Holy Theophany of our Lord Jesus Christ'],
    '01-07': [4, 3, 'Forerunner', 'Synaxis of the Forerunner'],
    '01-11': [3, 13, 'Theodosius', 'Theodosius the Cenobiarch'],
    '01-14': [4, 0, 'Theophany', 'Leavetaking of Theophany'],
    '01-17': [3, 13, 'Anthony', 'Anthony the Great'],
    '01-18': [3, 9, 'Athanasius and Cyril', 'Holy Hierarchs Athanasius and Cyril'],
    '01-19': [3, 8, 'Mark', 'Mark of Ephesus'],
    '01-20': [3, 13, 'Euthymius', 'Euthymius the Great'],
    '01-22': [5, 6, 'Timothy', 'Holy Apostle Timothy'],
    '01-24': [3, 23, 'Xenia', 'Xenia of St. Petersburg'],
    '01-25': [3, 8, 'Gregory', 'Gregory the Theologian'],
    '01-27': [3, 8, 'John', 'John Chrysostom'],
    '01-28': [4, 13, 'Ephrem', 'Ephrem the Syrian'],
    '01-29': [5, 10, 'Ignatius', 'Ignatius the God-Bearer'],
    '01-30': [3, 9, 'Holy Hierarchs', 'Three Holy Hierarchs'],
    '01-31': [4, 24, 'Cyrus and John', 'Holy Unmercenaries Cyrus and John'],
    '02-02': [2, 0, 'Meeting', 'Feast of the Meeting of Our Lord'],
    '02-06': [3, 12, 'Photius', 'Photius the Great'],
    '02-08': [5, 16, 'Theodore', 'Martyr Theodore the General'],
    '02-09': [4, 0, 'The Meeting', 'Leavetaking of the Meeting of Our Lord'],
    '02-10': [3, 10, 'Haralambos', 'Haralambos of Magnesia'],
    '02-11': [5, 10, 'Blase', 'Blase of Sebaste'],
    '02-14': [3, 9, 'Cyril and Methodius', 'Cyril and Methodius'],
    '02-17': [5, 16, 'Theodore', 'Martyr Theodore the Soldier'],
    '02-24': [3, 3, 'Head', 'First and Second Findings of the Head of the Baptist John'],
    '03-09': [3, 17, 'Martyrs of Sebaste', 'Forty Martyrs of Sebaste'],
    '03-12': [3, 8, 'Gregory', 'Gregory the Dialogist of Rome'],
    '03-25': [2, 1, 'Annunciation', 'Feast of the Annunciation'],
    '04-23': [3, 16, 'George', 'Greatmartyr George'],
    '04-25': [3, 6, 'Mark', 'Holy Apostle Mark'],
    '04-30': [3, 6, 'James', 'Holy Apostle James, the Brother of John'],
    '05-02': [4, 8, 'Athanasius', 'Athanasius the Great'],
    '05-08': [3, 6, 'John', 'Holy Apostle John'],
    '05-10': [4, 6, 'Simon', 'Holy Apostle Simon the Zealot'],
    '05-15': [5, 13, 'Pachomius', 'Pachomius the Great'],
    '05-21': [3, 8, 'Constantine and Helen', 'Constantine and Helen'],
    '05-25': [3, 3, 'Head', 'Third Finding of the Head of the Baptist John'],
    '06-01': [3, 16, 'Justin', 'Justin Martyr the Philosopher'],
    '06-04': [3, 8, 'Metrophanes', 'Metrophanes of Byzantium'],
    '06-08': [5, 16, 'Theodore', 'Martyr Theodore the General'],
    '06-11': [4, 7, 'Bartholomew and Barnabas', 'Holy Apostles Bartholomew and Barnabas'],
    '06-12': [3, 14, 'Onuphrius and Peter', 'Onuphrius and Peter of Mount Athos'],
    '06-24': [3, 3, 'Nativity', 'The Nativity of the Baptist John'],
    '06-29': [3, 7, 'Peter and Paul', 'Holy Apostles Peter and Paul'],
    '06-30': [4, 7, 'Apostles', 'Synaxis of the 12 Apostles'],
    '07-01': [4, 24, 'Cosmas and Damian', 'Holy Unmercenaries Cosmas and Damian'],
    '07-05': [4, 13, 'Athanasius', 'Athanasius of Athos'],
    '07-08': [4, 16, 'Procopius', 'Greatmartyr Procopius'],
    '07-10': [3, 10, 'Joseph', 'Joseph of Damascus'],
    '07-11': [3, 18, 'Euphemia', 'Greatmartyr Euphemia'],
    '07-12': [3, 13, 'Paisios', 'Paisios the New of Mount Athos'],
    '07-13': [4, 5, 'Gabriel', 'Archangel Gabriel'],
    '07-15': [4, 17, 'Cyricus and Julitta', 'Martyrs Cyricus and Julitta'],
    '07-17': [4, 18, 'Marina', 'Greatmartyr Marina'],
    '07-20': [3, 4, 'Elijah', 'Holy Prophet Elijah'],
    '07-22': [4, 6, 'Mary', 'Mary Magdalene'],
    '07-24': [3, 17, 'Boris and Gleb', 'Martyrs Boris and Gleb'],
    '07-26': [3, 18, 'Paraskeva', 'Martyr Paraskeva'],
    '07-27': [3, 24, 'Panteleimon', 'Martyr and Healer Panteleimon'],
    '08-01': [4, 2, 'Procession', 'Procession of the Cross'],
    '08-02': [5, 10, 'Stephen', 'Protomartyr Stephen'],
    '08-06': [1, 0, 'Transfiguration', 'The Holy Transfiguration of Our Lord'],
    '08-13': [4, 0, 'Transfiguration', 'Leavetaking of the Transfiguration'],
    '08-15': [2, 1, 'Dormition', 'The Dormition of the Theotokos'],
    '08-23': [4, 1, 'Dormition', 'Leavetaking of the Dormition of the Theotokos'],
    '08-25': [4, 7, 'Bartholomew and Titus', 'Holy Apostles Bartholomew and Titus'],
    '08-26': [5, 19, 'Adrian and Natalie', 'Martyrs Adrian and Natalie'],
    '08-29': [3, 3, 'Beheading', 'Beheading of the Baptist John'],
}


# ---------------------------------------------------------------------------
# Menaion lookup
# ---------------------------------------------------------------------------
def _lookup_menaion(menaion_date, weekday):
    """Return (rank, service_type_name, service_name, long_name, menaion_data) or None."""
    relative = _RELATIVE_FEASTS.get(menaion_date)
    if relative and relative[2] is not None:
        # Relative feast requires specific weekday
        if relative[2] != weekday:
            relative = None

    fixed = _FIXED_FEASTS.get(menaion_date)

    rel_rank = relative[0] if relative else 7
    fix_rank = fixed[0] if fixed else 7
    rank = min(rel_rank, fix_rank)

    if rank >= 7:
        return None

    if fix_rank == rank:
        feast = fixed
        service_type_id = feast[1]
        service_name = feast[2]
        long_name = feast[3]
    else:
        feast = relative
        service_type_id = feast[1]
        service_name = feast[3]
        long_name = feast[4]

    # Resolve service type id to class name
    service_type = _menaion_class.get(service_type_id, 'Master')

    # Look up in menaion JSON
    men_entry = _menaion.get(service_type)
    if men_entry:
        men_services = men_entry['services']
        # Replace placeholder (name) with actual saint name
        men_services = _substitute_name(men_services, service_name)
    else:
        men_services = None

    full_entry = _full_menaion.get(menaion_date)
    full_services = (full_entry or {}).get('services') if full_entry else None

    return {
        'rank': rank,
        'service_type': service_type,
        'service_name': service_name,
        'long_name': (full_entry or {}).get('name') or long_name,
        'services': men_services,
        'full_services': full_services,
        'full_name': (full_entry or {}).get('name'),
    }


def _substitute_name(obj, name):
    """Recursively replace (name) placeholder with actual saint name in strings."""
    if isinstance(obj, str):
        return obj.replace('(name)', name).replace(
            '<i class="name">(name)</i>', f'<i class="name">{name}</i>'
        )
    elif isinstance(obj, dict):
        return {k: _substitute_name(v, name) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [_substitute_name(item, name) for item in obj]
    return obj


# ---------------------------------------------------------------------------
# Main resolver
# ---------------------------------------------------------------------------
RANK_NAMES = {
    1: 'Great Feast',
    2: 'Vigil',
    3: 'Polyeleos',
    4: 'Doxology',
    5: 'Six Stichera',
    6: 'Afterfeast',
    7: 'Simple',
}


def resolve(month, day, year, calendar=1, rank=None, menaion_source='general'):
    """
    Resolve all liturgical variables for a given date.

    Args:
        month, day, year: date components
        calendar: 0 = new calendar, 1 = old calendar (default)
        rank: override feast rank (1-7). 7 = simple service (octoechos only).
              None = use the rank from the feast calendar.
        menaion_source: 'general' (24 saint classes, default),
                        'full' (366-day, not yet available),
                        'none' (skip menaion entirely)

    Returns dict with:
      - liturgical: paschalion data (pascha_offset, tone, lent_week, etc.)
      - period: 'lent' | 'pre_lent' | 'paschal' | 'normal'
      - rank: effective rank used (from calendar or override)
      - rank_name: human-readable rank label
      - menaion_source: which menaion was used ('general', 'full', 'none')
      - sources: which JSON sources contributed data
      - triodion / pentecostarion / octoechos / menaion: entry data
      - feast: feast info (rank, name, long_name, service_type)
    """
    month = int(month) if isinstance(month, str) else month
    day = int(day) if isinstance(day, str) else day
    year = int(year) if isinstance(year, str) else year

    service_date = date(year, month, day)
    weekday = service_date.weekday()  # 0=Mon .. 6=Sun

    # Old calendar offset
    if calendar == 1:
        date_oc = service_date - timedelta(days=13)
        menaion_date = date_oc.strftime('%m-%d')
    else:
        menaion_date = service_date.strftime('%m-%d')

    lit = paschalion(month, day, year)
    offset = lit['pascha_offset']
    tone = lit['weekly_tone']

    # Determine liturgical period
    if lit['lent_week'] is not None and lit['lent_week'] > 0:
        period = 'lent'
    elif lit['lent_week'] is not None and lit['lent_week'] <= 0:
        period = 'pre_lent'
    elif lit['pascha_week'] is not None or (0 <= offset <= 56):
        period = 'paschal'
    else:
        period = 'normal'

    # Determine effective menaion source
    if menaion_source == 'full':
        # Full menaion (366 days) not yet extracted — fall back to general
        effective_menaion = 'general'
        menaion_note = 'full menaion not yet available, using general'
    elif menaion_source == 'none':
        effective_menaion = 'none'
        menaion_note = None
    else:
        effective_menaion = 'general'
        menaion_note = None

    # Simple service (rank 7) means no menaion
    skip_menaion = effective_menaion == 'none' or rank == 7

    sources = []
    result = {
        'date': service_date.isoformat(),
        'weekday': weekday,
        'weekday_name': ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                         'Friday', 'Saturday', 'Sunday'][weekday],
        'calendar': calendar,
        'menaion_date': menaion_date,
        'liturgical': lit,
        'period': period,
        'menaion_source': effective_menaion if not skip_menaion else 'none',
        'menaion_note': menaion_note,
        'sources': sources,
        'triodion': None,
        'pentecostarion': None,
        'octoechos': None,
        'menaion': None,
        'full_menaion': None,
        'feast': None,
    }

    # --- Triodion ---
    if rank != 7:  # simple service skips moveable books too
        tri_key = _triodion_key(offset)
        if tri_key and tri_key in _triodion:
            tri_entry = _triodion[tri_key]
            result['triodion'] = {
                'key': tri_key,
                'desc': tri_entry['desc'],
                'services': tri_entry['services'],
            }
            sources.append('triodion')

    # --- Pentecostarion ---
    if rank != 7:
        pent_key = _pentecostarion_key(offset)
        if pent_key and pent_key in _pentecostarion:
            pent_entry = _pentecostarion[pent_key]
            result['pentecostarion'] = {
                'key': pent_key,
                'desc': pent_entry['desc'],
                'services': pent_entry['services'],
            }
            sources.append('pentecostarion')

    # --- Octoechos ---
    oct_key = _octoechos_key(tone, weekday)
    if oct_key and oct_key in _octoechos:
        oct_entry = _octoechos[oct_key]
        result['octoechos'] = {
            'key': oct_key,
            'tone': tone,
            'desc': oct_entry['desc'],
            'services': oct_entry['services'],
        }
        sources.append('octoechos')

    # --- Menaion ---
    if not skip_menaion:
        men = _lookup_menaion(menaion_date, weekday)
        if men:
            result['menaion'] = men
            result['feast'] = {
                'rank': men['rank'],
                'service_type': men['service_type'],
                'service_name': men['service_name'],
                'long_name': men['long_name'],
            }
            sources.append('menaion')
            if men.get('full_services'):
                result['full_menaion'] = {
                    'date': menaion_date,
                    'name': men.get('full_name'),
                    'services': men['full_services'],
                }
                sources.append('full_menaion')
                result['menaion_source'] = 'full'

    # Effective rank: override > feast calendar > 7 (simple)
    feast_rank = result['feast']['rank'] if result['feast'] else 7
    effective_rank = rank if rank is not None else feast_rank
    result['rank'] = effective_rank
    result['rank_name'] = RANK_NAMES.get(effective_rank, f'Rank {effective_rank}')

    return result


def resolve_service(month, day, year, service_type, calendar=1,
                    rank=None, menaion_source='general'):
    """
    Resolve variables for a specific service type (vespers, matins, liturgy, etc.)
    by merging from all applicable sources according to the priority chain.

    Args:
        service_type: 'vespers', 'matins', 'liturgy', 'compline', etc.
        rank: override rank (7 = simple/octoechos only)
        menaion_source: 'general', 'full', 'none'

    Returns a dict of variables ready for template rendering.
    """
    ctx = resolve(month, day, year, calendar, rank=rank,
                  menaion_source=menaion_source)
    period = ctx['period']
    effective_rank = ctx['rank']

    from assembly import merge_service, as_hymn_list

    tri_svc = (ctx['triodion'] or {}).get('services', {}).get(service_type)
    pent_svc = (ctx['pentecostarion'] or {}).get('services', {}).get(service_type)
    oct_svc = (ctx['octoechos'] or {}).get('services', {}).get(service_type)
    men_svc = ((ctx['menaion'] or {}).get('services') or {}).get(service_type)
    full_svc = ((ctx.get('full_menaion') or {}).get('services') or {}).get(service_type)

    merged = merge_service(
        service_type,
        rank=effective_rank,
        weekday=ctx['weekday'],
        period=period,
        oct_svc=oct_svc if isinstance(oct_svc, dict) else {},
        men_svc=men_svc if isinstance(men_svc, dict) else {},
        full_svc=full_svc if isinstance(full_svc, dict) else {},
        tri_svc=tri_svc if isinstance(tri_svc, dict) else {},
        pent_svc=pent_svc if isinstance(pent_svc, dict) else {},
    )
    moveable_name = merged.pop('_moveable_book', None)
    if as_hymn_list((full_svc or {}).get('stichera')):
        primary_name = 'full_menaion'
    else:
        primary_name = moveable_name or (
            'triodion' if period in ('lent', 'pre_lent') else
            'pentecostarion' if period == 'paschal' else
            'menaion' if men_svc else 'octoechos'
        )
    if effective_rank == 7:
        primary_name = 'octoechos'

    merged['_period'] = period
    merged['_sources'] = ctx['sources']
    merged['_primary'] = primary_name
    merged['_feast'] = ctx.get('feast')
    merged['_rank'] = effective_rank
    merged['_rank_name'] = ctx['rank_name']
    merged['_menaion_source'] = ctx['menaion_source']
    merged['_weekday'] = ctx['weekday']
    merged['_tone'] = (ctx['liturgical'] or {}).get('weekly_tone')
    merged['_date'] = ctx['date']
    merged['_calendar'] = calendar

    return merged


# ---------------------------------------------------------------------------
# CLI test
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 4:
        m, d, y = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    else:
        today = date.today()
        m, d, y = today.month, today.day, today.year

    print(f'Resolving {m}/{d}/{y}...')
    ctx = resolve(m, d, y)

    print(f'\nDate:    {ctx["date"]} ({ctx["weekday_name"]})')
    print(f'Period:  {ctx["period"]}')
    print(f'Sources: {ctx["sources"]}')

    lit = ctx['liturgical']
    print(f'\nPascha offset: {lit["pascha_offset"]}')
    print(f'Tone:          {lit["weekly_tone"]}')
    print(f'Lent week:     {lit["lent_week"]}')
    print(f'Pascha week:   {lit["pascha_week"]}')
    print(f'Weeks after:   {lit["weeks_after"]}')

    if ctx['triodion']:
        tri = ctx['triodion']
        print(f'\nTriodion:  key={tri["key"]}, {tri["desc"]}')
        print(f'  Services: {list(tri["services"].keys())}')

    if ctx['pentecostarion']:
        p = ctx['pentecostarion']
        print(f'\nPentecostarion: key={p["key"]}, {p["desc"]}')
        print(f'  Services: {list(p["services"].keys())}')

    if ctx['octoechos']:
        o = ctx['octoechos']
        print(f'\nOctoechos: key={o["key"]}, tone={o["tone"]}, {o["desc"]}')
        print(f'  Services: {list(o["services"].keys())}')

    if ctx['menaion']:
        men = ctx['menaion']
        print(f'\nMenaion:   {men["service_type"]} — {men["long_name"]}')
        if men['services']:
            print(f'  Services: {list(men["services"].keys())}')

    if ctx['feast']:
        f = ctx['feast']
        print(f'\nFeast:     rank={f["rank"]}, {f["long_name"]}')

    # Show merged vespers
    print('\n' + '='*60)
    print('MERGED VESPERS:')
    print('='*60)
    vs = resolve_service(m, d, y, 'vespers')
    for k, v in vs.items():
        if k.startswith('_'):
            print(f'  {k}: {v}')
        elif isinstance(v, str):
            print(f'  {k}: {v[:80]}...' if len(str(v)) > 80 else f'  {k}: {v}')
        elif isinstance(v, list):
            print(f'  {k}: [{len(v)} items]')
        else:
            print(f'  {k}: {v}')
