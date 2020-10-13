# Test Automation Framework Toolkit (TAFT)
Base infrastructure test automation framework toolkit

## Description
This framework contains base classes and methods for automating web-based (front-end) and back-end applications

## Features
   1. Front-end web application user action automation
   2. Virtual machine remote back-end access and shell (BASH) operations
   3. PostgreSQL query automation
   4. REST API / HTTP Request query automation
   5. Basic JSON processing
   6. Data ingestion

## Installation Requirements
   1. [Python 3.8.3](https://www.python.org/ftp/python/3.8.3/)
   2. [PIP] (https://pypi.org/project/pip/)
   3. [Chrome 85.0] (https://www.google.com/chrome/)
   4. [Firefox 81.0](https://www.mozilla.org/en-US/firefox/81.0/releasenotes/)
   5. [Chrome Driver ](https://chromedriver.storage.googleapis.com/index.html?path=85.0.4183.87/) - already included in library
   6. [Gecko Driver v0.27.0](https://github.com/mozilla/geckodriver/releases) - already included in library

## Installation
   1. Install Chrome or Firefox browsers whichever will be needed for testing
   2. Install Python and PIP
   3. Add python path to PATH in environment variables
   4. Go to Utility directory and nstall additional Python libraries / dependencies: pip install -r requirements.txt
   5. Go to Config directory and configure PostgreSQL server information in Localhost_config.py. Optionally, define additional test configuration data in Common_config.py

## Test Case Execution
   1. Within Tests directory, execute in console `robot --pythonpath <path to AutomationFramework directory> --debugfile debug.txt --loglevel <log level i.e. debug> --outputdir <path to target output directory> --include <included Robot tags> --exclude <excluded Robot tags> -t <test case to run> .`
   2. Alternatively, sample execution would be to run run.bat in AutomationFramework\Tests\SystemTests\TestAutomationPracticeProject\TestCases\. Results would be located in Results directory one level above it.