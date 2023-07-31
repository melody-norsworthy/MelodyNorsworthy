
########################## TEST PLAN ##################################
# Description: The Python Scripts contain test cases to verify the
# login and error catching capabilities for the hudl.com website.
# Prepared By: Melody Norsworthy, melody.norsworthy@gmail.com
# Date: August 1, 2023
# Filename: HUDLLoginTests.py
# 
# SETUP
# 1. Install Python 3.11 Interpreter Runtime Dev Tool
# 2. Install Selenium - run "pip install selenium" from CLI.
# 3. Install Firefox Webdriver (or alternative webdriver)
#  
# ENTRANCE CRITERIA 
#     URL for login: www.hudl.com
#     UserId and Password will not be included in the code, Please insert your own userid and password.
#     Valid Userid - This will need to be updated prior to running the test.  
#     Valid Password - This will need to be updated prior to running the test. 
#     System is in the LOGOUT state

# EXIT CRITERIA
#   Goal of test occurs as stated in individual test cases.
#
# TEST CASES

# These test cases should be named with the cooresponding test case number from the test repository.
# Smoke Tests to be automated:
# Login001 - AUTOMATED - file login001.py - login occurs successfully with valid credentials 
# Login002 - AUTOMATED - file login002.py - Error message received when password is blank/Invalid 
# Login003 - AUTOMATED - file login003.py -login does not occur with invalid UserId and appropriate warning is displayed - AUTOMATED - file login002.py
# Login004 - Forgot Password Link
# Login005 - Login with Facebook Link
# Login006 - Login with Google Link
# Login007 - Create Account
# Login008 - Code Injection - code does not execute
# LOGIN009 - Large font Size
# LOGIN010 - Accessibility - buttons have alternative text
# LOGIN011 - Accessibility - Screen Reader
# This series of tests may be broken into seperate files to allow more flexibity in execution.
# For this example, all tests are included in the same file.
# NOTE: NOrmally this type of test plan would be in a test case repositiry such as Jira.  
########################## END OF TEST PLAN #################################

######################### SETUP ###########################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
import time
from selenium.webdriver.support import expected_conditions as EC

# PROVIDE YOUR OWN USERNAME and PASSWORD!!!
username = 'xxx@gmail.com'
password = 'xxx'
homePage = 'https://www.hudl.com/'

#################### TEST CASE LOGIN001 #####################
# TEST CASE: LOGIN001
# DESCRIPTION: This test case will verify successful login to the HUDL site.
# ENTRANCE CRITERIA: Valid username and password have been added to variables in SETUP.
# EXIT CRITERIA: Successful login occurs
#############################################################

now = datetime.now()
start_time = now.strftime("%H:%M:%S")
print ("*** Test case Login001 start time:", start_time)
# Step 01. Open instance of firefox
driver = webdriver.Firefox()
# Step 02. Navigate to website
driver.get(homePage)
# Step 03. Maximize window
driver.maximize_window()
# Setp 04. Verify that the HUDL website is available
current_url = driver.current_url
if current_url == homePage:
   print('Hudl landing page accessed', current_url)
else:
   print('URL verification failed - website not accessable')
   print('expected URL: ',homePage)
   print('actual URL: ',current_url)
   driver.close()
# Step 05. Click the login button 
element=driver.find_element(By.PARTIAL_LINK_TEXT,'Log').click()
# Step 06. Select Hudl from the drop down menu
element=driver.find_element(By.PARTIAL_LINK_TEXT,'Hudl').click()
# Step 07. Input the UserName and Password
element=driver.find_element(By.ID,"email")
element.send_keys(username)
element=driver.find_element(By.ID,"password")
element.send_keys(password)
# Step 08. Click on the continue button to login
driver.find_element(By.ID,"logIn").click()
# Setp 09. Verify login is successful
get_title = driver.title
if get_title == 'Log In':
   print('Test Passed - Login successful')
else:
   print('Test Failed - Login unsuccessful')
# Setp 10. Record end time 
now = datetime.now()
end_time = now.strftime("%H:%M:%S")
print ("*** Test case Login001 end time:", end_time)
driver.close()

