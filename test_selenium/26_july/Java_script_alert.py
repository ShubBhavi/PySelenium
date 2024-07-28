import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import pytest
from dotenv import load_dotenv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException,ElementNotSelectableException


def test_alert_topic():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    button=driver.find_element(By.CSS_SELECTOR,"button[onclick='jsAlert()']")
    button.click()
    WebDriverWait(driver,10).until(EC.alert_is_present())
    # # ignore_list=(ElementNotVisibleException,ElementNotSelectableException)
    # # WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=ignore_list).until(EC.alert_is_present())
    alert=driver.switch_to.alert
    alert.accept()
    result=driver.find_element(By.CSS_SELECTOR,"#result")
    print(result.text)



    button3 = driver.find_element(By.CSS_SELECTOR, "button[onclick='jsConfirm()']")
    button3.click()
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert1 = driver.switch_to.alert
    alert1.dismiss()
    result2 = driver.find_element(By.CSS_SELECTOR, "#result")
    print(result2.text)



    button2 = driver.find_element(By.CSS_SELECTOR, "button[onclick='jsPrompt()']")
    button2.click()
    WebDriverWait(driver,10).until(EC.alert_is_present())
    alert1=driver.switch_to.alert
    alert1.send_keys("shubham")
    alert1.accept()
    result1=driver.find_element(By.CSS_SELECTOR,"#result")
    print(result1.text)

    time.sleep(5)
    driver.quit()