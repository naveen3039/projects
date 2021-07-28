#!/usr/bin/python3.8
############# Script Details #################################################################

# Script Name            :  e_commerce.py
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

# 4.To check the functionality of the given E-commerce website. 
 
# 5.A log file created with the current date time along with message specified.

# 6.Navigate to the corresponding URL and check the current value of username, password and email id and send values of your userid, 
#   emailid from the script and reading the password from text file.

################################################################################################
# Importing required modules for the Script.
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import json
import time
import logging


# The setting basic configuration of log_file format and level
logging.basicConfig(
    filename="class_room.log",
    filemode="w",
    format="%(asctime)s :: %(message)s",
    level=logging.INFO,
)

#Accessing a json file for access password
with open('config.json') as config_file:
    logging.info('opened a config.json file and collected data')
    data = json.load(config_file)

#Automating webbrowser without displaying  
op = Options()
op.add_argument('headless')

#The setting of basic configuration of seleninum 
browser = {
"URL" :"https://www.amazon.in/",
"driver" : Chrome(options= op)
}

logging.info("Setted basic configurations Automating webbrowser without displaying")

#Created a class Amazon
class Amazon:
    
    #The intialising some values 
    def __init__(self):
        self.url=browser["URL"]
        self.driver=browser["driver"]
        self.action=ActionChains(self.driver)
        self.driver.implicitly_wait(30)
        logging.info('webdriver of chorme has been configured')
    
    #Getting the amazon home page
    def get_page(self):
        self.driver.get(self.url)
        logging.info('Getting amazon home page')
    
    #Created a method which is redirecting signup page
    def sign_up_page(self):
        self.signup_page_cursor = self.driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[3]/div/a[2]")
        self.action.move_to_element(self.signup_page_cursor).perform()
        self.signup_page=self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[3]/div[2]/div[2]/div/div[1]/div/div/a').click()
        logging.info("Created a method which is redirecting signup page")
    

    #Created a method which redirecting signup page  user name field
    def signup_name_field(self,name):
        self.name=self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[1]/input')
        self.name.send_keys(name)
        logging.info('Created a method which redirecting signup page  user name field')
        return self.name
    
    #Created a method which redirecting signup page  mobile field
    def signup_mobile_field(self,mobile):
        self.mobile=self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[2]/div/div/div/div[2]/input")
        self.mobile.send_keys(mobile)
        logging.info('Created a method which redirecting signup page  mobile field')
        return self.mobile
    
    
    #Created a method which redirecting signup page  password field
    def signup_password_field(self,password):    
        self.password=self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[4]/div/input")
        self.password.send_keys(password)
        logging.info('Created a method which redirecting signup page  password field')
        return self.password
    
    #Created a method which redirecting signup submit page
    def sign_up(self):
        time.sleep(3)
        sign_up=self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[6]/span/span/input").click()
        logging.info('redirected signup success_page')
        time.sleep(3)
    
    #Created a method which quit from browser
    def quit(self):
        logging.info("brower was closed")
        self.driver.quit() 

    #Created a method which to get input field value
    def get_field_value(self,field):
        logging.info("GETTNG REQUSTED VALUE")
        return field.get_attribute('value')
    
    #Created a method checking INPUT field 
    def field_failure(self,field_name,name):
        #Checking whether error in outerhtml
        if "error" in field_name.get_attribute('outerHTML'):  
            #Checking colour property for errors
            if field_name.value_of_css_property('border-bottom-color') == "rgba(221, 0, 0, 1)":
                logging.info(f" got colour rgba(221, 0, 0, 1) pls enter {name}")
                return f" got colour rgba(221, 0, 0, 1) pls enter {name}"
    

#Created a class Amazonwebpage inherits properties from Amazon class
class Amazonwebpage(Amazon):
     
    #The intialising some values  
    def __init__(self):
        super().__init__()
        logging.info("Collecting all the constructed properties of Amazon class")
    
    #Created a method which is redirecting signin page
    def sign_in_page(self):
        self.signin_page = self.driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[3]/div/a[2]").click()
        logging.info("Created a method which is redirecting signin page")

    #Created a method which is redirecting signin username field
    def signin_username_field(self,name):
        self.username = self.driver.find_element_by_id("ap_email")
        self.username.send_keys(name)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[2]/span/span/input").click()
        logging.info('Created a method which is redirecting signin username field')
        return self.username
    
    #Created a method which is redirecting signin password field
    def signin_password_field(self,password):
        self.password = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div/form/div/div[1]/input')
        self.password.send_keys(password)
        time.sleep(3)
        logging.info('Created a method which is redirecting signin password field')
        return self.password
    
    #Created a method which is redirecting to forgot password link
    def forgot_password(self):
        time.sleep(3)
        self.forgot_password = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[1]/div[1]/div[2]/a").click()
        time.sleep(3)
        logging.info("Created a method which is redirecting to forgot password link")
    
    #Created a method which is redirecting to signin page
    def signin(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div/form/div/div[2]/span/span/input').click()
        logging.info("Created a method which is redirecting to sign page link")
    
    #Created a method which is redirecting to signout link
    def signout(self):
        self.sign_out_cursor = self.driver.find_element_by_xpath('//*[@id="nav-link-accountList"]')
        self.action=ActionChains(self.driver)
        self.action.move_to_element(self.sign_out_cursor).perform()
        time.sleep(3)
        logging.info('Created a method which is redirecting to signout link')
        signout=self.driver.find_element_by_xpath('//*[@id="nav-item-signout"]').click()
