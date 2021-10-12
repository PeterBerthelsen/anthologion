"""
Version 0.0.8
Updated 10/8/2021

Change Log:
10/8/2021 - 0.0.8 - Initial Creation, added try loop/switch on process_pdf
"""
import os
import inspect
import fitz
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from io import TextIOWrapper

SERGIUS = 'http://www.st-sergius.org/'

def process_pdf (filename:str, url:str=None, service:str=None, local:bool=True):
    """
    Downloads PDF from website or opens locally, saves it off, parses text contents, then removes file.
    If initial method (local vs. web) fails, it will attempt the other.
    Returns string value of PDF text.
    """
    payload = ''
    caller = inspect.stack()[1][1].split('\\')[-1][:-3] #name of file (no extension) calling function
    for i in inspect.stack():
        print(i)
    dir = os.path.dirname(caller)
    page = { #for each file, a corresponding page on the St. Sergius site
        'octoechos': 'services/oktiochos/'
        ,'menaion': 'services/menaion/'
    }
    folder = { #for each file, a corresponding local folder
        'octoechos': 'services\octoechos'
        ,'menaion': 'services\menaion'
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
                with fitz.open(os.path.join(dir,folder.get(service if service else caller),f)) as content:
                    for page in content: #read each page
                        payload += page.getText() #add each page to payload
                return payload #return payload string
        except:
            print(f'Gathering {filename} from local = {local} FAILED! Attempting with local = {not local}')
            local = not local

def insert_html (target_html_file:str, target_html_element:str, html_to_insert:str):
        """
        Takes in a file name for source service (e.g. vespers), name element where
        moveable HTML will be inserted (e.g. '.vespers-aposticha'), and HTML string
        to inject. Inserts the HTML, then returns the full combined HTML string.
        """
        caller = inspect.stack()[1][1].split('\\')[-1] #name of file calling function
        dir = os.path.dirname(caller)
        folder = { #for each file, a corresponding local folder
            'octoechos.py': 'docs\html'
            ,'menaion.py': 'docs\html'
        }
        f = open(os.path.join(dir, folder.get(caller),target_html_file))
        source = BeautifulSoup(f, 'html.parser')
        element = source.select_one(target_html_element)
        insert = BeautifulSoup(html_to_insert, 'html.parser')
        element.append(insert)
        #payload = source.prettify()
        return source.prettify()#payload
