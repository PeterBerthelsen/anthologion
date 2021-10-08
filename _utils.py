"""
Version 0.0.8
Updated 10/8/2021

Change Log:
10/8/2021 - 0.0.8 - Initial Creation, added try loop/switch on process_pdf
"""
import os
import inspect
import fitz
from urllib.request import Request, urlopen

SERGIUS = 'http://www.st-sergius.org/'

def process_pdf (filename:str, url:str=None, service:str=None, local:bool=True):
    """
    Downloads PDF from website or opens locally, saves it off, parses text contents, then removes file.
    If initial method (local vs. web) fails, it will attempt the other.
    Returns string value of PDF text.
    """
    payload = ''
    caller = inspect.stack()[1][1].split('\\')[-1] #name of file calling function
    dir = os.path.dirname(caller)
    page = { #for each file, a corresponding page on the St. Sergius site
        'octoechos.py': 'services/oktiochos/'
        ,'menaion.py': 'services/menaion'
    }
    folder = { #for each file, a corresponding local folder
        'octoechos.py': 'services\octoechos'
        ,'menaion.py': 'services\menaion'
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
                with fitz.open(os.path.join(dir,folder.get(caller),f)) as content:
                    for page in content: #read each page
                        payload += page.getText() #add each page to payload
                return payload #return payload string
        except:
            print(f'Gathering {filename} from local = {local} FAILED! Attempting with local = {not local}')
            local = not local
