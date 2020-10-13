'''
Created on 7 Apr 2020

@author: jalmonte
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.common.exceptions import WebDriverException
from time import sleep

import os
ABSPATH = '\\'.join(os.path.abspath(__file__).split('\\')[0:-2])

CHROMEDRIVER = f"{ABSPATH}\Drivers\chromedriver.exe"
FIREFOXDRIVER = f"{ABSPATH}\Drivers\geckodriver.exe"

INJECTJQUERY = """
    javascript:(function() {
        function l(u, i) {
            var d = document;
            if (!d.getElementById(i)) {
                var s = d.createElement('script');
                s.src = u;
                s.id = i;
                d.body.appendChild(s);
            }
        }
        l('//code.jquery.com/jquery-3.2.1.min.js', 'jquery')
    })();
"""

class SeleniumWebAutomationTools():
    def __init__(self, browser = "Chrome", **options):
        '''
        initializes web driver to either Chrome or Firefox and optionally sets default download directory
        '''
        if browser == "Chrome":            
            if options:
                _chromeoptions = ChromeOptions()
                if "deviceName" in options.keys():
                    _chromeoptions.add_experimental_option("mobileEmulation", { "deviceName": options["deviceName"] })
                if "downloadDir" in options.keys():
                    _chromeoptions.add_experimental_option("prefs", {"download.default_directory": options["downloadDir"]})
                self._driver = webdriver.Chrome(executable_path = CHROMEDRIVER, options = _chromeoptions)
            else:
                self._driver = webdriver.Chrome(executable_path = CHROMEDRIVER)
        elif browser == "Firefox":
            _fp = webdriver.FirefoxProfile()
            _fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf")
            _fp.set_preference("browser.download.manager.showWhenStarting", False)
            _fp.set_preference("browser.download.folderList", 2)
            _fp.set_preference("pdfjs.disabled", True)
            if downloadDir:
                _fp.set_preference("browser.download.dir", downloadDir)
            self._driver = webdriver.Firefox(executable_path = FIREFOXDRIVER, firefox_profile = _fp)
        else:
            raise RuntimeError("Unsupported or unknown browser with no available driver.")
        
        self._actions = ActionChains(self._driver)
        self._driver.maximize_window()
    
    #Enablers
    
    def open_url(self, url, retry = 5, interval = 5, wait_time = 10):
        '''
        opens a given URL
        '''
        
        for i in range(retry):
            self._driver.get(url)
            if "404 Not Found" in self._driver.title:
                print("Unable to open url: {}".format(url))
                sleep(interval)
                continue
            else:
                self._driver.implicitly_wait(wait_time)
                break
        else:
            raise RuntimeError("Retry expired. Unable to open specified url.")
        
    def get_title(self):
        '''
        returns the title of the currently opened session
        '''
        return self._driver.title
        
    def close_browser(self):
        '''
        closes the current active tab
        '''
        self._driver.close()
        
    def close_all_browsers(self):
        '''
        closes all tabs
        '''
        self._driver.quit()
    
    def _query_builder(self, selector):
        '''
        Takes in a jquery selector and builds jquery syntax
        '''
        return "$(\"{}\").get(0)".format(selector)
        
    def _inject_jquery(self):
        '''
        automatically inject jquery to browser
        '''
        self._driver.execute_script(INJECTJQUERY)
        sleep(3)
    
    #Element Locators
        
    def locate_element(self, selector, frame = None, retry = 5, interval = 1):
        '''
        returns the web element given a jquery selector
        '''
        query = self._query_builder(selector)
        
        self._driver.switch_to.default_content()
        if frame:
            self._driver.switch_to.frame(frame)
        for i in range(retry):
            try:
                _web_element = self._driver.execute_script("return {}".format(query))
                if _web_element:
                    #self._driver.execute_script("arguments[0].scrollIntoView();", _web_element)
                    return _web_element
                else:
                    sleep(interval)
            except WebDriverException as e:
                if "not defined" in str(e) or "unsupported pseudo: regex" in str(e):
                    self._inject_jquery()
                else:
                    print("Locate Exception: {}".format(str(e)))
                    sleep(interval)
                continue
        else:
            raise RuntimeError("Retry expired. Unable to find specified element.")        
    
    #Element Verifications
            
    def is_displayed(self, selector, frame = None, retry = 5, interval = 1):
        '''
        verifies if a web element given by selector is displayed
        '''
        self.locate_element(selector, frame, retry, interval).is_displayed()

    def is_enabled(self, selector, frame = None, retry = 5, interval = 1):
        '''
        verifies if a web element given by selector is enabled
        '''
        self.locate_element(selector, frame, retry, interval).is_enabled()
        
    def is_selected(self, selector, frame = None, retry = 5, interval = 1):
        '''
        verifies if a web element given by selector is selected
        '''
        self.locate_element(selector, frame, retry, interval).is_selected()
        
    def is_image_uploaded(self, selector, filename, frame = None, retry = 5, interval = 1):
        '''
        verifies if an image is already uploaded to specified selector
        '''
        _loc = self.locate_element(selector, frame, retry, interval)
        for _l in _loc:
            _image_source = _l.get_attribute("src")
            if filename in _image_source:
                return True
            else:
                continue
        else:
            return False

    #User Actions

    def input_text(self, selector, text, frame = None, retry = 5, interval = 1):
        '''
        inputs text to given element
        '''
        _loc = self.locate_element(selector, frame, retry, interval)
        _loc.clear()
        _loc.send_keys(text)
        
    def get_text(self, selector, frame = None, retry = 5, interval = 1):
        '''
        gets text from a given element
        '''
        return self.locate_element(selector, frame, retry, interval).get_attribute('value')

    def click(self, selector, frame = None, retry = 5, interval = 1):
        '''
        clicks a particular web element given by selector
        '''
        self.locate_element(selector, frame, retry, interval).click()

    def hover(self, selector, frame = None, retry = 5, interval = 1):
        '''
        hovers mouse over a particular web element
        '''
        _loc = self.locate_element(selector, frame, retry, interval)
        self._actions.move_to_element(_loc).perform()
        
    def double_click(self, selector, frame = None, retry = 5, interval = 1):
        '''
        double clicks a particular web element
        '''
        _loc = self.locate_element(selector, frame, retry, interval)
        self._actions.double_click(_loc).perform()
        
    def right_click(self, selector, frame = None, retry = 5, interval = 1):
        '''
        right clicks a particular web element
        '''
        _loc = self.locate_element(selector, frame, retry, interval)
        self._actions.context_click(_loc).perform()
        
    def drag_and_drop(self, src_selector, dest_selector, src_frame = None, dest_frame = None, retry = 5, interval = 1):
        '''
        drag and drops a particular web element from source to destination
        '''
        _src_loc = self.locate_element(src_selector, src_frame, retry, interval)
        _dest_loc = self.locate_element(dest_selector, dest_frame, retry, interval)
        self._actions.drag_and_drop(_src_loc, _dest_loc).perform()

    def select(self, selector, text, frame = None, retry = 5, interval = 1):
        '''
        selects a value from a given drop down list
        '''
        _loc = self.locate_element(selector, frame, retry, interval)
        
        Select(_loc).select_by_visible_text(text)
        
    def scroll_element_to_view(self, selector, frame = None, retry = 5, interval = 1):
        '''
        scrolls window until element comes into view
        '''
        _loc = self.locate_element(selector, frame, retry, interval)
        self._driver.execute_script("arguments[0].scrollIntoView();", _loc)
        
    def upload_file(self, selector, file_name, frame = None, retry = 5, interval = 1):
        '''
        uploads a given file to a web element
        '''
        _loc = self.locate_element(selector, frame, retry, interval)
        _loc.clear()
        _loc.send_keys(file_name)
    
    #Alert Management
        
    def accept_alert(self):
        '''
        accepts the actively visible alert
        '''
        self._driver.switch_to.alert.accept()

    def dismiss_alert(self):
        '''
        dismisses the actively visible alert
        '''
        self._driver.switch_to.alert.dismiss()

    def input_text_to_alert(self, text):
        '''
        inputs text to alert
        '''
        self._driver.switch_to.alert.send_keys(text)
    
    def get_alert_text(self):
        '''
        returns the alert text
        '''
        return self._driver.switch_to.alert.text
    
    #Window Handle Management
    
    def switch_to_window(self, title):
        '''
        switches to a specific window given by its title
        '''
        for handle in self._driver.window_handles:
            self._driver.switch_to.window(handle)
            if self._driver.title == title:
                break
        else:
            raise RuntimeError("Unable to find window with title: {}".format(title))
        
    #Tools
    
    def capture_page_screenshot(self, filename, directory = None):
        '''
        captures page screenshot and store it in directory as provided filename
        '''
        if directory:
            if not os.path.isdir(directory):
                raise RuntimeError("Invalid or missing directory: {}".format(directory))
            else:
                _path = '{}/{}'.format(directory, filename)
        else:
            _path = '{}/{}'.format(os.getcwd().replace('\\', '/'), filename)
        print("Saving screenshot as: {}".format(_path))
        self._driver.save_screenshot(_path)