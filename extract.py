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
    except: #error thrown if all searches fail (index error)
        return [0,input_string]
    try:
        while end == -1: #again, while no result is found...
            j += 1 #iterate...
            end = input_string.find(end_searches[j],start_position)
    except:
        output = input_string[begin + len(start_searches[i]):]
        return [begin, output]
    output = input_string[begin + len(start_searches[i]):end]
    return [begin, output]

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
    compline_beginning, compline_service = string_search(input_string, service_searches.get('compline'), service_searches.get('matins'))
    matins_beginning, matins_service = string_search(input_string, service_searches.get('matins'), service_searches.get('liturgy'))
    liturgy_beginning, liturgy_service = string_search(input_string, service_searches.get('liturgy'))
    #print(vespers_beginning, compline_beginning, matins_beginning, liturgy_beginning)

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
    vespers_stichera_location, vespers_stichera = string_search(vespers_service, vespers_search.get('stichera'), vespers_search.get('theotokion'))
    vespers_theotokion_location, vespers_theotokion = string_search(vespers_service, vespers_search.get('theotokion'), vespers_search.get('prokeimenon'), vespers_stichera_location)
    vespers_prokeimenon_location, vespers_prokeimenon = string_search(vespers_service, vespers_search.get('prokeimenon'), vespers_search.get('aposticha'))
    vespers_aposticha_location, vespers_aposticha = string_search(vespers_service, vespers_search.get('aposticha'), vespers_search.get('apolytichion'), vespers_prokeimenon_location)
    vespers_apolytichion_location, vespers_apolytichion = string_search(vespers_service, vespers_search.get('apolytichion'), vespers_search.get('dismissal'), vespers_aposticha_location)
    vespers_dismissal_location, vespers_dismissal = string_search(vespers_service, vespers_search.get('dismissal'))

    #remove service notes from certain vespers elements
    vespers_stichera = vespers_stichera[:vespers_theotokion_location] #above vespers_search sometimes doesn't trigger on theotokion...
    vespers_stichera = vespers_stichera[:vespers_stichera.find('Glory from the Menaion')] #Sunday note after stichera
    vespers_stichera = vespers_stichera[:vespers_stichera.find('Then the Stichera from the Menaion')] #Sunday for blank stichera

    #regex to remove extra text:
    vespers_stichera = vespers_stichera.replace('Israel hope in the Lord,', 'Israel hope in the Lord.') #t4d6 typo
    vespers_stichera = vespers_stichera.replace('\n','').split('Verse: ')[1:] #split by presence of Verse, then remove front matter
    vespers_stichera = [re.sub(r'^.*?\.\s','',s).strip() for s in vespers_stichera] #remove Verses (each is start of line to a period)
    #   remove instructions for addtional stichera from the actual text of the stichera
    vespers_stichera = [re.sub(r'These Stichera.*?:$','',s) for s in vespers_stichera]
    vespers_stichera = [re.sub(r'Then the Stichera.*?:$','',s) for s in vespers_stichera]
    vespers_stichera = [re.sub(r'Other Stichera.*?:$','',s) for s in vespers_stichera]
    vespers_stichera = [re.sub(r'\. Then.*?.*?:$','.',s) for s in vespers_stichera]
    vespers_stichera = ['<p class="stichera moveable">' + s + '</p>' for s in vespers_stichera] #HTML wrap
    #   ---
    vespers_theotokion = vespers_theotokion[:vespers_theotokion.find('Then “O Joyous Light ...”')] #clip off at instructions after in case prior search failed
    vespers_theotokion = vespers_theotokion.replace('\n','').strip() #remove line breaks and white space
    vespers_theotokion = re.sub(r'\Athe','The',vespers_theotokion) #capitalize The
    vespers_theotokion = '<p><i class="note moveable">' + vespers_theotokion.replace('on: ','on</i><br />').replace('tic:','tic</i><br />') + '</p>' #HTML formatting
    vespers_theotokion = vespers_theotokion.replace('in the same tone:','in the same tone</i><br />') #HTML formatting
    #   ---
    vespers_prokeimenon = re.sub(r'\nVouchsafe.*','',vespers_prokeimenon).strip() #remove service instructions after prokeimenon text
    vespers_prokeimenon = re.sub(r'^the','The',vespers_prokeimenon).strip() #capitalize The, remove white space
    vespers_prokeimenon = '<p class="note moveable">' + re.sub(r':\s\n','</p><p class="moveable">',vespers_prokeimenon) #HTML formatting
    vespers_prokeimenon = re.sub(r'\.\s\nVerse: ','</p><p class="moveable">Verse: ',vespers_prokeimenon) + '</p>' #HTML formatting
    #   ---
    vespers_aposticha = re.sub(r'Glory from the Menaion.*?$','',vespers_aposticha) #removes instructions
    vespers_aposticha = re.sub(r'^the','The',vespers_aposticha).strip() #capitalize The, remove white space
    vespers_aposticha = vespers_aposticha.replace('Tone VIII', 'Tone VIII:') #t8d2 typo
    vespers_aposticha = vespers_aposticha.replace('Tone VI ', 'Tone VI: ') #t6d4 typo
    vespers_aposticha = '<p class="moveable"><i class=note">' + re.sub(r'(:.\s\n|:.\n)','</i></p><p class="moveable"',vespers_aposticha) + '</p>' #HTML formatting first row
    vespers_aposticha = re.sub(r'\.\s\n','.</p><p class="moveable">',vespers_aposticha) #HTML formatting line breaks for stichera
    vespers_aposticha = vespers_aposticha.replace('\nVerse: ','</p><p class="moveable">Verse: ').replace('\n','') #HTML formatting line breaks for verses
    vespers_aposticha = vespers_aposticha.replace('To the Martyrs:','<i class="note">To the Martyrs:</i>') #HTML formatting
    vespers_aposticha = vespers_aposticha.replace('For the reposed:','<i class="note">For the reposed:</i>') #HTML formatting
    vespers_aposticha = vespers_aposticha.replace('Verse:','<i class="note">Verse:</i>') #HTML formatting
    #   ---
    vespers_apolytichion = vespers_apolytichion.replace('\n','').strip() #remove line breaks and white space
    vespers_apolytichion = re.sub(r'\Athe','The',vespers_apolytichion) #capitalize The
    vespers_apolytichion = '<p><i class="note moveable">' + vespers_apolytichion.replace('ion: ','ion</i><br />') + '</p>' #HTML formatting

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
tone = 3
sergius_day = 1
octoechos_url = f'http://www.st-sergius.org/services/oktiochos/{tone}-{sergius_day}.pdf'
octoechos = octoechos_variables(download_pdf(octoechos_url, 'octoechos'), sergius_day)
ss = octoechos.get('vespers').get('stichera')
for s in ss:
    print(f'{s}\n--------------------------------')
print(octoechos.get('vespers').get('theotokion'))
print('---------------')
print(octoechos.get('vespers').get('prokeimenon'))
print('---------------')
print(octoechos.get('vespers').get('aposticha'))
print('---------------')
print(octoechos.get('vespers').get('apolytichion'))
print('---------------')


#For multiples
tt = [1,2,3,4,5,6,7,8]
dd = [1,2,3,4,5,6,7]

# for t in tt:
#     for d in dd:
#         tone = t
#         sergius_day = d
#         octoechos_url = f'http://www.st-sergius.org/services/oktiochos/{tone}-{sergius_day}.pdf'
#         octoechos = octoechos_variables(download_pdf(octoechos_url, 'octoechos'), sergius_day)
#         print(f'---------------------------------\n{t}/{d}')
#         print(octoechos.get('vespers').get('apolytichion'))

        # ss = octoechos.get('vespers').get('stichera')
        # for s in ss:
        #     print(f'{s}')
