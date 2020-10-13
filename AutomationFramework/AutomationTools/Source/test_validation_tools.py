'''
Created on 28 Sep 2020

@author: jalmonte
'''

class TestValidation():
    @staticmethod
    def assertEqual(val1, val2, message = None):
        if not val1 == val2:
            raise AssertionError(message)
        
    @staticmethod
    def assertNotEqual(val1, val2, message = None):
        if not val1 != val2:
            raise AssertionError(message)
        
    @staticmethod
    def assertIsNone(val, message = None):
        if not val == None:
            raise AssertionError(message)
        
    @staticmethod
    def assertIsNotNone(val, message = None):
        if val == None:
            raise AssertionError(message)