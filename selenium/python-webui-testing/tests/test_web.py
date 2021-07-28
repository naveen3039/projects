##########################################################################################################
#Script Details

# Script name               :       test_web.py
# Script version            :       python 3.8.3
# Prepared By               :       naveen.kumar5@infinite.com
# Create Date               :       03-06-21
# Last Modification Date    :       04-06-21

##############################################################################################
#Purpose of the script
##############################################################################################

#1.Automating the website using automation testing with python,selenium

##############################################################################################
#Below points considered in the script:
##############################################################################################

#1.Install the selenium

#2.Write the python code with selenium webdriver using chrome

#3.Creating a pages folder having __init__.py , result.py, search.py in it.

#4.In tests create the confest.py for fixtures, browser automating

#5.Read Config files in Python Selenium Tests in conftest.py

#6.Tested some cases using automating the browser

#################################################################################################


import pytest
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
import logging

# The setting basic configuration of log_file format and level
logging.basicConfig(
    filename="Test_automation.log",
    filemode="w",
    format="%(asctime)s :: %(message)s",
    level=logging.INFO
    )

logging.info('created a test function for duckduckgo web')
def test_basic_duckduckgo_search(browser):
  # Set up test case data
  PHRASE = 'panda'
  logging.info("Taking panda as phrase")
  # Search for the phrase
  search_page = DuckDuckGoSearchPage(browser)
  logging.info('The function calls the browser')
  search_page.load()
  logging.info('loads specified url ')
  search_page.search(PHRASE)
  logging.info('Started searching specified phrase')
  # Verify that results appear
  result_page = DuckDuckGoResultPage(browser)
  logging.info('Result getting loaded')
  assert result_page.link_div_count() > 0
  assert result_page.phrase_result_count(PHRASE) > 0
  assert result_page.search_input_value() == PHRASE
logging.info('End of all test cases and program')