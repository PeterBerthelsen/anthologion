"""
Version 0.1.4
Updated 10/26/2021

Change Log:
9/29/2021 - 0.0.1 - Initial Working Build - Web Scraping Added
10/1/2021 - 0.0.2 - Vespers Regex & HTML formatting added
10/3/2021 - 0.0.3 - Compline Regex & HTML formatting added
10/4/2021 - 0.0.4 - Nocturns Regex & HTML formatting added
10/5/2021 - 0.0.6 - Matins (sessional hymns) Regex & HTML formatting added
10/7/2021 - 0.0.7 - Matins (canon) Regex & HTML formatting added
10/8/2021 - 0.0.8 - Integrated with _utils, Matins Regex & HTML formatting added
10/13/2021 - 0.1.0 - Minor syntax updates for Vespers build
10/14/2021 - 0.1.1 - Variables updated for Flask integration
10/21/2021 - 0.1.3 - Updated variables, removed vespers prokeimenon from payload
10/26/2021 - 0.1.4 - Added Liturgy variables
"""
import os
import re
from bs4 import BeautifulSoup
from _utils import process_pdf

def string_search (input_string:str, start_searches:list=[], end_searches:list=[], start_position:int=0):
    """
    Takes in a string and a list of strings.
    performs various find() functions on input string
    (at start position) for each search until a result is given.
    returns list: [starting location found (int), processed string with no search term]
    """
    i = -1 #iterators will start at 0 in loop
    j = -1 #iterating after would mess up the return section by 1 index position
    begin = -1 #find method returns -1 if no result is found
    end = -1
    try:
        while begin == -1: #while no result is found, search next in searches
            i += 1 #iterate...
            begin = input_string.find(start_searches[i],start_position)
    except: #error thrown if all begin searches fail (index error)
        return [0,input_string]
    try:
        while end == -1: #again, while no result is found...
            j += 1 #iterate...
            end = input_string.find(end_searches[j],start_position)
    except:  #error thrown if all end searches fail (index error)
        output = input_string[begin + len(start_searches[i]):]
        return [begin, output]
    #successfully found begin and end, returning processed string.
    output = input_string[begin + len(start_searches[i]):end]
    return [begin, output]

def octoechos_variables (input_string:str):
    """
    Uses string data from PDF extract to generate octoechos variable portions of the service.
    Text is divided at common breakpoints from PDFs, then formatted for use.
    Returns list with variables at set index locations.
    """

    #Establish Beginnings
    #Header text has font shadows, so lettering is often doubled
    #Line breaks are inconsistent with parser on headers, so partials are included
    #The below lists accurately capture portion for each day (avoiding Little Vespers on Saturday Evening)
    service_searches = {
        'vespers': [
            'AATT VVEESSPPEERRSS'
            ,'GRREEAATT  VVEESSPPEERRSS'
            ,'AT GREAT VESPERS'
            ,'VEESSPPEERRS'
            ,'VESPERS'
        ]
        ,'compline': [
            'AATT  CCOOMMPPLLIINNEE'
            ,'GRREEAATT  CCOOMMPPLLIINNEE'
            ,'MPPLLIIN'
            ,'COOMMPPLLIINNE'
            ,'COMPLINE'
        ]
        ,'nocturns': [
            'AATT  NNOOCCTTUURRNNSS'
            ,'NOOCCTTUURRNNS'
            ,'OCCTTUURRN'
            ,'NOCTURNES'
        ]
        ,'matins': [
            'AATT  MMAATTIINNSS'
            ,'AT MATINS'
            ,'MAATTIIN'
            ,'MATINS'
        ]
        ,'liturgy': [
            'AATT  LLIITTUURRG'
            ,'LIITTUURRGGY'
            ,'LIITTUURRG'
            ,'LITURGY'
        ]
    }

    vespers_beginning, vespers_service = string_search(input_string, service_searches.get('vespers'), service_searches.get('compline'))
    nocturns_beginning, nocturns_service = string_search(input_string, service_searches.get('nocturns'), service_searches.get('matins'))
    if nocturns_beginning > 0: #if nocturns service exists (Sundays)...
        compline_beginning, compline_service = string_search(input_string, service_searches.get('compline'), service_searches.get('nocturns'))
    else: #no nocturns (weekdays)...
        compline_beginning, compline_service = string_search(input_string, service_searches.get('compline'), service_searches.get('matins'))
        nocturns_beginning = None
        nocturns_service = None
    matins_beginning, matins_service = string_search(input_string, service_searches.get('matins'), service_searches.get('liturgy'))
    liturgy_beginning, liturgy_service = string_search(input_string, service_searches.get('liturgy'))
    #print(vespers_beginning, compline_beginning, nocturns_beginning, matins_beginning, liturgy_beginning)

    #create dictionary to return
    payload = {
        'vespers': octoechos_vespers(vespers_service)
        ,'compline': octoechos_compline(compline_service)
        ,'matins': octoechos_matins(matins_service)
        ,'liturgy': octoechos_liturgy(liturgy_service)
    }
    if nocturns_service:
        payload['nocturns'] = octoechos_compline(nocturns_service)

    return payload

def octoechos_vespers (service:str):
    """
    Formats vespers-specific service section and returns vespers parts dictionary
    """
    #Dictionary for Return
    vespers_parts = {}

    #Estalish Vespers breakpoints
    vespers_search = {
        'stichera': [
            'On “Lord I have cried ...”, '
            ,'“Lord I have cried ...”, '
            ,'“Lord, I have cried ...”, '
            ,'I have cried ...”, '
        ]
        ,'theotokion': [
            'Glory.,., Now & ever ..., ' #t5d7 typo
            ,'Glory ..., Now & Ever ..., '
            ,'Glory ..., Now & ever ..., '
            ,'Glory ..., Now & Ever ...,'
            ,'Glory ..., Now & ever ...,'
            ,'Glory..., Now & ever ...,'
            ,'Glory..., Now & Ever ...,'
        ]
        ,'prokeimenon': [
            'Then, “О Joyous Light ...”, '
            ,'Then, “О Joyous Light ...”; '
            ,'Then, “О Joyous Light ...”, '
            ,'After the Entrance and “O Joyous Light ...”,'
            ,'O Joyous Light ...'
            ,'O Joyous Light'
        ]
        ,'aposticha': [
            'On the Aposticha, '
            ,'Vouchsafe, О Lord ..., Litany: Let us complete ..., Then:'
        ]
        ,'apolytichion': [
            'Glory,.., Now & ever ...,' #t8d6 typo
            ,'Glory ..., Now & ever ..., Stavrotheotokion:  \n' #t1d4 repeat label
            ,'Glory ..., Now & Ever ...,'
            ,'Glory ..., Now & ever ...,'
            ,'Glory..., Now & Ever ...,'
            ,'Glory..., Now & ever ...,'
        ]
        ,'dismissal': [
            'Now Master, Trisagion' #t3d1 formatting
            ,'Then, “Now lettest Thou Thy servant depart ...”,'
            ,'“Now lettest Thou Thy servant depart ...”,'
            ,'And the Dismissal.'
        ]
    }

    #Parse Vespers Parts...
    vespers_stichera_location, vespers_stichera = string_search(service, vespers_search.get('stichera'), vespers_search.get('theotokion'))
    vespers_theotokion_location, vespers_theotokion = string_search(service, vespers_search.get('theotokion'), vespers_search.get('prokeimenon'), vespers_stichera_location)
    vespers_prokeimenon_location, vespers_prokeimenon = string_search(service, vespers_search.get('prokeimenon'), vespers_search.get('aposticha'))
    vespers_aposticha_location, vespers_aposticha = string_search(service, vespers_search.get('aposticha'), vespers_search.get('apolytichion'), vespers_prokeimenon_location)
    vespers_apolytichion_location, vespers_apolytichion = string_search(service, vespers_search.get('apolytichion'), vespers_search.get('dismissal'), vespers_aposticha_location)
    vespers_dismissal_location, vespers_dismissal = string_search(service, vespers_search.get('dismissal'))

    #remove service notes from certain vespers elements
    vespers_stichera = vespers_stichera[:vespers_theotokion_location] #above vespers_search sometimes doesn't trigger on theotokion...
    vespers_stichera = vespers_stichera[:vespers_stichera.find('Glory from the Menaion')] #Sunday note after stichera
    vespers_stichera = vespers_stichera[:vespers_stichera.find('Then the Stichera from the Menaion')] #Sunday for blank stichera
    #regex to remove extra text:
    vespers_stichera = vespers_stichera.replace('Israel hope in the Lord,', 'Israel hope in the Lord.') #t4d6 typo
    vespers_stichera = vespers_stichera.replace('\n','').split('Verse: ') #split by presence of Verse
    vespers_stichera_tone = vespers_stichera.pop(0) #remove front matter
    vespers_stichera_tone = re.sub(r'.*(stichera.*?:|resurrection stichera.*?:)',r'<p><i class="note">\1</i></p>',vespers_stichera_tone,flags=re.I)
    vespers_stichera_tone = re.sub(r'(spec[ .,]+mel[ .,]+:.*:)',r'<p><i class="note">\1</i></p>',vespers_stichera_tone,flags=re.I)
    vespers_stichera = [re.sub(r'^.*?\.\s','',s).strip() for s in vespers_stichera] #remove Verses (each is start of line to a period)
    #   remove instructions for addtional stichera from the actual text of the stichera
    vespers_stichera = [re.sub(r'These Stichera.*?:$','',s) for s in vespers_stichera]
    vespers_stichera = [re.sub(r'Then the Stichera.*?:$','',s) for s in vespers_stichera]
    vespers_stichera = [re.sub(r'Other Stichera.*?:$','',s) for s in vespers_stichera]
    vespers_stichera = [re.sub(r'\. Then.*?.*?:$','.',s) for s in vespers_stichera]
    vespers_stichera = ['<p class="stichera"><i class="note">*</i>' + s + '</p>' for s in vespers_stichera] #HTML wrap
    #   ---
    vespers_theotokion = vespers_theotokion[:vespers_theotokion.find('Then “O Joyous Light ...”')] #clip off at instructions after in case prior search failed
    vespers_theotokion = vespers_theotokion.replace('\n','').strip() #remove line breaks and white space
    vespers_theotokion = re.sub(r'\Athe','The',vespers_theotokion) #capitalize The
    vespers_theotokion = '<p><i class="note">' + vespers_theotokion.replace('on: ','on</i><br />').replace('tic:','tic</i><br />') + '</p>' #HTML formatting
    vespers_theotokion = vespers_theotokion.replace('in the same tone:','in the same tone</i><br />') #HTML formatting
    #   ---
    # vespers_prokeimenon = re.sub(r'\nVouchsafe.*','',vespers_prokeimenon).strip() #remove service instructions after prokeimenon text
    # vespers_prokeimenon = re.sub(r'^the','The',vespers_prokeimenon).strip() #capitalize The, remove white space
    # vespers_prokeimenon = '<p class="note">' + re.sub(r':\s\n','</p><p>',vespers_prokeimenon) #HTML formatting
    # vespers_prokeimenon = re.sub(r'\.\s\nVerse: ','</p><p><i class="note">Verse:</i> ',vespers_prokeimenon) + '</p>' #HTML formatting
    #   ---
    vespers_aposticha = re.sub(r'Glory from the Menaion.*?$','',vespers_aposticha) #removes instructions
    vespers_aposticha = re.sub(r'^the','The',vespers_aposticha).strip() #capitalize The, remove white space
    vespers_aposticha = vespers_aposticha.replace('Tone VIII', 'Tone VIII:') #t8d2 typo
    vespers_aposticha = vespers_aposticha.replace('Tone VI ', 'Tone VI: ') #t6d4 typo
    vespers_aposticha = '<p><i class="note">' + re.sub(r'(:.\s\n|:.\n)','</i></p><p>',vespers_aposticha) + '</p>' #HTML formatting first row
    vespers_aposticha = re.sub(r'\.\s\n','.</p><p>',vespers_aposticha) #HTML formatting line breaks for stichera
    vespers_aposticha = vespers_aposticha.replace('\nVerse: ','</p><p>Verse: ').replace('\n','') #HTML formatting line breaks for verses
    vespers_aposticha = vespers_aposticha.replace('To the Martyrs:','<i class="note">To the Martyrs:</i>') #HTML formatting
    vespers_aposticha = vespers_aposticha.replace('For the reposed:','<i class="note">For the reposed:</i>') #HTML formatting
    vespers_aposticha = vespers_aposticha.replace('Verse:','<i class="note">Verse:</i>') #HTML formatting
    #   ---
    vespers_apolytichion = vespers_apolytichion.replace('\n','').strip() #remove line breaks and white space
    vespers_apolytichion = re.sub(r'\Athe','The',vespers_apolytichion) #capitalize The
    vespers_apolytichion = '<p><i class="note moveable">' + vespers_apolytichion.replace('ion: ','ion</i><br />') + '</p>' #HTML formatting

    #build service dictionary parts for payload
    vespers_parts['stichera'] = vespers_stichera
    vespers_parts['stichera_tone'] = vespers_stichera_tone
    vespers_parts['doxastichon'] = ''
    vespers_parts['theotokion'] = vespers_theotokion
    #vespers_parts['prokeimenon'] = vespers_prokeimenon #handled by hymns.py
    vespers_parts['aposticha'] = vespers_aposticha
    vespers_parts['apolytichion'] = vespers_apolytichion
    vespers_parts['readings'] = ''

    return vespers_parts

def octoechos_compline (service:str):
    """
    Formats compline-specicic service section and returns compline parts dictionary
    Also works for Nocturns as they are the same format consisting of Odes only...
    """
    #Dictionary for Return
    compline_parts = {}

    #Establish Compline breakpoints & Format HTML
    service = re.sub(r'(O\s*O\s*D\s*D\s*E\s*E\s*|О\s*О\s*D\s*D\s*E\s*E\s*)','|<h3>Ode ',service).split('|') #break up duplicate ODE text (two font types...), split odes
    service = [re.sub(r'\s*\nIrmos:','</h3><p><i class="note">Irmos:</i>',s) for s in service] #close ODE header, wrap Irmos in note tag
    service = [re.sub(r'([Rr]efrain:|[A-Za-z]*[Tt]heotokion:|[Ss]essional [Hh]ymn.*:|[Ss]pec\.\s*Mel\.:.*:)',r'<i class="note">\1</i>',s) for s in service] #service notes
    service = [re.sub(r'\(([Tt]hrice|[Tt]wice)\)',r'<i class="note">\1</i>',s) for s in service]
    service = [s.replace('XX','X').replace('VV','V').replace('II','I') for s in service] #Remove duplicate Roman Numerals
    service = [re.sub(r'([^\w,*\?;]) \n',r'\1 \n</p><p>',s) for s in service] #close paragraphs after punctuation+line breaks
    service = [re.sub(r'<p>$','',s).replace('\n','') for s in service] #remove last vesitigial p tag
    service[0] = re.sub(r'^.*[Cc]anon','<h2>Canon',service[0]).strip().replace('</p>','') + '</h2>' #format Canon Header, ditch p tag added to longer canon names (line break)
    service[-1] = re.sub(r'<p>\s?[Tt]hen[., ]\s?(“|[Tt]he [Hh]ymn [Oo]f|[Tt]he [Rr]est.*([Nn]octurn|[Cc]ompline)).*','',service[-1]) #strip contents after final ode

    compline_parts['odes'] = service

    return compline_parts

def octoechos_matins (service:str):
    """
    Formats matins-specific service section and returns matins parts dictionary
    """
    #Dictionary for Return
    matins_parts = {}

    #Establish Matins breakpoints
    matins_search = {
        'resurrection': [ #resurrection troparion (sundays)
            'On “God is The Lord ...,”'
            ,'God is The Lord ...,”'
            ,'the Resurrection Troparion'
        ]
        ,'session1': [
            'After the 1st chanting of the Psalter'
        ]
        ,'session2': [
            'After the 2nd, chanting of the Psalter' #t2d2 typo
            ,'After the 2nd chanting of the Psalter'
        ]
        ,'session3': [
            'After the 3rd chanting of the Psalter'
        ]
        ,'ascent': [
            'The Songs of Ascent:'
            ,'Songs of Ascent'
        ] #sunday
        ,'canon': [
            'Then the Canons:'
            ,'Canon of '
            ,'canon of '
            ,'Canon to'
            ,'canon to'
            ,'DEE  II'
        ]
        ,'praises': [ #weekday
            'On the Praises'
            ,'On the Praises,'
        ]
        ,'aposticha': [
            'On the Aposticha'
            ,'Aposticha'
        ]
        ,'dismissal': [
            'Glory ..., The Eothinon'
            ,'Then, “It is good to give thanks ...,”'

        ]
    }

    #Parse Matins Parts...
    matins_resurrection_location, matins_resurrection = string_search(service, matins_search.get('resurrection'), matins_search.get('session1'))
    matins_session1_location, matins_session1 = string_search(service, matins_search.get('session1'), matins_search.get('session2'))
    if matins_resurrection_location > 0: #sundays
        matins_session2_location, matins_session2 = string_search(service, matins_search.get('session2'), matins_search.get('ascent'))
        matins_session3_location, matins_session3 = string_search(service, matins_search.get('session3'), matins_search.get('ascent'))
        matins_ascent_location, matins_ascent = string_search(service, matins_search.get('ascent'), matins_search.get('canon'))
    else: #weekdays
        matins_session2_location, matins_session2 = string_search(service, matins_search.get('session2'), matins_search.get('canon'))
        matins_session3_location, matins_session3 = string_search(service, matins_search.get('session3'), matins_search.get('canon'))
        matins_ascent_location = None
        matins_ascent = None
    #matins_praises_location, matins_praises = string_search(service, matins_search.get('praises'), matins_search.get('canon'))
    matins_aposticha_location, matins_aposticha = string_search(service, matins_search.get('aposticha'), matins_search.get('dismissal'))
    matins_dismissal_location, matins_dismissal = string_search(service, matins_search.get('dismissal'))

    #Canons sometimes have descriptive text BEFORE Ode I, sometimes no text at all before Ode I, sometimes Resurrection, sometimes indicator text...
    #   This means the canon needs a special delimiter to find the text properly...
    try:
        matins_canon_location = re.search(r'\n(Canon |Resurrection Canon )',service,flags=re.M)
        matins_canon = service[matins_canon_location.start():matins_aposticha_location]
    except AttributeError: #None returned...
        matins_canon_location, matins_canon = string_search(service, matins_search.get('canon'), matins_search.get('aposticha'))
    try:
        matins_praises_location = re.search(r'\n[Oo]n [Tt]he [Pp]raises[,. ]', matins_canon,flags=re.M)
        matins_praises = matins_canon[matins_praises_location.start() + 22:] #Trims search term out
    except AttributeError: #None returned...
        matins_praises_location = matins_praises = None

    #Clearing unused variables
    matins_resurrection = None if matins_resurrection_location == 0 else matins_resurrection
    matins_resurrection_location = None if matins_resurrection_location == 0 else matins_resurrection_location
    matins_session3 = None if matins_session3_location == 0 else matins_session3
    matins_session3_location = None if matins_session3_location == 0 else matins_session3_location


    #processing service components:
    #Resurrection Troparion (Sundays)
    if matins_resurrection:
        matins_resurrection = '<p>' + re.sub(r'\([Tt]wice\)','<i class="note">Twice.</i></p>',matins_resurrection) #Format 'twice', close paragraph
        matins_resurrection = re.sub(r'Glory.*otherwise[; ]+Glory[., ]+Now & Ever[., ]+',r'<div class="menaion matins troparion"></div>',matins_resurrection, flags=re.I) #div for Menaion
        matins_resurrection = re.sub(r'\s*([Tt]he [Tt]heotokion.*:)'
            ,r'<div class="simple matins troparion"><p>Glory ..., Now & Ever ...,</p></div><p><i class="note">\1</i></p><p>',matins_resurrection) + '</p>' #format troparion
        matins_parts['resurrection'] = matins_resurrection
    #Sessional Hymns 1
    matins_session1 = re.sub(r'([Vv]erse:|[A-Za-z]*[Tt]heotokion:|[Ss]essional [Hh]ymn.*:|[Ss]pec\.\s*Mel\.*?:.*?:)',r'<i class="note">\1</i>',matins_session1) #service notes
    matins_session1 = re.sub(r'([^\w,*\?;]) \n',r'\1 \n</p><p>',matins_session1).replace('\n','')  #close paragraphs after punctuation+line breaks, remove line breaks
    matins_session1 = re.sub(r'<p>\s*After the 2nd.?\s+chant.*',r'',matins_session1, flags=re.I) #remove extra content starting at 3rd Sessional hymn
    matins_session1 = re.sub(r'^.*?</p>',r'',matins_session1) #removes all content up to & including vestigial p close tag
    matins_parts['session1'] = matins_session1
    #Sessional Hymns 2
    matins_session2 = re.sub(r'([Vv]erse:|[A-Za-z]*[Tt]heotokion:|[Ss]essional [Hh]ymn.*:|[Tt]o [Tt]he [Mm]artyrs.*:|[Ss]pec\.\s*Mel\.:.*:)',r'</p><p><i class="note">\1</i>',matins_session2) #service notes
    matins_session2 = re.sub(r'([^\w,*\?;]) \n',r'\1 \n</p><p>',matins_session2).replace('\n','')  #close paragraphs after punctuation+line breaks, remove line breaks
    matins_session2 = re.sub(r'<p>\s*If a polyeleos.*',r'',matins_session2, flags=re.I) #remove extra content starting at polyeleos (Sundays)
    matins_session2 = re.sub(r'<p>\s*After the 3rd.?\s+chant.*',r'',matins_session2, flags=re.I) #remove extra content starting at 3rd Sessional hymn
    matins_session2 = re.sub(r'After the 3rd chant.*',r'',matins_session2, flags=re.I) #t2d4 typo
    matins_session2 = re.sub(r'^.*?<i',r'<i',matins_session2) #removes all content up to i tag
    matins_session2 = re.sub(r'<p>(O+D+|O+D+E+\s+I+).*', r'',matins_session2) #removes excess content after up to Ode (needed for Saturdays)
    matins_parts['session2'] = matins_session2
    #Sessional Hymns 3
    if matins_session3:
            matins_session3 = re.sub(r'([Vv]erse:|[A-Za-z]*[Tt]heotokion:|[Ss]essional [Hh]ymn.*:|[Ss]pec\.\s*Mel\.:.*:)',r'<i class="note">\1</i>',matins_session3) #service notes
            matins_session3 = re.sub(r'([^\w,*\?;]) \n',r'\1 \n</p><p>',matins_session3).replace('\n','')  #close paragraphs after punctuation+line breaks, remove line breaks
            matins_session3 = re.sub(r'^.*?<i',r'<i',matins_session3) #removes all content up to i tag
            matins_session3 = re.sub(r'<p>(O+D+|O+D+E+\s+I+).*', r'',matins_session3) #removes excess content after up to Ode
            matins_session3 = re.sub(r'<p>[Cc]anon ([Tt]o|[Oo]f).*', r'',matins_session3) #removes excess content after up to Canon
            matins_parts['session3'] = matins_session3
    #Hymns of Ascent: (Sundays)
    if matins_ascent:
        #prokeimenon for Sunday captured in ascent
        matins_prokeimenon = 'Prokeimenon' + re.split(r'[Pp]rokeimenon',matins_ascent,maxsplit=1)[1] #grab prokeimenon from ascent
        matins_prokeimenon = re.sub(r'.*([Pp]rokeimenon.*:)',r'<p><i class="note">\1</i></p><p>',matins_prokeimenon) #header note
        matins_prokeimenon = re.sub(r'Let every breath.*',r'</p>',matins_prokeimenon,flags=re.I) #clear out excess
        matins_prokeimenon = re.split(r'The Sunday.*Gospel',matins_prokeimenon,flags=re.I)[0] #split from reading
        matins_prokeimenon = re.sub(r'([Tt]he [Vv]erse:|[Vv]erse:)',r'</p><p><i class="note">\1</i>',matins_prokeimenon) #notes for verses
        matins_parts['prokeimenon'] = matins_prokeimenon
        #then format the hymns of ascent
        matins_ascent = re.split(r'[Pp]rokeimenon',matins_ascent)[0] #grab text before prokeimenon
        matins_ascent = re.sub(r'([0-9][A-Za-z]+ [Aa]ntiphon:)',r'</p><p><i class="note">\1</i></p><p>',matins_ascent) #note antiphon headers
        matins_ascent = re.sub(r'(Glory[ .,]+Now & Ever[ .,]+)',r'</p><p>\1</p><p>',matins_ascent,flags=re.I) #line break on G, N&E
        matins_parts['ascent'] = matins_ascent
    #Matins Canon
    matins_canon = re.sub(r'(O\s*O\s*D\s*D\s*E\s*E\s*|О\s*О\s*D\s*D\s*E\s*E\s*)\s+([XVI]+)\s+',r'</p><h3>Ode \2</h3><p>',matins_canon) #Ode headers
    matins_canon = re.sub(r'^(.*[Aa]crostic.*)\n',r'\1',matins_canon,flags=re.M)#removes line breaks from lengthy titles for capture below
    matins_canon = re.sub(r'^(.*[Aa]crostic.*)\n',r'\1',matins_canon,flags=re.M)#removes line breaks from REALLY lengthy titles for capture below
    matins_canon = re.sub(r'\([Tt]wice[.]?\)',r'<i class="note">Twice.</i></p><p>',matins_canon)
    matins_canon = re.sub(r', and make prostrations.', r'<i class="note"> Prostrations.</i>',matins_canon)
    matins_canon = re.sub(r'(Resurrection canon.*|Canon.*|To the Martyrs:|Refrain:|[A-Za-z]*Theotokion:|Ikos:|And after each.*:|Verse:|Another[ ,].*\n?.*:)'
                        ,r'</p><p><i class="note">\1</i>',matins_canon,flags=re.I) + '</p>'#service notes
    matins_canon = re.sub(r'[Ii]rmos:',r'</p><p><i class="note">Irmos:</i>',matins_canon)
    matins_canon = re.sub(r'The Troparia from the Menaion, then the appointed Katavasia.*\s*'
                        ,r'</p><div class="matins menaion canon troparia"></div><div class="matins katavasia"></div><p>',matins_canon, flags=re.I) # menaion notes
    matins_canon = re.sub(r'(<p>The small litany:\s*</p>|<p>The small litany:\s*(.*Kontakion.*:))'
                        ,r'<p>Lord, have mercy. <i class="note">Twelve Times.</i></p><p><i class="note">\2</i></p>',matins_canon,flags=re.I) #litany replace
    matins_canon = re.sub(r'<p>The small litany:.*',r'</p>',matins_canon.replace('\n',''),flags=re.I) #final litany replace
    matins_canon = matins_canon.replace('XX','X').replace('VV','V').replace('II','I') #Remove duplicate Ode Roman Numerals
    matins_canon = re.sub(r'Then, [“"].*','',matins_canon.replace('\n','')) #remove excess after canon
    matins_parts['canon'] = matins_canon
    #Praises / Lauds (Saturdays)
    if matins_praises:
        matins_praises = matins_praises
        matins_praises = re.sub(r'([Ss]tichera.*:)',r'<p><i class="note">\1</i></p>',matins_praises)
        matins_praises = re.sub(r'^(Verse:.*\n?.*\.)',r'</p>\1<p>',matins_praises,flags=re.I|re.M)
        matins_praises = re.sub(r'(To the Martyrs:|For the Reposed:|[A-Za-z]*Theotokion:|Verse:)'
                            ,r'</p><p><i class="note">\1</i>',matins_praises,flags=re.I) + '</p>'#service notes
        matins_praises = re.sub(r'Glory[ .,]+Now & Ever[ .,]+',r'</p><p>Glory ..., Now & Ever ...,</p><p>',matins_praises, flags=re.I)
        matins_parts['praises'] = matins_praises
    #Aposticha
    matins_aposticha = matins_aposticha
    matins_aposticha = re.sub(r'^(Verse:.*\n?.*\.)',r'</p>\1<p>',matins_aposticha,flags=re.I|re.M) #seperate verses
    matins_aposticha = re.sub(r'(Spec[., ]+Mel[ .,]+:.*:|[A-Za-z]*Theotokion:|Verse:|To the Martyrs:|other stichera.*:)'
                        ,r'</p><p><i class="note">\1</i>',matins_aposticha,flags=re.I) #service notes
    matins_aposticha = re.sub(r'Glory[ .,]+Now & Ever[ .,]+',r'</p><p>Glory ..., Now & Ever ...,</p><p>',matins_aposticha, flags=re.I) #now and ever
    matins_aposticha = matins_aposticha[re.search(r'(Stichera.*?:|resurrection stichera.*?:)',matins_aposticha,flags=re.I).start():]
    matins_aposticha = re.sub(r'^(resurrection stichera.*?:|stichera.*?:)\s+\n',r'<p><i class="note">\1</i></p>'
                        ,matins_aposticha,count=1,flags=re.I) #clear front matter
    matins_parts['aposticha'] = matins_aposticha

    return matins_parts

def octoechos_liturgy(service:str):
    """
    Formats liturgy-specific service section and returns liturgy parts dictionary
    """
    #Dictionary for Return
    liturgy_parts = {}
    #Estalish Litury breakpoints
    beatitudes_start = re.search(r'At The Liturgy Beatitudes', service, flags=re.I) #3-1 redundancy
    beatitudes_start = re.search(r'(On the beatitudes|beatitudes)',service, flags=re.I) if not beatitudes_start else beatitudes_start
    res_troparion_start = re.search(r'(resurrection troparion|troparion of the resurrection)', service, flags=re.I)
    res_kontakion_start = re.search(r'(resurrection kontakion|kontakion of the resurrection)', service, flags=re.I)
    prokeimenon_start = re.search(r'on (monday|tuesday|wednesday|thursday|friday|saturday|sunday)[, ]?',service, flags=re.I)
    prokeimenon_start = re.search(r'Prokeimenon[, ]+',service) if not prokeimenon_start else prokeimenon_start
    if res_troparion_start: #if resurrection troparion is present, end there, otherwise, the prokeimenon
        troparia = service[beatitudes_start.start():res_troparion_start.start()]
    else:
        troparia = service[beatitudes_start.start():prokeimenon_start.start()]
    troparia = re.sub(r'(.*?[Bb]eatitudes.*?[Tt]one [ivIV]+(?<!(:)\n))',r'\1:',troparia) #adding ':' missing from 3-1
    troparia = re.sub(r'([Tt]one [ivIV]+.*?:)',r'\1|',troparia) #bar off tone tone for later split
    troparia = re.sub(r'([Tt]heotokion:|[Mm]artyricon:|[Tt]o the [Mm]artyrs:|[Ff]or the [Rr]eposed:)',r'<i class="note">\1</i>',troparia,re.I)
    troparia = re.sub(r'([!.?”"’])[ ]+?\n',r'\1|<i class="note">*</i>',troparia.strip(), flags=re.M).split('|') #split along new line
    liturgy_parts['troparia_tone'] = '<p><i class="note">' + troparia.pop(0) + '</i></p>' #tone note as it's own variable
    troparia = [re.sub(r'^: ',r'<i class="note">*</i>',t) for t in troparia] #removing excess ':' sometimes added
    troparia = ['<p>' + re.sub(r'\n',r'',t.strip()) + '</p>' for t in troparia]

    if res_troparion_start:
        res_troparion = service[res_troparion_start.start():res_kontakion_start.start()]
        res_troparion = re.sub(r'(([Tt]roparion of the [Rr]esurrection|[Rr]esurrection [Tt]roparion).*?:)',r'<p><i class="note">\1</i></p><p>',res_troparion.replace('\n','')) + '</p>'
        liturgy_parts['resurrection_troparion'] = res_troparion
        res_kontakion = service[res_kontakion_start.start():prokeimenon_start.start()]
        res_kontakion = re.sub(r'(([Kk]ontakion of the [Rr]esurrection|[Rr]esurrection [Kk]ontakion).*?:)',r'<p><i class="note">\1</i></p><p>',res_kontakion.replace('\n','')) + '</p>'
        res_kontakion = re.sub(r'The\s+</p>',r'</p>',res_kontakion) #'the' captured from 'The Prokeimenon' beginning needs to be removed.
        liturgy_parts['resurrection_kontakion'] = res_kontakion

    prokeimenon = service[prokeimenon_start.start():]
    prokeimenon = re.sub(r'on (monday|tuesday|wednesday|thursday|friday|saturday|sunday).*?:\s+',r'',prokeimenon.replace('\n','').strip(),flags=re.I) #remove line breaks and extra label
    prokeimenon = re.sub(r'communion verse:.*',r'',prokeimenon,flags=re.I) #remove communion verse and everything after
    prokeimenon = re.sub(r'(the verse:|verse:|alleluia.*?:|and for the departed.*?:|prokeimenon.*?:)',r'</p><p><i class="note">\1</i>',prokeimenon,flags=re.I) #common line breaks needed

    alleluia = '<p><i class="note">' + re.sub(r'.*(alleluia.*?:.*)',r'\1',prokeimenon,flags=re.I)
    liturgy_parts['alleluia'] = alleluia

    prokeimenon = re.sub(r'(.*)<p><i class="note">alleluia.*:.*',r'\1',prokeimenon,flags=re.I)
    liturgy_parts['prokeimenon'] = prokeimenon
