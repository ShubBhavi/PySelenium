import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_app():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com")

    email=driver.find_element(By.ID,"login-username")
    email.send_keys("shubhambhavi888@gmail.com")

    password = driver.find_element(By.ID, "login-password")
    password.send_keys("password")

    button = driver.find_element(By.ID , "js-login-btn")
    button.click()

    # error=driver.find_element(By.XPATH,"//div[@class='Mt(40px)']")
    # print(error.text)
    # assert error.text == "Your email, password, IP address or location did not match","not correct"


       # alert=driver.switch_to.alert
    # alert_text=alert.text
    # print(alert_text)
    # #



    # Your email, password, IP address or location did not match</div>


    time.sleep(12)
    driver.quit()

# <input
# type="email"
# class="text-input W(100%)"
# name="username"
# id="login-username"
# data-qa="hocewoqisi">

# <input type="password" class="text-input W(100%)" name="password" id="login-password" data-qa="jobodapuxe">

# <button type="submit" id="js-login-btn" class="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)" onclick="login.login(event)" data-qa="sibequkica">
# 									<span class="icon loader hidden" data-qa="zuyezasugu"></span>
# 									<span data-qa="ezazsuguuy">Sign in</span>
# 								</button>