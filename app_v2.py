"""
Anthologion v2.0 - Database-driven Flask Application
Modern rewrite using PostgreSQL instead of live PDF parsing

Routes:
  /                     - Main service page (Vespers by default)
  /api/vespers          - JSON API for Vespers service
  /api/paschalion       - JSON API for paschalion calculation
  /api/feast            - JSON API for feast lookup
  /api/texts/<source>   - JSON API for text queries
  /health               - Health check for Railway
"""

from flask import Flask, request, render_template_string, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime, date
import os
import json

app = Flask(__name__)

DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://localhost/anthologion')


def get_db():
    """Get PostgreSQL database connection with RealDictCursor"""
    return psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)


# ============================================================
# HTML TEMPLATE
# ============================================================
SERVICE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <style>
        :root {
            --primary: #8B0000;
            --accent: #4B0082;
            --bg: #FFFEF5;
            --text: #2C1810;
            --verse: #555;
            --rubric: #8B0000;
            --border: #D4C5A9;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, Georgia, serif;
            max-width: 750px;
            margin: 0 auto;
            padding: 20px;
            background: var(--bg);
            color: var(--text);
            line-height: 1.7;
        }
        h1 {
            text-align: center;
            color: var(--primary);
            font-size: 1.8em;
            margin-bottom: 5px;
            letter-spacing: 2px;
        }
        .subtitle {
            text-align: center;
            color: var(--accent);
            font-size: 1.1em;
            margin-bottom: 20px;
        }
        .info-bar {
            background: #F5F0E0;
            border: 1px solid var(--border);
            border-left: 4px solid var(--primary);
            padding: 12px 16px;
            margin: 15px 0;
            font-size: 0.9em;
        }
        .info-bar strong { color: var(--primary); }
        .section-header {
            color: var(--primary);
            font-size: 1.2em;
            margin: 30px 0 10px;
            border-bottom: 1px solid var(--border);
            padding-bottom: 5px;
        }
        .rubric {
            font-style: italic;
            color: var(--rubric);
            font-size: 0.95em;
            margin: 8px 0;
        }
        .sticheron {
            margin: 15px 0;
            padding-left: 20px;
        }
        .verse {
            font-style: italic;
            color: var(--verse);
            font-size: 0.9em;
            margin-bottom: 3px;
        }
        .source-tag {
            display: inline-block;
            font-size: 0.7em;
            background: #E8E0D0;
            color: var(--accent);
            padding: 1px 6px;
            border-radius: 3px;
            margin-left: 8px;
            vertical-align: middle;
        }
        .tone-tag {
            display: inline-block;
            font-size: 0.75em;
            background: var(--primary);
            color: white;
            padding: 1px 6px;
            border-radius: 3px;
            margin-left: 5px;
        }
        .nav {
            text-align: center;
            margin: 20px 0;
            font-size: 0.9em;
        }
        .nav a {
            color: var(--accent);
            margin: 0 10px;
            text-decoration: none;
        }
        .nav a:hover { text-decoration: underline; }
        footer {
            margin-top: 40px;
            padding-top: 15px;
            border-top: 1px solid var(--border);
            text-align: center;
            font-size: 0.8em;
            color: #999;
        }
        @media (max-width: 600px) {
            body { padding: 10px; font-size: 15px; }
            h1 { font-size: 1.4em; }
        }
    </style>
</head>
<body>
    <h1>VESPERS</h1>
    <div class="subtitle">{{ feast_name }}</div>

    <div class="info-bar">
        <strong>Date:</strong> {{ date_str }} |
        <strong>Tone:</strong> {{ tone or 'N/A' }} |
        <strong>Rank:</strong> {{ rank_name }} |
        <strong>Calendar:</strong> {{ calendar_name }}
    </div>

    <div class="nav">
        <a href="?m={{ prev_month }}&d={{ prev_day }}&y={{ prev_year }}&c={{ calendar }}">&larr; Previous Day</a>
        |
        <a href="?c={{ calendar }}">Today</a>
        |
        <a href="?m={{ next_month }}&d={{ next_day }}&y={{ next_year }}&c={{ calendar }}">Next Day &rarr;</a>
    </div>

    {% for section in sections %}
        {% if section.source == 'rubric' or section.source == 'system' %}
            {% if section.section_name == 'header' %}
                {# Already shown in header #}
            {% else %}
                <h2 class="section-header">{{ section.text_content }}</h2>
                {% if section.rubric %}
                <div class="rubric">{{ section.rubric }}</div>
                {% endif %}
            {% endif %}
        {% else %}
            <div class="sticheron">
                {% if section.verse_text %}
                <div class="verse">Verse: {{ section.verse_text }}</div>
                {% endif %}
                {% if section.rubric %}
                <div class="rubric">{{ section.rubric }}
                    {% if section.tone %}<span class="tone-tag">Tone {{ section.tone }}</span>{% endif %}
                    <span class="source-tag">{{ section.source }}</span>
                </div>
                {% endif %}
                <div>{{ section.text_content }}</div>
            </div>
        {% endif %}
    {% endfor %}

    {% if not sections %}
    <div class="info-bar">
        <strong>Note:</strong> No texts loaded yet for this date/tone combination.
        Database needs to be populated with Octoechos and Menaion texts.
    </div>
    {% endif %}

    <footer>
        Anthologion v2.0 &mdash; Database-Driven Liturgical Service Generator<br>
        <small>Generated from PostgreSQL in {{ gen_time }}ms</small>
    </footer>
</body>
</html>
"""


# ============================================================
# ROUTES
# ============================================================

@app.route('/')
def index():
    """Main service generation page"""
    import time
    start = time.time()

    # Parse date parameters
    today = datetime.today()
    month = request.args.get('m', today.month, type=int)
    day = request.args.get('d', today.day, type=int)
    year = request.args.get('y', today.year, type=int)
    calendar = request.args.get('c', 0, type=int)  # 0=new, 1=old

    try:
        service_date = date(year, month, day)
    except ValueError:
        return "Invalid date", 400

    # Calculate prev/next days
    from datetime import timedelta
    prev_date = service_date - timedelta(days=1)
    next_date = service_date + timedelta(days=1)

    try:
        with get_db() as conn:
            cursor = conn.cursor()

            # Call generate_vespers() stored procedure
            cursor.execute("""
                SELECT * FROM generate_vespers(%s, %s)
                ORDER BY section_order, text_order
            """, (service_date, 'old' if calendar == 1 else 'new'))
            sections = cursor.fetchall()

            # Get paschalion info for display
            cursor.execute("""
                SELECT * FROM calculate_paschalion(%s, %s, %s)
            """, (year, month, day))
            paschalion = cursor.fetchone()

            # Get feast info for display
            cursor.execute("""
                SELECT * FROM get_feast_for_date(%s, %s)
            """, (service_date, 'old' if calendar == 1 else 'new'))
            feast = cursor.fetchone()

            cursor.close()

        tone = paschalion['weekly_tone'] if paschalion else None
        feast_name = feast['feast_name'] if feast else 'Ordinary Day'
        feast_rank = feast['rank'] if feast else 7

        rank_names = {
            1: 'Great Feast', 2: 'Vigil', 3: 'Polyeleos',
            4: 'Doxology', 5: 'Six Stichera', 6: 'Afterfeast', 7: 'Ordinary'
        }

        gen_time = round((time.time() - start) * 1000, 1)

        return render_template_string(
            SERVICE_TEMPLATE,
            title=f"Vespers - {feast_name}",
            feast_name=feast_name,
            date_str=service_date.strftime('%B %d, %Y'),
            tone=tone,
            rank_name=rank_names.get(feast_rank, 'Ordinary'),
            calendar=calendar,
            calendar_name='Old Calendar' if calendar == 1 else 'New Calendar',
            sections=sections,
            prev_month=prev_date.month, prev_day=prev_date.day, prev_year=prev_date.year,
            next_month=next_date.month, next_day=next_date.day, next_year=next_date.year,
            gen_time=gen_time
        )

    except psycopg2.OperationalError:
        return render_template_string("""
        <html><body style="font-family: sans-serif; max-width: 600px; margin: 40px auto; padding: 20px;">
        <h1>Database Not Connected</h1>
        <p>Set the <code>DATABASE_URL</code> environment variable to your PostgreSQL connection string.</p>
        <p>Then run <code>schema_v2.sql</code>, <code>feast_calendar.sql</code>, and <code>typikon_rules.sql</code> to set up the database.</p>
        <h2>Quick Setup</h2>
        <pre>
export DATABASE_URL="postgresql://user:pass@host:5432/anthologion"
psql $DATABASE_URL -f database/schema_v2.sql
psql $DATABASE_URL -f database/feast_calendar.sql
psql $DATABASE_URL -f database/typikon_rules.sql
        </pre>
        </body></html>
        """), 503


@app.route('/api/vespers')
def api_vespers():
    """JSON API: Generate Vespers for a date"""
    month = request.args.get('m', datetime.today().month, type=int)
    day = request.args.get('d', datetime.today().day, type=int)
    year = request.args.get('y', datetime.today().year, type=int)
    calendar = request.args.get('c', 'new')

    try:
        service_date = date(year, month, day)
    except ValueError:
        return jsonify({"error": "Invalid date"}), 400

    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM generate_vespers(%s, %s)
            ORDER BY section_order, text_order
        """, (service_date, calendar))
        sections = cursor.fetchall()
        cursor.close()

    return jsonify({
        "date": str(service_date),
        "calendar": calendar,
        "sections": [dict(s) for s in sections]
    })


@app.route('/api/paschalion')
def api_paschalion():
    """JSON API: Paschalion calculation"""
    month = request.args.get('m', datetime.today().month, type=int)
    day = request.args.get('d', datetime.today().day, type=int)
    year = request.args.get('y', datetime.today().year, type=int)

    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM calculate_paschalion(%s, %s, %s)", (year, month, day))
        result = cursor.fetchone()
        cursor.close()

    if result:
        # Convert dates to strings for JSON
        result = dict(result)
        result['pascha_date'] = str(result['pascha_date'])
        result['pentecost_date'] = str(result['pentecost_date'])

    return jsonify(result)


@app.route('/api/feast')
def api_feast():
    """JSON API: Feast lookup for a date"""
    month = request.args.get('m', datetime.today().month, type=int)
    day = request.args.get('d', datetime.today().day, type=int)
    year = request.args.get('y', datetime.today().year, type=int)
    calendar = request.args.get('c', 'new')

    try:
        service_date = date(year, month, day)
    except ValueError:
        return jsonify({"error": "Invalid date"}), 400

    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM get_feast_for_date(%s, %s)", (service_date, calendar))
        result = cursor.fetchone()
        cursor.close()

    if result:
        result = dict(result)
        result['saint_names'] = list(result.get('saint_names', []))

    return jsonify(result or {"feast_name": None, "rank": 7, "message": "No feast for this date"})


@app.route('/api/texts/<source>/<service>/<text_type>')
def api_texts(source, service, text_type):
    """JSON API: Query liturgical texts"""
    tone = request.args.get('tone', type=int)
    weekday = request.args.get('weekday', type=int)
    saint_class = request.args.get('saint_class')

    with get_db() as conn:
        cursor = conn.cursor()

        query = """
            SELECT text_order, tone, text_content, verse_text, melody_spec, rubric_notes
            FROM liturgical_texts
            WHERE source = %s AND service_type = %s AND text_type = %s
        """
        params = [source, service, text_type]

        if tone is not None:
            query += " AND tone = %s"
            params.append(tone)
        if weekday is not None:
            query += " AND weekday = %s"
            params.append(weekday)
        if saint_class:
            query += " AND saint_class = %s"
            params.append(saint_class)

        query += " ORDER BY text_order"

        cursor.execute(query, params)
        results = cursor.fetchall()
        cursor.close()

    return jsonify([dict(r) for r in results])


@app.route('/health')
def health():
    """Health check for Railway deployment"""
    try:
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1")
            cursor.close()
        return jsonify({"status": "healthy", "database": "connected"})
    except Exception as e:
        return jsonify({"status": "unhealthy", "error": str(e)}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
