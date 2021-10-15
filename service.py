"""
Version 0.1.1
Updated 10/14/2021

Change Log:
10/11/2021 - 0.0.8 - Initial Creation, Vespers elements
10/12/2021 - 0.0.9 - Paschalion (def pascha) calculations started.
10/13/2021 - 0.0.9 - Tone of the week added to Paschalion
10/13/2021 - 0.1.0 - Initial build of Vespers service complete
10/14/2021 - 0.1.1 - Updated variables for Flask integration
"""
import os
from prokeimena import vespers_prokeimena
from kathisma import parse_kathisma
from datetime import datetime, timedelta, date
from octoechos import octoechos_variables
from _utils import process_pdf
from bs4 import BeautifulSoup

def is_leap_year(year):
    """
    Determine whether given a year is a leap year.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def paschalion(month, day, year):
    """
    Takes in a date and determines the last pascha, next pashca, and current weeks after pentecost
    returns list value
    """
    #convert strings to int
    month = int(month) if type(month) == str else month
    day = int(day) if type(day) == str else day
    year = int(year) if type(year) == str else year

    moveable_dates = {}
    T = datetime(year,month,day)
    Y = year
    L = is_leap_year(Y)
    #Offset for Old Calendar
    if Y <= 2099:
        O = 13
    elif 2100 < Y <= 2199:
        O = 14
    elif 2200 < Y <= 2299:
        O = 15
    elif 2300 < Y <= 2499:
        O = 15

    # a = Y % 19
    # b = ((19 * a) + 15) % 30
    # c = (Y + (Y // 4) + b) % 7
    # d = b - c
    # M = ((d + 40) // 44) + 3
    # D = ((d + 28) - 31) * (M // 4)

    a = Y % 4
    b = Y % 7
    c = Y % 19
    d = ((19 * c) + 15) % 30
    e = ((2 * a) + (4 * b) - d + 34) % 7
    f = d + e + 114
    M = f // 31
    D = (f % 31) + 1


    #print(M, D, Y)
    this_pascha = datetime(Y,M,D) + timedelta(days=O)
    this_pentecost = this_pascha + timedelta(days=49) #7 weeks after Pascha
    last_pascha = last_pentecost = lent_week = pascha_week = weeks_after = feast_day = weekly_tone = None #establish variables
    pascha_offset = (T - this_pascha).days

    #Calculate Liturgical Week based on Paschal date
    if pascha_offset < -70: #BEFORE lent period (no Triodion), get weeks after P
        last_pentecost = paschalion(month=12,day=31,year=Y-1).get('pentecost') #Last Year's Pentecost
        weeks_after = (((T - last_pentecost).days - 1) // 7) + 1 #Weeks after previous year P
        #print(f'{T}: {weeks_after} weeks after... ')

    elif -70 <= pascha_offset <= -49: #Weeks before Lent (Triodion in use)
        lent_week = (pascha_offset + 48) // 7 #Weeks before lent (negative integer)
        #print(f'{T}: {lent_week} week before lent!')

    elif -49 < pascha_offset < 0: #During Lent (Triodion in use)
        lent_week = ((pascha_offset + 48) // 7 ) + 1 #Week of lent (positive integer)
        #print(f'{T}: {lent_week} week of lent!')

    elif 0 <= pascha_offset <= 49: #During Paschal period (Pentecostarion in use)
        pascha_week = (pascha_offset // 7) + 1 #Week of Pascha (integer)
        #print(f'{T}: {pascha_week} week of Pascha!')

    elif pascha_offset > 49: #After Pentecost (no Pentecostarion)
        weeks_after = (((T - this_pentecost).days - 1) // 7) + 1 #Week after Pentecost
        #print(f'{T}: {weeks_after} weeks after...')

    #Calculate Tone of the Week
    if pascha_week: #Currently in the Paschal season. This is where the tones reset
        #No tone for Bright Week or Pentecost, otherwise, tone 1 is pascha week 2, etc.
        weekly_tone = None if pascha_week == 1 or pascha_week == 8 else (pascha_week - 1)

    elif -7 <= pascha_offset < 0: #Holy Week, No tone
        weekly_tone = None

    elif pascha_offset > 0: #Past Pascha in a given year...
        weekly_tone = (pascha_offset) // 7 #tones iterate weekly
        weekly_tone = (weekly_tone % 8) if weekly_tone > 8 else weekly_tone #after tone 8, back to 1
        weekly_tone = 8 if not weekly_tone else weekly_tone #mod 0 returns none, meaning tone 8

    elif pascha_offset < 0: #Before Pascha/Holy Week in a given year...
        last_pascha = paschalion(month=12,day=31,year=Y-1).get('pascha')
        last_pascha_offset = (T - last_pascha).days
        weekly_tone = (last_pascha_offset) // 7 #tones iterate weekly
        weekly_tone = (weekly_tone % 8) if weekly_tone > 8 else weekly_tone #after tone 8, back to 1
        weekly_tone = 8 if not weekly_tone else weekly_tone #mod 0 returns none, meaning tone 8

    moveable_dates['pascha'] = this_pascha
    moveable_dates['pentecost'] = this_pentecost
    moveable_dates['pascha_offset'] = (T - this_pascha).days
    moveable_dates['is_pascha'] = True if T == this_pascha else False
    moveable_dates['is_pentecost'] = True if T == this_pentecost else False
    moveable_dates['lent_week'] = lent_week if lent_week else None #week of lent
    moveable_dates['pascha_week'] = pascha_week if pascha_week else None
    moveable_dates['weeks_after'] = weeks_after if weeks_after else None
    moveable_dates['weekly_tone'] = weekly_tone if weekly_tone else None

    return moveable_dates

def rubrics(rank:int, octoechos=None, menaion=None, paschal=None):
    """
    Takes in dictionaries from various sources.
    Determines moveable service portions based on rank.
    Returns dictionary of moveable portions to use for each service assembly.
    """
    if rank < 7 and not (menaion or paschal):
        print(f'Service rank {rank} with no menaion or triodion/pentecostarion! \nGenerating simple service instead')
        rank = 7

    if rank == 7: #simple service
        return octoechos

def vespers(date:str, parts:dict, kathisma_number:int, weekday:int):
    vfil = open('static/html/vespers.html') #html template
    vespers = BeautifulSoup(vfil, 'html.parser') #service html
    vdate = vespers.select_one('.vespers-date') #date field from service html
    stichera = vespers.select('.vespers-sticheron') #list of stichera from service html
    theotokion = vespers.select_one('.vespers-theotokion') #theotokion field from service html
    kathisma = vespers.select_one('.vespers-kathisma') #kathisma field from service html
    prokeimenon = vespers.select_one('.vespers-prokeimenon') #prokeimenon field from service html
    aposticha = vespers.select_one('.vespers-aposticha') #aposticha field from service html
    apolytichion = vespers.select_one('.vespers-apolytichion') #apolytichion field from service html

    #Iterate in reverse through sticheron divs inserting stichera grabbed in reverse order
    for s, p in zip(stichera[::-1], parts.get('vespers').get('stichera')[::-1]):
        try:
            s.append(BeautifulSoup(p, 'html.parser'))
        except IndexError:
            pass
    kathisma_reading = parse_kathisma(kathisma_number)
    kathisma_html = kathisma_reading.get('title')+kathisma_reading.get(1)+kathisma_reading.get(2)+kathisma_reading.get(3)
    vdate.append(BeautifulSoup(date, 'html.parser'))
    theotokion.append(BeautifulSoup(parts.get('vespers').get('theotokion'),'html.parser'))
    kathisma.append(BeautifulSoup(kathisma_html, 'html.parser'))
    prokeimenon.append(BeautifulSoup(vespers_prokeimena(weekday), 'html.parser'))
    aposticha.append(BeautifulSoup(parts.get('vespers').get('aposticha'),'html.parser'))
    apolytichion.append(BeautifulSoup(parts.get('vespers').get('apolytichion'),'html.parser'))

    return vespers.prettify()

def generate_day(month=None, day=None, year=None, calendar=1):
    """
    Takes a date value, and determines service rank & resources needed
    Calendar (0=New/1=Old)
    """
    #convert strings to int
    month = int(month) if type(month) == str else month
    day = int(day) if type(day) == str else day
    year = int(year) if type(year) == str else year
    calendar = int(calendar) if type(calendar) == str else calendar

    today = datetime.today()
    month = month if month else today.month
    day = day if day else today.day
    year = year if year else today.year
    service_date = date(year=year,month=month,day=day)
    date_oc = service_date - timedelta(days=13)
    liturgical_day = paschalion(month=month, day=day, year=year)
    tone = liturgical_day.get('weekly_tone')

    if tone: #If a tone is returned, we need octoechos, so we need sergius day for file format.
        sergius_day = service_date.weekday() + 2 if service_date.weekday() < 6 else service_date.weekday() - 5
        octoechos_file = f'{tone}-{sergius_day}'
    octoechos = octoechos_variables(process_pdf(filename=octoechos_file,service='octoechos')) if tone else None

    kathisma_rubric = {
        #day of week: [vespers, [matins]]
        0: [0,[4,5]] #Monday
        ,1: [6,[7,8]] #Tuesday
        ,2: [9,[10,11]] #Wednesday
        ,3: [12,[13,14]] #Thursday
        ,4: [15,[19,20]] #Friday
        ,5: [18,[16,17]] #Saturday
        ,6: [1,[2,3]] #Sunday
    }

    #Date strings, used for text within HTML
    day_string = service_date.strftime('%m/%d/%Y')
    day_string_oc = day_string + ' / ' + date_oc.strftime('%m/%d/%Y')

    #Night strings, used for Vespers service within HTML
    night_string = (service_date - timedelta(days=1)).strftime('%m/%d/%Y')
    night_string_oc = night_string + ' / ' + (date_oc - timedelta(days=1)).strftime('%m/%d/%Y')

    fixed_feasts = {
        #MM-DD: #[Service Name, Menaion, Rank]
    }

    moveable_feasts = {
        #Pascha offset: #[Service Name, Paschal, Rank]
    }

    """
    Logic will be added here to gather feast days from above dictionaries to determine rank...
    Also needed for Triodion/Pentecostarion (for paschal variable on rubrics)...
    Until then, simple services via octoechos will be generated.
    """
    rank = 7

    #variables = rubrics(etc, etc,)
    #for now, just octoechos
    variables = octoechos

    html = '<head><link href="../static/css/main.css" rel="stylesheet"/></head><body><div id="wrapper"><div id="main"><section class="post">'

    #Generating Vespers
    if calendar == 0: #New Calendar
        html += vespers(
            date=night_string
            ,parts=variables
            ,kathisma_number=kathisma_rubric.get(service_date.weekday())[0]
            ,weekday=service_date.weekday()
        )
    else: #Old Calendar
        html += vespers(
            date=night_string_oc
            ,parts=variables
            ,kathisma_number=kathisma_rubric.get(service_date.weekday())[0]
            ,weekday=service_date.weekday()
        )
    html += '</section></div></div></body>'
    return html
#
# with open('docs/html/test.html', 'wt', encoding='utf-8') as f:
#     f.write(generate_day(calendar=0))
