'''
Created on 7 Apr 2020

@author: jalmonte
'''

from html.parser import HTMLParser
import urllib.request
from bs4 import BeautifulSoup

class HTMLParserTools(HTMLParser):
    def __init__(self, URL):
        '''
        initializes and parses target HTML given by url
        '''
        self._parser = HTMLParser()
        
        _weburl = urllib.request.urlopen(URL)
        self.content = _weburl.read().decode('utf-8', 'ignore')
        #self._parser.feed(self.content)
        _weburl.close()
            
    def get_content(self):
        '''
        getter method for HTML content
        '''
        return self.content
    
    
class HTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        '''
        handles tags after feeding HTML to HTMLParser
        '''
        print(f"Encountered a tag: {tag}")
        for attr in attrs:
            print(f"\tEncountered an attribute {attr[0]} with value {attr[1]}")