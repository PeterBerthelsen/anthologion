"""
Version 0.1.5
Updated 10/28/2021

Change Log:
10/8/2021 - 0.0.8 - Initial build, dictionary
10/28/2021 - 0.1.5 - started building vespers
"""
import os
import re
from _utils import process_pdf

menaion_class = {
    #general menaion classes
    #names correspond to .pdf file names (w/ typos)
    '1':'Theotokos'
    ,'2':'Cross'
    ,'3':'St John Baptist'
    ,'4':'Prophet'
    ,'5':'Angels'
    ,'6':'Apostle'
    ,'7':'Apostles'
    ,'8':'Heirarch'
    ,'9':'Heirarchs'
    ,'10':'Hieromartyr'
    ,'11':'Heiromartyrs'
    ,'12':'HieroConfessor'
    ,'13':'MonasticMartyr'
    ,'14':'MonasticMartyrs'
    ,'15':'Holy Fathers'
    ,'16':'Martyr'
    ,'17':'Martyrs'
    ,'18':'Martyress'
    ,'19':'Martyresses'
    ,'20':'Nun'
    ,'21':'Nuns'
    ,'22':'NunMartyr'
    ,'23':'Fools'
    ,'24':'Unmercenaries'
}

def menaion_vespers(service:str, name:str):
    """
    Formats vespers-specific service section and returns vespers parts dictionary
    """
    #Dictionary for Return
    vespers_parts = {}
    print(service.replace('\n', ' ')[:100])
    #still throwing error on Holy Fathers service....
    stichera_breakpoint = re.search(r'(On ["“]Lord[, ]+I have cried.*?|stichera),',service.replace('\n', ' '),flags=re.I)
    print(stichera_breakpoint)
    theotokion_breakpoint = re.search(r'glory[ .,]+now & ever[ .,]+',service,flags=re.I)
    first_reading_breakpoint = re.search(r'',service.replace('\n', ' '),flags=re.I)
    second_reading_breakpoint = re.search(r'',service.replace('\n', ' '),flags=re.I)
    third_reading_breakpoint = re.search(r'',service.replace('\n', ' '),flags=re.I)
    aposticha_breakpoint = re.search(r'',service.replace('\n', ' '),flags=re.I)
    apolytichion_breakpoint = re.search(r'',service.replace('\n', ' '),flags=re.I)

    stichera = service[stichera_breakpoint.start():theotokion_breakpoint.start()]
    vespers_parts['stichera'] = stichera

    return vespers_parts

def menaion_matins(service:str, name:str):
    return service

def menaion_liturgy(service:str, name:str):
    return service

def menaion_variables (input_string:str, name:str):
    """
    Uses string data from PDF to extract to generate menaion variables for services
    Text is divided at common breakpints from PDFs, then formatted for use.
    Returns list with variables at set index location.
    """

    matins_breakpoint = re.search(r'[A ]+[T ]+[M ]+[A ]+[T ]+[I ]+[N ]+[S ]+',input_string.replace('\n', ' '),flags=re.I)
    liturgy_breakpoint = re.search(r'[A ]+[T ]+[L ]+[I ]+[T ]+[U ]+[R ]+[G ]+[Y ]+',input_string.replace('\n', ' '),flags=re.I)
    vespers_service = input_string[:matins_breakpoint.start()]
    matins_service = input_string[matins_breakpoint.start():liturgy_breakpoint.start()]
    liturgy_service = input_string[liturgy_breakpoint.start():]

    payload = {
        'vespers': menaion_vespers(vespers_service,name)
        ,'matins': menaion_matins(matins_service,name)
        ,'liturgy': menaion_liturgy(liturgy_service,name)
    }

    return payload

#
# test = re.search(r'glory[., ]+now & ever[., ]+','Glory ..., Now & Ever ...,',flags=re.I)
# print(test)
with open('test.html', 'w') as f:
    for id, m in menaion_class.items():
        print(m)
        menaion = menaion_variables(process_pdf(filename=m, service='menaion'),name="testing")
        f.write(menaion.get('vespers').get('stichera'))
