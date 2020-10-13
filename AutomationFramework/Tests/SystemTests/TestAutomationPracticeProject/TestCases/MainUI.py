import sys
sys.path.insert(1, '..\\..\\..\\..')
sys.path.insert(1, '..\\..\\..\\..\\Resources')
sys.path.insert(1, '..\\..\\..\\..\\Config')

import os
from time import sleep

import UniversalResources
from AutomationTools import *
from Common_config import *
from Localhost_config import *

def test_click():
    '''
    Test for click() and locate_element() method
    '''
    swat = SeleniumWebAutomationTools(CHROME_BROWSER, downloadDir = DOWNLOAD_DIRECTORY)
    swat.open_url(TESTAUTOMATIONPRACTICE_URL)
     
    swat.click(testAutomationPracticeBlogspot.main.alert_button)
    sleep(3)
    TestValidation.assertEqual(swat.get_alert_text(), ALERT_TEXT, f"Unable to click the button. Expected alert to pop up with text {ALERT_TEXT} but got {swat.get_alert_text()}.")
    swat.accept_alert()
    swat.close_all_browsers()

def test_input_text():
    '''
    Test for input_text() and get_text() method
    '''
    swat = SeleniumWebAutomationTools(CHROME_BROWSER, downloadDir = DOWNLOAD_DIRECTORY)
    swat.open_url(TESTAUTOMATIONPRACTICE_URL)
    
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
    
    TestValidation.assertEqual(_first_name, FIRST_NAME, f"Unable to input text. Expected {FIRST_NAME} got {_first_name}.")
    TestValidation.assertEqual(_last_name, LAST_NAME, f"Unable to input text. Expected {LAST_NAME} got {_last_name}.")
    TestValidation.assertEqual(_phone, PHONE, f"Unable to input text. Expected {PHONE} got {_phone}.")
    TestValidation.assertEqual(_country, COUNTRY, f"Unable to input text. Expected {COUNTRY} got {_country}.")
    TestValidation.assertEqual(_city, CITY, f"Unable to input text. Expected {CITY} got {_city}.")
    TestValidation.assertEqual(_city, CITY, f"Unable to input text. Expected {EMAIL} got {_email}.")

    sleep(3)
    swat.close_all_browsers()

def test_hover():
    '''
    Test for hover() method
    '''
    swat = SeleniumWebAutomationTools(CHROME_BROWSER, downloadDir = DOWNLOAD_DIRECTORY)
    swat.open_url(TESTAUTOMATIONPRACTICE_URL)
    
    swat.hover(testAutomationPracticeBlogspot.main.hover)
    sleep(3)
    TestValidation.assertIsNotNone(swat.locate_element(testAutomationPracticeBlogspot.main.tooltip), f"Unable to hover mouse over selector.")
    swat.close_all_browsers()

def test_double_click():
    '''
    Test for double_click() method
    '''
    swat = SeleniumWebAutomationTools(CHROME_BROWSER, downloadDir = DOWNLOAD_DIRECTORY)
    swat.open_url(TESTAUTOMATIONPRACTICE_URL)
    
    swat.double_click(testAutomationPracticeBlogspot.main.double_click)
    sleep(3)
    TestValidation.assertEqual(HELLO_WORLD, swat.get_text(testAutomationPracticeBlogspot.main.field2), f"Unable to double click mouse over selector.")
    swat.close_all_browsers()
   
def test_right_click():
    '''
    Test for right_click(), select_from_context_menu(), and locate_element_from_context_menu() method
    '''
    swat = SeleniumWebAutomationTools(CHROME_BROWSER, downloadDir = DOWNLOAD_DIRECTORY)
    swat.open_url(TESTAUTOMATIONPRACTICE_URL)
    
    swat.right_click(testAutomationPracticeBlogspot.main.right_click, frame = testAutomationPracticeBlogspot.main.frame)
    sleep(3)
    
    swat.close_all_browsers()

def test_drag_and_drop():
    '''
    Test for drag_and_drop() method
    '''
    swat = SeleniumWebAutomationTools(CHROME_BROWSER, downloadDir = DOWNLOAD_DIRECTORY)
    swat.open_url(TESTAUTOMATIONPRACTICE_URL)
    
    sleep(3)
    swat.drag_and_drop(testAutomationPracticeBlogspot.main.drag_src, testAutomationPracticeBlogspot.main.drag_dest)
    sleep(3)
    TestValidation.assertIsNotNone(swat.locate_element(testAutomationPracticeBlogspot.main.dropped), f"Unable to drag and drop element from source to target selector.")
    swat.close_all_browsers()
    
def test_select():
    '''
    Test for select() method
    '''
    swat = SeleniumWebAutomationTools(CHROME_BROWSER, downloadDir = DOWNLOAD_DIRECTORY)
    swat.open_url(TESTAUTOMATIONPRACTICE_URL)
    
    swat.select(testAutomationPracticeBlogspot.main.speed_menu, SPEED)
    swat.select(testAutomationPracticeBlogspot.main.file_menu, FILE)
    swat.select(testAutomationPracticeBlogspot.main.number_menu, NUMBER)
    swat.select(testAutomationPracticeBlogspot.main.product_menu, PRODUCT)
    swat.select(testAutomationPracticeBlogspot.main.animal_menu, ANIMAL)
    sleep(3)

    swat.close_all_browsers()