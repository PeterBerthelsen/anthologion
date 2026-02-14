"""
Anthologion v2.0 - Database-driven Flask Application
Modern rewrite using PostgreSQL instead of live PDF parsing
"""

from flask import Flask, request, render_template_string, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime, date
import os

app = Flask(__name__)

# Database connection - from Railway environment variable
DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://localhost/anthologion')


def get_db_connection():
    """Get PostgreSQL database connection"""
    return psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)


def calculate_paschalion(year, month, day):
    """
    Call the database function to calculate paschalion
    Returns tone, pascha offset, liturgical week info
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM calculate_paschalion(%s, %s, %s)
        """, (year, month, day))
        result = cursor.fetchone()
        cursor.close()
        return dict(result) if result else None


def get_vespers_texts(tone, weekday):
    """
    Query database for Vespers texts based on tone and weekday
    Much cleaner than parsing PDFs!
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()

        # Get stichera on "Lord I have cried"
        cursor.execute("""
            SELECT text_order, verse_text, text_content
            FROM liturgical_texts
            WHERE source = 'octoechos'
            AND service_type = 'vespers'
            AND text_type = 'sticheron'
            AND tone = %s
            AND weekday = %s
            ORDER BY text_order
        """, (tone, weekday))
        stichera = cursor.fetchall()

        # Get theotokion
        cursor.execute("""
            SELECT text_content
            FROM liturgical_texts
            WHERE source = 'octoechos'
            AND service_type = 'vespers'
            AND text_type = 'theotokion'
            AND tone = %s
            AND weekday = %s
            AND (rubric_notes IS NULL OR rubric_notes != 'Aposticha Theotokion')
            LIMIT 1
        """, (tone, weekday))
        theotokion = cursor.fetchone()

        # Get aposticha
        cursor.execute("""
            SELECT text_order, verse_text, text_content
            FROM liturgical_texts
            WHERE source = 'octoechos'
            AND service_type = 'vespers'
            AND text_type = 'aposticha'
            AND tone = %s
            AND weekday = %s
            ORDER BY text_order
        """, (tone, weekday))
        aposticha = cursor.fetchall()

        # Get prokeimenon (from fixed_texts table)
        cursor.execute("""
            SELECT text_content
            FROM fixed_texts
            WHERE text_category = 'prokeimenon'
            AND weekday = %s
            LIMIT 1
        """, (weekday,))
        prokeimenon = cursor.fetchone()

        cursor.close()

        return {
            'stichera': stichera,
            'theotokion': theotokion,
            'aposticha': aposticha,
            'prokeimenon': prokeimenon
        }


def get_kathisma(kathisma_number):
    """
    Query database for kathisma reading
    Instead of using the hardcoded kathisma.py
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT text_html
            FROM fixed_texts
            WHERE text_category = 'kathisma'
            AND kathisma_number = %s
            ORDER BY stasis_number
        """, (kathisma_number,))

        stases = cursor.fetchall()
        cursor.close()

        return ''.join([s['text_html'] for s in stases if s['text_html']])


# ============================================================
# ROUTES
# ============================================================

@app.route('/')
def index():
    """
    Main service generation endpoint
    Query params: m (month), d (day), y (year), c (calendar: 0=new, 1=old)
    """
    # Get parameters
    month = request.args.get('m', datetime.today().month, type=int)
    day = request.args.get('d', datetime.today().day, type=int)
    year = request.args.get('y', datetime.today().year, type=int)
    calendar = request.args.get('c', 0, type=int)  # 0=new, 1=old

    # Calculate paschalion using database function
    paschalion = calculate_paschalion(year, month, day)

    if not paschalion:
        return "Error calculating paschalion", 500

    tone = paschalion['weekly_tone']
    service_date = date(year, month, day)
    weekday = service_date.weekday()  # Python weekday: 0=Monday, 6=Sunday

    # Kathisma schedule (same as original code)
    kathisma_rubric = {
        0: 0,   # Monday
        1: 6,   # Tuesday
        2: 9,   # Wednesday
        3: 12,  # Thursday
        4: 15,  # Friday
        5: 18,  # Saturday
        6: 1    # Sunday
    }

    # Build service HTML
    html = render_template_string("""
<!DOCTYPE html>
<html>
<head>
    <title>Vespers - {{ date_str }}</title>
    <style>
        body { font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, serif; max-width: 800px; margin: 40px auto; padding: 20px; }
        h1 { text-align: center; color: #8B0000; }
        h2 { color: #4B0082; margin-top: 30px; }
        .note { font-style: italic; color: #666; }
        .sticheron { margin: 20px 0; padding-left: 20px; }
        .verse { font-style: italic; color: #444; margin-bottom: 5px; }
        .info { background: #f0f0f0; padding: 10px; border-left: 4px solid #8B0000; margin: 20px 0; }
    </style>
</head>
<body>
    <h1>Vespers</h1>
    <div class="info">
        <strong>Date:</strong> {{ date_str }}<br>
        <strong>Tone:</strong> {{ tone }}<br>
        <strong>Pascha Offset:</strong> {{ pascha_offset }} days<br>
        <strong>Calendar:</strong> {{ 'Old Calendar' if calendar == 1 else 'New Calendar' }}
    </div>

    <h2>Kathisma {{ kathisma_num }}</h2>
    <div class="note">Kathisma reading would appear here (from database)</div>

    <h2>Stichera on "Lord, I have cried"</h2>
    <div class="note">Tone {{ tone }} stichera:</div>
    {% for sticheron in stichera %}
    <div class="sticheron">
        {% if sticheron.verse_text %}
        <div class="verse">Verse: {{ sticheron.verse_text }}</div>
        {% endif %}
        <div>{{ sticheron.text_content }}</div>
    </div>
    {% endfor %}

    {% if theotokion %}
    <h2>Theotokion</h2>
    <div class="sticheron">{{ theotokion.text_content }}</div>
    {% endif %}

    <h2>Prokeimenon</h2>
    <div class="sticheron">
        {% if prokeimenon %}
        {{ prokeimenon.text_content }}
        {% else %}
        <div class="note">(Daily prokeimenon from database)</div>
        {% endif %}
    </div>

    <h2>Aposticha</h2>
    {% for stich in aposticha %}
    <div class="sticheron">
        {% if stich.verse_text %}
        <div class="verse">Verse: {{ stich.verse_text }}</div>
        {% endif %}
        <div>{{ stich.text_content }}</div>
    </div>
    {% endfor %}

    <hr style="margin: 40px 0;">
    <div class="info">
        <strong>Database-Driven Generation</strong><br>
        This service was generated by querying PostgreSQL, not parsing PDFs!<br>
        <small>Anthologion v2.0 - Proof of Concept</small>
    </div>
</body>
</html>
    """,
        date_str=f"{month}/{day}/{year}",
        tone=tone or 'N/A',
        pascha_offset=paschalion['pascha_offset'],
        calendar=calendar,
        kathisma_num=kathisma_rubric.get(weekday, 1),
        stichera=[] if not tone else get_vespers_texts(tone, weekday)['stichera'],
        theotokion=None if not tone else get_vespers_texts(tone, weekday)['theotokion'],
        prokeimenon=get_vespers_texts(tone, weekday)['prokeimenon'] if tone else None,
        aposticha=[] if not tone else get_vespers_texts(tone, weekday)['aposticha']
    )

    return html


@app.route('/api/paschalion')
def api_paschalion():
    """
    API endpoint for paschalion calculation
    Returns JSON
    """
    month = request.args.get('m', datetime.today().month, type=int)
    day = request.args.get('d', datetime.today().day, type=int)
    year = request.args.get('y', datetime.today().year, type=int)

    result = calculate_paschalion(year, month, day)

    # Convert date objects to strings for JSON
    if result:
        result['pascha_date'] = str(result['pascha_date'])
        result['pentecost_date'] = str(result['pentecost_date'])

    return jsonify(result)


@app.route('/api/texts/<source>/<service>/<text_type>')
def api_texts(source, service, text_type):
    """
    API endpoint to query liturgical texts
    Example: /api/texts/octoechos/vespers/sticheron?tone=1&weekday=6
    """
    tone = request.args.get('tone', type=int)
    weekday = request.args.get('weekday', type=int)

    with get_db_connection() as conn:
        cursor = conn.cursor()

        query = """
            SELECT text_order, text_content, verse_text, rubric_notes
            FROM liturgical_texts
            WHERE source = %s
            AND service_type = %s
            AND text_type = %s
        """
        params = [source, service, text_type]

        if tone is not None:
            query += " AND tone = %s"
            params.append(tone)

        if weekday is not None:
            query += " AND weekday = %s"
            params.append(weekday)

        query += " ORDER BY text_order"

        cursor.execute(query, params)
        results = cursor.fetchall()
        cursor.close()

        return jsonify([dict(r) for r in results])


@app.route('/health')
def health():
    """Health check endpoint for Railway"""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1")
            cursor.close()
        return jsonify({"status": "healthy", "database": "connected"})
    except Exception as e:
        return jsonify({"status": "unhealthy", "error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
