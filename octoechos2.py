"""
Test for better octoechos processing.
"""


import re
from _utils import open_service, regex_parse

def vespers(input:str):
    """
    processing vespers variables...
    """


    search = re.search(r'AT (GREAT VESPERS|VESPERS).*(AT COMPLINE|COMPLINE)',input,flags=re.S)
    service = input[search.start():search.end()]

    stichera_search = re.search(r'On.*?Lord[, ]+I[, ]+have[, ]+cried[ ,.]+.*?glory[ .,]{3,}',service,flags=re.S|re.I)
    s_theotokion_search = re.search(r'^glory[ .,]{3,}now & ever[ .,]{3,}',service,flags=re.M|re.I)
    prokeimenon_search = re.search(r'prokeimenon.*?(Vouchsafe|On the Aposticha)',service,flags=re.S|re.I)
    aposticha_search = re.search(r'(on the aposticha|aposticha).*?glory[ .,]{3,}',service,flags=re.S|re.I)

    stichera = service[stichera_search.start():s_theotokion_search.start()]
    s_theotokion = service[s_theotokion_search.end():prokeimenon_search.start()]
    prokeimenon = service[prokeimenon_search.start():prokeimenon_search.end()]
    aposticha = service[aposticha_search.start():aposticha_search.end()]
    a_theotokion = service[aposticha_search.end():]

    stichera = re.split(r'Verse:.*?\n',stichera,flags=re.S)

    variables = {
        'stichera': stichera
        #,'stichera_tone': stichera_tone
        ,'doxastichon': ''
        ,'theotokion': s_theotokion
        ,'prokeimenon': prokeimenon
        ,'aposticha': aposticha
        ,'aposticha_theotokion': a_theotokion
    }
    return variables

if __name__ == '__main__':
    tt = [1,2,3,4,5,6,7,8]
    dd = [1,2,3,4,5,6,7]
    with open('test.html','w') as f:
        for t in tt:
            for d in dd:
                fil = f'{t}-{d}.txt'
                print(fil)
                v = vespers(open_service(service='test',filename=fil))
                f.write(f'<h1>{t}-{d}</h1>')
                f.write('<h2>Stichera</h2>')
                for s in v.get('stichera'):
                    f.write('*' + s.replace('О', 'O') + '<br>')
                f.write('<h2>Theotokion</h2>')
                f.write(v.get('theotokion').replace('О', 'O'))
                f.write('<h2>Prokeimenon</h2>')
                f.write(v.get('prokeimenon').replace('О', 'O'))
                f.write('<h2>Aposticha</h2>')
                f.write(v.get('aposticha').replace('О', 'O'))
                f.write(v.get('aposticha_theotokion').replace('О', 'O'))



    x = vespers(open_service(service='test', filename='2-2.txt'))
