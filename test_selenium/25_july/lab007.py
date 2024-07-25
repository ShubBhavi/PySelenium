import time

from selenium import webdriver
import logging
from selenium.webdriver.common.by import By


def test_login_details_chrome():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # using CSS selector you can login to the page
    make_appointment = driver.find_element(By.CSS_SELECTOR, "#btn-make-appointment")
    make_appointment.click()




    # list_elements_p = driver.find_elements(By.XPATH, "//p[contains(text(),'A')]")
    # for i in list_elements_p:
    #     if i.text == "Copyright © CURA Healthcare Service 2024":
    #         i.click()
    #     print(i.text)

    time.sleep(5)
    driver.quit()