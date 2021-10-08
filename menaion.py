"""
Version 0.0.8
Updated 10/8/2021

Change Log:
10/8/2021 - 0.0.8 - Initial build, dictionary
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
