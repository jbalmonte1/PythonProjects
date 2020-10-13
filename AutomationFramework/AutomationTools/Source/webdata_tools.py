'''
Created on 7 Apr 2020

@author: jalmonte
'''

import urllib.request

class WebDataTools():
    def __init__(self):
        self._proxies = {"http": "http://10.158.17.67:8080", "https": "https://10.158.17.67:8080"}
        proxy_support = urllib.request.ProxyHandler(self._proxies)
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener)
        
    def open_webpage(self, url):
        '''
        Opens a web page
        '''
        self.weburl = urllib.request.urlopen(url)    
        
    def get_return_code(self):
        '''
        Returns return code
        '''
        return self.weburl.getcode()
    
    def read_webpage(self):
        '''
        Returns weburl content of type 'bytes'
        '''
        return self.weburl.read()
    
    def convertostring(self, data):
        '''
        Returns string format of weburl of type 'bytes'
        '''
        return data.decode('utf-8')
    
    
