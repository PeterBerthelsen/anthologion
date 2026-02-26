"""
Anthologion API — Liturgical service variable resolver.

MVP: returns JSON variables for any date, sourced entirely from
pre-extracted JSON data. No PDF reads, no database.

Usage:
    python3 api.py                          # runs on port 5000
    PORT=8080 python3 api.py                # custom port

Endpoints:
    GET /api/resolve?m=2&d=26&y=2026
        Full liturgical context for a date.

    GET /api/resolve?m=2&d=26&y=2026&service=vespers
        Merged variables for a specific service type.

    GET /api/paschalion?m=2&d=26&y=2026
        Just the paschalion (liturgical calendar) data.

    GET /health
        Health check.

Query parameters (all optional — defaults to today):
    m         Month (1-12)
    d         Day (1-31)
    y         Year
    service   Filter to one service: vespers, matins, liturgy, compline, etc.
    calendar  0 = new calendar (default), 1 = old calendar
"""

import os
from datetime import datetime, date
from flask import Flask, request, jsonify
from resolver import resolve, resolve_service, paschalion

app = Flask(__name__)


def _parse_date(args):
    """Extract month/day/year from request args, defaulting to today."""
    today = datetime.today()
    m = args.get('m', today.month, type=int)
    d = args.get('d', today.day, type=int)
    y = args.get('y', today.year, type=int)
    return m, d, y


def _serialize(obj):
    """Make an object JSON-safe (handle datetime, date, etc.)."""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    if isinstance(obj, dict):
        return {k: _serialize(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_serialize(i) for i in obj]
    return obj


@app.route('/api/resolve')
def api_resolve():
    """
    Main endpoint: resolve all liturgical variables for a date.

    Optional `service` param filters to a single merged service type.
    """
    m, d, y = _parse_date(request.args)
    calendar = request.args.get('calendar', 1, type=int)
    service = request.args.get('service', None)

    try:
        date(y, m, d)  # validate
    except ValueError:
        return jsonify({'error': f'Invalid date: {m}/{d}/{y}'}), 400

    if service:
        merged = resolve_service(m, d, y, service, calendar)
        return jsonify(_serialize({
            'date': f'{y}-{m:02d}-{d:02d}',
            'service': service,
            'calendar': 'old' if calendar == 1 else 'new',
            'variables': merged,
        }))

    ctx = resolve(m, d, y, calendar)
    return jsonify(_serialize({
        'date': ctx['date'],
        'weekday': ctx['weekday'],
        'weekday_name': ctx['weekday_name'],
        'calendar': 'old' if calendar == 1 else 'new',
        'period': ctx['period'],
        'sources': ctx['sources'],
        'liturgical': ctx['liturgical'],
        'feast': ctx['feast'],
        'triodion': _summary(ctx['triodion']),
        'pentecostarion': _summary(ctx['pentecostarion']),
        'octoechos': _summary(ctx['octoechos']),
        'menaion': _menaion_summary(ctx['menaion']),
    }))


def _summary(entry):
    """Summarize a source entry (key, desc, available services) without full text."""
    if not entry:
        return None
    return {
        'key': entry.get('key'),
        'desc': entry.get('desc'),
        'tone': entry.get('tone'),
        'services': list(entry.get('services', {}).keys()),
    }


def _menaion_summary(entry):
    """Summarize menaion entry."""
    if not entry:
        return None
    return {
        'rank': entry.get('rank'),
        'service_type': entry.get('service_type'),
        'service_name': entry.get('service_name'),
        'long_name': entry.get('long_name'),
        'services': list((entry.get('services') or {}).keys()),
    }


@app.route('/api/paschalion')
def api_paschalion():
    """Paschalion calculation for a date."""
    m, d, y = _parse_date(request.args)

    try:
        date(y, m, d)
    except ValueError:
        return jsonify({'error': f'Invalid date: {m}/{d}/{y}'}), 400

    result = paschalion(m, d, y)
    return jsonify(_serialize(result))


@app.route('/health')
def health():
    """Health check."""
    return jsonify({
        'status': 'ok',
        'version': '3.0.0',
        'data_sources': ['triodion', 'pentecostarion', 'octoechos', 'menaion'],
    })


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', '1') == '1'
    app.run(host='0.0.0.0', port=port, debug=debug)
