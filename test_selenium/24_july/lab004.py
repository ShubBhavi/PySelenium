import time

from selenium import webdriver
import logging
from selenium.webdriver.common.by import By


def test_login_details_chrome():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # button=driver.find_element(By.ID,"btn-make-appointment")
    # button.click()
    # print(driver.current_url)
    # assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/profile.php#login"

    # button = driver.find_elements(By.CLASS_NAME, "btn btn-dark btn-lg")
    # button[0].click()

    # button = driver.find_element(By.PARTIAL_LINK_TEXT, "Appointment")
    # button.click()

    # button = driver.find_element(By.PARTIAL_LINK_TEXT, "Make")
    # button.click()

    # button = driver.find_element(By.LINK_TEXT, "Make Appointment")
    # button.click()

    # button = driver.find_elements(By.CLASS_NAME, "btn.btn-dark.btn-lg")
    # button[1].click()


    time.sleep(5)
    driver.quit()
# a
# id="btn-make-appointment"
# href="./profile.php#login"
# class="btn btn-dark btn-lg">
# Make Appointment
# </a>