import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton

def test_chrome():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    driver.maximize_window()

    clickable=driver.find_element(By.XPATH,"//input[@id='clickable']")
    hover=driver.find_element(By.XPATH,"//input[@id='hover']")
    drag=driver.find_element(By.XPATH,"//div[@id='draggable']")
    drop=driver.find_element(By.XPATH,"//div[@id='droppable']")




    actions=ActionChains(driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(clickable,"shubham").key_up(Keys.SHIFT).perform()
    # double click to select
    actions.double_click(clickable).perform()
    # hover mouse to the particular element
    actions.move_to_element(hover).perform()

    # darg and drop
    actions.drag_and_drop(drag,drop).perform()
    url=driver.find_element(By.XPATH,"//a[@id='click']")
    url.click()

    action_builder=ActionBuilder(driver)
    action_builder.pointer_action.pointer_down(MouseButton.BACK)
    action_builder.perform()
    time.sleep(15)