import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton

def test_chrome():
    driver=webdriver.Chrome()
    driver.get("https://flipkart.com")
    driver.maximize_window()

    title=driver.find_element(By.NAME,'q')
    title.send_keys("AC")

    action=ActionChains(driver)
    svg=driver.find_element(By.XPATH,"//*[local-name()='svg']/*[local-name()='path' and @stroke='#717478']")

    action.move_to_element(svg).click().perform()

    # svg=driver.find_element(By.XPATH,"//*[local-name()='svg']/*[local-name()='path' and @stroke='#717478']")

    time.sleep(10)
