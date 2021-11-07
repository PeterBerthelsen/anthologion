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
from hymns import forerunner_troparia, forerunner_megalynaria, forerunner_kontakia

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

def menaion_liturgy(service:str, name:str, service_type:str):
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

def menaion_variables (input_string:str, name:str, service_type:str):
    """
    Uses string data from PDF to extract to generate menaion variables for services
    Text is divided at common breakpints from PDFs, then formatted for use.
    Returns list with variables at set index location.
    """
    #Insert name variable into service
    input_string = re.sub(r'[(]name.*?[)]',f'<i class="name">{name}</i>',input_string,flags=re.S)
    input_string = input_string.replace('О', 'O') #replace known cyrillic chracter \u041e which throws error

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


if __name__=='__main__':
    with open('test.html', 'w') as f:
        for id, m in menaion_class.items():
            #if m == 'Holy Fathers':
            f.write(f'<h2>{m}</h2>')
            menaion = menaion_variables(process_pdf(filename=m, service='menaion'),name=m, service_type=m)
            # for b in menaion.get('liturgy').get('beatitudes'):
            #     f.write(b)
            # f.write(menaion.get('liturgy').get('troparion'))
            # f.write(menaion.get('liturgy').get('kontakion'))
            # f.write(menaion.get('liturgy').get('prokeimenon'))
            f.write(menaion.get('liturgy').get('readings'))

            # f.write(menaion.get('matins').get('troparion'))
            # if menaion.get('matins').get('session1'):
            #     f.write(menaion.get('matins').get('session1'))
            # if menaion.get('matins').get('session2'):
            #     f.write(menaion.get('matins').get('session2'))
            # if menaion.get('matins').get('megalynarion'):
            #     f.write(menaion.get('matins').get('megalynarion'))
            # if menaion.get('matins').get('session3'):
            #     f.write(menaion.get('matins').get('session3'))
            # if menaion.get('matins').get('prokeimenon'):
            #     f.write(menaion.get('matins').get('prokeimenon'))
            # if menaion.get('matins').get('readings'):
            #     f.write(menaion.get('matins').get('readings'))
            # if menaion.get('matins').get('after50'):
            #     f.write(menaion.get('matins').get('after50'))
            # f.write(menaion.get('matins').get('canon'))
            # f.write(menaion.get('matins').get('exapostilarion'))
            # f.write(menaion.get('matins').get('praises'))
            # if menaion.get('matins').get('apolytichion'):
            #     f.write(menaion.get('matins').get('apolytichion'))
            # # #--------------------------------------------------------------------------
            # for s in menaion.get('vespers').get('stichera'):
            #     f.write(s.replace('О','O') + '\n')
            # #Compare these with Anthologion later for confirmation!!!
            # if menaion.get('vespers').get('doxastichon'):
            #     f.write('<h3>Doxastichon</h3>')
            #     f.write(menaion.get('vespers').get('doxastichon'))
            # if menaion.get('vespers').get('dogmaticon'):
            #     f.write('<h3>Dogmaticon</h3>')
            #     f.write(menaion.get('vespers').get('dogmaticon'))
            # if menaion.get('vespers').get('theotokion'):
            #     f.write('<h3>Theotokion</h3>')
            #     f.write(menaion.get('vespers').get('theotokion'))
            # f.write(menaion.get('vespers').get('readings'))
            # f.write(menaion.get('vespers').get('aposticha'))
            # f.write(menaion.get('vespers').get('aposticha_theotokion'))
            # f.write(menaion.get('vespers').get('apolytichion'))
