import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder


def test_svg():
    driver=webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    driver.maximize_window()
    time.sleep(5)
    actions = ActionChains(driver)
    states = driver.find_elements(By.XPATH,"//*[local-name()='svg']/*[local-name()='g'][7]/*[local-name()='g']/*[local-name()='g']/*[local-name()='path']")
    for i in states:
        state_name = i.get_attribute("aria-label")
        # print(state_name)
        if state_name == "Rajasthan  ":
            actions.move_to_element(i).click().perform()
            break

    time.sleep(15)