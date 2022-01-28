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

from flask import Flask, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms.fields import DateField, RadioField, SelectField, SubmitField
from wtforms.validators import DataRequired
from service import generate_day
from calendar import monthrange
from datetime import datetime
app = Flask(__name__,template_folder='static/html')
app.config['SECRET_KEY'] = 'boughtahondabutishouldaboughtakia'

class HomeForm(FlaskForm):
    lit_dt = DateField(format='%m-%d-%Y', validators=[DataRequired()])
    cal_fl = SelectField(choices=[(1,'New Calendar'),(0,'Old Calendar')])
    var_fl = RadioField(choices=[(None, 'Full Service'),('true','Variables Only')])
    submit = SubmitField()

@app.route("/", methods=['POST','GET'])
def home():
    form = HomeForm()
    if request.method == 'POST':
        calendar = form.cal_fl.data
        vars = None if form.var_fl.data == 'None' else form.var_fl.data
        print(vars)
        if vars:
            return redirect(f"/day?date={form.lit_dt._value()}&c={calendar}&vars={vars}")
        else:
            return redirect(f"/day?date={form.lit_dt._value()}&c={calendar}")
    else:
        return render_template(
            'home.html'
            ,today = datetime.today()
            ,form = form
        )

@app.route("/day", methods=['POST','GET'])
def main():
    dd = request.args.get('date', None)
    if dd:
        month = int(dd.split('-')[1])
        day = int(dd.split('-')[2])
        year = int(dd.split('-')[0])
    else:
        month = request.args.get('m', None)
        day = request.args.get('d', None)
        year = request.args.get('y', None)
    calendar = request.args.get('c', 1)
    schedule = request.args.get('s',None)
    variables_only = request.args.get('vars',None)
    print(f' Loaded "/" for date: {month}/{day}/{year} ~ calendar: {calendar}')
    if variables_only:
        template = 'variableDay.html'
        schedule = 'vcnmt'
    else:
        template = 'liturgicalDay.html'

    liturgics = generate_day(
        month=month
        ,day=day
        ,year=year
        ,calendar=calendar
        ,schedule=schedule
        ,variables_only_flag=variables_only
    )

    post = render_template(
        template
        ,liturgics = liturgics
    )

    return render_template(
        'liturgicalPost.html'
        ,post = post
    )
    return html

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
    contents = '<h2>Days</h2>'
    post = ''
    if variables_only:
        template = 'variableDay.html'
        schedule = 'vcnmt'
    else:
        template = 'liturgicalDay.html'

    for day in days:
        liturgics = generate_day(
            month=month
            ,day=day
            ,year=year
            ,calendar=calendar
            ,schedule=schedule
            ,variables_only_flag=variables_only
        )

        contents += render_template(
            'liturgicalContents.html'
            ,liturgics = liturgics
        )

        post += render_template(
            template
            ,liturgics = liturgics
        )

    return render_template(
        'liturgicalPost.html'
        ,contents = contents
        ,post = post
    )

if __name__ == "__main__":
    app.run(threaded=True, debug=True, port=5000)
