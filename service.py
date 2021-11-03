"""
Version 0.1.4
Updated 10/21/2021

Change Log:
10/11/2021 - 0.0.8 - Initial Creation, Vespers elements
10/12/2021 - 0.0.9 - Paschalion (def pascha) calculations started.
10/13/2021 - 0.0.9 - Tone of the week added to Paschalion
10/13/2021 - 0.1.0 - Initial build of Vespers service complete
10/14/2021 - 0.1.1 - Updated variables for Flask integration
10/21/2021 - 0.1.3 - Updated generate_day for templating, added exception handling
                    -Deleted vespers() and is_leap_year()
10/27/2021 - 0.1.4 - Added table of contents to generate_day()
"""
import os
import re
from flask import render_template
from hymns import vespers_prokeimena, compline_troparia
from kathisma import parse_kathisma
from datetime import datetime, timedelta, date
from octoechos import octoechos_variables
from menaion import menaion_variables
from _utils import process_pdf
from bs4 import BeautifulSoup

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

def rubrics(rank:int, weekday:int, name:str='(name)', octoechos=None, menaion=None, paschal=None):
    """
    Takes in dictionaries from various sources.
    Determines moveable service portions based on rank.
    Returns dictionary of moveable portions to use for each service assembly.
    """
    variables = {'rank': rank, 'name': name}

    if rank < 7 and not (menaion or paschal):
        print(f'Service rank {rank} with no menaion or triodion/pentecostarion! \nGenerating simple service instead')
        rank = 7

    if rank == 7: #simple service
        return octoechos

    if not paschal:
        #ranked service outside Lent/Pentecost
        #we will be working with the octoechos and menaion
        vespers = {}
        #build out stichera

        vo_stichera_needed = 6 #determined by rank
        vm_stichera_needed = 4 #determined by rank

        vo_stichera = octoechos.get('vespers').get('stichera')
        vm_stichera = menaion.get('vespers').get('stichera')
        if weekday == 6:
            vo_stichera = vo_stichera[:7] #7 resurrection stichera.
        else:
            vo_stichera = vo_stichera[:3] #with menaion only 3 used.
        po_stichera = []
        pm_stichera = []
        #payload_stichera = []

        vo_duplicates = vo_stichera_needed - len(vo_stichera)
        vm_duplicates = vm_stichera_needed - len(vm_stichera)
        #enumerate octoechos stichera, assign duplicates as needed
        for i, s in enumerate(vo_stichera):
            po_stichera.append(s)
            print(f'Added {s[41:52]}')
            if i + 1 <= vo_duplicates:
                po_stichera.append(s)
                print(f'*Added {s[41:52]}')
        print(f'{len(po_stichera)} from octoechos added!')

        #enumerate menaion stichera, assign duplicates as needed
        for i, s in enumerate(vm_stichera):
            pm_stichera.append(s)
            print(f'Added {s[24:35]}')
            if i + 1<= vm_duplicates:
                pm_stichera.append(s)
                print(f'*Added {s[24:35]}')
        print(f'{len(pm_stichera)} from menaion added!')
        vespers['stichera'] = po_stichera + pm_stichera

        #determine stichera tone
        vespers['stichera_tone'] = menaion.get('vespers').get('stichera_tone')

        #doxastichon from menaion
        vm_doxastichon = menaion.get('vespers').get('doxastichon',None)
        if vm_doxastichon:
            vespers['doxastichon'] = vm_doxastichon

        #dogmaticon from menaion
        vm_dogmaticon = menaion.get('vespers').get('dogmaticon',None)
        if vm_dogmaticon:
            vespers['dogmaticon'] = vm_dogmaticon

        #determine theotokion
        vo_theotokion = octoechos.get('vespers').get('theotokion')
        vm_theotokion = menaion.get('vespers').get('theotokion',None)
        vespers['theotokion'] = vm_theotokion if vm_theotokion else vo_theotokion

        #readings from menaion
        vespers['readings'] = menaion.get('vespers').get('readings')

        #determine aposticha
        aposticha = menaion.get('vespers').get('aposticha', None)
        if not aposticha:
            aposticha = octoechos.get('vespers').get('aposticha')
        vespers['aposticha'] = aposticha
        vespers['aposticha_theotokion'] = menaion.get('vespers').get('aposticha_theotokion')

        #use all apolytichia, menaion then octoechos.
        vo_apolytichion = octoechos.get('vespers').get('apolytichion')
        vm_apolytichion = menaion.get('vespers').get('apolytichion')
        vespers['apolytichion'] = vm_apolytichion + vo_apolytichion

        compline = octoechos.get('compline') #no menaion variables
        nocturns = octoechos.get('nocturns') #no menaion variables
        matins = octoechos.get('matins') #octoechos until menaion established
        liturgy = octoechos.get('liturgy') #liturgy until menaion established
        variables['vespers'] = vespers
        variables['compline'] = compline
        variables['matins'] = matins
        variables['liturgy'] = liturgy

        return variables

def generate_day(month=None, day=None, year=None, calendar=1, schedule=None):
    try:
        #convert strings to int
        month = int(month) if type(month) == str else month
        day = int(day) if type(day) == str else day
        year = int(year) if type(year) == str else year
    except ValueError: #If string value contains non-int values
        month = day = year = None
    try: #calendar handled separately
        calendar = int(calendar) if type(calendar) == str else calendar
    except ValueError: #If string value contains non-int values
        calendar = 1

    today = datetime.today()
    month = month if month else today.month
    day = day if day else today.day
    year = year if year else today.year

    #establish custom schedule
    schedule = schedule if schedule else 'vcnm136t9'
    do_vespers = re.search(r'v',schedule,flags=re.I)
    do_compline = re.search(r'c',schedule,flags=re.I)
    do_nocturns = re.search(r'n',schedule,flags=re.I)
    do_matins = re.search(r'm',schedule,flags=re.I)
    do_typika = re.search(r't',schedule,flags=re.I)
    do_first = re.search(r'1',schedule,flags=re.I)
    do_third = re.search(r'3',schedule,flags=re.I)
    do_sixth = re.search(r'6',schedule,flags=re.I)
    do_ninth = re.search(r'9',schedule,flags=re.I)

    try:
        #create service day variables
        service_date = date(year=year,month=month,day=day)
        date_oc = service_date - timedelta(days=13)
        liturgical_day = paschalion(month=month, day=day, year=year)
    except ValueError: #If month/day/year value passed was too large/small
        #forcing variables to match current day
        month = today.month
        day = today.day
        year = today.year
        service_date = date(year=year,month=month,day=day)
        date_oc = service_date - timedelta(days=13)
        liturgical_day = paschalion(month=month, day=day, year=year)

    tone = liturgical_day.get('weekly_tone')
    weekday = service_date.weekday()

    if tone: #If a tone is returned, we need octoechos, so we need sergius day for file format.
        sergius_day = weekday + 2 if weekday < 6 else weekday - 5
        octoechos_file = f'{tone}-{sergius_day}'
        octoechos = octoechos_variables(
            input_string = process_pdf(
                filename=octoechos_file
                ,service='octoechos'
            )
        )
    else: #if no tone is returned (Holy week, etc)
        octoechos = None

    kathisma_rubric = {
        #day of week: [vespers, nocturns, [matins]]
        0: [0,17,[4,5]] #Monday
        ,1: [6,17,[7,8]] #Tuesday
        ,2: [9,17,[10,11]] #Wednesday
        ,3: [12,17,[13,14]] #Thursday
        ,4: [15,17,[19,20]] #Friday
        ,5: [18,9,[16,17]] #Saturday
        ,6: [1,None,[2,3]] #Sunday
    }

    #Date strings, used for text within HTML
    day_string = service_date.strftime('%m/%d/%Y')
    day_string_oc = day_string + ' (' + date_oc.strftime('%m/%d/%Y') + ')'
    link_date = service_date.strftime('%m%d%Y')

    #Night strings, used for Vespers service within HTML
    night_string = (service_date - timedelta(days=1)).strftime('%m/%d/%Y')
    night_string_oc = night_string + ' (' + (date_oc - timedelta(days=1)).strftime('%m/%d/%Y') + ')'

    fixed_feasts = {
        #MM-DD: #[Service Name, Service Type, Rank]
        # 'MM-DD': ['Kursk Root Icon', 'Theotokos', 4] #uncomment to test menaion...
    }

    #grabs menaion info from dictionary if available
    menaion_service = fixed_feasts.get('MM-DD', None)
    service_name = menaion_service[0] if menaion_service else None
    menaion_file = menaion_service[1] if menaion_service else None
    rank = menaion_service[2] if menaion_service else 7 #menaion rank or simple service

    if menaion_service:
        menaion = menaion_variables(
            input_string = process_pdf(
                filename=menaion_file
                ,service='menaion'
            )
                ,name=service_name
                ,service_type=menaion_file
        )
    else:
        menaion = None

    moveable_feasts = {
        #Pascha offset: #[Service Name, Paschal, Rank]
    }
    paschal = None #for now...

    """
    Logic will be added here to gather feast days from above dictionaries to determine rank...
    Will need variable logic for OC NC for menaion.
    Also needed for Triodion/Pentecostarion (for paschal variable on rubrics)...
    Until then, simple services via octoechos will be generated.
    """

    liturgics = {} #dictionary for return
    liturgics['link_date'] = link_date
    liturgics['day_string'] = day_string
    links = [f'<a href="#{link_date}">{day_string}</a>']

    variables = rubrics(
        rank=rank
        ,weekday=weekday
        ,name=service_name
        ,octoechos=octoechos
        ,menaion=menaion
        ,paschal=paschal
    )

    #create services, grabbing service variables from rubic variables
    #add template variables, then render
    #add service to liturgics dictionary for return
    if do_vespers:
        vespers_variables = variables.get('vespers')
        vespers_variables['vespers_kathisma'] = parse_kathisma(kathisma_rubric.get(weekday)[0])
        vespers_variables['night_date'] = night_string_oc if calendar == 1 else night_string
        vespers_variables['prokeimenon'] = vespers_prokeimena(weekday)
        vespers_variables['link'] = f'{link_date}-vespers'
        links.append(f'<a href="#{link_date}-vespers">Vespers</a>')
        vespers = render_template('vespers.html',variables=vespers_variables, weekday=weekday, name=service_name)
        liturgics['vespers'] = vespers

    if do_compline:
        compline_variables = variables.get('compline')
        compline_variables['troparion'] = compline_troparia(weekday=weekday, rank=rank)
        compline_variables['night_date'] = night_string_oc if calendar == 1 else night_string
        compline_variables['link'] = f'{link_date}-compline'
        links.append(f'<a href="#{link_date}-compline">Compline</a>')
        compline = render_template('smallCompline.html', variables=compline_variables, weekday=weekday)
        liturgics['compline'] = compline

    if do_nocturns:
        nocturns_variables = variables.get('nocturns', {})
        nocturns_variables['kathisma'] = parse_kathisma(kathisma_rubric.get(weekday)[1])
        nocturns_variables['date'] = day_string_oc if calendar == 1 else day_string
        nocturns_variables['link'] = f'{link_date}-nocturns'
        links.append(f'<a href="#{link_date}-nocturns">Nocturns</a>')
        nocturns = render_template('nocturns.html', variables=nocturns_variables, weekday=weekday)
        liturgics['nocturns'] = nocturns

    if do_matins:
        matins_variables = variables.get('matins')
        matins_variables['kathisma1'] = parse_kathisma(kathisma_rubric.get(weekday)[2][0])
        matins_variables['kathisma2'] = parse_kathisma(kathisma_rubric.get(weekday)[2][1])
        matins_variables['date'] = day_string_oc if calendar == 1 else day_string
        matins_variables['link'] = f'{link_date}-matins'
        links.append(f'<a href="#{link_date}-matins">Matins</a>')
        matins = render_template('matins.html', variables = matins_variables, weekday=weekday, tone=tone, rank=rank, name=service_name)
        liturgics['matins'] = matins

    if do_typika or do_first or do_third or do_sixth or do_ninth:
        #all hours use typika variables
        typika_variables = variables.get('liturgy')
        #The hours require troparia and kontakia. These are built out separately
        #NC can be grabbed from: https://www.oca.org/saints/lives/yyyy/mm/dd
        #OC can be grabbed from: https://www.holytrinityorthodox.com/calendar/index.php?year=yyyy&today=dd&month=mm&trp=1&tzo=0
        hours_troparia = []
        res_troparion = typika_variables.get('resurrection_troparion')
        if res_troparion:
            hours_troparia.append(res_troparion)
        hours_kontakia = []
        res_kontakion = typika_variables.get('resurrection_kontakion')
        if res_kontakion:
            hours_kontakia.append(res_kontakion)


    if do_typika:
        typika_variables['date'] = day_string_oc if calendar == 1 else day_string
        typika_variables['link'] = f'{link_date}-typika'
        #(link appended below)
        typika = render_template('typika.html', variables = typika_variables, name=service_name)
        liturgics['typika'] = typika

    if do_first:
        first_variables = {'troparia': hours_troparia, 'kontakia': hours_kontakia}
        first_variables['date'] = day_string_oc if calendar == 1 else day_string
        first_variables['link'] = f'{link_date}-first'
        links.append(f'<a href="#{link_date}-first">First Hour</a>')
        first = render_template('first.html', variables = first_variables)
        liturgics['first'] = first

    if do_third:
        third_variables = {'troparia': hours_troparia, 'kontakia': hours_kontakia}
        third_variables['date'] = day_string_oc if calendar == 1 else day_string
        third_variables['link'] = f'{link_date}-third'
        links.append(f'<a href="#{link_date}-third">Third Hour</a>')
        third = render_template('third.html', variables = third_variables)
        liturgics['third'] = third

    if do_sixth:
        sixth_variables = {'troparia': hours_troparia, 'kontakia': hours_kontakia}
        sixth_variables['date'] = day_string_oc if calendar == 1 else day_string
        sixth_variables['link'] = f'{link_date}-sixth'
        links.append(f'<a href="#{link_date}-sixth">Sixth Hour</a>')
        sixth = render_template('sixth.html', variables = sixth_variables)
        liturgics['sixth'] = sixth

    if do_typika:
        #adding typika link in correct order
        links.append(f'<a href="#{link_date}-typika">Typika</a>')

    if do_ninth:
        ninth_variables = {'troparia': hours_troparia, 'kontakia': hours_kontakia}
        ninth_variables['date'] = day_string_oc if calendar == 1 else day_string
        ninth_variables['link'] = f'{link_date}-ninth'
        links.append(f'<a href="#{link_date}-ninth">Ninth Hour</a>')
        ninth = render_template('ninth.html', variables = ninth_variables)
        liturgics['ninth'] = ninth

    liturgics['links'] = links

    return liturgics


if __name__ == '__main__':
    day = generate_day()
