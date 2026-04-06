"""
Download Triodion and Pentecostarion PDFs from st-sergius.org

URL PATTERNS DISCOVERED:
  Triodion (pre-Lenten):  services/triod/0-{N}.pdf    (N = 1..~50)
  Triodion (Lenten):      services/triod/{N}.pdf       (N = 1..~80)
  Pentecostarion:         services/pent/{WD}.pdf       (W = week, D = day)

IMPORTANT: The Triodion PDFs are indexed by CALENDAR day, not LITURGICAL day.
  - Liturgical day starts at Vespers (evening before)
  - So "Saturday Vespers" content is liturgically SUNDAY
  - This offset is handled in the extraction step, not download

RUN THIS LOCALLY (not in sandbox):
    python3 database/download_triodion_pentecostarion.py

Requires: pip install requests (or just urllib)
"""

import os
import time
from urllib.request import Request, urlopen
from urllib.error import HTTPError

BASE_URL = 'https://st-sergius.org/services/'
OUTPUT_DIR_TRIOD = os.path.join(os.path.dirname(__file__), '..', 'services', 'triodion')
OUTPUT_DIR_PENT = os.path.join(os.path.dirname(__file__), '..', 'services', 'pentecostarion')

HEADERS = {'User-Agent': 'Mozilla/5.0 (Anthologion Project)'}


def download_pdf(url, output_path, retries=3):
    """Download a PDF with retry logic"""
    for attempt in range(retries):
        try:
            req = Request(url, headers=HEADERS)
            resp = urlopen(req, timeout=15)
            data = resp.read()

            if len(data) < 500:
                return False  # Too small, probably error page

            with open(output_path, 'wb') as f:
                f.write(data)
            return True

        except HTTPError as e:
            if e.code == 404:
                return False  # File doesn't exist
            if attempt < retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2 ** attempt)

    return False


def download_triodion():
    """
    Download all Triodion PDFs.

    Structure (based on discovered URLs):
      Pre-Lenten period:  triod/0-{N}.pdf
        0-10 = Publican & Pharisee Sunday Vespers
        0-14 = Friday/Saturday stichera
        0-37 = Meatfare Sunday
        Range: probably 0-1 through 0-50

      Lenten period:       triod/{N}.pdf
        13 = Week 1 Wednesday Matins
        16 = Week 1 Saturday Matins
        17 = Week 2 (Sunday?)
        36 = Week 3 Saturday Matins
        37 = Week 3 Sunday (Cross)
        74 = Holy Thursday Matins
        75 = Holy Friday Matins
        Range: probably 1 through 80+
    """
    os.makedirs(OUTPUT_DIR_TRIOD, exist_ok=True)

    print("=" * 60)
    print("DOWNLOADING TRIODION PDFs")
    print("=" * 60)

    found = []

    # Pre-Lenten period (0-N pattern)
    print("\n--- Pre-Lenten Period (triod/0-N.pdf) ---")
    for n in range(1, 60):
        filename = f'0-{n}.pdf'
        url = BASE_URL + 'triod/' + filename
        output = os.path.join(OUTPUT_DIR_TRIOD, filename)

        if os.path.exists(output):
            print(f"  SKIP: {filename} (already exists)")
            found.append(filename)
            continue

        if download_pdf(url, output):
            size = os.path.getsize(output)
            print(f"  OK:   {filename} ({size:,} bytes)")
            found.append(filename)
        # Don't print misses to reduce noise

        time.sleep(0.3)  # Be polite to the server

    # Lenten period (N pattern)
    print("\n--- Lenten Period + Holy Week (triod/N.pdf) ---")
    for n in range(1, 90):
        filename = f'{n}.pdf'
        url = BASE_URL + 'triod/' + filename
        output = os.path.join(OUTPUT_DIR_TRIOD, filename)

        if os.path.exists(output):
            print(f"  SKIP: {filename} (already exists)")
            found.append(filename)
            continue

        if download_pdf(url, output):
            size = os.path.getsize(output)
            print(f"  OK:   {filename} ({size:,} bytes)")
            found.append(filename)

        time.sleep(0.3)

    print(f"\nTriodion: {len(found)} PDFs downloaded to {OUTPUT_DIR_TRIOD}")
    return found


def download_pentecostarion():
    """
    Download all Pentecostarion PDFs.

    Structure (based on discovered URLs):
      pent/{WD}.pdf where W=week (0-8), D=day (1-7)

      Known examples:
        42.pdf = Week 4, Day 2 (Tuesday)
        61.pdf = Week 6, Day 1 (Sunday evening)
        64.pdf = Week 6, Day 4 (Thursday = Ascension)
        82.pdf = Week 8, Day 2 (Tuesday)

      Also possible: pent/0-{N}.pdf for Bright Week or special services
    """
    os.makedirs(OUTPUT_DIR_PENT, exist_ok=True)

    print("\n" + "=" * 60)
    print("DOWNLOADING PENTECOSTARION PDFs")
    print("=" * 60)

    found = []

    # Week-Day pattern (WD.pdf)
    # Week 0 = Bright Week, Weeks 1-8 = Thomas through All Saints
    print("\n--- Pentecostarion (pent/WD.pdf) ---")
    for week in range(0, 10):
        for day in range(0, 8):
            filename = f'{week}{day}.pdf'
            url = BASE_URL + 'pent/' + filename
            output = os.path.join(OUTPUT_DIR_PENT, filename)

            if os.path.exists(output):
                print(f"  SKIP: {filename} (already exists)")
                found.append(filename)
                continue

            if download_pdf(url, output):
                size = os.path.getsize(output)
                day_names = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
                day_name = day_names[day] if day < 7 else f'D{day}'
                print(f"  OK:   {filename} (Week {week}, {day_name}) ({size:,} bytes)")
                found.append(filename)

            time.sleep(0.3)

    # Also try sequential pattern (in case some use plain numbers)
    print("\n--- Pentecostarion sequential (pent/N.pdf) ---")
    for n in range(1, 60):
        filename = f'{n}.pdf'
        if filename in found:
            continue  # Already got this one

        url = BASE_URL + 'pent/' + filename
        output = os.path.join(OUTPUT_DIR_PENT, filename)

        if os.path.exists(output):
            found.append(filename)
            continue

        if download_pdf(url, output):
            size = os.path.getsize(output)
            print(f"  OK:   {filename} ({size:,} bytes)")
            found.append(filename)

        time.sleep(0.3)

    print(f"\nPentecostarion: {len(found)} PDFs downloaded to {OUTPUT_DIR_PENT}")
    return found


def main():
    print("=" * 60)
    print("ANTHOLOGION: Triodion & Pentecostarion PDF Download")
    print("=" * 60)
    print(f"\nSource: st-sergius.org")
    print(f"Triodion output:       {os.path.abspath(OUTPUT_DIR_TRIOD)}")
    print(f"Pentecostarion output: {os.path.abspath(OUTPUT_DIR_PENT)}")
    print()

    triod_files = download_triodion()
    pent_files = download_pentecostarion()

    print("\n" + "=" * 60)
    print("DOWNLOAD COMPLETE")
    print("=" * 60)
    print(f"  Triodion:       {len(triod_files)} PDFs")
    print(f"  Pentecostarion: {len(pent_files)} PDFs")
    print(f"  Total:          {len(triod_files) + len(pent_files)} PDFs")
    print()
    print("Next step: Run the extraction script to convert to JSON:")
    print("  python3 database/extract_triodion_pentecostarion.py")


if __name__ == '__main__':
    main()
