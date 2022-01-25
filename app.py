"""
Version 0.1.3
Updated 10/21/2021

Change Log:
10/13/2021 - 0.1.0 - Initial Creation
10/14/2021 - 0.1.1 - Stable Vespers generation with variables
10/21/2021 - 0.1.3 - Updated for jinja templating and rendering

for local hosting:
set FLASK_APP=app
set FLASK_ENV=development
flask run
"""

from flask import Flask, request, render_template
from service import generate_day
from calendar import monthrange
from datetime import datetime
app = Flask(__name__,template_folder='static/html')

@app.route("/", methods=['GET'])
def main():
    month = request.args.get('m', None)
    day = request.args.get('d', None)
    year = request.args.get('y', None)
    calendar = request.args.get('c', 1)
    schedule = request.args.get('s',None)
    variables_only = request.args.get('vars',None)
    print(f' Loaded "/" for date: {month}/{day}/{year} ~ calendar: {calendar}')
    if variables_only:
        return render_template(
            'variableDay.html'
            ,liturgics = generate_day(
                month=month
                ,day=day
                ,year=year
                ,calendar=calendar
                ,schedule='vcnmt'
                ,variables_only_flag=variables_only
            )
        )
    else:
        return render_template(
            'liturgicalDay.html'
            ,liturgics = generate_day(
                month=month
                ,day=day
                ,year=year
                ,calendar=calendar
                ,schedule=schedule
            )
        )

@app.route("/now", methods=['GET'])
def now():
    rubric = {
        0: 'n'
        ,1: 'n'
        ,2: 'n'
        ,3: 'm'
        ,4: 'm'
        ,5: 'm'
        ,6: 'm'
        ,7: '1'
        ,8: '1'
        ,9: '1'
        ,10: '1'
        ,11: '1'
        ,12: '3'
        ,13: '3'
        ,14: '3'
        ,15: '6'
        ,16: '6'
        ,17: 't'
        ,18: 't'
        ,19: '9'
        ,20: '9'
        ,21: 'v'
        ,22: 'v'
        ,23: 'v'
        ,24: 'n'
    }
    gmt = request.args.get('gmt',0)
    gmt = int(gmt)
    hour = datetime.now().hour + gmt
    hour = hour if hour >= 0 else hour + 24
    month = request.args.get('m', None)
    day = request.args.get('d', None)
    year = request.args.get('y', None)
    calendar = request.args.get('c', 1)
    return render_template(
        'liturgicalDay.html'
        ,liturgics = generate_day(
            month=month
            ,day=day
            ,year=year
            ,calendar=calendar
            ,schedule=rubric.get(hour)
        )
    )

@app.route("/month", methods=['GET'])
def build_month():
    month = request.args.get('m', None)
    year = request.args.get('y', None)
    calendar = request.args.get('c', 1)
    schedule = request.args.get('s',None)
    variables_only = request.args.get('vars',None)
    today = datetime.today()
    month = int(month) if type(month) == str else month
    month = month if month else today.month
    year = int(year) if type(year) == str else year
    year = year if year else today.year
    days = range(1,monthrange(year,month)[1] + 1)
    contents = '<h2>Contents</h2>'
    header = """<head><link href="../static/css/main.css" rel="stylesheet"/>
    <link rel="shortcut icon" href="{{ url_for("static", filename="favicon.ico") }}">
    </head><body><div id="wrapper"><div id="main">"""
    html = ''
    if variables_only:
        month_template = 'variableMonth.html'
        schedule = 'vcnmt'
    else:
        month_template = 'liturgicalMonth.html'

    for day in days:
        contents += render_template(
            'liturgicalContents.html'
            ,liturgics = generate_day(
                month=month
                ,day=day
                ,year=year
                ,calendar=calendar
                ,schedule=schedule
                ,variables_only_flag=variables_only
            )
        )
        html += render_template(
            month_template
            ,liturgics = generate_day(
                month=month
                ,day=day
                ,year=year
                ,calendar=calendar
                ,schedule=schedule
                ,variables_only_flag=variables_only
            )
        )
    contents = '<section class="post" id="contents">' + contents + '</section>'
    html = header + contents + html
    html += '</div></div></body>'
    return html

if __name__ == "__main__":
    app.run(threaded=True, debug=True, port=5000)
