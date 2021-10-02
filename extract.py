import os
import io
import re
import requests
import fitz
from urllib.request import Request, urlopen

def download_pdf (url:str, filename:str):
    """
    Downloads PDF from website, saves it off, parses text contents, then removes file.
    Returns string value of PDF text.
    """
    r = urlopen(Request(url)) #open the URL
    f = filename + '.pdf' #set download file name
    file = open(f, 'wb') #open file
    file.write(r.read()) #write content/download file
    file.close() #close/save the file
    with fitz.open(f) as content: #open for extraction
        payload = ''
        for page in content: #read each page
            payload += page.getText() #add each page to payload
    os.remove(f) #delete downloaded file after payload established
    return payload #return payload string

def string_search (input_string:str, searches:list, start_position:int=0):
    """
    Takes in a string and a list of strings.
    performs various find() functions on input string
    (at start position) for each search until a result is given.
    returns list: [starting location found (int), processed string with no search term]
    """
    i = -1 #iterate will start at 0
    index = -1 #find method returns -1 if no result is found
    try:
        while index == -1: #while no result is found, search next in searches
            i += 1 #iterate...
            index = input_string.find(searches[i],start_position)
    except: #error thrown if all searches fail (index error)
        return [0,input_string]
    output = input_string[index + len(searches[i]):]
    return [index, output]

def octoechos_variables (input_string:str, sergius_day:int):
    """
    Uses string data from PDF extract to generate octoechos variable portions of the service.
    Text is divided at common breakpoints from PDFs, then formatted for use.
    Returns list with variables at set index locations.
    """
    vespers_parts = {}
    compline_parts = {}
    matins_parts = {}

    #Establish Beginnings
    #Header text has font shadows, so lettering is often doubled
    #Line breaks are inconsistent with parser on headers, so partials are included
    #The below lists accurately capture portion for each day (avoiding Little Vespers on Saturday Evening)
    vespers_string = [
        'AATT VVEESSPPEERRSS'
        ,'GRREEAATT  VVEESSPPEERRSS'
        ,'AT GREAT VESPERS'
        ,'VEESSPPEERRS'
        ,'VESPERS'
    ]
    compline_string = [
        'AATT  CCOOMMPPLLIINNEE'
        ,'GRREEAATT  CCOOMMPPLLIINNEE'
        ,'MPPLLIIN'
        ,'COOMMPPLLIINNE'
        ,'COMPLINE'
    ]
    matins_string = [
        'AATT  MMAATTIINNSS'
        ,'AT MATINS'
        ,'MAATTIIN'
        ,'MATINS'
    ]
    liturgy_string = [
        'AATT  LLIITTUURRG'
        ,'LIITTUURRGGY'
        ,'LIITTUURRG'
        ,'LITURGY'
    ]

    vespers_beginning = string_search(input_string, vespers_string)[0]
    compline_beginning = string_search(input_string, compline_string)[0]
    matins_beginning = string_search(input_string, matins_string)[0]
    liturgy_beginning = string_search(input_string, liturgy_string)[0]

    #print(vespers_beginning, compline_beginning, matins_beginning, liturgy_beginning)

    vespers_service = input_string[vespers_beginning:compline_beginning - 1]
    compline_service = input_string[compline_beginning:matins_beginning - 1]
    matins_service = input_string[matins_beginning:liturgy_beginning - 1]
    liturgy_service = input_string[liturgy_beginning:]

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
        ]
        ,'prokeimenon': [
            'Then, “О Joyous Light ...”, '
            ,'After the Entrance and “O Joyous Light ...”,'
        ]
        ,'aposticha': [
            'On the Aposticha, '
            ,'Vouchsafe, О Lord ..., Litany: Let us complete ..., Then:'
        ]
        ,'apolytichion': [
            'Glory.,., Now & ever ..., ' #t5d7 typo
            ,'Glory ..., Now & Ever ..., '
            ,'Glory ..., Now & ever ..., '
            ,'Glory ..., Now & Ever ...,'
            ,'Glory ..., Now & ever ...,'
        ]
        ,'dismissal': [
            'Then, “Now lettest Thou Thy servant depart ...”,'
            ,'“Now lettest Thou Thy servant depart ...”,'
        ]
    }

    #Establish Matins breakpoints
    matins_search = {
        'session1': []
        ,'session2': []
        ,'session3': []
        ,'canon': []
        ,'aposticha': []
        ,'apolytichion': []
        ,'dismissal': []
    }

    #Parse Vespers Parts...
    vespers_stichera_location, vespers_stichera = string_search(vespers_service, vespers_search.get('stichera'))
    vespers_theotokion_location, vespers_theotokion = string_search(vespers_service, vespers_search.get('theotokion'), vespers_stichera_location)
    vespers_prokeimenon_location, vespers_prokeimenon = string_search(vespers_service, vespers_search.get('prokeimenon'))
    vespers_aposticha_location, vespers_aposticha = string_search(vespers_service, vespers_search.get('aposticha'))
    vespers_apolytichion_location, vespers_apolytichion = string_search(vespers_service, vespers_search.get('apolytichion'), vespers_aposticha_location)
    vespers_dismissal_location, vespers_dismissal = string_search(vespers_service, vespers_search.get('dismissal'))

    #remove service notes from certain vespers elements
    vespers_stichera = vespers_stichera[:vespers_theotokion_location - 1]
    vespers_theotokion = vespers_theotokion[:vespers_prokeimenon_location - 1]
    vespers_prokeimenon = vespers_prokeimenon[:vespers_aposticha_location - 1]
    vespers_aposticha = vespers_aposticha[:vespers_apolytichion_location - 1]
    vespers_apolytichion = vespers_apolytichion[:vespers_dismissal_location - 1]
    vespers_stichera = vespers_stichera[:vespers_stichera.find('Glory from the Menaion')] #Sunday note after stichera
    vespers_stichera = vespers_stichera[:vespers_stichera.find('Then the Stichera from the Menaion')] #Sunday for blank stichera

    #attempt #2 at splitting stichera: REGEX!
    #regex to
    vespers_stichera = vespers_stichera.replace('\n','').split('Verse: ')[1:]
    vespers_stichera = [re.sub(r'^.*?\.','',s).strip() for s in vespers_stichera]
    #text_after = re.sub(regex_search_term, regex_replacement, text_before)

    print(f'{len(vespers_stichera)} stichera found from the octoechos')
    #build service dictionary parts for payload
    vespers_parts['stichera'] = vespers_stichera
    vespers_parts['theotokion'] = vespers_theotokion
    vespers_parts['prokeimenon'] = vespers_prokeimenon
    vespers_parts['aposticha'] = vespers_aposticha
    vespers_parts['apolytichion'] = vespers_apolytichion

    #create dictionary to return
    payload = {
        'vespers': vespers_parts
        ,'compline': compline_parts
        ,'matins': matins_parts
    }
    return payload


#For Single
tone = 5
sergius_day = 7
octoechos_url = f'http://www.st-sergius.org/services/oktiochos/{tone}-{sergius_day}.pdf'
octoechos = octoechos_variables(download_pdf(octoechos_url, 'octoechos'), sergius_day)
print(octoechos.get('vespers').get('theotokion'))
# ss = octoechos.get('vespers').get('stichera')
# for s in ss:
#     print(f'{s}\n--------------------------------')

#For multiples
tt = [1,2,3,4,5,6,7,8]
dd = [1,2,3,4,5,6,7]
#
# for t in tt:
#     for d in dd:
#         tone = t
#         sergius_day = d
#         octoechos_url = f'http://www.st-sergius.org/services/oktiochos/{tone}-{sergius_day}.pdf'
#         octoechos = octoechos_variables(download_pdf(octoechos_url, 'octoechos'), sergius_day)
#         test_v = octoechos.get('vespers').get('stichera')[:50]
#         print(f'{t}/{d}/    {test_v}\n--------------------------------------------')
