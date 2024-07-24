import time

from selenium import webdriver
import logging
from selenium.webdriver.common.by import By


def test_login_details_chrome():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    make_appointment=driver.find_element(By.XPATH,"//a[@id='btn-make-appointment']")
    make_appointment.click()
    # the value we are using is normal xpath

    # make_appointment = driver.find_element(By.XPATH, "/html/body/header/div/a")
    # make_appointment.click()
    # # the value which we are using  is absolute path

    #
    # make_appointment=driver.find_element(By.XPATH,"// a[contains(text(), 'Make Appointment')]")
    # make_appointment.click()
    # # this we have used xpath functions called conatians where we can can execute the path using the value wether it conatins some refering value
    #
    # make_appointment = driver.find_element(By.XPATH, "// a[contains(text(), 'Appointment')]")
    # make_appointment.click()
    # this we have used xpath functions called conatians where we can can execute the path using the value wether it conatins some refering value



    # make_appointment = driver.find_elements(By.XPATH, "//a[@class='btn btn-dark btn-lg']")
    # make_appointment[0].click()
    # this we have used class value to show that there are multiple class in the page
    # so we have used the find elemets fucntion


    # make_appointment = driver.find_element(By.XPATH, "//a[@href='./profile.php#login']")
    # make_appointment.click()
    # # this we are using the href locator




    # (//header/div/..) this two dots use to find te parent of a child

    time.sleep(5)
    driver.quit()