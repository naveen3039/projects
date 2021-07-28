##########################################################################################################
#Script Details

# Script name               :       web_test.py
# Script version            :       python 3.8.3
# Prepared By               :       naveen.kumar5@infinite.com
# Create Date               :       07-06-21
# Last Modification Date    :       07-06-21

##############################################################################################
#Purpose of the script
##############################################################################################

#1.Creating the job and getting the report with the python code

##############################################################################################
#Below points considered in the script:
##############################################################################################


#1.By using python code provide project name, job_name, token.

#2.The token will be generated in integrations and copy it and paste in token.

#3.If test case is passed then report generates in Test_project .

#################################################################################################

from src.testproject.sdk.drivers import webdriver
import logging

# The setting basic configuration of log_file format and level
logging.basicConfig(
    filename="Test_automation.log",
    filemode="w",
    format="%(asctime)s :: %(message)s",
    level=logging.INFO
    )

def simple_test():
    logging.info('providing the project_name,job_name,token here')
    driver=webdriver.Chrome(project_name='naveen',  job_name='12345',token = 'tkAuDAeEc9jaNPSB1NyRQTASz-HAf2ZNdzJ4lH5GtXI1')
    logging.info('providing the details of testproject with automation using selenium webdriver')
    driver.get("https://example.testproject.io/web/")

    driver.find_element_by_css_selector("#login").click()

    passed = driver.find_element_by_css_selector("#logout").is_displayed()

    print("Test passed") if passed else print("Test failed")

    driver.quit()


if __name__ == "__main__":
    simple_test()
logging.info('execution ends here')