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
from bs4 import BeautifulSoup
app = Flask(__name__,template_folder='static/html')

@app.route("/", methods=['GET'])
def main():
    month = request.args.get('m', None)
    day = request.args.get('d', None)
    year = request.args.get('y', None)
    calendar = request.args.get('c', None)
    print(f' Loaded "/" for date: {month}/{day}/{year} ~ calendar: {calendar}')
    return render_template('liturgicalDay.html', liturgics = generate_day(month=month, day=day, year=year, calendar=calendar))

if __name__ == "__main__":
    app.run(threaded=True, debug=True, port=5000)
