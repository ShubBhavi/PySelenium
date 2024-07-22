import time

from selenium import webdriver
import logging

def test_login_details():
    driver=webdriver.Chrome()
    driver.get("https://www.google.com")
    print(driver.title)

    driver.back()
    driver.get("https://www.bing.com")
    print(driver.title)

    driver.forward()
    driver.get("https://www.facebook.com")
    print(driver.title)

    driver.back()
    print(driver.title)

    
    time.sleep(5)
    driver.quit()