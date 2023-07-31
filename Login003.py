
######################### SETUP ###########################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
import time
from selenium.webdriver.support import expected_conditions as EC

# This is an invalid username and passwword. 
username = 'melody.norsworthy'
password = 'Test123!'
homePage = 'https://www.hudl.com/'
message = 'If you are a Hudl user, log in with your Hudl account here.'
#################### TEST CASE LOGIN003 #####################
# TEST CASE: LOGIN003
# DESCRIPTION: This test case will verify an error message with invalid Username
# ENTRANCE CRITERIA: invalid username added to variables in SETUP.
# EXIT CRITERIA: Error Message is received
#############################################################

now = datetime.now()
start_time = now.strftime("%H:%M:%S")
print ("*** Test case Login003 start time:", start_time)
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
element.send_keys('')
# Step 08. Click on the continue button to login
driver.find_element(By.ID,"logIn").click()
# Step 09. Verify error message is received

get_source = driver.page_source
if message in get_source:
   print('Test Passed - Error Message Found: ',message)
else:
   print('Test Failed - Error Message Not Found')

# Setp 10. Record end time 
now = datetime.now()
end_time = now.strftime("%H:%M:%S")
print ("*** Test case Login003 end time:", end_time)
driver.close()

