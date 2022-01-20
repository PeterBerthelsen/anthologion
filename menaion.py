"""
Version 0.1.8
Updated 11/7/2021

Change Log:
10/8/2021   - 0.0.8 - Initial build, dictionary
10/28/2021  - 0.1.5 - started building vespers
11/5/2021   - 0.1.7 - finished vespers and matins
11/7/2021   - 0.1.8 - finished typika
"""
import os
import re
from _utils import process_pdf, string_search
from hymns import forerunner_troparia, forerunner_megalynaria, forerunner_kontakia, daily_compline_troparia

menaion_class = {
    #general menaion classes
    #names correspond to .pdf file names (w/ typos)
    '0': 'Master'
    ,'1':'Theotokos' #Mother of God
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

def menaion_vespers(service:str, name:str, service_type:str, weekday:int):
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

    #establish breakpoints
    stichera_beginning, stichera = string_search(service, vespers_search.get('stichera'),vespers_search.get('theotokion'))
    doxastichon_beginning, doxastichon = string_search(service, vespers_search.get('doxastichon'), vespers_search.get('readings'))
    theotokion_beginning, theotokion = string_search(service, vespers_search.get('theotokion'), vespers_search.get('readings'))
    readings_beginning, readings = string_search(service, vespers_search.get('readings'),vespers_search.get('aposticha'))
    aposticha_beginning, aposticha = string_search(service.replace('\n', ' '), vespers_search.get('aposticha'))
    aposticha2_beginning, aposticha2 = string_search(aposticha, vespers_search.get('aposticha2'))
    apolytichion_beginning, apolytichion = string_search(service,vespers_search.get('apolytichion'),vespers_search.get('apolytichion2'))
    #print(doxastichon_beginning, theotokion_beginning, readings_beginning, aposticha_beginning, apolytichion_beginning)

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
    #should probably redo this. removing while iterating is bad...works for this single use, though.
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

def menaion_matins(service:str, name:str, service_type:str, weekday:int):
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
            ,'After the 1st Kathisma, '
        ]
        ,'session2': [
            'After the 2nd chanting of the Psalter, '
            ,'After the 2nd Kathisma, '
        ]
        ,'megalynarion': [
            'After the Polyeleos, The Megalynarion:'
            ,'After the Polyeleos'
            ,'The Megalynarion'
        ]
        ,'session3': [
            'After the 3rd chanting of the Psalter'
            ,'After the Polyeleos, the Sessional Hymn'
            ,'After the Polyeleos the Sessional Hymn'
        ]
        ,'ascent': [
            'The Songs of Ascent:'
            ,'The Song of Ascents:'
            ,'Songs of Ascent'
        ]
        ,'prokeimenon': [
            'Prokeimenon'
            ,'The Prokeimenon'
        ]
        ,'readings': [
            'Let Every breath ...,'
            ,'Let every breath ...,'
            ,'Let every breath.'
            ,'THE GOSPEL ACCORDING TO '
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
            ,'On the Aposticha' #unmercenaries has this??
        ]
        ,'apolytichion': [
            'Doxology'
            ,'After Our Father .., '
            ,'if there is no Typicon sing the following:'

        ]

    }

    #establish breakpoints
    troparion_beginning, troparion = string_search(service, matins_search.get('troparion'), matins_search.get('session1'))
    session1_beginning, session1 = string_search(service, matins_search.get('session1'), matins_search.get('session2'))
    session2_beginning, session2 = string_search(service, matins_search.get('session2'), matins_search.get('megalynarion'),session1_beginning)
    megalynarion_beginning, megalynarion = string_search(service, matins_search.get('megalynarion'), matins_search.get('session3'),session2_beginning)
    session3_beginning, session3 = string_search(service, matins_search.get('session3'), matins_search.get('ascent'))
    ascent_beginning, ascent = string_search(service, matins_search.get('ascent'), matins_search.get('prokeimenon'))
    prokeimenon_beginning, prokeimenon = string_search(service, matins_search.get('prokeimenon'), matins_search.get('readings'))
    readings_beginning, readings = string_search(service, matins_search.get('readings'), matins_search.get('after50'))
    after50_beginning, after50 = string_search(service, matins_search.get('after50'), matins_search.get('canon'))
    exapostilarion_beginning, exapostilarion = string_search(service, matins_search.get('exapostilarion'), matins_search.get('praises'))
    praises_beginning, praises = string_search(service, matins_search.get('praises'), matins_search.get('apolytichion'))
    if exapostilarion_beginning == 0: #for some reason exapostilarion and canon searches do not work with string_search.
        try: #using custom logic for these...
            exapostilarion_beginning = re.search(r'Exapostilarion',service,flags=re.I).start()
            exapostilarion = service[exapostilarion_beginning:praises_beginning]
        except:
            exapostilarion_beginning = 0
    canon_beginning = re.search(r'(The Canon|Canon)',service,flags=re.I).start()
    canon = service[canon_beginning:exapostilarion_beginning]
    apolytichion_beginning, apolytichion = string_search(service, matins_search.get('apolytichion'))

    #print(service_type, exapostilarion_beginning, praises_beginning, apolytichion_beginning)

    if service_type == 'St John Baptist':
        troparion = forerunner_troparia.get(name, None)
        if not troparion:
            troparion = forerunner_troparia.get('The General Troparion')
        matins_parts['troparion'] = troparion
    else:
        troparion = re.sub(r'the (Troparion.*?:)',r'<p><i class="note">The \1</i></p><p>',troparion)
        troparion = re.sub(r' of the Resurrection .*?Glory ...',r'',troparion) #Holy Fathers anomoly
        troparion = re.sub(r'(Glory[ .,]+Now & Ever[ .,]+|Now & Ever[ .,]+).*',r'</p>',troparion.replace('\n',' '),flags=re.I)
        troparion = re.sub(r'[(]Twice[)]',r'<i class="note">Twice.</i>',troparion)
        matins_parts['troparion'] = troparion

    if service_type == 'Holy Fathers':
        matins_parts['session1'] = None
        matins_parts['session2'] = None
        matins_parts['session3'] = None
        matins_parts['megalynarion'] = None
        matins_parts['ascent'] = None
        matins_parts['prokeimenon'] = None
        matins_parts['readings'] = None
        matins_parts['after50'] = None
    else:
        session1 = re.sub(r'^the Sessional Hymn[ .,:]',r'The Sessional Hymn ',session1) #capitalize
        session1 = re.sub(r'(The Sessional.*?:|Spec[. ]+Mel[. ]+:.*?:|[a-zA-Z]*heotokion.*?:)',r'</p><p><i class="note">\1</i></p><p>',session1) #note sections
        session1 = re.sub(r'[(]Twice[)]',r'<i class="note">Twice</i>.</p><p>',session1) #notes for 'twice'
        session1 = re.sub(r'(.*)(the foregoing is repeated).*',r'\1</p><p><i class="note">(\2)</i></p>',session1.replace('\n',' '))

        matins_parts['session1'] = session1

        session2 = re.sub(r'^the Sessional Hymn[ .,:]',r'The Sessional Hymn ',session2) #capitalize
        session2 = re.sub(r'(The Sessional.*?:|Spec[. ]+Mel[. ]+:.*?:|[a-zA-Z]*heotokion.*?:)',r'</p><p><i class="note">\1</i></p><p>',session2) #note sections
        session2 = re.sub(r'[(]Twice[)]',r'<i class="note">Twice</i>.</p><p>',session2) #notes for 'twice'
        session2 = re.sub(r'(.*)(the foregoing is repeated).*',r'\1</p><p><i class="note">(\2)</i></p>',session2.replace('\n',' '))
        session2 = re.sub(r'After Praise ye the name of the Lord.*',r'',session2) #end matter on St John Baptist
        matins_parts['session2'] = session2

        #Need logic here to handle St John Baptist megalynaria...
        #
        #
        megalynarion = re.sub(r'^[ ,]+the (Megalynarion:)',r'<p><i class="note">\1</i></p><p>',megalynarion.replace('\n',' '))
        megalynarion = re.sub(r'(Verse:)',r'</p><p><i class="note">\1</i>',megalynarion)
        matins_parts['megalynarion'] = megalynarion

        session3 = 'The Sessional Hymn' + session3[1:]
        session3 = re.sub(r'(The Sessional.*?:|Spec[. ]+Mel[. ]+:.*?:|[a-zA-Z]*heotokion.*?:)',r'</p><p><i class="note">\1</i></p><p>',session3) #note sections
        session3 = re.sub(r'[(]Twice[)]',r'<i class="note">Twice</i>.</p><p>',session3) #notes for 'twice'
        session3 = re.sub(r'((?<!<p>)Glory ..., Now & Ever ...,)',r'</p><p>\1',session3)
        session3 = re.sub(r'(.*)(the foregoing is repeated).*',r'\1</p><p><i class="note">(\2)</i></p>',session3.replace('\n',' '))
        session3 = re.sub(r'([Ii]f of Polyeleos|If not a Resurrection).*',r'',session3) #end matter, clipping into ascents
        matins_parts['session3'] = session3

        ascent = ascent.replace(', First Antiphon', '') #Unmercenaries typo
        ascent = re.sub(r'^.*(in Tone [VI]+:)',r'<p><i class="notes">The Song of Ascent, First Antiphon \1</i></p><p>',ascent)
        ascent = re.sub(r'(Glory[ .,]+Now & Ever[ .,]+)',r'</p><p>\1</p><p>',ascent)
        ascent = re.sub(r'Prokeimenon.*',r'',ascent.replace('\n',' '))
        matins_parts['ascent'] = ascent

        prokeimenon = re.sub(r'^.*(Tone [VI]+:)',r'<p><i class="note">The Prokeimenon in \1</i></p><p>',prokeimenon.replace('\n',' '))
        prokeimenon = re.sub(r'[ ]*The Prokeimenon:[ ]*',r'',prokeimenon,flags=re.I)
        prokeimenon = re.sub(r'(Verse:)',r'</p><p><i class="note">\1</i>',prokeimenon) + '<p>'
        matins_parts['prokeimenon'] = prokeimenon

        readings = re.sub(r'^ST',r'THE GOSPEL ACCORDING TO ST',readings) #Nun/Nuns search cuts this
        readings = '<h3>' + re.sub(r'([)][ .]*)',r'\1</h3><p>',readings.replace('\n',' ')) + '</p>'
        matins_parts['readings'] = readings

        after50 = re.sub(r'The Canon.*',r'',after50.replace('\n',' '))
        after50 = after50.replace('Sessional Hymn:','Sessional Hymn,') #theotokos typo
        after50 = after50.replace('Or for many','Sessional Hymn, For Several Angels') #angels conditional
        after50 = after50.replace('. In Tone VI','</p><p>The Sessional Hymn, in Tone VI') #apostle typo
        after50 = re.sub(r'(Then the|the| )[ ]*(Sessional Hymn.*?:)',r'</p><p><i class="note">The \2</i></p><p>',after50)
        after50 = re.sub(r'(Now & Ever)',r'</p><p>\1',after50)
        after50 = re.sub(r'([Ii]n Tone [VI]+:)',r'<i class="note">\1</i>',after50)
        matins_parts['after50'] = after50

        apolytichion = apolytichion.replace('(Also for the Beheading)','') #St John Baptist header
        apolytichion = re.sub(r'.*?(troparion.*?:)',r'</p><p><i class="note">\1</i></p><p>',apolytichion,flags=re.I|re.S)
        apolytichion = re.sub(r'</p><p><i class="note">(Troparion is sung after the Doxology:|Troparion for the feast [(]from above[)] or else:)</i></p><p>',r'',apolytichion,flags=re.S) #unmercenaries typo
        apolytichion = re.sub(r'(Glory[ .,]{3,}Now & Ever[ .,]+.*|The Dismissal.*)',r'</p>',apolytichion,flags=re.I|re.S)
        matins_parts['apolytichion'] = apolytichion

    #the rest of the parts are in all services
    canon = canon.replace('Thou that wast of Thine own will ...”.', 'Thou that wast of Thine own will ...”:') #Cross Ode 6 typo
    canon = re.sub(r'(O\s*O\s*D\s*D\s*E\s*E\s*|О\s*О\s*D\s*D\s*E\s*E\s*)\s+([XVI]+)\s+',r'</p><h3>Ode \2</h3><p>',canon) #Ode headers
    canon = re.sub(r'^(.*[Aa]crostic.*)\n',r'\1',canon,flags=re.M)#removes line breaks from lengthy titles for capture below
    canon = re.sub(r'^(.*[Aa]crostic.*)\n',r'\1',canon,flags=re.M)#removes line breaks from REALLY lengthy titles for capture below
    canon = re.sub(r'\([Tt]wice[.]?\)',r'<i class="note">Twice.</i></p><p>',canon)
    canon = re.sub(r', and make prostrations.', r'<i class="note"> Prostrations.</i>',canon)
    canon = re.sub(r'(The Kontakion|Kontakion).*?from the Typi[ck]on.*?following[:,]',r'',canon,flags=re.S|re.I)
    canon = re.sub(r'(Trinitarion:|Katavasia.*?:|The Canon.*?:|(The | )Sessional Hymn.*?:|(The K|K)ontakion.*?:|Refrain:|(The [a-z]*|[a-z]*)Theotokion.*?:|(The I|I)kos:|Spec[ .]+Mel[. :]+.*?:|Verse:|\n\s*Another[ ,].*?:)'
                        ,r'</p><p><i class="note">\1</i>',canon,flags=re.I|re.S) + '</p>'#service notes
    canon = re.sub(r'[Ii]rmos:',r'</p><p><i class="note">Irmos:</i>',canon)
    canon = re.sub(r'(?<!<p>)(Glory [.,]{3,})',r'<p>\1',canon)
    canon = re.sub(r'(Glory[ .,]{3,}Now & Ever[ .,]+)(the same.|the foregoing is repeated.)',r'\1</p><p><i class="note">the foregoing is repeated.</i>',canon,flags=re.I)
    #Need logic here to handle St John Baptist Kontakia
    if service_type == 'St John Baptist':
        canon = re.sub(r'THE KONTAKIA.*[*] O wise Baptist of Christ, save us all.\s*',r'<<KONTAKIA HERE>>',canon,flags=re.I|re.S)
        canon = canon.replace('<<KONTAKIA HERE>>',forerunner_kontakia.get(name, ''))
    canon = canon.replace('XX','X').replace('VV','V').replace('II','I') #Remove duplicate Ode Roman Numerals
    canon = re.sub(r'Then, [“"].*','',canon.replace('\n','')) #remove excess after canon
    matins_parts['canon'] = canon

    exapostilarion = re.sub(r'^(?<!Exapostilarion )(in Tone [VI]+:)',r'Exapostilarion \1',exapostilarion,flags=re.I)
    exapostilarion = re.sub(r'(Exapostilarion.*?:)',r'<i class="note">\1</i></p><p>',exapostilarion,flags=re.I)
    exapostilarion = re.sub(r'(Glory[ .,]{3,}Now & Ever[ .,]+)',r'</p><p>\1',exapostilarion,flags=re.I)
    exapostilarion = re.sub(r'(spec[. ]+mel[. ]+:.*?:|[a-z]*theotokion.*?:)',r'</p><p><i class="note">\1</i>',exapostilarion,flags=re.I)
    exapostilarion = '<p>' + exapostilarion + '</p>'
    matins_parts['exapostilarion'] = exapostilarion

    #Praises.. individual stichera!?
    #For now, just use octoechos..
    #
    #
    matins_parts['praises'] = praises

    return matins_parts

def menaion_liturgy(service:str, name:str, service_type:str, weekday:int):
    """
    Formats liturgy-specific service section and returns matins parts dictionary
    """
    #Dictionary for Return
    liturgy_parts = {}

    #Establish Matins breakpoints
    liturgy_search = {
        'beatitudes': [
            'Typika and Beatitudes'
            ,'On the Beatitudes'
            ,'Beatitudes'
        ]
        ,'troparion': [
            'The Troparion, in Tone'
            ,'Troparion'
        ]
        ,'kontakion': [
            'The Kontakion, in Tone'
            ,'Kontakion'
        ]
        ,'prokeimenon': [
            'The Prokeimenon'
            ,'Prokeimenon'
        ]
    }

    service = re.sub(r'Troparion.*?Kontakion.*?Typicon.*?:',r'',service,flags=re.S|re.I) #remove Troparion/Kontakion header to give valid search results
    beatitudes_beginning, beatitudes = string_search(service,liturgy_search.get('beatitudes'),liturgy_search.get('troparion'))
    troparion_beginning, troparion = string_search(service,liturgy_search.get('troparion'),liturgy_search.get('kontakion'))
    kontakion_beginning, kontakion = string_search(service,liturgy_search.get('kontakion'),liturgy_search.get('prokemenon'))
    prokeimenon_beginning, prokeimenon = string_search(service,liturgy_search.get('prokeimenon'))
    beatitudes = re.sub(r'\A\s*([.]\s*|[,].*?:\s*)([a-zA-Z])',r'\2',beatitudes,flags=re.S) #front matter
    beatitudes = re.sub(r'\A.*?ODE VI.*?\n',r'',beatitudes) #fools, front matter
    #beatitudes = re.sub(r'',r'',beatitudes,flags=re.I|re.S)
    beatitudes = re.sub(r'([.])\s*\n',r'\1|',beatitudes,re.S)
    beatitudes = re.sub(r'[(]Twice[)]',r'<i class="note">|the foregoing is repeated.</i>|',beatitudes)
    beatitudes = re.sub(r'([a-zA-Z]*Theotokion)',r'<i class="note">\1</i>',beatitudes,flags=re.I|re.S)
    beatitudes = re.sub(r'|(\s*The\s*\Z|TROPARIA.*)',r'',beatitudes,flags=re.S|re.M)
    #errant line splits:
    beatitudes.replace('||','|') #double breaks (happen on a few occurences of "(Twice)")
    beatitudes = re.sub(r'[|]Illumine', ' Illumine', beatitudes) #theotokos, period @ EOL

    beatitudes = ['<p>' + b + '</p>' for b in beatitudes.split('|')]
    liturgy_parts['beatitudes'] = beatitudes

    if service_type == 'St John Baptist':
        liturgy_parts['troparion'] = forerunner_troparia.get(name,'')
        liturgy_parts['kontakion'] = forerunner_kontakia.get(name,'')
    else:
        troparion = re.sub(r'(^.*?:)',r'<p><i class="note">Troparion\1</i></p><p>',troparion) + '</p>'
        liturgy_parts['troparion'] = troparion
        kontakion = re.sub(r'(^.*?:)(.*?)Prokeimenon.*',r'<p><i class="note">Kontakion\1</i></p><p>\2</p>',kontakion,flags=re.S)
        liturgy_parts['kontakion'] = kontakion

    prokeimenon = re.sub(r'(Tone [VI]+),',r'\1:',prokeimenon) #fools/unmercenaries typo
    prokeimenon = prokeimenon.replace('of the Fathers:','of the Fathers,') #Holy Fathers formatting
    prokeimenon = prokeimenon.replace('(Psalm 15:3, 8)','') #unmercenaries formatting
    prokeimenon = re.sub(r'(^.*?:)(.*?)[A-Z ]{5,}.*',r'<p><i class="note">Prokeimenon\1</i></p><p>\2',prokeimenon,flags=re.S)
    prokeimenon = re.sub(r'Verse:',r'</p><p><i class="note">Verse:</i>',prokeimenon)
    prokeimenon = re.sub(r'THE [0-9].*',r'',prokeimenon) #end matter, clipping on ordinal titles for readings
    liturgy_parts['prokeimenon'] = prokeimenon

    readings_beginning = re.search(r'(THE READING|THE EPISTLE|THE 1st EPISTLE|THE 2nd EPISTLE|THE FIRST EPISTLE|THE SECOND|THE ACTS)',service,flags=re.I)
    readings = service[readings_beginning.start():]
    readings = readings.replace('(and are)','and are') #close paren at EOL in Apostle
    readings = readings.replace('behind (him)','behind him') #Nuns Gospel reading
    readings = re.sub(r'(in Tone [VI]+),',r'\1:',readings,flags=re.I|re.S) #fools typo
    readings = '<h3>' + re.sub(r'[)][.]*\s*\n',r')</h3><p>',readings,flags=re.S)
    readings = re.sub(r'(GOSPEL|THE GOSPEL|THE HOLY GOSPEL)',r'<h3>\1',readings) + '</p>'
    readings = re.sub(r'(The Communion|Communion) .*',r'',readings,flags=re.S)
    readings = re.sub(r'(Alleluia.*?:|Verse:)',r'</p><p><i class="note">\1</i>',readings,flags=re.I|re.S)
    liturgy_parts['readings'] = readings
    return liturgy_parts

def menaion_variables (input_string:str, name:str, service_type:str, weekday:int):
    """
    Uses string data from PDF to extract to generate menaion variables for services
    Text is divided at common breakpints from PDFs, then formatted for use.
    Returns list with variables at set index location.
    """
    #Insert name variable into service / gather variables for master service
    if service_type == 'Master':
        source = {
            'vespers': master_vespers
            ,'matins': master_matins
            ,'liturgy': master_liturgy
        }
        payload = {
            'vespers': {}
            ,'matins': {}
            ,'liturgy': {}
        }
        for service, variables in source.items():
            #each service from source...
            for part, text in variables.items():
                #each variable within the service from source
                if type(text) == list:
                    l = []
                    for t in text:
                        i = re.sub(r'[(]name.*?[)]',f'<i class="name">{name}</i>',t,flags=re.S)
                        l.append(i)
                    payload[service][part] = l
                elif type(text) == str:
                    i = re.sub(r'[(]name.*?[)]',f'<i class="name">{name}</i>',text,flags=re.S)
                    payload[service][part] = i
        payload['matins']['troparion'] = daily_compline_troparia.get(weekday)
        return payload
    else:
        input_string = re.sub(r'[(]name.*?[)]',f'<i class="name">{name}</i>',input_string,flags=re.S)
        input_string = input_string.replace('О', 'O') #replace known cyrillic chracter \u041e which throws error

    #breakpoints needed modification. Each letter paired with space triggered matches on 6+ spaces in wrong places.
    matins_breakpoint = re.search(r'[A]+[T]+[ ]{1,2}[M ]+[A]+[T]+[I]+[N ]+[S ]+',input_string.replace('\n', ' '),flags=re.I)
    liturgy_breakpoint = re.search(r'[A ]+[T ]+[L ]+[I]+[T]+[U]+[R]+[G ]+[Y ]+',input_string.replace('\n', ' '),flags=re.I)
    vespers_service = input_string[:matins_breakpoint.start()]
    matins_service = input_string[matins_breakpoint.start():liturgy_breakpoint.start()]
    liturgy_service = input_string[liturgy_breakpoint.start():]

    payload = {
        'vespers': menaion_vespers(vespers_service,name,service_type,weekday)
        ,'matins': menaion_matins(matins_service,name,service_type,weekday)
        ,'liturgy': menaion_liturgy(liturgy_service,name,service_type,weekday)
    }

    return payload


master_vespers = {
    'stichera_tone': '<p><i class="note">The Stichera, in Tone VI: Spec. Mel.: "O Lord, the grave of Lazarus..."</i></p>'
    ,'stichera': [
        '<p><i class="note">*</i>Thou, O Lord, that dost fill up every thing with Thy Divinity and through Thy clemency hast united Thyself unto men, one of the two natures being invisible, hast become visible after Thy coming out of the pure one and dost shew the image of Thy bodily form in Thy (name of the event) ; thereunto having come we adore Thee, O Master, and knowing Thee as the Maker, we pray: Blessed art Thou, O Saviour, have mercy upon us.</p>'
        ,'<p><i class="note">*</i>O Lord, the incomprehensible mystery of Thine economy which was forecast from the beginning, Thou dost in Thy coming make known and in assurance thereof hast Thou shewn unto the world Thy divine (name of the event); Thou hast filled everything with joy and renewed afresh the nature of man, desiring to save him: Blessed art Thou, O God, have mercy upon us.</p>'
        ,'<p><i class="note">*</i>O Lord, most glorious is the condescension of Thy compassion! Dwelling on high in the bosom of the Father as indescribable and incomprehensible, on Thy coming to the earth-born Thou wast seen now; wherefore we honour Thy festival (name of the event), that Thou mayest deliver us from passions who on account of it honour Thee, the Master, that hast revivified us from death through sins. Blessed art Thou, O Saviour, have mercy upon us.</p>'
        ,'<p><i class="note">*</i>O Lord, Thou didst become incarnate as Thou desiredst, having been pleased to show both our indigence and abundance of Thy compassion, whereby Thou hast deified me-the earth. We glorify Thee, O Lover of man, seeing the example of Thine economy in Thy (name of the event). Do grant therewithal unhindered entry into Eden unto Thy servants, overlooking all their sins.</p>'
    ]
    ,'theotokion': '<p><i class="note">Thetokion in Tone VIII:</i></p><p>O Master, Lover of man! Great is the depth of Thine economy; from generation to generation dost Thou benefit Thy creation; without forsaking the bosom of the Father, as man in the flesh didst Thou appear on earth and hast come calling all to repentance. As the King and God we adore Thee, since Thou destroyest our enemies and savest Thine endurable people who celebrate Thy honoured (name of the event.).</p>'
    ,'readings': """<h3>The Reading from the Book of Exodus (20:12-18).</h3><p>The Lord said unto Moses: Come up to Me into the mount and be there; and I will give thee tables of stone, and a law, and commandments which I have written that thou mayest teach them. And Moses and his minister Joshua rose up and went up into the mount of God, and Moses said unto the elders: Tarry ye here for us until we come again unto you; and, behold, Aaron and Hur are with you; if any man have any matters to do, let him come unto them. And Moses went up into the mount, and a cloud covered the mount. And the glory of the Lord came down upon Mount Sinai, and the cloud covered it six days. And the seventh day the Lord called unto Moses out of the midst of the cloud. And the sight of the glory of the Lord was like a devouring fire on the top of the mount in the eyes of the children of Israel. And Moses went into the midst of the cloud and gat him up into the mount; and was in the mount forty days and forty nights.</p><h3>The Reading from the Book of Deuteronomy. (4:1,6-15).</h3><p> Moses said unto the people: Now hearken, O Israel, unto the statutes and unto the judgments which I teach you for to do them, that ye may live. Keep therefore and do them;3 for this is your wisdom and your understanding in the sight of thenations, which shall hear all these statutes and say: surely this great nation is a wise and understanding people, as the Lord our God is in all things that we call upon Him for. And now take heed to yourselves, all ye the house of Israel, and keep your souls diligently, lest ye forget the things which your eyes have seen, and lest they depart from your hearts all the days of your life. But teach them your sons and your sons' sons, specially the day that ye stood before the Lord your God in Horeb, when the Lord said unto me: Gather me the people together and I will make them hear my words, that they may learn to fear me all the days that they shall live upon the earth, and that they may teach their children. .And ye came near and stood under the mountain, and the mountain burned with fire unto the midst of heaven, with darkness, clouds and thick darkness. And the Lord spake unto you out of the midst of the fire: ye heard the voice of the words, but saw no similitude, only ye heard a voice. And He declared unto you His covenant, which He commanded you to perform. Aid the Lord commanded me at that time to teach you statutes and judgments that ye might do them in the land. The Lord spake unto you in Horeb out of the midst of the fire.</p><h3>The Reading from the Book of Deuteronomy (5:1-7,9,10,23-26,28; 6:1,2,4,5,13,18).</h3><p>Moses called all Israel, and said unto them: Hear, O Israel the statutes and judgments which I speak in your ears this day, that ye may learn them and keep and do them: The Lord God made a covenant with you in Horeb, not with your fathers alone did the Lord make His covenant, but with you also. The Lord talked face to face in Horeb out of the midst of the fire, and I stood between the Lord and you at that time to declare unto you the words of the Lord saying: I am the Lord thy God, which brought thee out of the land of Egypt, from the house of bondage; there are no others gods beside Me, for I the Lord thy God am a jealous God, shewing mercy unto thousands of them that love Me and keep My commandments. And it came to pass when ye heard the voice out of the midst of fire, and the mountain did burn with fire, that ye all came near unto me,and ye said: Behold, the Lord our God hath shewed us His glory, and we have heard His voice out of the midst of the fire. We have seen this day that God doth talk with man and he liveth. Now, why should we die? for this great fire will consume us; if we hear the voice of the Lord our God any more, then we shall die. For who is there of all flesh, that hath heard the voice of the Lord speaking out of the midst of the fire, and liveth? And the Lord heard the voice of your words, when ye spoke unto me, and I said unto you all the commandments, the statutes and the judgments which the Lord commanded you that ye might fear all His statutes, that He may be merciful unto you and that ye may increase in the land. Hear, Israel, the Lord your God is one Lord. And thou shalt love the Lord thy God with all thy thought, with all thy heart, with all thy soul and with all thy might; thou shalt fear Him and serve Him alone, cleave unto Him, thou shalt swear by His name and shalt do that which is good in His sight, that it may be well with thee."""
    ,'aposticha_theotokion': '<p><i class="note">Theotokion, in Tone VIII:</i></p><p>O Lord; desiring to fulfil what Thou host ordained from the beginning, Thou halt selected from among all Thy creatures ministers of Thy mystery: from angels * Gabriel, from man * the Virgin, from heavens * the star, from earth --the mountain, from wilderness * the manger, from waters ** the Jordan in which Thou hast destroyed the impious deeds ofall; O our Saviour, glory to Thee.</p>'
}
master_matins = {
    'session1': '<p><i class="note">The Sessional Hymn in Tone I:</i></p><p><i class="note">Spec. Mel.: "Thy Sepulchre...":</i></p><p>Thy grace hath been poured upon us, O Saviour, when Thou, Incomprehensible One, becamest visible, and the darkness of illusion hath disappeared. Wherefore do Thou set our steps in the light of Thy countenance, so that, walking in accordance with Thy commandments, we may be made worthy to see Thee, the Light unapproachable.</p><p>Glory ..., Now & Ever ...,</p><p>Thy grace hath been poured upon us, O Saviour, when Thou, Incomprehensible One, becamest visible, and the darkness of illusion hath disappeared. Wherefore do Thou set our steps in the light of Thy countenance, so that, walking in accordance with Thy commandments, we may be made worthy to see Thee, the Light unapproachable.</p>'
    ,'session2': '<p><i class="note">The Sessional Hymn in Tone V:</i></p><p><i class="note">Spec. Mel.: "The Co-unoriginate...":</i></p><p>The Co-unoriginate Son of the Father and Ever-existing, Invisible in Thy nature and Intactable, having come under the conditions of time, Thou hast, through Thine ineffable goodness, left us, O Master, of Thy circumscribed body the sweet image in (name of the event) for the salvation of our souls. </p><p>Glory ..., Now & Ever ...,</p><p>The Co-unoriginate Son of the Father and Ever-existing, Invisible in Thy nature and Intactable, having come under the conditions of time, Thou hast, through Thine ineffable goodness, left us, O Master, of Thy circumscribed body the sweet image in (name of the event) for the salvation of our souls. </p>'
    ,'session3': '<p><i class="note">The Sessional Hymn in Tone IV:</i></p><p><i class="note">Spec. Mel.: "Thou that hast ascended...":</i></p><p>There is no longer lamentation in the countenance of Adam, since Adam was put on by His Maker, Who appeareth unto all in the likeness of Adam\'s countenance and moveth the communities of the pious unto love that they may with one voice hymn: Glory, O Master, Lover of man, to Thine extreme condescension.</p><p>Glory ..., Now & Ever ...,</p><p>There is no longer lamentation in the countenance of Adam, since Adam was put on by His Maker, Who appeareth unto all in the likeness of Adam\'s countenance and moveth the communities of the pious unto love that they may with one voice hymn: Glory, O Master, Lover of man, to Thine extreme condescension.</p>'
    ,'prokeimenon': '<p><i class="note">The Prokeimenon in Tone IV:</i></p><p>Lord, we shall walk in the light of Thy countenance, and in Thy name shall we rejoice6 unto the ages.</p><p><i class="note">Verse:</i> All the ends of the earth have seen the salvation of our God. The Gospel of the Festival that happeneth to be.</p>'
    ,'readings': ''
    ,'after50': '<p><i class="note">The Sessional Hymn, in Tone VIII:</i></p><p>O Lord; desiring to fulfil what Thou host ordained from the beginning, Thou halt selected from among all Thy creatures ministers of Thy mystery: from angels * Gabriel, from man * the Virgin, from heavens * the star, from earth * the mountain, from wilderness * the manger, from waters ** the Jordan in which Thou hast destroyed the impious deeds ofall; O our Saviour, glory to Thee.</p>'
    ,'exapostilarion': '<p><i class="note">Exapostilarion, Spec. Mel.: "O ye women..."</i></p><p>A mystery the greatest and withheld from angels, through the benevolence of the Father and the working of the Holy Spirit was accomplished as a fulfilment of prophecy: the Unoriginate Word having accepted an origin, as a man was born of the Virgin for the salvation of the world and unto the redemption of mankind. <i class="note">Thrice</i>.</p>'
    ,'canon': """
    <p><i class="note">The Canon, Tone IV:</i></p>
    <h3>Ode I</h3>
    <p><i class="note">The Irmos:</i></p><p> Unto Him that of old hath instructed Israel running away from Pharaoh\'s bondage, and hath fed them in the wilderness, unto our God, the Deliverer, let us sing; for He is glorified. On the day set apart for our festival let us, O people, open our mouths and expound with our tongues the divine manifestation of Christ our God in (name of the event) cheerfully singing: For He is glorified. The Light Ever-existing, carrying out the words of the Father and desiring to shew His grace, hath taken the form of a servant for our sake and manifested Himself in the manner of His divine (name of the event), highly illumining us with light. O come ye all, let us in faith celebrate Christ\'s (name of the event), and intelligently offering the divine melody, let us glorify Him and vociferate harmoniously: Christ is come
    unto the restoration of the darkened. Let us sing unto Him, for He is glorified.</p>
    <p><i class="note">Thetokion:</i> This day\'s manifestation of the birth of the God incarnate we have truly learned through thee, O all-pure one, and honouring thee were accounted worthy to behold (name of the event) of thy Son; Whom supplicate to save us from every danger.</p>
    <p><i class="note">For Katavasia:</i> Covered with divine darkness, the one slow of speech hath proclaimed the God-written law, for, having thrown the mire off his mental eye, he doth see the Existing One and ac- quireth knowledge of the Spirit, praising with divine songs.</p>
    <h3>Ode III</h3>
    <p><i class="note">The Irmos:</i></p><p> Neither in wisdom, nor in power and riches we glory, but in Thee,O Christ, the Hypo static Wisdom of the Father, for there is no one moreholy than Thou art, O Lover of man. Master by nature, Thou, O Christ, didst unite Thyself untoThy servants and becamest visible, working for us various forms of salvation which we now glorify in Thy (name of the event), for there is no one more holy than Thou art, O Lover of man. Thy people, O Christ, who are enlightened by the faith in Thee, brightly celebrate Thy divine festival (name of the event); honouring which we get delivered from dangers; vouchsafe unto us, O Saviour, the Kingdom of heaven also. O Life Hypostatical ! Having now tasted of death in the flesh and thereby made life to flow unto the dead, Thou hast, O Christ, granted us as meditator of life Thine awaking and Thy (name of the event).
    <p><i class="note">Thetokion:</i> The salvation hath before shone forth in the flesh out of thee in the world, and now unto the faithful through thee, O God\'s Mother, the life appeared in Christ\'s light-bearing (name of the event) ; for the sake thereof do, O Theotokos, supplicate thy Son to deliver us from dangers and from everlasting torments.
    <p><i class="note">Katavasia: The fetters of the childless womb, and the unbearable insults from a</i> fruitful foe have of old been done away with in the case of Anna the prophetess solely by her prayer, brought with an afflicted spirit unto the Mighty One and God of wisdom.
    <p><i class="note">The Sessional Hymn, Tone IV:</i></p><p><i class="note">Spec. Mel.: "Thou that wastlifted up on the cross..."</i></p>
    <p>We implore Thee, O Master and Merciful Saviour, to deliver from all enemies both visible and invisible, from incursions of other nations and from all manner of dangers and confusion, us who in faith and with love celebrate Thy divine (name of the event) ; for the sake thereof do vouchsafe that we may obtain the enjoyment of eternal good things. <p>Glory ..., Now & Ever ...,</p> We implore Thee, O Master and Merciful Saviour, to deliver from all enemies both visible and invisible, from incursions of other nations and from all manner of dangers and confusion, us who in faith and with love celebrate Thy divine (name of the event) ; for the sake thereof do vouchsafe that we may obtain the enjoyment of eternal good things.</p>
    <h3>Ode IV</h3>
    <p><i class="note">The Irmos:</i></p><p>Perceiving the unfathomable divine council with regard to the incarnation from the virgin of Thee, the High One, the prophet Habbakuk called out: Glory to Thy might, O Lord. The divine festival of One Who in the flesh drew so near unto men, as a light hath come to the newly elected Israel and enlighteneth to day the ends of the whole world by His (name of the event): Glory to Thy might, O Lord. Having been illumined, Moses was of old made worthy to see God\'s glory in Thy signs, and the new Israel doth now behold Thee, the Deliverer, clearly face to face: Glory to Thy might, O Lord. Behold, all ye people, the wonderful things, rejoice now in spirit, hymning (name of the event) of Christ, Who hath appeared on earth unto men for their salvation: Glory to Thy might, O Lord.</p>
    <p><i class="note">Theotokion:</i> O most pure Theotokos, save us that flee unto thee and celebrate Thy Son\'s divine (name of the event), and always supplicate Him to grant us remission of sins.</p>
    <p><i class="note">Katavasia:</i> O King of Kings, Sole from the only One, the Only Word of the Uncaused Father, Thou in Thy bounty hast truly sent down Thy Co-equal in might Spirit upon the apostles that hymn Thee: Glory to Thy might, O Lord.</p>
    <h3>Ode V</h3>
    <p><i class="note">The Irmos:</i></p><p> Thou Who hast dispersed the primordiate light that the works may in the light hymn Thee, O Christ, as the Creator, do in Thy light direct our paths. Let us to-day clap our hands and shout with our voices the praises of the Lord, for, behold, He hath truly appeared, enlightening all the faithful with the divine (name of the event) of His most pure body. The assemblies of the faithful are to-day enlightened and the bands of heretics put to shame at the sight of the adoration of (name of the event) of Christ, the Deliverer having assumed the bodily form. The festivity is come and the great mystery hath shone forth light from the countenance of the Lord in the well-arranged festival of the divine (name of the event) of the Lord, for therewithal were granted unto all the captives peace and joy.</p>
    <p><i class="note">Thetokion:</i> Let the clouds drop sweetness from above unto the earthly, at thine intercession, O most holy Virgin; having taken compassion of the world, thy Son and our God hath to-day raised the horn of the Christians ; to-day hath He granted salvation unto the faithful by his divine (name of the event). </p>
    <p><i class="note">Katavasia:</i> O ye, illustrious children of the church ! Receive the fire-breathing dew of the Spirit for the perfect purification of sins, for now from Zion hath gone forth the law - the grace of the Spirit in the shape of the tongues of fire.</p>
    <h3>Ode VI</h3>
    <p><i class="note">The Irmos:</i></p><p>Celebrating this divine and all-honourable feast of the Mother of God, come ye Godly- wise, let us clap our hands, glorifying the God that was born of her. Life hath shone forth unto the dead, and light hath come unto those that were already blind, and unto those grievously afflicted hath sprung up a cure, and salvation hath come nigh unto all through the lightbearing (name of the event) of Christ. Let every intelligence rejoice, now clearly seeing the spiritual festival of the divine (name of the event), which doth shed enlightenment unto those that adore Him. O Lord, the heavens, seeing Thee, declare Thy glory, O Jesus Christ, they call together all Thy faithful to the hymning of Thy divine (name of the event), and those that are to come unto the knowledge of true repentance. </p>
    <p><i class="note">Thetokion:</i> O Mother of God ! there appeared unto the nations a sign and sure salvation, O pure Virgin, in the light of the honoured (name of the event) of Thy Son; Him supplicate to save us that recall Thee, and deliver from dangers and incursions of pagans with thine interces- sions. </p>
    <p><i class="note">Katavasia:</i> O Christ! Thou hast shone forth from the Virgin unto us, O Master, as propitiation and salvation, that, just as once the prophet Jonah out of the belly of a sea-monster, Thou mightest rescue from corruption Adam, fallen with all his race.</p>
    <p><i class="note">Kontakion, in Tone II:</i> O uncircumscribed Word of the Father! knowing Thine undrawn by hand, but God-made icon to be the trophy of Thine ineffable and divine economy respecting men and of Thine undoubted incarnation, we honour Thee in kissing it.</p>
    <p><i class="note">Ikos:</i> Giving assurance unto men of the mystery of His incarnation, the Lord becometh Himself circumscribed by His God-and-man form; the Archetype thereof doth He seat on the Father\'s throne to be worshipped of the bodiless angels, and the adoration of an image of the Archetype hath He granted unto us; which embracing with our souls and hearts, we honour Him in kissing it.</p>
    <h3>Ode VII</h3>
    <p><i class="note">The Irmos:</i></p><p> The Abrahamic youths have once in Babylon trodden under their feet the flame of the furnace, calling out in songs: O God of our fathers, blessed art Thou. Every city and country rejoice together with the new Zion in faithful celebration; for the King of her glory, Christ, hath come in the form of His venerable festival (name of the event) and saveth those that adore Him and vociferate: O God of our fathers, blessed art Thou. The sayings of the God-voiced prophets have been fulfilled in the Holy Scriptures, for now we see the accomplishment in Christ\'s (name of the event); thereby is the world enlightened and with its brilliant shine are saved those that sing: O God of our fathers, blessed art Thou. </p>
    <p><i class="note">Thetokion:</i> With the earthly the heavenly are rejoicing, and the multitude of all the saints participate in the rejoicings; both the kings and princes, the rich and poor * we are all celebrating; for Christ hath prepared for us an enlightenment in the picture of His festival ** the god-effecting similitude which He hath received from the Virgin.</p>
    <p><i class="note">Katavasia :</i> Harmoniously have once resounded the instruments in honour of the golden-made, lifeless idol, and the light-bearing grace of the Comforter doth animate to the vociferation: O Sole Trinity, equal in might, unoriginate, blessed art Thou.
    <h3>Ode VIII</h3>
    <p><i class="note">The Irmos:</i></p><p> The youths in Babylon, burning with the divine zeal, have manfully scorned both the tyrant and the flame, and being thrown into the midst of the fire, but bedewed, sung : Bless the Lord, all ye the works of the Lord. Being perfect God by nature, Thou wast seen a perfect man also, preserving in both natures their properties, and as God giving assurance of the divine (name of the event) in the flesh; Him adoring we sing: Bless the Lord, all ye the works of the Lord. Exalt the horn, O Word of God, of those who confess Thee to be God and man and who glorify Thy (name of the event), wherewith Thou hast vouchsafed unto all the faithful the life eternal and made of no effect the rage of the pagans, haters of Thy divine might. The new law shineth and the church is adorned, for the lightof Thy divine glory, O Christ the God, hath gone forth and manifested Thy light-like countenance in Thy (name of the event) unto the salvation of Thy people that vociferate unto Thee: Bless the Lord, all ye the works of the Lord. </p>
    <p><i class="note">Thetokion:</i> O Thou, restoration of the fallen, joy of the despairing, instructress of those gone astray, healer of the sick and salvation for all Christians - do preserve, O Sovereign-Lady Theotokos, us that honour (name of the event) of Thy Son; supplicate of Him that we may be delivered from the incursions of foreign nations.</p>
    <p><i class="note">Katavasia: The triply-shining form of Godhead looseth the chains and bedeweth</i> the flame; the youths hymn and the whole creation blesseth the Only Saviour and Maker as Benefactor.</p>
    <h3>Ode IX</h3>
    <p><i class="note">The Irmos :</i></p><p> Thy bringing forth hath proved incorrupt : God hath passed out of thy loins, as flesh-bearer did He appear on earth and hath lived among men ; wherefore we all magnify thee, O Theotokos. Let us sing an ode of thanksgiving unto the Lord who was pleased to grant us exceedingly abundant riches in (name of the event) of His divine flesh which in battles affordeth so strong a support and honouring which we the faithful magnify Thee. O the wonders above understanding which Thou, O Lord, hast made for us that trust in Thee! For just as (name of the event) was, Thou hast ineffably and awfully shown unto all the image thereof; do deliver those that honour it, from every anger and fall. O Word of God, Wisdom and Might and Image of the Father! O God comprehensible! Do make us worthy to accomplish the joyful celebration of Thy festival (name of the event) in the light of good works, spiritually magnifying Thee.</p>
    <p><i class="note">Thetokion:</i> Truly thy height, O most pure one, is that of the mystery of God and the depth that of the divine and ineffable wisdom. For the Most High was unspeakably born of thee and the Invisible One became Visible in His fleshly (name of the event); adoring which we the faithful magnify thee.</p>
    <p><i class="note">Katavasia: Hail thou, O Queen, the glory of both mother and maiden, for no</i> mouth, however fluent and well-spoken, can be so eloquent as worthily to hymn thee, and every mind faileth to comprehend thy bringing forth; wherefore we with one voice glorify thee.</p>
    """
    ,'apolytichion': '<p><i class="note">In Tone I</i></p><p>O come, let us, O people, celebrate Christ\'s (name of the event), let us concentrate our minds and feelings and we shall see Him who hath taken His flesh from the pure Virgin, being perfect Son both in his Godhead and humanity; wherefore let us call: O Holy God * the Father Unoriginate, O Holy Mighty * the Son Incarnate, O Holy Immortal * the Comforting Spirit * the Holy Trinity ** glory to Thee.</p>'
}
master_liturgy = {
    'beatitudes': [
        '<p><i class="note">*</i>Neither in wisdom, nor in power and riches we glory, but in Thee, O Christ, the Hypostatic Wisdom of the Father, for there is no one moreholy than Thou art, O Lover of man.</p>'
        ,'<p><i class="note">*</i>Master by nature, Thou, O Christ, didst unite Thyself untoThy servants and becamest visible, working for us various forms of salvation which we now glorify in Thy (name of the event), for there is no one more holy than Thou art, O Lover of man.</p>'
        ,'<p><i class="note">*</i>Thy people, O Christ, who are enlightened by the faith in Thee, brightly celebrate Thy divine festival (name of the event); honouring which we get delivered from dangers; vouchsafe unto us, O Saviour, the Kingdom of heaven also.</p>'
        ,'<p><i class="note">*</i>O Life Hypostatical! Having now tasted of death in the flesh and thereby made life to flow unto the dead, Thou hast, O Christ, granted us as meditator of life Thine awaking and Thy (name of the event)</p>'
        ,'<p><i class="note">*</i>Celebrating this divine and all-honourable feast of the Mother of God, come ye Godly- wise, let us clap our hands, glorifying the God that was born of her.</p>'
        ,'<p><i class="note">*</i>Life hath shone forth unto the dead, and light hath come unto those that were already blind, and unto those grievously afflicted hath sprung up a cure, and salvation hath come nigh unto all through the lightbearing (name of the event) of Christ.</p>'
        ,'<p><i class="note">*</i>Let every intelligence rejoice, now clearly seeing the spiritual festival of the divine (name of the event), which doth shed enlightenment unto those that adore Him.</p>'
        ,'<p><i class="note">*</i>O Lord, the heavens, seeing Thee, declare Thy glory, O Jesus Christ, they call together all Thy faithful to the hymning of Thy divine (name of the event), and those that are to come unto the knowledge of true repentance. </p>'
    ]
}

if __name__=='__main__':
    with open('test.html', 'w') as f:
        #for id, m in menaion_class.items():
        m = 'Master'
        #if m == 'Holy Fathers':
        f.write(f'<h2>{m}</h2>')
        #menaion = menaion_variables(process_pdf(filename=m, service='menaion'),name=m, service_type=m, weekday=0)
        menaion = menaion_variables(input_string=None, name='Holy Sepulcre', service_type=m, weekday=0)
        for b in menaion.get('liturgy').get('beatitudes'):
            f.write(b)
        # f.write(menaion.get('liturgy').get('troparion'))
        # f.write(menaion.get('liturgy').get('kontakion'))
        # f.write(menaion.get('liturgy').get('prokeimenon'))
        # f.write(menaion.get('liturgy').get('readings'))

        f.write(menaion.get('matins').get('troparion'))
        if menaion.get('matins').get('session1'):
            f.write(menaion.get('matins').get('session1'))
        if menaion.get('matins').get('session2'):
            f.write(menaion.get('matins').get('session2'))
        if menaion.get('matins').get('megalynarion'):
            f.write(menaion.get('matins').get('megalynarion'))
        if menaion.get('matins').get('session3'):
            f.write(menaion.get('matins').get('session3'))
        if menaion.get('matins').get('prokeimenon'):
            f.write(menaion.get('matins').get('prokeimenon'))
        if menaion.get('matins').get('readings'):
            f.write(menaion.get('matins').get('readings'))
        if menaion.get('matins').get('after50'):
            f.write(menaion.get('matins').get('after50'))
        f.write(menaion.get('matins').get('canon'))
        f.write(menaion.get('matins').get('exapostilarion'))
        # f.write(menaion.get('matins').get('praises'))
        if menaion.get('matins').get('apolytichion'):
            f.write(menaion.get('matins').get('apolytichion'))
        # # #--------------------------------------------------------------------------
        for s in menaion.get('vespers').get('stichera'):
            f.write(s.replace('О','O') + '\n')
        # if menaion.get('vespers').get('doxastichon'):
        #     f.write('<h3>Doxastichon</h3>')
        #     f.write(menaion.get('vespers').get('doxastichon'))
        # if menaion.get('vespers').get('dogmaticon'):
        #     f.write('<h3>Dogmaticon</h3>')
        #     f.write(menaion.get('vespers').get('dogmaticon'))
        if menaion.get('vespers').get('theotokion'):
            f.write('<h3>Theotokion</h3>')
            f.write(menaion.get('vespers').get('theotokion'))
        f.write(menaion.get('vespers').get('readings'))
        # f.write(menaion.get('vespers').get('aposticha'))
        f.write(menaion.get('vespers').get('aposticha_theotokion'))
        # f.write(menaion.get('vespers').get('apolytichion'))
