from selenium import webdriver
import logging

# Selenium ?
# Selenium 3, 4 ?
# Selenium 3 ->  Selenium 4

# Selenium 3
# 1.you need to set up the Browser Drivers - Machine - PC/Mac
# 2. Problem - browser


# Selenium 4 ( most 70% ) Selenium 4
# W3c - protocol, Selenium Manager - Which will automatically download the
# browser driver for you

# QA -> Focus -> Test case
def test_login_chrome():
    driver=webdriver.Chrome()
    Logger=logging.getLogger(__name__)
    # Create a Session with POST Request(API POST Request),
    # Fresh Chrome Browser will be open, Session ID is created. #3l2kjh3g2hj1kl2
    # SessionId - 68614348f0cb4f521b963ed00eefbd0a
    driver.get("https://www.google.com")
    driver.maximize_window()
    print(driver.title)
    Logger.info(driver.title)

# pytest.ini we must add because it is a one time adding all the info
# 1 Session ID -> close ID will be deleted
# Multiple windows in same session.
# -v incrrase the logs
# -s means print the printing statements
# -q runs quitely
