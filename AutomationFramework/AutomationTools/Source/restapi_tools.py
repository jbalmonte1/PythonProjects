'''
Created on 22 Sep 2020

@author: jalmonte
'''

import requests

class RestApiTools():
    def __init__(self, URL):
        self._url = URL
        
    def get(self, endpoint, verify = False, auth = None):
        '''
        Sends a get request to target endpoint
        '''
        if auth:
            response = requests.get(self._url + endpoint, verify = verify, auth = auth)
        else:
            response = requests.get(self._url + endpoint, verify = verify)
        
        if "200" in str(response):
            return response.json()
        else:
            raise RuntimeError(f"Get request returned {response} response.")
    
    def put(self, endpoint, body, verify = False, auth = None):
        '''
        Sends a put request to target endpoint with given body
        '''
        if auth:
            response = requests.put(self._url + endpoint, data = body, verify = verify, auth = auth)
        else:
            response = requests.put(self._url + endpoint, data = body)
            
        if "201" in str(response):
            return str(response)
        else:
            raise RuntimeError(f"Put request returned {response} response.")
        
    def post(self, endpoint, body, verify = False, auth = None):
        '''
        Sends a put request to target endpoint with given body
        '''
        if auth:
            response = requests.post(self._url + endpoint, data = body, verify = verify, auth = auth)
        else:
            response = requests.post(self._url + endpoint, data = body)
            
        if "201" in str(response):
            return str(response)
        else:
            raise RuntimeError(f"Post request returned {response} response.")
        
    def delete(self, endpoint, verify = False, auth = None):
        '''
        Sends a delete request to target endpoint
        '''
        if auth:
            response = requests.delete(self._url + endpoint, verify = verify, auth = auth)
        else:
            response = requests.delete(self._url + endpoint)
            
        if "204" in str(response):
            return str(response)
        else:
            raise RuntimeError(f"Delete request returned {response} response.")
        
    def patch(self, endpoint, body, verify = False, auth = None):
        '''
        Sends a patch request to target endpoint with given body
        '''
        if auth:
            response = requests.patch(self._url + endpoint, data = body, verify = verify, auth = auth)
        else:
            response = requests.patch(self._url + endpoint, data = body)
            
        if "200" in str(response):
            return response.json()
        else:
            raise RuntimeError(f"Patch request returned {response} response.")