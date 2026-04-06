"""
Extract all general Menaion PDFs into menaion_data.json
using the existing menaion.py parsing functions.

These are template services for each saint class (Apostle, Martyr, etc.)
The actual saint name/date comes from the calendar/typikon at runtime.

Usage:
    python3 database/extract_menaion.py
"""

import os
import sys
import json
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
os.chdir(BASE_DIR)

import fitz
from menaion import menaion_variables, menaion_class


def normalize_section_headers(text):
    """Normalize liturgical section headers so menaion.py regexes can match.

    Some PDFs have 'AT THE LITURGY' / 'AT THE MATINS' but the parser
    expects 'AT LITURGY' / 'AT MATINS' (no 'THE').
    """
    text = re.sub(r'AT\s+THE\s+LITURGY', 'AT LITURGY', text, flags=re.I)
    text = re.sub(r'AT\s+THE\s+MATINS', 'AT MATINS', text, flags=re.I)
    return text


def read_pdf_text(service_dir, filename):
    """Read PDF using plain get_text() to match process_pdf output format."""
    f = filename if filename.endswith('.pdf') else filename + '.pdf'
    path = os.path.join(BASE_DIR, 'services', service_dir, f)
    if not os.path.exists(path):
        return None
    payload = ''
    with fitz.open(path) as doc:
        for page in doc:
            payload += page.get_text()
    return payload


def extract_all():
    results = {}
    errors = []

    for class_id, class_name in sorted(menaion_class.items()):
        print(f'  Processing class {class_id}: {class_name}...', end=' ')

        if class_name == 'Master':
            # Master service is hardcoded in menaion.py, no PDF needed
            try:
                data = menaion_variables('', name='(name)', service_type='Master', weekday=0)
                results[class_name] = {
                    'class_id': class_id,
                    'class_name': class_name,
                    'desc': 'Master/General service (hardcoded)',
                    'services': data,
                }
                print('OK (hardcoded)')
            except Exception as e:
                print(f'ERROR: {e}')
                errors.append(class_name)
            continue

        try:
            text = read_pdf_text('menaion', class_name)
            if not text:
                print('EMPTY')
                errors.append(class_name)
                continue

            # Normalize headers so the parser regexes match
            text = normalize_section_headers(text)

            # Use a placeholder name and weekday 0 (Sunday) for extraction
            data = menaion_variables(text, name='(name)', service_type=class_name, weekday=0)

            # Count components
            svc_count = len(data)
            comp_count = sum(
                len(v) if isinstance(v, dict) else 1
                for v in data.values()
            )

            results[class_name] = {
                'class_id': class_id,
                'class_name': class_name,
                'desc': f'{class_name} general service',
                'services': data,
            }

            print(f'{svc_count} services, {comp_count} components')

        except Exception as e:
            print(f'ERROR: {e}')
            errors.append(class_name)

    return results, errors


def main():
    print('=' * 60)
    print('EXTRACTING GENERAL MENAION (26 saint classes)')
    print('=' * 60)

    results, errors = extract_all()

    # Write JSON
    json_path = os.path.join(BASE_DIR, 'database', 'menaion_data.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f'\nWrote {len(results)} entries to {json_path}')

    if errors:
        print(f'\nErrors on: {errors}')

    # Summary
    total_svc = sum(len(d['services']) for d in results.values())
    print(f'\nMenaion: {len(results)} saint classes, {total_svc} service sections')


if __name__ == '__main__':
    main()
