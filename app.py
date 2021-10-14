"""
Version 0.1.1
Updated 10/14/2021

Change Log:
10/13/2021 - 0.1.0 - Initial Creation
10/14/2021 - 0.1.1 - Stable Vespers generation with variables

for local hosting:
set FLASK_APP=app
set FLASK_ENV=development
flask run
"""

from flask import Flask, request
from service import generate_day
app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():

    month = request.args.get('m', None)
    day = request.args.get('d', None)
    year = request.args.get('y', None)
    calendar = request.args.get('c', None)
    print(f'{month}/{day}/{year} ~ {calendar}')
    return generate_day(month=month, day=day, year=year, calendar=calendar)

# if __name__ == "__main__":
#     app.run(threaded=True, port=5000)
