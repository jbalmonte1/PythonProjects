import sys
from unittest.case import SkipTest
sys.path.insert(1, '..\\..')

import unittest
import os
from time import sleep
from AutomationTools import *

URL = "http://testautomationpractice.blogspot.com/"
CHROME_BROWSER = "Chrome"
FIREFOX_BROWSER = "Firefox"
DOWNLOAD_DIRECTORY = "..\Data\Downloads"

ALERT_TEXT = "Press a button!"
FIRST_NAME = "Anthony Edward"
LAST_NAME = "Stark"
PHONE = "+639950134772"
COUNTRY = "America"
CITY = "New York"
EMAIL = "tony.stark@gmail.com"

SPEED = "Faster"
FILE = "PDF file"
NUMBER = "3"
PRODUCT = "Google"
ANIMAL = "Avatar"

HELLO_WORLD = "Hello World!"

def test_decorator(func):
    def print_test_description(*func_args, **func_kwargs):
        print('================')
        print(f'Executing {func.__name__}'.upper())
        print('================')
        return func(*func_args, **func_kwargs)
    return print_test_description

class UnitTestSeleniumWebAutomation(unittest.TestCase):
    @SkipTest
    @test_decorator
    def test_click(self):
        '''
        Test for click() and locate_element() method
        '''
        swat = SeleniumWebAutomationTools(CHROME_BROWSER, downloadDir = DOWNLOAD_DIRECTORY)
        swat.open_url(URL)
        
        swat.click(testAutomationPracticeBlogspot.main.alert_button)
        sleep(3)
        self.assertEqual(swat.get_alert_text(), ALERT_TEXT, f"Unable to click the button. Expected alert to pop up with text {ALERT_TEXT} but got {swat.get_alert_text()}.")
        swat.accept_alert()
        swat.close_all_browsers()
    
    @SkipTest
    @test_decorator
    def test_input_text(self):
        '''
        Test for input_text() and get_text() method
        '''
        swat = SeleniumWebAutomationTools(CHROME_BROWSER, downloadDir = DOWNLOAD_DIRECTORY)
        swat.open_url(URL)
        
        swat.input_text(testAutomationPracticeBlogspot.main.first_name_textfield, FIRST_NAME, frame = testAutomationPracticeBlogspot.main.frame)
        swat.input_text(testAutomationPracticeBlogspot.main.last_name_textfield, LAST_NAME, frame = testAutomationPracticeBlogspot.main.frame)
        swat.input_text(testAutomationPracticeBlogspot.main.phone_textfield, PHONE, frame = testAutomationPracticeBlogspot.main.frame)
        swat.input_text(testAutomationPracticeBlogspot.main.country_textfield, COUNTRY, frame = testAutomationPracticeBlogspot.main.frame)
        swat.input_text(testAutomationPracticeBlogspot.main.city_textfield, CITY, frame = testAutomationPracticeBlogspot.main.frame)
        swat.input_text(testAutomationPracticeBlogspot.main.email_textfield, EMAIL, frame = testAutomationPracticeBlogspot.main.frame)
        
        _first_name = swat.get_text(testAutomationPracticeBlogspot.main.first_name_textfield, frame = testAutomationPracticeBlogspot.main.frame)
        _last_name = swat.get_text(testAutomationPracticeBlogspot.main.last_name_textfield, frame = testAutomationPracticeBlogspot.main.frame)
        _phone = swat.get_text(testAutomationPracticeBlogspot.main.phone_textfield, frame = testAutomationPracticeBlogspot.main.frame)
        _country = swat.get_text(testAutomationPracticeBlogspot.main.country_textfield, frame = testAutomationPracticeBlogspot.main.frame)
        _city = swat.get_text(testAutomationPracticeBlogspot.main.city_textfield, frame = testAutomationPracticeBlogspot.main.frame)
        _email = swat.get_text(testAutomationPracticeBlogspot.main.email_textfield, frame = testAutomationPracticeBlogspot.main.frame)
        
        self.assertEqual(_first_name, FIRST_NAME, f"Unable to input text. Expected {FIRST_NAME} got {_first_name}.")
        self.assertEqual(_last_name, LAST_NAME, f"Unable to input text. Expected {LAST_NAME} got {_last_name}.")
        self.assertEqual(_phone, PHONE, f"Unable to input text. Expected {PHONE} got {_phone}.")
        self.assertEqual(_country, COUNTRY, f"Unable to input text. Expected {COUNTRY} got {_country}.")
        self.assertEqual(_city, CITY, f"Unable to input text. Expected {CITY} got {_city}.")
        self.assertEqual(_city, CITY, f"Unable to input text. Expected {EMAIL} got {_email}.")
    
        sleep(3)
        swat.close_all_browsers()
    
    @SkipTest
    @test_decorator
    def test_hover(self):
        '''
        Test for hover() method
        '''
        swat = SeleniumWebAutomationTools(CHROME_BROWSER, downloadDir = DOWNLOAD_DIRECTORY)
        swat.open_url(URL)
        
        swat.hover(testAutomationPracticeBlogspot.main.hover)
        sleep(3)
        self.assertIsNotNone(swat.locate_element(testAutomationPracticeBlogspot.main.tooltip), f"Unable to hover mouse over selector.")
        swat.close_all_browsers()
    
    @SkipTest
    @test_decorator
    def test_double_click(self):
        '''
        Test for double_click() method
        '''
        swat = SeleniumWebAutomationTools(CHROME_BROWSER, downloadDir = DOWNLOAD_DIRECTORY)
        swat.open_url(URL)
        
        swat.double_click(testAutomationPracticeBlogspot.main.double_click)
        sleep(3)
        self.assertEqual(HELLO_WORLD, swat.get_text(testAutomationPracticeBlogspot.main.field2), f"Unable to double click mouse over selector.")
        swat.close_all_browsers()
    
    @SkipTest    
    @test_decorator
    def test_right_click(self):
        '''
        Test for right_click(), select_from_context_menu(), and locate_element_from_context_menu() method
        '''
        swat = SeleniumWebAutomationTools(CHROME_BROWSER, downloadDir = DOWNLOAD_DIRECTORY)
        swat.open_url(URL)
        
        swat.right_click(testAutomationPracticeBlogspot.main.right_click, frame = testAutomationPracticeBlogspot.main.frame)
        sleep(3)
        
        swat.close_all_browsers()
    
    @SkipTest
    @test_decorator
    def test_drag_and_drop(self):
        '''
        Test for drag_and_drop() method
        '''
        swat = SeleniumWebAutomationTools(CHROME_BROWSER, downloadDir = DOWNLOAD_DIRECTORY)
        swat.open_url(URL)
        
        sleep(3)
        swat.drag_and_drop(testAutomationPracticeBlogspot.main.drag_src, testAutomationPracticeBlogspot.main.drag_dest)
        sleep(3)
        self.assertIsNotNone(swat.locate_element(testAutomationPracticeBlogspot.main.dropped), f"Unable to drag and drop element from source to target selector.")
        swat.close_all_browsers()
        
    @test_decorator
    def test_select(self):
        '''
        Test for select() method
        '''
        swat = SeleniumWebAutomationTools(CHROME_BROWSER, downloadDir = DOWNLOAD_DIRECTORY)
        swat.open_url(URL)
        
        swat.select(testAutomationPracticeBlogspot.main.speed_menu, SPEED)
        swat.select(testAutomationPracticeBlogspot.main.file_menu, FILE)
        swat.select(testAutomationPracticeBlogspot.main.number_menu, NUMBER)
        swat.select(testAutomationPracticeBlogspot.main.product_menu, PRODUCT)
        swat.select(testAutomationPracticeBlogspot.main.animal_menu, ANIMAL)
        sleep(3)

        swat.close_all_browsers()
        
if __name__ == '__main__':
    unittest.main()