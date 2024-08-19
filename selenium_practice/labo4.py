import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_chrome():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()

    # <input
    # type="email"
    # class="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi"
    # xpath="1">
    #
    make_appoint=driver.find_element(By.XPATH,"//a[contains(text(),'Make')]")
    make_appoint.click()

    make_appoint = driver.find_element(By.XPATH, "//a[starts-with(text(),'Make')]")
    make_appoint.click()

    assert driver.title=="CURA Healthcare Service","its not"


    # username= driver.find_elements(By.NAME,"username")
    # username[0].send_keys("yzbdueuxgt@txcct.com")
    #
    # # username= driver.find_element(By.ID,"login-username")
    # # username.send_keys("yzbdueuxgt@txcct.com")
    #
    #
    # # username= driver.find_element(By.XPATH,"//input[@id='login-username']")
    # # username.send_keys("yzbdueuxgt@txcct.com")
    #
    # password=driver.find_element(By.ID,"login-password")
    # password.send_keys("Shubham@1980")

    # butn=driver.find_element(By.ID,"js-login-btn")
    # butn.click()

    # free_trail=driver.find_element(By.PARTIAL_LINK_TEXT,"Start a free")
    # free_trail.click()


    time.sleep(20)