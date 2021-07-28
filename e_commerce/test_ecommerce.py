#!/usr/bin/python3.8
############# Script Details #################################################################

# Script Name            :  test_ecommerce.py
# Script version         :  3.8.5
# Prepared By            :  naveen.kumar5@infinite.com
# Created_date           :  16-06-21
# last_modification_date :  18-06-21

##############################################################################################
# Purpose of the script
##############################################################################################
# 1.automating the E-commerce website using automation testing with python,selenium
##############################################################################################
# contents of the script:
##############################################################################################

# 1.Install the selenium

# 2.Write the python code with selenium webdriver using chrome

# 3.This script is designed such that create a account and login in a ecommerce site

# 4.To test the functionality of the given E-commerce website. 
 
# 5.A log file created with the current date time along with message specified.

# 6.Navigate to the corresponding URL and check the current value of username, password and email id and send values of your userid, 
#   emailid from the script and reading the password from text file.
  
# 7.Tested with some test cases on differnt methods

################################################################################################
# Importing required modules for the Script
from e_commerce import Amazonwebpage,data
import pytest
import re
import logging
import os

#Seted path for capture live loggers
pytest.main(args=["-sv", os.path.abspath(__file__)]) 

#Fixed Amazon class browser for testing their methods
@pytest.fixture
def browser():
    config = Amazonwebpage()
    logging.info("Seted Amazon class browser")
    return config

#Testing amazon home page
def test_getpage(browser):
    browser.get_page()
    logging.info("Tested with some test cases for amazon home page")
    assert browser.driver.current_url == "https://www.amazon.in/"
    assert browser.driver.current_url != "https://www.amazon.com/"

#Testing amazon signup page
def test_signup_page(browser):
    browser.get_page()
    browser.sign_up_page()   
    logging.info("Tested with some test cases for amazon signup page")
    assert "www.amazon.in/ap/register?" in browser.driver.current_url
    assert "www.amazon.com/ap/register" not in browser.driver.current_url

#Testing input field of data of signup page
def test_field_data():
    logging.info("Tested with some test cases for input field data of signup page")
    assert re.fullmatch(r'[a-zA-Z0-9 _]*', "Naveen kumar")  != None
    assert re.fullmatch(r'[a-zA-Z0-9 _]*',data['password']) != None
    assert re.fullmatch(r'[0-9]\d{9}$',"8333054404") != None

#Testing input field of signup page
def test_field(browser):
    browser.get_page()
    browser.sign_up_page()
    name=browser.signup_name_field("Naveen kumar")
    mobile=browser.signup_mobile_field("8333054404")
    password=browser.signup_password_field(data["password"])
    logging.info("Tested with some test cases input field of signup page ")
    assert browser.get_field_value(name) == 'Naveen kumar'
    assert browser.get_field_value(mobile) == '8333054404'
    assert browser.get_field_value(password) == data['password']


#Testing  signup page
def test_signup(browser):
    browser.get_page()
    browser.sign_up_page()
    name=browser.signup_name_field("Naveen kumar")
    mobile=browser.signup_mobile_field("8333054404")
    password=browser.signup_password_field(data["password"])
    browser.sign_up()
    logging.info("Tested with some test cases of signup page ")
    assert 'https://www.amazon.in/ap/mobileclaimconflict?' in browser.driver.current_url
    assert 'https://www.amazon.com/ap/mobileclaimconflict?' not in  browser.driver.current_url

#Testing Input field with Negative cases
def test_field_failure(browser):
    browser.get_page()
    browser.sign_up_page()
    name=browser.signup_name_field("")
    mobile=browser.signup_mobile_field("")
    password=browser.signup_password_field("")
    browser.sign_up()
    logging.info("Tested with negative test cases input field ")
    assert browser.field_failure(name,"name") ==  f" got colour rgba(221, 0, 0, 1) pls enter name" , "you have given correct input"
    assert browser.field_failure(password,"password") ==  f" got colour rgba(221, 0, 0, 1) pls enter password" , "you have given correct input" 
    assert browser.field_failure(mobile,"mobile") ==  f" got colour rgba(221, 0, 0, 1) pls enter mobile" , "you have given correct input"


#Testing amazon signin page
def test_signin_page(browser):
    browser.get_page()
    browser.sign_in_page()
    logging.info("Tested with some test cases for amazon signin page")
    assert  "www.amazon.in/ap/signin?" in browser.driver.current_url
    assert  "https://www.amazon.com/ap/signin?" not in browser.driver.current_url

#Testing input field of data of signin page
def test_signin_username_field(browser):
    browser.get_page()
    browser.sign_in_page()
    username=browser.signin_username_field("8333054404")
    logging.info("Tested with some test cases for input field data of signin page")
    assert re.fullmatch(r'[0-9]\d{9}$',"8333054404") != None
    assert browser.driver.current_url == 'https://www.amazon.in/ap/signin'
    assert browser.driver.current_url != 'https://www.amazon.com/ap/signin'

#Testing input field of data of signin page with negative cases
def test_signin_username_field_failure(browser):
    browser.get_page()
    browser.sign_in_page()
    username=browser.signin_username_field("")
    logging.info("Tested with negative test cases for input field data of signin page")
    assert browser.field_failure(username,"username") !=  f" got colour rgba(221, 0, 0, 1) pls enter username" , "you have given correct input"
    assert browser.driver.current_url != 'https://www.amazon.in/ap/signin'

#Testing input field of data of signin page 
def test_signin_password_field(browser):
    browser.get_page()
    browser.sign_in_page()
    username=browser.signin_username_field("8333054404")
    password=browser.signin_password_field(data["password"])
    logging.info("Tested with some cases for input field data of signin page")
    assert re.fullmatch(r'[a-zA-Z0-9 _]*',data['password']) != None
    assert browser.get_field_value(password) == data['password']
    assert browser.driver.current_url != 'https://www.amazon.com/ap/signin'

#Testing input field of data of signin page with negative cases
def test_signin_password_field_failure(browser):
    browser.get_page()
    browser.sign_in_page()
    username=browser.signin_username_field("8333054404")
    password=browser.signin_password_field("")
    browser.signin()
    logging.info("Tested with negative test cases for input field data of signin page")
    assert browser.field_failure(password,"password") !=  f" got colour rgba(221, 0, 0, 1) pls enter password" , "you have given correct input"
    assert browser.driver.current_url == 'https://www.amazon.in/ap/signin'

#Testing signin page of amazon
def test_signin(browser):
    browser.get_page()
    browser.sign_in_page()
    username=browser.signin_username_field("8333054404")
    password=browser.signin_password_field(data['password'])
    browser.signin()
    browser.signout()
    logging.info("Tested with some test cases of amazon siguppage")
    assert "https://www.amazon.in/" in  browser.driver.current_url
    assert "https://www.amazon.com/" not in  browser.driver.current_url


#Testing signoutpage of amazon
def test_signout(browser):
    browser.get_page()
    browser.sign_in_page()
    username=browser.signin_username_field("8333054404")
    password=browser.signin_password_field(data['password'])
    browser.signin()
    browser.signout()
    logging.info("Tested with some test cases of amazon signoutpage")
    assert "www.amazon.in/ap/signin" in browser.driver.current_url
    assert "www.amazon.com/ap/signin" not in browser.driver.current_url

#Testing forgot_password page of amazon
def test_forgotpassword(browser):
    browser.get_page()
    browser.sign_in_page()
    username=browser.signin_username_field("8333054404")
    browser.forgot_password()
    logging.info("Tested with some test cases of amazon forgot passwordpage")
    assert "www.amazon.in/ap/forgotpassword?"  in browser.driver.current_url
    assert "www.amazon.com/ap/forgotpassword?" not in browser.driver.current_url








    
