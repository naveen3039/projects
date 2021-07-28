from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
import re
import json

with open('config.json') as config_file:
    data = json.load(config_file)


URL = "https://www.amazon.in/"
driver = Chrome()
driver.get(URL)
driver.implicitly_wait(15)
action = ActionChains(driver)

signout= driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[3]/div/a[2]")
action.move_to_element(signout).perform()
driver.find_element_by_xpath('/html/body/div[1]/header/div/div[3]/div[2]/div[2]/div/div[1]/div/div/a').click()

name=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[1]/input')
if "error" in name.get_attribute('outerHTML'):   
    if name.value_of_css_property('border-bottom-color') == "rgba(221, 0, 0, 1)":
        print(f" got colour rgba(221, 0, 0, 1) pls enter username or email")
name.send_keys('Naveen kumar')

mobile=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[2]/div/div/div/div[2]/input")
if "error" in mobile.get_attribute('outerHTML'): 
    if mobile.value_of_css_property('border-bottom-color') == "rgba(221, 0, 0, 1)":
        print(f" got colour rgba(221, 0, 0, 1) pls enter mobile")
mobile.send_keys('9182945740')

password=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[4]/div/input")
if "error" in password.get_attribute('outerHTML'):  
    if password.value_of_css_property('border-bottom-color') == "rgba(221, 0, 0, 1)":
        print(f" got colour rgba(221, 0, 0, 1) pls enter password")
password.send_keys(data["password"])

if re.fullmatch(r'[a-zA-Z0-9 _]*',name.get_attribute('value')):
    if re.fullmatch(r'[a-zA-Z0-9_]*',password.get_attribute('value')):
        if re.fullmatch(r'[0-9]\d{9}$',mobile.get_attribute('value')):
            driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[6]/span/span/input").click()
            print('account_created')
            signup_sucess='https://www.amazon.in/ap/mobileclaimconflict?'
            if signup_sucess in driver.current_url:
                driver.get(URL)

if driver.current_url == URL:            
def check():
    signin= driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[3]/div/a[2]").click()
    username = driver.find_element_by_id("ap_email")
    username.send_keys("8333054404")
    cont= driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[2]/span/span/input').click()
    if "error" in username.get_attribute('outerHTML'):    
        if username.value_of_css_property('border-bottom-color') == "rgba(221, 0, 0, 1)":
            print(f" got colour rgba(221, 0, 0, 1) pls enter username or email")
    password = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div/form/div/div[1]/input')
    return password
check()

forgot_password = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[1]/div[1]/div[2]/a").click()
forgot_link="www.amazon.in/ap/forgotpassword?"
if  forgot_link in driver.current_url:
    print('redirected to forgot password url sucessfully')
driver.get(URL)    
password=check()
password.send_keys(data["password"])
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div/form/div/div[2]/span/span/input').click()
print(password.value_of_css_property('border-bottom-color'))
if "error" in password.get_attribute('outerHTML'):
    print(password.value_of_css_property('border-bottom-color'))
    if password.value_of_css_property('border-bottom-color')== "rgba(221, 0, 0, 1)":
        print(f"expected color is rgb(221, 0, 0) and got rgba(221, 0, 0, 1)")
user_link="www.amazon.in/?ref_=nav_ya_signin&"
if  user_link in driver.user_link:
    print('redirected to user link successfully')
driver.quit()