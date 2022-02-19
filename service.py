"""
Version 0.1.9
Updated 11/8/2021

Change Log:
10/11/2021 - 0.0.8  - Initial Creation, Vespers elements
10/12/2021 - 0.0.9  - Paschalion (def pascha) calculations started.
10/13/2021 - 0.0.9  - Tone of the week added to Paschalion
10/13/2021 - 0.1.0  - Initial build of Vespers service complete
10/14/2021 - 0.1.1  - Updated variables for Flask integration
10/21/2021 - 0.1.3  - Updated generate_day for templating, added exception handling
                    - Deleted vespers() and is_leap_year()
10/27/2021 - 0.1.4  - Added table of contents to generate_day()
11/5/2021  - 0.1.7  - Updated Rubrics for Menaion Matins
                    - Updated generate_day() for matins use
11/7/2021 - 0.1.8   - Updated Rubrics for Menaion Typika
11/8/2021 - 0.1.9   - Updated Fixed feasts for first half of November

"""
import os
import re
from flask import render_template
from hymns import vespers_prokeimena, compline_troparia
from kathisma import parse_kathisma
from datetime import datetime, timedelta, date
from octoechos import octoechos_variables
from menaion import menaion_variables, menaion_class
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

def rubrics(rank:int, weekday:int, name:str='(name)', octoechos=None, menaion=None, paschal=None, service_type=None):
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
        vo = octoechos.get('vespers')
        vm = menaion.get('vespers') if menaion else None

        #build out stichera
        if rank == 1:
            vo_stichera_needed = 4
            vm_stichera_needed = 6
        elif rank == 2:
            vo_stichera_needed = 2 if weekday == 6 else 2
            vm_stichera_needed = 6
        elif rank == 3:
            vo_stichera_needed = 6 if weekday == 6 else 0
            vm_stichera_needed = 4 if weekday == 6 else 6
        else:
            vo_stichera_needed = 6 if weekday == 6 else 3
            vm_stichera_needed = 4 if weekday == 6 else 3

        vo_stichera = vo.get('stichera')
        vm_stichera = vm.get('stichera') if vm else None

        if weekday == 6:
            vo_stichera = vo_stichera[:7] #7 resurrection stichera.
        else:
            vo_stichera = vo_stichera[:3] #with menaion only 3 used.

        if rank == 8:
            vespers['m_stichera'] = vm_stichera if vm else None
            vespers['o_stichera'] = vo_stichera
        else:
            po_stichera = []
            pm_stichera = []

            vo_duplicates = vo_stichera_needed - len(vo_stichera)
            vm_duplicates = vm_stichera_needed - len(vm_stichera)

            #enumerate octoechos stichera, assign duplicates as needed
            for i, s in enumerate(vo_stichera):
                po_stichera.append(s)
                if i + 1 <= vo_duplicates:
                    po_stichera.append(s)

            #enumerate menaion stichera, assign duplicates as needed
            for i, s in enumerate(vm_stichera):
                pm_stichera.append(s)
                if i + 1<= vm_duplicates:
                    pm_stichera.append(s)

            vespers['stichera'] = po_stichera + pm_stichera

        #determine stichera tone
        vespers['stichera_tone'] = vm.get('stichera_tone') if vm else None

        #doxastichon from menaion
        vm_doxastichon = vm.get('doxastichon',None) if vm else None
        if vm_doxastichon:
            vespers['doxastichon'] = vm_doxastichon

        #dogmaticon from menaion
        vm_dogmaticon = vm.get('dogmaticon',None) if vm else None
        if vm_dogmaticon:
            vespers['dogmaticon'] = vm_dogmaticon

        #determine theotokion
        vo_theotokion = vo.get('theotokion', None)
        vm_theotokion = vm.get('theotokion', None) if vm else None
        if rank == 8:
            vespers['m_theotokion'] = vm_theotokion if vm else None
            vespers['o_theotokion'] = vo_theotokion
        elif vo_theotokion or vm_theotokion:
            vespers['theotokion'] = vm_theotokion if vm_theotokion else vo_theotokion

        #readings from menaion
        vespers['readings'] = vm.get('readings') if vm else None

        #determine aposticha
        if rank == 8:
            vespers['m_aposticha'] = vm.get('aposticha', None) if vm else None
            vespers['o_aposticha'] = vo.get('aposticha', None)
            #vespers['m_aposticha_theotokion'] = vm.get('aposticha_theotokion', None) if vm else None
            #vespers['o_aposticha_theotokion'] = vo.get('aposticha_theotokion')
        else:
            aposticha = vm.get('aposticha', None)
            if not aposticha:
                aposticha = vo.get('aposticha')
            vespers['aposticha'] = aposticha

            #aposticha theotokion may need to be swapped based on rank...
            #for now it's just based on presence of menaion or not.
            aposticha_theotokion = vm.get('aposticha_theotokion')
            if not aposticha_theotokion:
                aposticha_theotokion = vo.get('aposticha_theotokion')
            vespers['aposticha_theotokion'] = aposticha_theotokion


        vm_apolytichion = vm.get('apolytichion', None) if vm else None
        vespers['apolytichion'] = vm_apolytichion if vm_apolytichion else None

        #Matins
        matins = {}
        mo = octoechos.get('matins')
        mm = menaion.get('matins') if menaion else None

        mm_troparion = mm.get('troparion', None) if mm else None
        mo_troparion = mo.get('troparion', None)
        if rank == 8:
            matins['m_troparion'] = mm_troparion if mm else None
            matins['o_troparion'] = mo_troparion
        elif mm_troparion or mo_troparion:
            matins['troparion'] = mm_troparion if mm_troparion else mo_troparion

        if rank == 8:
            matins['o_session1'] = mo.get('session1')
            matins['o_session2'] = mo.get('session2')
            matins['o_session3'] = mo.get('session3')
            matins['m_session1'] = mm.get('session1') if mm else None
            matins['m_session2'] = mm.get('session2') if mm else None
            matins['m_session3'] = mm.get('session3') if mm else None
            matins['o_ascent'] = mo.get('ascent')
            matins['apolytichion'] = mm.get('apolytichion') if mm else None
            matins['megalynarion'] = mm.get('megalynarion') if mm else None
        elif service_type == 'Holy Fathers':
            matins['session1'] = mo.get('session1')
            matins['session2'] = mo.get('session2')
            matins['session3'] = mo.get('session3')
            matins['ascent'] = mo.get('ascent')
            matins['prokeimenon'] = mo.get('prokeimenon')
        else:
            #sessional hymns are taken from the menaion for all ranks. Except Holy Fathers
            matins['session1'] = mm.get('session1')
            matins['session2'] = mm.get('session2')
            matins['session3'] = mm.get('session3')
            matins['apolytichion'] = mm.get('apolytichion')
            matins['megalynarion'] = mm.get('megalynarion')

        #aposticha currently only in octoechos, not used rank 4 or higher
        if rank >= 5: #six verse & afterfeast
            matins['aposticha'] = mo.get('aposticha')

        matins['exapostilarion'] = mm.get('exapostilarion') if mm else None

        if rank <= 3 or rank == 8: #polyeleos or higher
            mo_prokeimenon = mo.get('prokeimenon', None)
            mm_prokeimenon = mm.get('prokeimenon', None) if mm else None
            if rank == 8:
                matins['m_prokeimenon'] = mm_prokeimenon
                matins['o_prokeimenon'] = mo_prokeimenon
            elif mm_prokeimenon or mo_prokeimenon:
                matins['prokeimenon'] = mm_prokeimenon if mm_prokeimenon else mo_prokeimenon

            matins['readings'] = mm.get('readings', None) if mm else None
            matins['after50'] = mm.get('after50', None) if mm else None

            mo_ascent = mo.get('ascent', None)
            mm_ascent = mm.get('ascent', None) if mm else None
            if rank == 8:
                matins['m_ascent'] = mm_ascent if mm else None
                matins['o_ascent'] = mo_ascent
                matins['m_canon'] = mm.get('canon') if mm else None
                matins['o_canon'] = mo.get('canon')
            elif mo_ascent or mm_ascent:
                matins['ascent'] = mm_ascent if mm_ascent else mo_ascent
                matins['canon'] = mm.get('canon')
        else:
            matins['canon'] = mo.get('canon')

        #currently using octoechos praises. Need to do work on changing format to stichera to get menaion working.
        matins['praises'] = mo.get('praises')

        #establish Typika variables
        liturgy = {}
        to = octoechos.get('liturgy')
        tm = menaion.get('liturgy') if menaion else None

        to_beatitudes = to.get('beatitudes')
        tm_beatitudes = tm.get('beatitudes') if tm else None

        if rank == 8:
            liturgy['m_beatitudes'] = tm_beatitudes
            liturgy['o_beatitudes'] = to_beatitudes
        else:
            if weekday == 6:
                beatitudes_needed = 10
                feast_beatitudes = len(tm_beatitudes)
                extra_beatitudes = beatitudes_needed - feast_beatitudes
            elif rank <= 3:
                beatitudes_needed = 8
                feast_beatitudes = len(tm_beatitudes)
                extra_beatitudes = beatitudes_needed - feast_beatitudes
            elif rank > 6:
                beatitudes_needed = 6
                feast_beatitudes = len(tm_beatitudes)
                extra_beatitudes = beatitudes_needed - feast_beatitudes
            else: #afterfeast, 3 & 3
                beatitudes_needed = 6
                feast_beatitudes = 3
                extra_beatitudes = 3

            extra_beatitudes = None if extra_beatitudes <= 0 else extra_beatitudes
            if extra_beatitudes:
                beatitudes = to_beatitudes[0:extra_beatitudes] + tm_beatitudes[0:feast_beatitudes]
            else:
                beatitudes = tm_beatitudes
            liturgy['beatitudes'] = beatitudes

        if weekday == 6:
            liturgy['resurrection_troparion'] = to.get('resurrection_troparion')

        liturgy['troparion'] = tm.get('troparion') if tm else None
        liturgy['kontakion'] = tm.get('kontakion') if tm else None
        liturgy['prokeimenon'] = tm.get('prokeimenon') if tm else None
        liturgy['readings'] = tm.get('readings') if tm else None

        compline = octoechos.get('compline') #no menaion variables
        nocturns = octoechos.get('nocturns') #no menaion variables

        variables['vespers'] = vespers
        variables['compline'] = compline
        variables['nocturns'] = nocturns
        variables['matins'] = matins
        variables['liturgy'] = liturgy

        return variables

def generate_day(month=None, day=None, year=None, calendar=1, schedule=None, variables_only_flag=None):
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
    variables_only_flag = variables_only_flag if variables_only_flag else None

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

    print('pascha offset...')
    print(liturgical_day.get('pascha_offset'))
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

    relative_feasts = {
        #MM-DD: #[Rank, Service Type, Day of Week, Service Name, Service Long Name]
        '09-09': [6,1,None,'Nativity','Afterfeast of the Nativity of the Mother of God']
        ,'09-10': [6,1,None,'Nativity','Afterfeast of the Nativity of the Mother of God']
        ,'09-11': [6,1,None,'Nativity','Afterfeast of the Nativity of the Mother of God']
        ,'09-15': [4,2,None,'Elevation','Afterfeast of the Elevation of the Cross']
        ,'09-16': [4,2,None,'Elevation','Afterfeast of the Elevation of the Cross']
        ,'09-17': [4,2,None,'Elevation','Afterfeast of the Elevation of the Cross']
        ,'09-18': [4,2,None,'Elevation','Afterfeast of the Elevation of the Cross']
        ,'09-19': [4,2,None,'Elevation','Afterfeast of the Elevation of the Cross']
        ,'09-20': [4,2,None,'Elevation','Afterfeast of the Elevation of the Cross']
        ,'10-11': [3,15,6,'Holy Fathers','Our Holy Fathers of the Seventh Ecumenical Council']
        ,'10-12': [3,15,6,'Holy Fathers','Our Holy Fathers of the Seventh Ecumenical Council']
        ,'10-13': [3,15,6,'Holy Fathers','Our Holy Fathers of the Seventh Ecumenical Council']
        ,'10-14': [3,15,6,'Holy Fathers','Our Holy Fathers of the Seventh Ecumenical Council']
        ,'10-15': [3,15,6,'Holy Fathers','Our Holy Fathers of the Seventh Ecumenical Council']
        ,'10-16': [3,15,6,'Holy Fathers','Our Holy Fathers of the Seventh Ecumenical Council']
        ,'10-17': [3,15,6,'Holy Fathers','Our Holy Fathers of the Seventh Ecumenical Council']
        ,'11-22': [6,1,None,'Entrance','The Afterfeast of the Entrance of the Most Holy Theotokos into the Temple']
        ,'11-23': [6,1,None,'Entrance','The Afterfeast of the Entrance of the Most Holy Theotokos into the Temple']
        ,'11-24': [6,1,None,'Entrance','The Afterfeast of the Entrance of the Most Holy Theotokos into the Temple']
        ,'12-11': [4,4,6,'Forefathers','Sunday of Our Holy Forefathers']
        ,'12-12': [4,4,6,'Forefathers','Sunday of Our Holy Forefathers']
        ,'12-13': [4,4,6,'Forefathers','Sunday of Our Holy Forefathers']
        ,'12-14': [4,4,6,'Forefathers','Sunday of Our Holy Forefathers']
        ,'12-15': [4,4,6,'Forefathers','Sunday of Our Holy Forefathers']
        ,'12-16': [4,4,6,'Forefathers','Sunday of Our Holy Forefathers']
        ,'12-17': [4,4,6,'Forefathers','Sunday of Our Holy Forefathers']
        ,'12-18': [3,0,6,'Nativity', 'Sunday Before Nativity']
        ,'12-19': [3,0,6,'Nativity', 'Sunday Before Nativity']
        ,'12-20': [3,0,6,'Nativity', 'Sunday Before Nativity']
        ,'12-21': [3,0,6,'Nativity', 'Sunday Before Nativity']
        ,'12-22': [3,0,6,'Nativity', 'Sunday Before Nativity']
        ,'12-23': [3,0,6,'Nativity', 'Sunday Before Nativity']
        ,'12-24': [3,0,6,'Nativity', 'Sunday Before Nativity']
        ,'12-27': [6,0,None,'Nativity','The Afterfeast of the Nativity of our Lord']
        ,'12-28': [6,0,None,'Nativity','The Afterfeast of the Nativity of our Lord']
        ,'12-29': [6,0,None,'Nativity','The Afterfeast of the Nativity of our Lord']
        ,'12-30': [6,0,None,'Nativity','The Afterfeast of the Nativity of our Lord']
        ,'12-31': [4,0,None,'Nativity','The Leavetaking of the Nativity of our Lord']
        ,'01-01': [4,0,6,'Theophany','Sunday Before Theophany']
        ,'01-02': [4,0,6,'Theophany','Sunday Before Theophany']
        ,'01-03': [4,0,6,'Theophany','Sunday Before Theophany']
        ,'01-04': [4,0,6,'Theophany','Sunday Before Theophany']
        ,'01-05': [4,0,6,'Theophany','Sunday Before Theophany']
        ,'01-08': [6,0,None,'Theophany','Afterfeast of Theophany']
        ,'01-09': [6,0,None,'Theophany','Afterfeast of Theophany']
        ,'01-10': [6,0,None,'Theophany','Afterfeast of Theophany']
        ,'01-11': [6,0,None,'Theophany','Afterfeast of Theophany']
        ,'01-12': [6,0,None,'Theophany','Afterfeast of Theophany']
        ,'01-13': [6,0,None,'Theophany','Afterfeast of Theophany']
        ,'01-22': [3,17,6,'New Martyrs','Holy New Martyrs of Russia']
        ,'01-23': [3,17,6,'New Martyrs','Holy New Martyrs of Russia']
        ,'01-24': [3,17,6,'New Martyrs','Holy New Martyrs of Russia']
        ,'01-25': [3,17,6,'New Martyrs','Holy New Martyrs of Russia']
        ,'01-26': [3,17,6,'New Martyrs','Holy New Martyrs of Russia']
        ,'01-27': [3,17,6,'New Martyrs','Holy New Martyrs of Russia']
        ,'01-28': [3,17,6,'New Martyrs','Holy New Martyrs of Russia']
        ,'02-03': [6,0,None,'Meeting','Afterfeast of the Meeting of Our Lord, God & Savior Jesus Christ']
        ,'02-04': [6,0,None,'Meeting','Afterfeast of the Meeting of Our Lord, God & Savior Jesus Christ']
        ,'02-05': [6,0,None,'Meeting','Afterfeast of the Meeting of Our Lord, God & Savior Jesus Christ']
        ,'02-06': [6,0,None,'Meeting','Afterfeast of the Meeting of Our Lord, God & Savior Jesus Christ']
        ,'02-07': [6,0,None,'Meeting','Afterfeast of the Meeting of Our Lord, God & Savior Jesus Christ']
        ,'02-08': [6,0,None,'Meeting','Afterfeast of the Meeting of Our Lord, God & Savior Jesus Christ']
        ,'07-13': [3,15,6,'Holy Fathers','Our Holy Fathers of the Fourth Ecumenical Council']
        ,'07-14': [3,15,6,'Holy Fathers','Our Holy Fathers of the Fourth Ecumenical Council']
        ,'07-15': [3,15,6,'Holy Fathers','Our Holy Fathers of the Fourth Ecumenical Council']
        ,'07-16': [3,15,6,'Holy Fathers','Our Holy Fathers of the Fourth Ecumenical Council']
        ,'07-17': [3,15,6,'Holy Fathers','Our Holy Fathers of the Fourth Ecumenical Council']
        ,'07-18': [3,15,6,'Holy Fathers','Our Holy Fathers of the Fourth Ecumenical Council']
        ,'07-19': [3,15,6,'Holy Fathers','Our Holy Fathers of the Fourth Ecumenical Council']
        ,'08-07': [6,0,None,'Transfiguration','Afterfeast of the Holy Transfiguration of Our Lord, God & Savior Jesus Christ']
        ,'08-08': [6,0,None,'Transfiguration','Afterfeast of the Holy Transfiguration of Our Lord, God & Savior Jesus Christ']
        ,'08-09': [6,0,None,'Transfiguration','Afterfeast of the Holy Transfiguration of Our Lord, God & Savior Jesus Christ']
        ,'08-10': [6,0,None,'Transfiguration','Afterfeast of the Holy Transfiguration of Our Lord, God & Savior Jesus Christ']
        ,'08-11': [6,0,None,'Transfiguration','Afterfeast of the Holy Transfiguration of Our Lord, God & Savior Jesus Christ']
        ,'08-12': [6,0,None,'Transfiguration','Afterfeast of the Holy Transfiguration of Our Lord, God & Savior Jesus Christ']
        ,'08-16': [6,1,None,'Dormition','Afterfeast of the Dormition of the Theotokos']
        ,'08-17': [6,1,None,'Dormition','Afterfeast of the Dormition of the Theotokos']
        ,'08-18': [6,1,None,'Dormition','Afterfeast of the Dormition of the Theotokos']
        ,'08-19': [6,1,None,'Dormition','Afterfeast of the Dormition of the Theotokos']
        ,'08-20': [6,1,None,'Dormition','Afterfeast of the Dormition of the Theotokos']
        ,'08-21': [6,1,None,'Dormition','Afterfeast of the Dormition of the Theotokos']
        ,'08-22': [6,1,None,'Dormition','Afterfeast of the Dormition of the Theotokos']
        ,'10-11': [3,15,6,'Holy Fathers','Our Holy Fathers of the Seventh Ecumenical Council']
        ,'10-12': [3,15,6,'Holy Fathers','Our Holy Fathers of the Seventh Ecumenical Council']
        ,'10-13': [3,15,6,'Holy Fathers','Our Holy Fathers of the Seventh Ecumenical Council']
        ,'10-14': [3,15,6,'Holy Fathers','Our Holy Fathers of the Seventh Ecumenical Council']
        ,'10-15': [3,15,6,'Holy Fathers','Our Holy Fathers of the Seventh Ecumenical Council']
        ,'10-16': [3,15,6,'Holy Fathers','Our Holy Fathers of the Seventh Ecumenical Council']
        ,'10-17': [3,15,6,'Holy Fathers','Our Holy Fathers of the Seventh Ecumenical Council']
    }

    fixed_feasts = {
        #MM-DD: #[Rank, Service Type, Service Name, Day of Week, Service Long Name]
        '09-01': [4,16,'Symeon','Our Venerable Father Symeon the Stylite']
        ,'09-04': [4,4,'Moses and Aaron','Holy Prophets Moses and Aaron']
        ,'09-05': [5,4,'Zacharias','Holy Prophet Zacharias']
        ,'09-06': [4,5,'Michael','Archangel Michael']
        ,'09-08': [2,1,'Nativity','The Nativity of the Mother of God']
        ,'09-12': [4,1,'Nativity','Leavetaking of the Nativity of the Mother of God']
        ,'09-13': [4,0,'Sepulcher','Consecration of the Holy Sepulcher']
        ,'09-14': [1,2,'Elevation','Elevation of the Cross']
        ,'09-20': [4,16,'Eustathius','Greatmartyr Eustathius']
        ,'09-21': [4,2,'Elevation','Leavetaking of the Elevation of the Cross']
        ,'09-23': [4,3,'Conception','Conception of the Forerunner and Baptist John']
        ,'09-24': [5,18,'Thekla','Protomartyr Thekla']
        ,'09-25': [3,13,'Sergius','Sergius of Radonezh']
        ,'09-26': [3,6,'John','Holy Apostle John']
        ,'09-28': [4,12,'Chariton','Chariton the Confessor']
        ,'10-01': [3,1,'Protection','Protection of the Mother of God']
        ,'10-06': [4,6,'Thomas','Holy Apostle Thomas']
        ,'10-09': [4,6,'James','Holy Apostle James Alphaeus']
        ,'10-12': [3,13,'Symeon','Symeon the New Theologian']
        ,'10-18': [3,6,'Luke','Holy Apostle Luke']
        ,'10-19': [3,8,'John','John of Kronstadt']
        ,'10-23': [4,6,'James','Holy Apostle James, the Brother of the Lord']
        ,'10-26': [2,16,'Demetrius','The Holy and Glorious Great Martyr Demetrius, The Myrrh-Gusher of Thessalonica']
        ,'11-01': [5,24,'Cosmas and Damian','The Holy Cosmas and Damian, Wonderworkers and Unmercenary Physicians in Asia']
        ,'11-03': [4,16,'George','The Consecration of the Church of the Great Martyr George of Lydda']
        ,'11-06': [5,12,'Paul','Our Father among the Saints, Paul the Confessor, Archbishop of Constantinople']
        ,'11-08': [3,5,'Archangels Michael, Gabriel, Raphael, Uriel, Salaphiel, Judgudiel, and Barachiel','The Synaxis of the Angels']
        ,'11-09': [3,8,'Nectarius','Our Father among the Saints, Nectarius, Bishop of Pentapolis, Wonderworker of Aegina']
        ,'11-11': [4,12,'Theodore', 'Our Father among the Saints, Theodore the Studite']
        ,'11-13': [3,8,'John Chrysostom', 'Our Father among the Saints, John Chrysostom, Archbishop of Constantinople']
        ,'11-14': [4,6,'Philip','The Holy and Glorious Apostle Philip']
        ,'11-15': [5,17,'Shamuna, Guria, and Habib','The Holy Matryrs Shamuna, Guria, and Habib']
        ,'11-16': [3,6,'Matthew','The Holy Apostle and Evangelist Matthew']
        ,'11-21': [2,1,'Entrance','The Entrance of the Most Holy Theotokos into the Temple']
        ,'11-24': [3,18,'Catherine','The Holy Great Martyr Catherine of Alexandria']
        ,'11-25': [4,1,'Entrance','The Leavetaking of the Entrance of the Theotokos']
        ,'11-30': [3,6,'Andrew','The Holy and All-Praised Apostle Andrew, The First-Called']
        ,'12-04': [3,18,'Barbara','Holy Great-Martyr Barbara']
        ,'12-05': [3,13,'Sabbas','Our Venerable and God-Bearing Father, Sabbas the Sanctified']
        ,'12-06': [3,8,'Nicholas','Our Father Among the Saints Nicholas, Archbishop of Myra']
        ,'12-07': [4,8,'Ambrose','Our Father Among the Saints, Ambrose, Bishop of Milan']
        ,'12-09': [3,1,'Conception','The Conception of the Most Holy Theotokos by Saint Anna']
        ,'12-12': [3,8,'Spyridon','Our Venerable Father Spyridon The Wonderworker, Bishop of Tremithus']
        ,'12-15': [4,10,'Eleutherius','The Holy Hieromartyr Eleutherius']
        ,'12-17': [5,4,'Daniel','Holy Prophet Daniel']
        ,'12-20': [5,10,'Ignatius','Holy Hieromartyr Ignatius The God-Bearer']
        ,'12-25': [1,0,'Nativity','The Nativity, According To The Flesh, Of Our Lord, God & Savior Jesus Christ']
        ,'01-01': [3,8,'Basil','Bastil the Great']
        ,'01-02': [3,13,'Seraphim','Seraphim of Sarov']
        ,'01-06': [1,0,'Theophany','The Holy Theophany of our Lord, God & Savior Jesus Christ']
        ,'01-07': [4,3,'Forerunner','Synaxis of the Forerunner']
        ,'01-11': [3,13,'Theodosius','Theodosius the Cenobiarch']
        ,'01-14': [4,0,'Theophany','Leavetaking of Theophany']
        ,'01-17': [3,13,'Anthony','Anthony the Great']
        ,'01-18': [3,9,'Athanasius and Cyril','Holy Hierarchs Athanasius and Cyril']
        ,'01-19': [3,8,'Mark','Mark of Ephesus']
        ,'01-20': [3,13,'Euthymius','Euthymius the Great']
        ,'01-22': [5,6,'Timothy','Holy Apostle Timothy']
        ,'01-24': [3,23,'Xenia','Xenia of St. Petersburg']
        ,'01-25': [3,8,'Gregory','Gregory the Theologian']
        ,'01-27': [3,8,'John','John Chrysostom']
        ,'01-28': [4,13,'Ephrem','Ephrem the Syrian']
        ,'01-29': [5,10,'Ignatius','Ignatius the God-Bearer']
        ,'01-30': [3,9,'Holy Hierarchs','Three Holy Hierarchs']
        ,'01-31': [4,24,'Cyrus and John','Holy Unmercenaries Cyrus and John']
        ,'02-02': [2,0,'Meeting','Feast of the Meeting of Our Lord, God & Savior Jesus Christ']
        ,'02-06': [3,12,'Photius','Photius the Great']
        ,'02-08': [5,16,'Theodore','Martyr Theodore the General']
        ,'02-09': [4,0,'The Meeting of Our Lord','Feast of the Meeting of Our Lord, God & Savior Jesus Christ']
        ,'02-10': [3,10,'Haralambos','Haralambos of Magnesia']
        ,'02-11': [5,10,'Blase','Blase of Sebaste']
        ,'02-14': [3,9,'Cyril and Methodius','Cyril and Methodius']
        ,'02-17': [5,16,'Theodore','Martyr Theodore the Soldier']
        ,'02-24': [3,3,'Head','The First and Second Findings of the Head of the Holy & Glorious Prophet, Forerunner, and Baptist John']
        ,'03-09': [3,17,'Martyrs of Sebaste','Forty Martyrs of Sebaste']
        ,'03-12': [3,8,'Gregory','Gregory the Dialogist of Rome']
        ,'03-25': [2,1,'Annunciation','Feast of the Annunciation of Our Most Holy Lady, the Theotokos & Ever-Virgin Mary']
        ,'04-23': [3,16,'George','Greatmartyr George']
        ,'04-25': [3,6,'Mark','Holy Apostle Mark']
        ,'04-30': [3,6,'James','Holy Apostle James, the Brother of John']
        ,'05-02': [4,8,'Athanasius','Athanasius the Great']
        ,'05-08': [3,6,'John','Holy Apostle John']
        ,'05-10': [4,6,'Simon','Holy Apostle Simon the Zealot']
        ,'05-15': [5,13,'Pachomius','Pachomius the Great']
        ,'05-21': [3,8,'Constantine and Helen','Constantine and Helen (replace references to "hierarch" with "sovereign")']
        ,'05-25': [3,3,'Head','The Thrid Finding of the Precious Head of the Holy & Glorious Prophet, Forerunner, and Baptist John']
        ,'06-01': [3,16,'Justin','Justin Martyr the Philosopher']
        ,'06-04': [3,8,'Metrophanes','Metrophanes of Byzantium']
        ,'06-08': [5,16,'Theodore','Martyr Theodore the General']
        ,'06-11': [4,7,'Bartholomew and Barnabas','Holy Apostles Bartholomew and Barnabas']
        ,'06-12': [3,14,'Onuphrius and Peter','Onuphrius and Peter of Mount Athos']
        ,'06-24': [3,3,'Nativity','The Nativity of the Holy & Glorious Prophet, Forerunner, and Baptist John']
        ,'06-29': [3,7,'Peter and Paul','Holy Apostles Peter and Paul']
        ,'06-30': [4,7,'Apostles','Synaxis of the 12 Apostles']
        ,'07-01': [4,24,'Cosmas and Damian','Holy Unmercenaries Cosmas and Damian']
        ,'07-05': [4,13,'Athanasius','Athanasius of Athos']
        ,'07-08': [4,16,'Propcopius','Greatmartyr Procopius']
        ,'07-10': [3,10,'Joseph','Joseph of Damascus']
        ,'07-11': [3,18,'Euphemia','Greatmartyr Euphemia']
        ,'07-12': [3,13,'Paisios','Paisios the New of Mount Athos']
        ,'07-13': [4,5,'Gabriel','Archangel Gabriel']
        ,'07-15': [4,17,'Cyricus and Julitta','Martyrs Cyricus and Julitta']
        ,'07-17': [4,18,'Marina','Greatmartyr Marina']
        ,'07-20': [3,4,'Elijah','Holy Prophet Elijah']
        ,'07-22': [4,6,'Mary','Mary Magdalene (replace male pronouns with female in service)']
        ,'07-24': [3,17,'Boris and Gleb','Martyrs Boris and Gleb']
        ,'07-26': [3,18,'Paraskeva','Martyr Paraskeva']
        ,'07-27': [3,24,'Panteleimon','Martyr and Healer Panteleimon']
        ,'08-01': [4,2,'Procession','Procession of the Cross']
        ,'08-02': [5,10,'Stephen','Protomartyr Stephen']
        ,'08-06': [1,0,'Transfiguration','The Holy Transfiguration of Our Lord, God & Savior Jesus Christ']
        ,'08-13': [4,0,'Transfiguration','Leavetaking of the Transfiguration']
        ,'08-15': [2,1,'Dormition','The Dormition of Our Most Holy Lady, the Theotokos & Ever-Virgin Mary']
        ,'08-23': [4,1,'Dormition','Leavetaking of the Dormition of the Theotokos']
        ,'08-25': [4,7,'Bartholomew and Titus','Holy Apostles Bartholomew and Titus']
        ,'08-26': [5,19,'Adrian and Natalie','Martyrs Adrian and Natalie']
        ,'08-29': [3,3,'Beheading','The Beheading of the Holy & Glorious Prophet, Forerunner, and Baptist John']
    }

    #grabs menaion info from dictionary if available
    if calendar == 1: #old calendar
        menaion_date = date_oc.strftime('%m-%d')
    else: #new Calendar
        menaion_date = service_date.strftime('%m-%d')

    relative_feast = relative_feasts.get(menaion_date, None)
    if relative_feast and relative_feast[2]: #if a weekday is required...
        relative_feast = None if relative_feast[2] != weekday else relative_feast
    fixed_feast = fixed_feasts.get(menaion_date, None)
    relative_priority = relative_feast[0] if relative_feast else 7
    fixed_priority = fixed_feast[0] if fixed_feast else 7


    priority = min(relative_priority, fixed_priority)
    if priority < 7:
        if fixed_priority == priority:
            menaion_service = fixed_feast
            priority_type = 'fixed'
        elif relative_priority == priority:
            menaion_service = relative_feast
            priority_type = 'relative'
    else:
        menaion_service = None
        priority_type = None

    if menaion_service:
        rank = menaion_service[0]
        service_type = menaion_service[1]
        if priority_type == 'moveable' or priority_type == 'relative':
            service_name = menaion_service[3]
            service_long_name = menaion_service[4]
        elif priority_type == 'fixed':
            service_name = menaion_service[2]
            service_long_name = menaion_service[3]
        if type(service_type) == int:
            service_type = menaion_class.get(service_type)
        if service_type == 'Master':
            input_string = None
        else:
            input_string = process_pdf(filename=service_type,service='menaion')

        menaion = menaion_variables(
            input_string=input_string
            ,name=service_name
            ,service_type=service_type
            ,weekday=weekday
        )
        print(f'{priority_type} Menaion Service Found For {service_long_name}')
    else: #no menaion
        menaion = None
        service_type = None
        service_name = None
        service_long_name = None
        rank = 7
        print('No Menaion Service Found!')

    paschal = None #for now...

    liturgics = {} #dictionary for return
    liturgics['link_date'] = link_date
    liturgics['day_string'] = day_string
    links = [f'<a href="#{link_date}">{day_string}</a>']

    rank = 8 if variables_only_flag else rank

    variables = rubrics(
        rank=rank
        ,weekday=weekday
        ,name=service_name
        ,octoechos=octoechos
        ,menaion=menaion
        ,paschal=paschal
        ,service_type=service_type if service_type else None
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
        if variables_only_flag:
            liturgics['vespers'] = vespers_variables
            if service_long_name:
                liturgics['long_name'] = service_long_name
        else:
            vespers = render_template('vespers.html',variables=vespers_variables, weekday=weekday, name=service_name, long_name=service_long_name)
            liturgics['vespers'] = vespers

    if do_compline:
        compline_variables = variables.get('compline')
        compline_variables['troparion'] = compline_troparia(weekday=weekday, rank=rank)
        compline_variables['night_date'] = night_string_oc if calendar == 1 else night_string
        compline_variables['link'] = f'{link_date}-compline'
        links.append(f'<a href="#{link_date}-compline">Compline</a>')
        if variables_only_flag:
            liturgics['compline'] = compline_variables
        else:
            compline = render_template('smallCompline.html', variables=compline_variables, weekday=weekday)
            liturgics['compline'] = compline

    if do_nocturns:
        nocturns_variables = variables.get('nocturns', {})
        nocturns_variables = {} if not nocturns_variables else nocturns_variables
        nocturns_variables['kathisma'] = parse_kathisma(kathisma_rubric.get(weekday)[1])
        nocturns_variables['date'] = day_string_oc if calendar == 1 else day_string
        nocturns_variables['link'] = f'{link_date}-nocturns'
        links.append(f'<a href="#{link_date}-nocturns">Nocturns</a>')
        if variables_only_flag:
            liturgics['nocturns'] = nocturns_variables
        else:
            nocturns = render_template('nocturns.html', variables=nocturns_variables, weekday=weekday)
            liturgics['nocturns'] = nocturns

    if do_matins:
        matins_variables = variables.get('matins')
        matins_variables['kathisma1'] = parse_kathisma(kathisma_rubric.get(weekday)[2][0])
        matins_variables['kathisma2'] = parse_kathisma(kathisma_rubric.get(weekday)[2][1])
        matins_variables['date'] = day_string_oc if calendar == 1 else day_string
        matins_variables['link'] = f'{link_date}-matins'
        links.append(f'<a href="#{link_date}-matins">Matins</a>')
        if variables_only_flag:
            liturgics['matins'] = matins_variables
        else:
            matins = render_template('matins.html', variables = matins_variables, weekday=weekday, tone=tone, rank=rank, name=service_name, service_type=service_type, long_name=service_long_name)
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
        if variables_only_flag:
            liturgics['troparia'] = hours_troparia
            liturgics['kontakia'] = hours_kontakia

    if do_typika:
        typika_variables['date'] = day_string_oc if calendar == 1 else day_string
        typika_variables['link'] = f'{link_date}-typika'
        #(link appended below)
        if variables_only_flag:
            liturgics['typika'] = typika_variables
        else:
            typika = render_template('typika.html', variables = typika_variables, weekday=weekday, name=service_name, service_type=service_type, long_name=service_long_name)
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
