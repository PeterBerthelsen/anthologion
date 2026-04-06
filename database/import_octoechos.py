"""
Import extracted Octoechos texts into PostgreSQL database
This script demonstrates loading structured JSON data from PDF extraction
"""

import json
import psycopg2
from psycopg2.extras import execute_values
import os

# Database connection - adjust for your Railway PostgreSQL instance
DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://localhost/anthologion')

def import_vespers_data(json_file_path, db_conn):
    """
    Import Vespers data from JSON into liturgical_texts table
    """
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    tone = data.get('tone')
    day = data.get('day')

    # Map day name to weekday number (0=Monday, 6=Sunday)
    day_map = {
        'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3,
        'Friday': 4, 'Saturday': 5, 'Sunday': 6
    }
    weekday = day_map.get(day, 6)

    cursor = db_conn.cursor()

    # Import Stichera on "Lord I have cried"
    stichera_data = []
    for sticheron in data.get('stichera_on_lord_i_cried', []):
        stichera_data.append((
            'octoechos',  # source
            'vespers',    # service_type
            'sticheron',  # text_type
            tone,         # tone
            weekday,      # weekday
            None,         # rank (NULL for octoechos)
            None,         # menaion_class
            None,         # liturgical_period
            None,         # week_offset
            sticheron['text'],  # text_content
            sticheron['number'],  # text_order
            sticheron.get('verse'),  # verse_text
            None,         # melody_spec
            None,         # rubric_notes
            None          # metadata
        ))

    # Insert stichera
    insert_query = """
        INSERT INTO liturgical_texts (
            source, service_type, text_type, tone, weekday, rank,
            menaion_class, liturgical_period, week_offset, text_content,
            text_order, verse_text, melody_spec, rubric_notes, metadata
        ) VALUES %s
        ON CONFLICT DO NOTHING
    """

    if stichera_data:
        execute_values(cursor, insert_query, stichera_data)
        print(f"✓ Imported {len(stichera_data)} stichera for Tone {tone}, {day}")

    # Import Theotokion
    if data.get('theotokion'):
        cursor.execute("""
            INSERT INTO liturgical_texts (
                source, service_type, text_type, tone, weekday,
                text_content, text_order
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT DO NOTHING
        """, (
            'octoechos', 'vespers', 'theotokion', tone, weekday,
            data['theotokion'], 1
        ))
        print(f"✓ Imported theotokion for Tone {tone}, {day}")

    # Import Aposticha stichera
    aposticha_data = []
    for sticheron in data.get('aposticha', {}).get('stichera', []):
        aposticha_data.append((
            'octoechos', 'vespers', 'aposticha', tone, weekday,
            None, None, None, None,
            sticheron['text'],
            sticheron['number'],
            sticheron.get('verse'),
            None, None, None
        ))

    if aposticha_data:
        execute_values(cursor, insert_query, aposticha_data)
        print(f"✓ Imported {len(aposticha_data)} aposticha for Tone {tone}, {day}")

    # Import Aposticha Theotokion
    if data.get('aposticha', {}).get('theotokion'):
        cursor.execute("""
            INSERT INTO liturgical_texts (
                source, service_type, text_type, tone, weekday,
                text_content, text_order, rubric_notes
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT DO NOTHING
        """, (
            'octoechos', 'vespers', 'theotokion', tone, weekday,
            data['aposticha']['theotokion'], 2, 'Aposticha Theotokion'
        ))
        print(f"✓ Imported aposticha theotokion for Tone {tone}, {day}")

    db_conn.commit()
    cursor.close()


def batch_import_all_octoechos(pdf_dir, db_conn):
    """
    Process all Octoechos PDFs and import to database
    This is a placeholder for the full batch import process
    """
    print("\n" + "="*60)
    print("BATCH IMPORT PROCESS (To be implemented)")
    print("="*60)
    print("\nThis would:")
    print("1. Loop through all 56 Octoechos PDFs (8 tones × 7 days)")
    print("2. Extract text using Claude API or local processing")
    print("3. Parse into structured JSON")
    print("4. Import each file's data into the database")
    print("\nFor now, we're demonstrating with the single extracted file.")


def import_fixed_texts_kathismata(db_conn):
    """
    Import kathismata from the existing kathisma.py file
    This demonstrates migrating from hardcoded Python to database
    """
    import sys
    sys.path.append('/home/user/anthologion')

    try:
        from kathisma import parse_kathisma
    except ImportError:
        print("⚠ Could not import kathisma.py - skipping kathismata import")
        return

    cursor = db_conn.cursor()

    print("\n" + "="*60)
    print("IMPORTING KATHISMATA FROM kathisma.py")
    print("="*60)

    # The kathisma_rubric from service.py shows which kathisma for each day
    # For demonstration, import just Kathisma 1
    kathisma_data = parse_kathisma(1)

    # Import title
    cursor.execute("""
        INSERT INTO fixed_texts (
            text_key, text_category, text_content, text_html,
            kathisma_number, stasis_number
        ) VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (text_key) DO NOTHING
    """, (
        'kathisma_1_title', 'kathisma', 'First Kathisma',
        kathisma_data.get('title'), 1, None
    ))

    # Import each stasis
    for stasis_num in [1, 2, 3]:
        stasis_html = kathisma_data.get(stasis_num, '')
        if stasis_html:
            cursor.execute("""
                INSERT INTO fixed_texts (
                    text_key, text_category, text_content, text_html,
                    kathisma_number, stasis_number
                ) VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (text_key) DO NOTHING
            """, (
                f'kathisma_1_stasis_{stasis_num}', 'kathisma',
                f'First Kathisma, Stasis {stasis_num}', stasis_html,
                1, stasis_num
            ))

    db_conn.commit()
    cursor.close()
    print("✓ Imported Kathisma 1 (3 stases)")
    print("  (In full implementation, would import all 20 kathismata)")


def demo_query(db_conn):
    """
    Demonstrate querying the imported data
    """
    cursor = db_conn.cursor()

    print("\n" + "="*60)
    print("DEMO: QUERYING IMPORTED DATA")
    print("="*60)

    # Query stichera for Tone 1, Sunday
    cursor.execute("""
        SELECT text_order, verse_text, text_content
        FROM liturgical_texts
        WHERE source = 'octoechos'
        AND service_type = 'vespers'
        AND text_type = 'sticheron'
        AND tone = 1
        AND weekday = 6
        ORDER BY text_order
        LIMIT 3
    """)

    print("\nStichera on 'Lord I have cried' (Tone 1, Sunday):")
    print("-" * 60)
    for row in cursor.fetchall():
        order, verse, text = row
        print(f"\n{order}. Verse: {verse}")
        print(f"   {text[:100]}...")

    cursor.close()


if __name__ == '__main__':
    print("="*60)
    print("ANTHOLOGION DATA IMPORT - PROOF OF CONCEPT")
    print("="*60)

    # Note: This assumes PostgreSQL is set up with the schema
    # For the demo, we'll show what would happen without actually connecting

    print("\n⚠ NOTE: This is a demonstration script.")
    print("To actually run this, you need to:")
    print("1. Set up PostgreSQL (locally or on Railway)")
    print("2. Run the schema.sql to create tables")
    print("3. Set DATABASE_URL environment variable")
    print("4. Uncomment the connection code below")
    print("\nFor now, showing what the import process would do...\n")

    # Uncomment when PostgreSQL is ready:
    # try:
    #     conn = psycopg2.connect(DATABASE_URL)
    #     print("✓ Connected to database")
    #
    #     # Import the extracted Vespers data
    #     import_vespers_data('/tmp/vespers_extracted.json', conn)
    #
    #     # Import kathismata from existing code
    #     import_fixed_texts_kathismata(conn)
    #
    #     # Demo query
    #     demo_query(conn)
    #
    #     conn.close()
    #     print("\n✓ Import complete!")
    # except Exception as e:
    #     print(f"✗ Error: {e}")

    # For now, just show the structure
    print("\nExtracted data structure:")
    with open('/tmp/vespers_extracted.json', 'r') as f:
        data = json.load(f)
    print(f"  - Service: {data['service']}")
    print(f"  - Tone: {data['tone']}, Day: {data['day']}")
    print(f"  - Stichera count: {len(data['stichera_on_lord_i_cried'])}")
    print(f"  - Aposticha count: {len(data.get('aposticha', {}).get('stichera', []))}")

    print("\n" + "="*60)
    print("This would insert into the liturgical_texts table")
    print("with proper indexing on (source, tone, weekday, service_type)")
    print("="*60)
