import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder


def test_svg():
    driver=webdriver.Chrome()
    driver.get("https://www.flipkart.com/")

    words=driver.find_element(By.XPATH,"//input[@placeholder='Search for Products, Brands and More']")
    words.send_keys("AC")

    #the value here is the actual way to find the svg image element
    search_icon=driver.find_element(By.XPATH,"//*[local-name()='svg']/*[local-name()='path' and @stroke='#717478']")
    actions=ActionChains(driver)
    actions.move_to_element(search_icon).click().perform()

    time.sleep(10)