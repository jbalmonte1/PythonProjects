import sys
from unittest.case import SkipTest
from requests.auth import HTTPBasicAuth
sys.path.insert(1, '..\\..')

import unittest
import os
from time import sleep
from AutomationTools import *

USERNAME = "Nemuadmin"
PASSWORD = "nemuuser"
auth = HTTPBasicAuth(USERNAME, PASSWORD)

URL = "http://127.0.0.1:5000/"
ENDPOINT_APPINFO = "appinfo"
ENDPOINT_ECHOPARAM = "echoparam/this_is_a_test"
ENDPOINT_INFO_STEVE = "record/steve"
ENDPOINT_INFO_BRUCE = "record/bruce"
ENDPOINT_INVALID = "invalid"

ENDPOINT_APPINFO_RESULT = {'data': 'AppInfo'}
ENDPOINT_ECHOPARAM_RESULT = {'param': 'this_is_a_test'}
ENDPOINT_INFO_STEVE_RESULT = {'first_name': 'Steven Grant', 'last_name': 'Rogers', 'alias': 'Captain America', 'sex': 'Male', 'state': 'New York', 'country': 'America'}
ENDPOINT_INFO_STEVE_RESULT_2 = {'first_name': 'Steven Grant', 'last_name': 'Rogers', 'alias': 'Nomad', 'sex': 'Male', 'state': 'Unknown', 'country': 'Unknown'}
ENDPOINT_INFO_BRUCE_RESULT = {'first_name': 'Robert Bruce', 'last_name': 'Banner', 'alias': 'Hulk', 'sex': 'Male', 'state': 'Ohio', 'country': 'America'}

NEW_RECORD = {'first_name': 'Robert Bruce', 'last_name': 'Banner', 'alias': 'Hulk', 'sex': 'Male', 'state': 'Ohio', 'country': 'America'}
ORIGINAL_RECORD = {'alias': 'Captain America', 'state': 'New York', 'country': 'America'}
UPDATE_RECORD = {'alias': 'Nomad', 'state': 'Unknown', 'country': 'Unknown'}

RESPONSE_201 = "<Response [201]>"
RESPONSE_204 = "<Response [204]>"

def test_decorator(func):
    def print_test_description(*func_args, **func_kwargs):
        print('================')
        print(f'Executing {func.__name__}'.upper())
        print('================')
        return func(*func_args, **func_kwargs)
    return print_test_description

class UnitTestSeleniumWebAutomation(unittest.TestCase):
    @test_decorator
    def test_get(self):
        '''
        Test for get() method
        '''
        restapitool = RestApiTools(URL)
        
        response_appinfo = restapitool.get(ENDPOINT_APPINFO, auth = auth)
        response_echoparam = restapitool.get(ENDPOINT_ECHOPARAM, auth = auth)
        response_info = restapitool.get(ENDPOINT_INFO_STEVE, auth = auth)
        
        print(response_appinfo)
        print(response_echoparam)
        print(response_info)
        
        self.assertEqual(ENDPOINT_APPINFO_RESULT, response_appinfo, f"Expected {ENDPOINT_APPINFO_RESULT}, got {response_appinfo}")
        self.assertEqual(ENDPOINT_ECHOPARAM_RESULT, response_echoparam, f"Expected {ENDPOINT_ECHOPARAM_RESULT}, got {response_echoparam}")
        self.assertEqual(ENDPOINT_INFO_STEVE_RESULT, response_info, f"Expected {ENDPOINT_INFO_STEVE_RESULT}, got {response_info}")
    
    @test_decorator
    def test_put_delete(self):
        '''
        Test for put() and delete() method
        '''
        restapitool = RestApiTools(URL)
        
        #PUT
        response_info = restapitool.put(ENDPOINT_INFO_BRUCE, body = NEW_RECORD, auth = auth)
        print(response_info)
        self.assertEqual(RESPONSE_201, response_info, f"Expected {RESPONSE_201}, got {response_info}")
        
        #GET
        response_info = restapitool.get(ENDPOINT_INFO_BRUCE, auth = auth)
        print(response_info)
        self.assertEqual(ENDPOINT_INFO_BRUCE_RESULT, response_info, f"Expected {ENDPOINT_INFO_BRUCE_RESULT}, got {response_info}")
    
        #DELETE
        response_info = restapitool.delete(ENDPOINT_INFO_BRUCE, auth = auth)
        print(response_info)
        self.assertEqual(RESPONSE_204, response_info, f"Expected {RESPONSE_204}, got {response_info}")
        
        #GET
        try:
            response_info = restapitool.get(ENDPOINT_INFO_BRUCE, auth = auth)
        except:
            self.assertRaises(RuntimeError)
            
    @test_decorator
    def test_patch(self):
        '''
        Test for update() method
        '''
        restapitool = RestApiTools(URL)
        
        #UPDATE
        response_info = restapitool.patch(ENDPOINT_INFO_STEVE, body = UPDATE_RECORD, auth = auth)
        print(response_info)
        self.assertEqual(ENDPOINT_INFO_STEVE_RESULT_2, response_info, f"Expected {ENDPOINT_INFO_STEVE_RESULT_2}, got {response_info}")

        #GET
        response_info = restapitool.get(ENDPOINT_INFO_STEVE, auth = auth)
        print(response_info)
        self.assertEqual(ENDPOINT_INFO_STEVE_RESULT_2, response_info, f"Expected {ENDPOINT_INFO_STEVE_RESULT_2}, got {response_info}")

        #UPDATE
        response_info = restapitool.patch(ENDPOINT_INFO_STEVE, body = ORIGINAL_RECORD, auth = auth)
        print(response_info)
        self.assertEqual(ENDPOINT_INFO_STEVE_RESULT, response_info, f"Expected {ENDPOINT_INFO_STEVE_RESULT}, got {response_info}")

        #GET
        response_info = restapitool.get(ENDPOINT_INFO_STEVE, auth = auth)
        print(response_info)
        self.assertEqual(ENDPOINT_INFO_STEVE_RESULT, response_info, f"Expected {ENDPOINT_INFO_STEVE_RESULT}, got {response_info}")
            
    @test_decorator
    def test_get_invalid(self):
        '''
        Test for get() method with invalid entry
        '''
        restapitool = RestApiTools(URL)
        try:
            restapitool.get(ENDPOINT_INVALID, auth = auth)
        except:
            self.assertRaises(RuntimeError)     
        
if __name__ == "__main__":
    unittest.main()