import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def test_chrome():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()

    firstname=driver.find_element(By.XPATH,"//input[@name='firstname']")

    actions=ActionChains(driver)
    #sendkeys with shift
    actions.key_down(Keys.SHIFT).send_keys_to_element(firstname,"shubham").key_up(Keys.SHIFT).perform()
    sex= driver.find_element(By.ID, "sex-0")
    sex.click()

    url = driver.find_element(By.XPATH, "//a[normalize-space()='Click here to Download File']")
    actions.context_click(url).perform()

    time.sleep(10)