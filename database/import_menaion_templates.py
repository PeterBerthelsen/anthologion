"""
Import Menaion saint class templates into the liturgical_texts table.

Usage:
    python3 import_menaion_templates.py

Requires:
    - PostgreSQL database with schema_v2.sql applied
    - DATABASE_URL environment variable set
    - JSON template files in database/menaion_templates/
"""

import json
import os
import psycopg2
from psycopg2.extras import execute_values

DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://localhost/anthologion')
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'menaion_templates')


def import_template(cursor, template):
    """Import a single saint class template into liturgical_texts"""
    saint_class = template['saint_class']
    vespers = template['services']['vespers']
    matins = template['services']['matins']

    rows = []

    # ---- VESPERS STICHERA ----
    for sticheron in vespers.get('stichera_lord_i_cried', []):
        rows.append((
            'menaion', 'vespers', 'sticheron',
            sticheron.get('tone'), None,  # tone, weekday
            saint_class,
            sticheron['text'],
            sticheron['order'],
            None,  # verse_text
            sticheron.get('melody'),
            None,  # rubric_notes
            '{}'  # metadata
        ))

    # ---- VESPERS THEOTOKION ----
    if vespers.get('theotokion'):
        rows.append((
            'menaion', 'vespers', 'theotokion',
            vespers['theotokion'].get('tone'), None,
            saint_class,
            vespers['theotokion']['text'],
            1, None, None, None, '{}'
        ))

    # ---- VESPERS STAVROTHEOTOKION ----
    if vespers.get('stavrotheotokion'):
        rows.append((
            'menaion', 'vespers', 'stavrotheotokion',
            None, None,
            saint_class,
            vespers['stavrotheotokion']['text'],
            1, None, None, None, '{}'
        ))

    # ---- VESPERS IDIOMELON ----
    if vespers.get('idiomelon'):
        rows.append((
            'menaion', 'vespers', 'idiomelon',
            vespers['idiomelon'].get('tone'), None,
            saint_class,
            vespers['idiomelon']['text'],
            1, None, None, None, '{}'
        ))

    # ---- VESPERS DOGMATIC THEOTOKION ----
    if vespers.get('dogmatic_theotokion'):
        rows.append((
            'menaion', 'vespers', 'dogmatic_theotokion',
            vespers['dogmatic_theotokion'].get('tone'), None,
            saint_class,
            vespers['dogmatic_theotokion']['text'],
            1, None, None, None, '{}'
        ))

    # ---- VESPERS APOSTICHA ----
    for sticheron in vespers.get('aposticha', {}).get('stichera', []):
        rows.append((
            'menaion', 'vespers', 'aposticha',
            sticheron.get('tone'), None,
            saint_class,
            sticheron['text'],
            sticheron['order'],
            sticheron.get('verse'),
            None, None, '{}'
        ))

    # ---- VESPERS/MATINS TROPARION ----
    if vespers.get('troparion'):
        rows.append((
            'menaion', 'vespers', 'troparion',
            vespers['troparion'].get('tone'), None,
            saint_class,
            vespers['troparion']['text'],
            1, None, None, None, '{}'
        ))

    # ---- MATINS KONTAKION ----
    if matins.get('kontakion'):
        rows.append((
            'menaion', 'matins', 'kontakion',
            matins['kontakion'].get('tone'), None,
            saint_class,
            matins['kontakion']['text'],
            1, None, None, None, '{}'
        ))

    # ---- MATINS IKOS ----
    if matins.get('ikos'):
        rows.append((
            'menaion', 'matins', 'ikos',
            None, None,
            saint_class,
            matins['ikos']['text'],
            1, None, None, None, '{}'
        ))

    # ---- MATINS EXAPOSTILARION ----
    if matins.get('exapostilarion'):
        rows.append((
            'menaion', 'matins', 'exapostilarion',
            None, None,
            saint_class,
            matins['exapostilarion']['text'],
            1, None, None, None, '{}'
        ))

    # Insert all rows
    if rows:
        execute_values(cursor, """
            INSERT INTO liturgical_texts (
                source, service_type, text_type,
                tone, weekday,
                saint_class,
                text_content,
                text_order, verse_text, melody_spec, rubric_notes, metadata
            ) VALUES %s
        """, rows)

    return len(rows)


def main():
    print("="*60)
    print("MENAION TEMPLATE IMPORT")
    print("="*60)

    # Load all templates
    all_templates_path = os.path.join(TEMPLATES_DIR, 'all_templates.json')
    if not os.path.exists(all_templates_path):
        print(f"ERROR: {all_templates_path} not found")
        print("Run the template extraction script first.")
        return

    with open(all_templates_path, 'r', encoding='utf-8') as f:
        templates = json.load(f)

    print(f"\nFound {len(templates)} templates to import")

    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()

        total_rows = 0
        for saint_class, template in templates.items():
            count = import_template(cursor, template)
            total_rows += count
            print(f"  {saint_class}: {count} texts imported")

        conn.commit()
        cursor.close()
        conn.close()

        print(f"\nTotal: {total_rows} liturgical texts imported")
        print("Import complete!")

    except psycopg2.OperationalError as e:
        print(f"\nERROR: Could not connect to database")
        print(f"Set DATABASE_URL environment variable")
        print(f"Error: {e}")

        # Show what would be imported
        print(f"\nDRY RUN - Would import:")
        for saint_class, template in templates.items():
            vespers = template['services']['vespers']
            matins = template['services']['matins']
            count = (
                len(vespers.get('stichera_lord_i_cried', []))
                + (1 if vespers.get('theotokion') else 0)
                + (1 if vespers.get('stavrotheotokion') else 0)
                + (1 if vespers.get('idiomelon') else 0)
                + (1 if vespers.get('dogmatic_theotokion') else 0)
                + len(vespers.get('aposticha', {}).get('stichera', []))
                + (1 if vespers.get('troparion') else 0)
                + (1 if matins.get('kontakion') else 0)
                + (1 if matins.get('ikos') else 0)
                + (1 if matins.get('exapostilarion') else 0)
            )
            print(f"  {saint_class}: {count} texts")


if __name__ == '__main__':
    main()
