"""
Version 0.0.8
Updated 10/8/2021

Change Log:
10/8/2021 - 0.0.8 - Initial Creation, added try loop/switch on process_pdf
"""
import os
import re
import inspect
import fitz
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from io import TextIOWrapper

SERGIUS = 'http://www.st-sergius.org/'

def open_service(service:str, filename:str):
    payload = ''
    f = filename if '.' in filename else filename + '.pdf'
    # print(f[-4:])
    #f = filename if filename[-4:] == '.pdf' else filename + '.pdf' #set download file name
    src = f'services/{service}/{f}'
    if f[-4:] == '.pdf':
        with fitz.open(src) as content:
            for page in content: #read each page
                i = page.getText('blocks', flags=fitz.TEXT_INHIBIT_SPACES|fitz.TEXT_DEHYPHENATE)
                #print(i)
                if type(i) == str:
                    payload += i
                if type(i) == list:
                    for j in i:
                        if type(j) == str:
                            payload += j
                        if type(j) == tuple:
                            for k in j:
                                if type(k) == str:
                                    payload += k
    elif f[-4:] == '.txt':
        with open(src, 'r', encoding='utf-8') as fil:
            #print(fil)
            payload = fil.read()
    #payload = payload.replace('h2','p').replace('<b>','</p><p><b>')
    payload = re.sub(r'((?<![.!?:A-Z])\s*)\n',r'\1',payload)
    return payload #return payload string

def regex_parse(input:str, substitutions:dict, regex_flags=None):
    if not regex_flags:
        regex_flags = re.S|re.I
    output = input
    for search, replace in substitutions.items():
        output = re.sub(search,replace,output,regex_flags)
    return output

def process_pdf (filename:str, url:str=None, service:str=None, local:bool=True):
    """
    Downloads PDF from website or opens locally, saves it off, parses text contents, then removes file.
    If initial method (local vs. web) fails, it will attempt the other.
    Returns string value of PDF text.
    """
    #print(f'process_pdf initiated for file: {filename}')
    payload = ''
    caller = inspect.stack()[1][1].split('\\')[-1][:-3] #name of file (no extension) calling function
    # for i in inspect.stack():
    #     print(i)
    dir = os.path.dirname(caller)
    page = { #for each file, a corresponding page on the St. Sergius site
        'octoechos': 'services/oktiochos/'
        ,'menaion': 'services/menaion/'
    }
    folder = { #for each file, a corresponding local folder
        'octoechos': 'services/octoechos'
        ,'menaion': 'services/menaion'
    }
    f = filename if filename[-4:] == '.pdf' else filename + '.pdf' #set download file name

    for i in range(0,2): #two attempts max
        try:
            if local is False: #open file from web
                if not url or not service: #if no url given, find default
                    src = SERGIUS + page.get(caller) + f #base site + caller's page
                else:
                    src = url + service + f
                r = urlopen(Request(src)) #open the URL
                file = open(f, 'wb') #open file
                file.write(r.read()) #write content/download file
                file.close() #close/save the file
                with fitz.open(f) as content: #open for extraction
                    for page in content: #read each page
                        payload += page.getText() #add each page to payload
                os.remove(f) #delete downloaded file after payload established
                return payload #return payload string
            else: #gather file from web
                #if service is provided, grab from filepath, otherwise, use caller to determine...
                #print(f'opening local file: {os.path.join(dir,folder.get(service if service else caller),f)}')
                with fitz.open(os.path.join(dir,folder.get(service if service else caller),f)) as content:
                    for page in content: #read each page
                        payload += page.getText() #add each page to payload
                return payload #return payload string
        except:
            print(f'Gathering {filename} from local = {local} FAILED! Attempting with local = {not local}')
            local = not local

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

def format_text(input_string:str):
    '''
    Takes in plain text copied from online PDF resources
    Adds formatting, then outputs HTML
    '''

    replacements_with_case = {
        r'\n+\s+([^a-z]+)\s*\n': r'</p><h3>\1</h3><p>'
    }

    replacements_ignore_case = {
        r':\n': ':<br>'
        ,r'.*?([a-z]*theotokion.*?:|in tone [vi]+:)': r'</p><p><i>\1</i></p><p>'
        ,r'\n\s+[*](tone ([vi ]+|[0-9 ]+):)': r'<p><i>\1</i></p>'
    }

    formatted_string = regex_parse(input_string, replacements_with_case, re.S)
    formatted_string = regex_parse(formatted_string, replacements_ignore_case)

    return formatted_string
