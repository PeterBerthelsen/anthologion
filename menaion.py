"""
Version 0.1.5
Updated 10/28/2021

Change Log:
10/8/2021 - 0.0.8 - Initial build, dictionary
10/28/2021 - 0.1.5 - started building vespers
"""
import os
import re
from _utils import process_pdf, string_search

menaion_class = {
    #general menaion classes
    #names correspond to .pdf file names (w/ typos)
    '1':'Theotokos' #Mother of God
    ,'2':'Cross' #Holy Cross
    ,'3':'St John Baptist' #Forerunner
    ,'4':'Prophet' #Prphet
    ,'5':'Angels' #angels
    ,'6':'Apostle' #Apostle
    ,'7':'Apostles' #Several Apostles
    ,'8':'Heirarch' #Hierarch
    ,'9':'Heirarchs' #Several Hierarchs
    ,'10':'Hieromartyr' #hieromartyr
    ,'11':'Heiromartyrs' #several hieromartyrs
    ,'12':'HieroConfessor' #Confessor
    ,'13':'MonasticMartyr' #Male Ascetic
    ,'14':'MonasticMartyrs' #Several Male Ascetics
    ,'15':'Holy Fathers'
    ,'16':'Martyr' #Male Martyr
    ,'17':'Martyrs' #Several Male Martyrs
    ,'18':'Martyress' #Female Martyr
    ,'19':'Martyresses' #Several Female Martyrs
    ,'20':'Nun' #Female Ascetic
    ,'21':'Nuns' #Several Female Ascetics
    #,'22':'NunMartyr'
    ,'23':'Fools' #Fools
    ,'24':'Unmercenaries' #unmercenary healers
}

def menaion_vespers(service:str, name:str, service_type:str):
    """
    Formats vespers-specific service section and returns vespers parts dictionary
    """
    #Dictionary for Return
    vespers_parts = {'name': name}
    vespers_search = {
        'stichera': [
            'On “Lord, I have cried ...”, the Stichera,'
            ,'On “Lord, I have cried ...”,'
            ,'Lord, I have cried ...'
            ,'On “Lord'

        ]
        ,'doxastichon': [
            'If an Idiomelon be appointed, Glory ...,'
            ,'If an Idiomelion be appointed: Glory ...,'
            ,'If an Idiomelon be appointed. Glory ...,'
            ,'If an Idiomelon be appointed, Glory,'
            ,'Glory ..., in '
        ]
        ,'theotokion': [
            'Glory ..., Now & Ever ...,'
            ,'Glory ..., '
        ]
        ,'readings': [
            'The Entrance. The Prokeimenon of the day. The Three Lessons, if appointed.'
            ,'The Prokeimenon of the day. The Three Lessons if appointed: '
            ,'The Prokeimenon of the day. The Three Lessons, if appointed: '
            ,'The Prokeimenon of the day. The Three Lessons: '
            ,'The Prokeimenon of the day. The Three Lessons '
            ,'Prokeimenon of the day. Three Lessons. '
            ,'Three Lessons'
            ,'Prokeimenon of the day'
            ,'The Entrance.'
            ,'The readings for the Holy Fathers:'
        ]
        ,'aposticha': [
            'On the Aposticha, '
            ,'On the Aposticha'
        ]
        ,'aposticha2': [
            'The Troparion of the Festival from the Typicon.'
            ,'The Troparion from the Typicon.'
            ,'The Troparion,'
            ,'TTH' #St John Baptist 'THE TROPARIA' heading
            ,'The Troparion from the Typikon;'
            ,'The Troparion from the Typicon.'
            ,'Glory ..., Now & Ever ..., Theotokion or Stavrotheotokion'
            ,'If the celebration be with a Polyeleos'
            ,'The Dismissal'
            #,'Glory ..., Now & Ever ...,'
        ]
        ,'apolytichion': [
            'troparion'
            ,'Troparion'
        ]
        ,'apolytichion2': [
            '_______________________________________'
            ,'Glory ..., Now & Ever ..., Theotokion or Stavrotheotokion'
            ,'Glory ..., Now & Ever ..., Theotokion, or Stavrotheotokion'
            ,'The Dismissal'
        ]
    }

    service = re.sub(r'[(]name.*?[)]',name,service)

    #establish breakpoints
    stichera_beginning, stichera = string_search(service, vespers_search.get('stichera'),vespers_search.get('theotokion'))
    doxastichon_beginning, doxastichon = string_search(service, vespers_search.get('doxastichon'), vespers_search.get('readings'))
    theotokion_beginning, theotokion = string_search(service, vespers_search.get('theotokion'), vespers_search.get('readings'))
    readings_beginning, readings = string_search(service, vespers_search.get('readings'),vespers_search.get('aposticha'))
    aposticha_beginning, aposticha = string_search(service.replace('\n', ' '), vespers_search.get('aposticha'))
    aposticha2_beginning, aposticha2 = string_search(aposticha, vespers_search.get('aposticha2'))
    apolytichion_beginning, apolytichion = string_search(service,vespers_search.get('apolytichion'),vespers_search.get('apolytichion2'))
    print(doxastichon_beginning, theotokion_beginning, readings_beginning, aposticha_beginning, apolytichion_beginning)
    if theotokion_beginning > readings_beginning:
        #string_search grabbed later Glory ..., Now & Ever ..., and will cause a blank string
        theotokion_beginning = theotokion = None

    stichera = stichera[:stichera.find('If an Idiomelon be appointed,')] #excess text from Unmercenaries
    stichera = re.sub(r'(Spec\. Mel\.:.*?:)',r'\1|',stichera) #identify front matter
    stichera = re.sub(r'Verse:',r'|Verse:',stichera)
    stichera = re.sub(r'([.!][ ]*\n)',r'\1|',stichera) #identify end of line
    stichera = re.sub(r'[Gg]lory[ .,]{3,}.*',r'',stichera.replace('\n',' ')).split('|')
    stichera = [f'<p><i class="note">*</i>{s.strip()}</p>' for s in stichera] #add notes
    stichera_tone = stichera.pop(0) #separate tone notes
    stichera_tone = stichera_tone.replace('*</i>','') + '</i>'
    #additional formating, primarily for unique Holy Fathers service...
    for s in stichera:
        if s.find('Verse:') > 0:
            stichera.remove(s)
    for s in stichera:
        if s == '<p><i class="note">*</i></p>':
            stichera.remove(s)
    for s in stichera:
        if s[-8:] == '...,</p>':
            stichera.remove(s)
    vespers_parts['stichera'] = stichera
    vespers_parts['stichera_tone'] = stichera_tone

    if doxastichon_beginning > 0: #if a doxastichon exists...
        dogmaticon = doxastichon[doxastichon.find('Dogmatic '):] #dogmaticon is held in doxastichon variable
        doxastichon = '<p>' + doxastichon[:doxastichon.find('If the Celebration')].strip() + '</p>' #remove polyeleos notes
        doxastichon = re.sub (r'Now & Ever[ .,]+.*',r'',doxastichon.replace('\n', ' '),flags=re.I) #remove end matter
        doxastichon = re.sub(r'((in Tone|Tone) [VI]+:)',r'<i class="note">Doxastichon, \1</i></p><p>',doxastichon) #formatting
        vespers_parts['doxastichon'] = doxastichon

        dogmaticon = '<p>' + re.sub(r' [(].*[)]:.*?:',r':</p><p>',dogmaticon.replace('\n',' ')) + '</p>'
        dogmaticon = re.sub(r'(Dogmatic.*?:)',r'<i class="note">\1</i>',dogmaticon)
        dogmaticon = re.sub(r'[Tt]he [Ee]ntrance.*',r'',dogmaticon)
        if service_type != 'Holy Fathers': #no dogmaticon defined in Holy Fathers Service
            vespers_parts['dogmaticon'] = dogmaticon


    if theotokion:
        theotokion = theotokion[:theotokion.find('If an Idiomel')]
        theotokion = re.sub(r'.*?([a-z]*theotokion.*?:|in tone [vi]+:)'
            ,r'</p><p><i class="note">\1</i></p><p>',theotokion.strip(),flags=re.I) + '</p>'
        vespers_parts['theotokion'] = theotokion


    readings = re.sub(r'\n([^a-z]+)\s*\n',r'</p><h3>\1</h3><p>',readings)
    readings = re.sub(r'At the Litiya.*',r'',readings.replace('\n',' '))
    vespers_parts['readings'] = readings

    aposticha = aposticha.replace('these Stichera','These Stichera').replace('the Stichera', 'These Stichera')
    aposticha = aposticha[:aposticha2_beginning if aposticha2_beginning > 0 else -1]
    aposticha = '<p>' + re.sub(r'(These Stichera.*?:|Spec\. Mel.:.*?[:”"]+)',r'</p><i class=note">\1</i></p><p>',aposticha) + '</p>'
    aposticha = re.sub(r'(Verse:)(.*?\*.*?[.!])',r'</p><p><i class="note">\1</i>\2</p><p>',aposticha.replace('\n',' '))
    aposticha = re.sub(r'(Glory[ .,]+Now & Ever[ .,]+)',r'</p><p>\1</p><p>',aposticha,flags=re.I)
    aposticha = re.sub(r'((?<!Glory ..., )Now & Ever[ .,]+)',r'</p><p>\1',aposticha,flags=re.I)
    aposticha = re.sub(r'(Glory ..., (?!Now & Ever ...,))',r'</p><p>\1',aposticha,flags=re.I)
    aposticha = re.sub(r'([a-z]*theotokion.*?:)',r'</p><p><i class="note">\1</i>',aposticha,flags=re.I)
    aposticha = re.sub(r'(in Tone [VI]+.*?:|in the same tone and melody:)',r'<i class="note">\1</i></p><p>',aposticha,flags=re.I)
    polyeleos_aposticha = re.sub(r'(<p>\s*If the Celebration.*?Otherwise[,]?)',r'\1',aposticha,flags=re.I) #may need this later...
    aposticha = re.sub(r'<p>\s*If the Celebration.*?Otherwise[,]?',r'',aposticha,flags=re.I) #celebration as its own paragraph
    aposticha = re.sub(r'\s*If the Celebration.*?Otherwise[,]?',r'</p><p>Now & Ever ...,',aposticha,flags=re.I) #celebration at end of paragraph
    aposticha = re.sub(r'(Glory[ .,]+ in Tone [VI]+.*?sing the following:)',r'',aposticha,flags=re.I)
    aposticha = re.sub(r'(The Troparion|Troparion).*',r'',aposticha)
    aposticha_theotokion_location = re.search(r'Glory[ .,]{3,}',aposticha)
    aposticha_theotokion = aposticha[aposticha_theotokion_location.start():]
    aposticha = aposticha[:aposticha_theotokion_location.start()]
    if service_type != 'Holy Fathers': #Holy Fathers uses Octoechos aposticha
        vespers_parts['aposticha'] = aposticha
    vespers_parts['aposticha_theotokion'] = aposticha_theotokion



    apolytichion = '<p>Troparion' + re.sub(
        r'(of the Festival|[(]Also for the Beheading[)]|of the venerable nun-martyr|from the (Typicon|Typikon)).*?,*([, ]{0,2}in Tone [VI]+:)'
        ,r'\3</i>',apolytichion.replace('\n',' '),flags=re.I) + '</p>'
    apolytichion = re.sub(r'(Troparion.*?:)',r'<i class="note">\1</i>',apolytichion)
    apolytichion = apolytichion.replace('the Theotokion','Theotokion')
    apolytichion = re.sub(r'(Glory[ .,]{3,}Now & Ever[ .,]+)',r'</p><p>\1</p><p>',apolytichion)
    apolytichion = re.sub(r'(Theotokion.*?:)',r'<i class="note">\1</i>',apolytichion)
    apolytichion = apolytichion.replace('(Thrice)', '<i class="note">Thrice.</i>')
    vespers_parts['apolytichion'] = apolytichion

    return vespers_parts

def menaion_matins(service:str, name:str, service_type:str):
    """
    Formats matins-specific service section and returns matins parts dictionary
    """
    #Dictionary for Return
    matins_parts = {}

    #Establish Matins breakpoints
    matins_search = {
        'troparion': [
            'On “God is the Lord ...”, '
            ,'for God is the Lord, '
            ,'On “God is the Lord”, '
        ]
        ,'session1': [
            'After the 1st chanting of the Psalter, '
        ]
        ,'session2': [
            'After the 2nd chanting of the Psalter, '
        ]
        ,'megalynarion': [
            'After the Polyeleos, The Megalynarion:'
            ,'The Megalynarion'
        ]
        ,'session3': [
            'After the 3rd chanting of the Psalter'
            ,'After the Polyeleos, the Sessional Hymn'
        ]
        ,'ascent': [
            'The Songs of Ascent:'
            ,'Songs of Ascent'
        ]
        ,'prokeimenon': [
            'The Prokeimenon'
            ,'Prokeimenon'
        ]
        ,'readings': [
            'Let Every breath ...,'
            ,'Let every breath ...,'
            ,'Let every breath.'
        ]
        ,'after50': [
            'After the 50th Psalm:'
        ]
        ,'canon': [
            'The Canon,'
            'The Canon'
        ]
        ,'exapostilarion': [
            'Exapostilarion '
        ]
        ,'praises': [
            'On the Praises, '
        ]
        ,'apolytichion': [
            'After Our Father .., '
            ,'if there is no Typicon sing the following:'

        ]

    }

    #establish breakpoints
    troparion_beginning, troparion = string_search(service, matins_search.get('troparion'), matins_search.get('session1'))
    session1_beginning, session1 = string_search(service, matins_search.get('session1'), matins_search.get('session2'))
    session2_beginning, session2 = string_search(service, matins_search.get('session2'), matins_search.get('megalynarion'))
    megalynarion_beginning, megalynarion = string_search(service, matins_search.get('megalynarion'), matins_search.get('session3'))
    session3_beginning, session3 = string_search(service, matins_search.get('session3'), matins_search.get('ascent'))
    ascent_beginning, ascent = string_search(service, matins_search.get('ascent'), matins_search.get('prokeimenon'))
    prokeimenon_beginning, prokeimenon = string_search(service, matins_search.get('prokeimenon'), matins_search.get('readings'))
    readings_beginning, readings = string_search(service, matins_search.get('readings'), matins_search.get('after50'))
    after50_beginning, after50 = string_search(service, matins_search.get('after50'), matins_search.get('canon'))
    canon_beginning, canon = string_search(service, matins_search.get('canon'), matins_search.get('exapostilarion'))
    exapostilarion_beginning, exapostilarion = string_search(service, matins_search.get('exapostilarion'), matins_search.get('praises'))
    praises_beginning, praises = string_search(service, matins_search.get('praises'), matins_search.get('apolytichion'))
    apolytichion_beginning, apolytichion = string_search(service, matins_search.get('apolytichion'))
    print(name, troparion_beginning)

    return matins_parts

def menaion_liturgy(service:str, name:str, service_type:str):
    return service

def menaion_variables (input_string:str, name:str, service_type:str):
    """
    Uses string data from PDF to extract to generate menaion variables for services
    Text is divided at common breakpints from PDFs, then formatted for use.
    Returns list with variables at set index location.
    """

    #breakpoints needed modification. Each letter paired with space triggered matches on 6+ spaces in wrong places.
    matins_breakpoint = re.search(r'[A]+[T]+[ ]{1,2}[M ]+[A]+[T]+[I]+[N ]+[S ]+',input_string.replace('\n', ' '),flags=re.I)
    liturgy_breakpoint = re.search(r'[A ]+[T ]+[L ]+[I]+[T]+[U]+[R]+[G ]+[Y ]+',input_string.replace('\n', ' '),flags=re.I)
    vespers_service = input_string[:matins_breakpoint.start()]
    matins_service = input_string[matins_breakpoint.start():liturgy_breakpoint.start()]
    liturgy_service = input_string[liturgy_breakpoint.start():]

    payload = {
        'vespers': menaion_vespers(vespers_service,name,service_type)
        ,'matins': menaion_matins(matins_service,name,service_type)
        ,'liturgy': menaion_liturgy(liturgy_service,name,service_type)
    }

    return payload

#
# test = re.search(r'glory[., ]+now & ever[., ]+','Glory ..., Now & Ever ...,',flags=re.I)
# print(test)
if __name__=='__main__':
    with open('test.html', 'w') as f:
        for id, m in menaion_class.items():
            #if m == 'Holy Fathers':
            f.write(f'<h2>{m}</h2>')
            menaion = menaion_variables(process_pdf(filename=m, service='menaion'),name=m)
            #f.write(menaion.get('matins').get(''))

            # for s in menaion.get('vespers').get('stichera'):
            #     f.write(s.replace('О','O') + '\n')
            # #Compare these with Anthologion later for confirmation!!!
            # if menaion.get('vespers').get('doxastichon'):
            #     f.write('<h3>Doxastichon</h3>')
            #     f.write(menaion.get('vespers').get('doxastichon').replace('О','O')) #cyrillic character...
            # if menaion.get('vespers').get('dogmaticon'):
            #     f.write('<h3>Dogmaticon</h3>')
            #     f.write(menaion.get('vespers').get('dogmaticon').replace('О','O')) #cyrillic character...
            # if menaion.get('vespers').get('theotokion'):
            #     f.write('<h3>Theotokion</h3>')
            #     f.write(menaion.get('vespers').get('theotokion').replace('О','O')) #cyrillic character...
            # f.write(menaion.get('vespers').get('readings'))
            # f.write(menaion.get('vespers').get('aposticha'))
            # f.write(menaion.get('vespers').get('aposticha_theotokion'))
            # f.write(menaion.get('vespers').get('apolytichion'))
