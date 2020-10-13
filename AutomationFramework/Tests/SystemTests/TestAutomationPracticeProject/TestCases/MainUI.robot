*** Settings ***
Library           MainUI.py
Library           ../../../../Resources/UniversalResources.py
Suite Setup       Common Suite Setup
Suite Teardown    Common Suite Teardown

*** Test Cases ***
ST_01_01_0001 Test Click
    [Tags]    SystemTesting    WebTesting    TestAutomationPractice    Regression    Smoke
    Test Click
    
ST_01_01_0002 Test Input Text
    [Tags]    SystemTesting    WebTesting    TestAutomationPractice    Regression    Smoke
    Test Input Text
    
ST_01_01_0003 Test Hover
    [Tags]    SystemTesting    WebTesting    TestAutomationPractice    Regression
    Test Hover
    
ST_01_01_0004 Test Double Click
    [Tags]    SystemTesting    WebTesting    TestAutomationPractice    Regression    Smoke
    Test Double Click
    
ST_01_01_0005 Test Right Click
    [Tags]    SystemTesting    WebTesting    TestAutomationPractice    Regression
    Test Right Click
    
ST_01_01_0006 Test Drag And Drop
    [Tags]    SystemTesting    WebTesting    TestAutomationPractice    Regression    Smoke
    Test Drag And Drop
    
ST_01_01_0007 Test Select
    [Tags]    SystemTesting    WebTesting    TestAutomationPractice    Regression    Smoke
    Test Select