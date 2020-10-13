*** Settings ***
Documentation     = [MainUI] MainUI Feature Project =
...               This feature enables basic web manipulation features such as click, input text, hover, right click, select, drag and drop, and double click.
...               == Feature Goals ==
...               | =1= | =JIRA Number= | =Name= | =Description= |
...               | =1.1= | PR-276 | MainUI Feature Project | Goal of this feature is to add support for the basic web manipulation features in testautomationpractice.blogspot.com webpage. |
...
...               == Objectives ==
...               | =2= | =TEST OBJECTIVE= | =PRIORITY= |
...               | 2.1 | Test whether the web application is able to perform click function to button elements. | Critical |
...               | 2.2 | Test whether the web application is able to input text to text box elements. | Critical |
...               | 2.3 | Test whether the web application is able to show message upon mouse hover for selected web elements. | Critical |
...               | 2.4 | Test whether the web application is able to perform double click function to select web elements. | Critical |
...               | 2.5 | Test whether the web application is able to perform right click function to select web elements. | Major |
...               | 2.6 | Test whether the web application is able to support drag and drop functionality for select web elements. | Critical |
...               | 2.7 | Test whether the web application is able to show and select from a list of values in selection drop down elements. | Critical |
...
...               == Test Scope ==
...               === Inclusions ===
...               - Functional tests for mouse actions.
...               - Text verifications.
...
...               === Exclusions ===
...               - Error and provocative scenarios involving web elements having unsupported mouse actions.
...               - UI testing for aesthetic, design, web element location.
...               - Non-functional testing including Performance/Stability Testing during normal server operations.
...               - Cross-browser and cross-platform testing
...
...               == Test Environment Requirements ==
...               - testautomationpractice web page running on Chrome
...
...               == Test Approach ==
...               | =4= | =TEST STAGE= | =ENVIRONMENT= | =URL= | =DESCRIPTION= |
...               | 4.1 | System | localhost environment | http://testautomationpractice.blogspot.com | System Feature Testing Environment |