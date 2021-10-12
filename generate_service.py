"""
Version 0.0.8
Updated 10/11/2021

Change Log:
10/11/2021 - 0.0.8 - Initial Creation, Vespers elements
"""

import os
from octoechos import octoechos_variables
from _utils import process_pdf
from bs4 import BeautifulSoup

def rubrics(rank:int, octoechos=None, menaion=None, paschal=None):
    """
    Takes in dictionaries from various sources.
    """
    if rank < 7 and not (menaion or paschal):
        print(f'Service rank {rank} with no menaion or triodion/pentecostarion! \nGenerating simple service instead')
        rank = 7

    if rank == 7: #simple service
        return octoechos

def vespers(date:str, parts:dict):
    vfil = open('docs/html/vespers.html')
    vespers = BeautifulSoup(vfil, 'html.parser')
    stichera = vespers.select('.vespers-sticheron')
    theotokion = vespers.select_one('.vespers-theotokion')
    #Prokeimenon
    aposticha = vespers.select_one('.vespers-aposticha')
    apolytichion = vespers.select_one('.vespers-apolytichion')

    #add code for stichera logic....

    theotokion.append(BeautifulSoup(parts.get('vespers').get('theotokion'),'html.parser'))
    aposticha.append(BeautifulSoup(parts.get('vespers').get('aposticha'),'html.parser'))
    apolytichion.append(BeautifulSoup(parts.get('vespers').get('apolytichion'),'html.parser'))

    return vespers.prettify()


with open('docs/html/test.html', 'wt', encoding='utf-8') as f:
    f.write(vespers('7',rubrics(7,octoechos=octoechos_variables(process_pdf(filename='7-2',service='octoechos')))))
