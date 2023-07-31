# MelodyNorsworthy

########################## TEST PLAN ##################################
# Description: The Python Scripts contain test cases to verify the
# login and error catching capabilities for the hudl.com website.
# Prepared By: Melody Norsworthy, melody.norsworthy@gmail.com
# Date: August 1, 2023
# Github Location: 
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
# Additional Tests to be considered
# Login004 - Forgot Password Link
# Login005 - Login with Facebook Link
# Login006 - Login with Google Link
# Login007 - Create Account
# Login008 - Code Injection - code does not execute
# LOGIN009 - Large font Size
# LOGIN010 - Accessibility - buttons have alternative text
# LOGIN011 - Accessibility - Screen Reader
# This series of tests is broken into seperate files to allow more flexibity in execution.
# NOTE: Normally this type of test plan would be in a test case repositiry such as Jira.  
########################## END OF TEST PLAN #################################
