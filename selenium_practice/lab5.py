import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_chrome():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()




    username= driver.find_element(By.XPATH,"//input[@id='login-username']")
    username.send_keys("yzbdueuxgt@txcct.com")

    password=driver.find_element(By.ID,"login-password")
    password.send_keys("Shubham@1980")

    butn=driver.find_element(By.ID,"js-login-btn")
    butn.click()

    time.sleep(5)

    # Explicit wait
    WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".page-heading"),"Dashboard"))

    # fluent wait


    title=driver.find_element(By.XPATH,"//span[@class='Fw(semi-bold) ng-binding']")
    print(title.text)

    time.sleep(5)


    #
    #
    # # username= driver.find_element(By.XPATH,"//input[@id='login-username']")
    # # username.send_keys("yzbdueuxgt@txcct.com")
    #



    # free_trail=driver.find_element(By.PARTIAL_LINK_TEXT,"Start a free")
    # free_trail.click()


