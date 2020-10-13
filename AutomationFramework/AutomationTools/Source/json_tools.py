'''
Created on 7 Apr 2020

@author: jalmonte
'''

import json

class JsonTools():
    def __init__(self):
        pass
    
    def load_json(self, data):
        '''
        Takes in data in bytes and converts it to dictionary
        '''
        _jsondict = json.loads(data)
        return _jsondict