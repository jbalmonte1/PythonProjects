'''
Created on 27 Aug 2020

@author: jalmonte
'''

import sys
from selenium.webdriver.support.wait import WebDriverWait
sys.path.insert(1, "..")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

URL = "http://testautomationpractice.blogspot.com/"
URL_frame = "https://www.amazon.in"
DRIVERLOCATION = "..\AutomationTools\Drivers\chromedriver.exe"

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

selectors = {
    "alert_button": "button:contains('Click Me')",
    "new_window": "a.feed-link",
    "hover": "a:contains('Tooltips')",
    "double_click": "button:contains('Copy Text')",
    "drag_src": "div#draggable",
    "drag_dest": "div#droppable",
    "file_upload": "input.file_upload",
    "first_name_textfield": "#RESULT_TextField-1",
    "last_name_textfield": "#RESULT_TextField-2",
    "phone_textfield": "#RESULT_TextField-3",
    "country_textfield": "#RESULT_TextField-5",
    "city_textfield": "#RESULT_TextField-6",
    "email_textfield": "#RESULT_TextField-7",
    "frame": "frame-one1434677811"
}


def query_builder(selector):
    return "$(\"{}\").get(0)".format(selector)

if __name__ == "__main__":
        
    driver = webdriver.Chrome(DRIVERLOCATION)
    driver.maximize_window()
    
    driver.get(URL)
    #driver.implicitly_wait(10)
    
    #driver.execute_script(INJECTJQUERY)
    #sleep(5)
    
    #driver.switch_to.frame(selectors["frame"])
    
    #query = query_builder(selectors["country_textfield"])
    #print(query)
    #loc = driver.execute_script("return {}".format(query))
    #loc.send_keys("Philippines")
    #sleep(5)
    #print(loc.get_attribute("value"))

    #_src_loc = driver.execute_script("return {}",format("$('#draggable')"))
    #_dest_loc = driver.execute_script("return {}",format("$('#droppable')"))
    sleep(3)
    _src_loc = driver.find_element_by_xpath('//*[@id="draggable"]')
    _dest_loc = driver.find_element_by_xpath('//*[@id="droppable"]')
    actions = ActionChains(driver)
    actions.drag_and_drop(_src_loc, _dest_loc).perform()
    
    sleep(3)
    #driver.execute_script("arguments[0].scrollIntoView();", loc)
    #loc.send_keys("C:/Users/jbalm/Desktop/test.txt")
    
    driver.quit()
