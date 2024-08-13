import time

from selenium import webdriver

def test_chrome():
    driver=webdriver.Chrome()
    driver.get("https://www.google.com")
    driver.maximize_window()
    driver.get("https://facebook.com")

    driver.back()
    time.sleep(200)