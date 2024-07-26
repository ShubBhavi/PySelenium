import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import pytest
from dotenv import load_dotenv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException,ElementNotSelectableException
def test_login_details_chrome():
    load_dotenv()
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    make_appointment=driver.find_element(By.XPATH,"//a[@id='btn-make-appointment']")
    make_appointment.click()

    WebDriverWait(driver,5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"div[class='col-sm-12 text-center'] h2"),"Login"))

    username=driver.find_element(By.CSS_SELECTOR,"#txt-username")
    username.send_keys("John Doe")
    password=driver.find_element(By.CSS_SELECTOR,"#txt-password")
    password.send_keys("ThisIsNotAPassword")
    click_btn=driver.find_element(By.CSS_SELECTOR,"#btn-login")
    click_btn.click()

    ignore_list=(ElementNotVisibleException,ElementNotSelectableException)
    WebDriverWait(driver,30,poll_frequency=5,ignored_exceptions=ignore_list).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"label[for='combo_facility']")))

    heading=driver.find_element(By.CSS_SELECTOR,"label[for='combo_facility']")
    assert heading.text == "Facility"
    print(heading.text)


# implicit wait is global wait for all te elements