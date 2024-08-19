import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton

def test_chrome():
    driver=webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    driver.maximize_window()

    actions=ActionChains(driver)

    path_sates=driver.find_elements(By.XPATH,"//*[local-name()='svg']/*[local-name()='g'][7]/*[local-name()='g']/*[local-name()='g']//*[local-name()='path']")
    for states in path_sates:
        state_name=states.get_attribute("aria-label")
        print(state_name)
        if state_name=="Maharashtra  ":
            actions.move_to_element(states).click().perform()


    # svg=driver.find_element(By.XPATH,"//*[local-name()='svg']/*[local-name()='path' and @stroke='#717478']")

    time.sleep(10)
