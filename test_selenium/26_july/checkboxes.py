import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import pytest
from dotenv import load_dotenv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException,ElementNotSelectableException


def test_checkboxes():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
    for i in checkboxes:
        if not i.is_selected():
            i.click()


    # # for checking only one box1
    # checkboxes = driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)")
    # checkboxes.click()
    #
    # for unchecking the already checked box
    # checkboxes1 = driver.find_element(By.XPATH, "//input[2]")
    # checkboxes1.click()

    time.sleep(5)
    driver.quit()