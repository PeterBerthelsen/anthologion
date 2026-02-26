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

import os
from flask import Flask, request, send_file, render_template, redirect, after_this_request
from flask_wtf import FlaskForm
from wtforms.fields import DateField, RadioField, SelectField, SubmitField, BooleanField
from wtforms.validators import DataRequired
from service import generate_day
from calendar import monthrange
from datetime import datetime
app = Flask(__name__,template_folder='static/html')
app.config['SECRET_KEY'] = 'boughtahondabutishouldaboughtakia'

class HomeForm(FlaskForm):
    lit_dt = DateField(format='%m-%d-%Y', validators=[DataRequired()])
    type_fl = SelectField(choices=[('day','Day'),('month','Month')])
    cal_fl = SelectField(choices=[(0,'New Calendar'),(1,'Old Calendar')])
    #var_fl = RadioField(choices=[(None, 'Full Service'),('true','Variables Only')])
    down_fl = SelectField(choices=[(0,'View'),(1,'Download')])
    submit = SubmitField()

@app.route("/", methods=['POST','GET'])
def home():
    form = HomeForm()
    if request.method == 'POST':
        calendar = form.cal_fl.data
        download = form.down_fl.data
        type = form.type_fl.data
        #vars = None if form.var_fl.data == 'None' else form.var_fl.data
        #For now, all requests will be vars...
        vars = 'True'
        if vars:
            return redirect(f"/{type}?date={form.lit_dt._value()}&c={calendar}&vars={vars}&f={download}")
        else:
            return redirect(f"/{type}?date={form.lit_dt._value()}&c={calendar}&f={download}")
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
    download = request.args.get('f',None)
    download = True if download == '1' else False
    variables_only = request.args.get('vars',None)
    print(f' Loaded "/" for date: {month}/{day}/{year} ~ calendar: {calendar}')
    # if variables_only:
    #     template = 'variableDay.html'
    #     schedule = 'vcnmt'
    # else:
    #     template = 'liturgicalDay.html'
    template = 'variableDay.html'
    schedule = 'vcnmt'

    liturgics = generate_day(
        month=month
        ,day=day
        ,year=year
        ,calendar=calendar
        ,schedule=schedule
        ,variables_only_flag='True'
    )

    post = render_template(
        template
        ,liturgics = liturgics
    )

    html = render_template(
        'liturgicalPost.html'
        ,post = post
    )

    if download == True:
        f = f'{month}-{day}-{year} Anthologion.html'
        with open(f, 'wb') as file:
            file.write(html.replace('О', 'O').encode('utf-8'))
            return send_file(f, as_attachment=True)

    return html

# @app.route("/now", methods=['GET'])
# def now():
#     rubric = {
#         0: 'n'
#         ,1: 'n'
#         ,2: 'n'
#         ,3: 'm'
#         ,4: 'm'
#         ,5: 'm'
#         ,6: 'm'
#         ,7: '1'
#         ,8: '1'
#         ,9: '1'
#         ,10: '1'
#         ,11: '1'
#         ,12: '3'
#         ,13: '3'
#         ,14: '3'
#         ,15: '6'
#         ,16: '6'
#         ,17: 't'
#         ,18: 't'
#         ,19: '9'
#         ,20: '9'
#         ,21: 'v'
#         ,22: 'v'
#         ,23: 'v'
#         ,24: 'n'
#     }
#     gmt = request.args.get('gmt',0)
#     gmt = int(gmt)
#     hour = datetime.now().hour + gmt
#     hour = hour if hour >= 0 else hour + 24
#     month = request.args.get('m', None)
#     day = request.args.get('d', None)
#     year = request.args.get('y', None)
#     calendar = request.args.get('c', 1)
#     return render_template(
#         'liturgicalDay.html'
#         ,liturgics = generate_day(
#             month=month
#             ,day=day
#             ,year=year
#             ,calendar=calendar
#             ,schedule=rubric.get(hour)
#         )
#     )

@app.route("/month", methods=['GET'])
def build_month():
    dd = request.args.get('date', None)
    if dd:
        month = int(dd.split('-')[1])
        #day = int(dd.split('-')[2])
        year = int(dd.split('-')[0])
    else:
        month = request.args.get('m', None)
        #day = request.args.get('d', None)
        year = request.args.get('y', None)
    calendar = request.args.get('c', 1)
    schedule = request.args.get('s',None)
    download = request.args.get('f',None)
    download = True if download == '1' else False
    variables_only = request.args.get('vars','True')
    today = datetime.today()
    month = int(month) if type(month) == str else month
    month = month if month else today.month
    year = int(year) if type(year) == str else year
    year = year if year else today.year
    days = range(1,monthrange(year,month)[1] + 1)
    contents = '<h2>Days</h2>'
    post = ''
    # if variables_only:
    #     template = 'variableDay.html'
    #     schedule = 'vcnmt'
    # else:
    #     template = 'liturgicalDay.html'
    template = 'variableDay.html'
    schedule = 'vcnmt'


    for day in days:
        liturgics = generate_day(
            month=month
            ,day=day
            ,year=year
            ,calendar=calendar
            ,schedule=schedule
            ,variables_only_flag='True'
        )

        contents += render_template(
            'liturgicalContents.html'
            ,liturgics = liturgics
        )

        post += render_template(
            template
            ,liturgics = liturgics
        )

    html = render_template(
        'liturgicalPost.html'
        ,contents = contents
        ,post = post
    )

    if download == True:
        f = f'{month}-{year} Anthologion.html'
        with open(f, 'wb') as file:
            file.write(html.replace('О', 'O').encode('utf-8'))
            return send_file(f, as_attachment=True)

    return html

if __name__ == "__main__":
    app.run(threaded=True, debug=True, port=5000)
