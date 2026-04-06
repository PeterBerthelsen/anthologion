"""
Extract all 56 Octoechos PDFs into octoechos_data.json
using the existing octoechos.py parsing functions.

Octoechos files: {tone}-{day}.pdf (tone 1-8, day 1-7)
  day 1 = Saturday evening / Sunday
  day 2 = Sunday evening / Monday
  ...
  day 7 = Friday evening / Saturday

Usage:
    python3 database/extract_octoechos.py
"""

import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
os.chdir(BASE_DIR)

from _utils import open_service
from octoechos import octoechos_variables

DAY_NAMES = {
    1: 'Saturday Evening / Sunday',
    2: 'Sunday Evening / Monday',
    3: 'Monday Evening / Tuesday',
    4: 'Tuesday Evening / Wednesday',
    5: 'Wednesday Evening / Thursday',
    6: 'Thursday Evening / Friday',
    7: 'Friday Evening / Saturday',
}


def extract_all():
    results = {}
    errors = []

    for tone in range(1, 9):
        for day in range(1, 8):
            key = f'{tone}-{day}'
            print(f'  Processing {key}.pdf (Tone {tone}, {DAY_NAMES[day]})...', end=' ')

            try:
                text = open_service('octoechos', key)
                if not text:
                    print('EMPTY')
                    errors.append(key)
                    continue

                data = octoechos_variables(text)

                # Count what we got
                svc_count = len(data)
                comp_count = sum(
                    len(v) if isinstance(v, dict) else 1
                    for v in data.values()
                )

                results[key] = {
                    'tone': tone,
                    'day': day,
                    'desc': f'Tone {tone} - {DAY_NAMES[day]}',
                    'services': data,
                }

                print(f'{svc_count} services, {comp_count} components')

            except Exception as e:
                print(f'ERROR: {e}')
                errors.append(key)

    return results, errors


def main():
    print('=' * 60)
    print('EXTRACTING OCTOECHOS (56 files)')
    print('=' * 60)

    results, errors = extract_all()

    # Write JSON
    json_path = os.path.join(BASE_DIR, 'database', 'octoechos_data.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f'\nWrote {len(results)} entries to {json_path}')

    if errors:
        print(f'\nErrors on: {errors}')

    # Summary
    total_svc = sum(len(d['services']) for d in results.values())
    print(f'\nOctoechos: {len(results)} tone/day combos, {total_svc} service sections')


if __name__ == '__main__':
    main()
