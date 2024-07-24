import time

from selenium import webdriver
import logging
from selenium.webdriver.common.by import By


def test_login_details_chrome():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    button=driver.find_element(By.ID,"btn-make-appointment")
    button.click()
    print(driver.current_url)
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/profile.php#login","its and error"

    username=driver.find_element(By.NAME,"username")
    username.send_keys("John Doe")

    password=driver.find_element(By.NAME,"password")
    password.send_keys("ThisIsNotAPassword")

    login_buttom=driver.find_element(By.ID,"btn-login")
    login_buttom.click()

    print(driver.current_url)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment","its and error"

    # < input
    # type = "text"
    # class ="form-control"
    # id="txt-username"
    # name="username"
    # placeholder="Username"
    # value="" autocomplete="off" >

    # <input
    # type="password"
    # class="form-control"
    # id="txt-password"
    # name="password"
    # placeholder="Password"
    # value="" autocomplete="off">

    # <button
    # id="btn-login"
    # type="submit"
    # class="btn btn-default">
    # Login</button>

    time.sleep(5)
    driver.quit()