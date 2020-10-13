import sys
sys.path.insert(1, '..\\..')

import unittest
import datetime
from AutomationTools import *

URL = "https://en.wikipedia.org/wiki/Avenger"

def test_decorator(func):
    def print_test_description(*func_args, **func_kwargs):
        print('================')
        print(f'Executing {func.__name__}'.upper())
        print('================')
        return func(*func_args, **func_kwargs)
    return print_test_description

class UnitTestHTMLParser(unittest.TestCase):
    @test_decorator
    def test_feed(self):
        '''
        Test for HTMLParser class constructor
        '''
        htmlparsertools = HTMLParserTools(URL)
        print(htmlparsertools.get_content())
        
if __name__ == "__main__":
    unittest.main()