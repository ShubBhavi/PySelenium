import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton

# ACTION BUILDER IS FOR MOUSE CURSOR TO MOVE HERE AND THERE



def test_action_buttons():
    driver = webdriver.Chrome()
    # driver.get("https://awesomeqa.com/practice.html")
    # first_name=driver.find_element(By.XPATH,"//input[@name='firstname']")
    # first_name.send_keys("shubham")

    action=ActionChains(driver)
    #
    # action.key_down(Keys.SHIFT).send_keys(Keys.ARROW_LEFT).send_keys(Keys.ARROW_UP).key_up(Keys.SHIFT).perform()
    # time.sleep(3)
    # action.send_keys(Keys.BACK_SPACE).send_keys_to_element(first_name,"Boss").perform()
    # time.sleep(7)



    # hoverable

    # driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    # hoverable=driver.find_element(By.ID,"hover")
    # action.move_to_element(hoverable).perform()
    # time.sleep(5)

#     drag and drop
#     drag= driver.find_element(By.ID,"draggable")
#     drop= driver.find_element(By.ID, "droppable")
#
#     action.drag_and_drop(drag,drop).perform()


    # scroll down
    # driver.get("https://www.selenium.dev/documentation/webdriver/actions_api/mouse/")
    # driver.maximize_window()
    # scroll_name=driver.find_element(By.ID,"drag-and-drop-by-offset")
    # time.sleep(2)
    #
    # action.scroll_to_element(scroll_name).perform()





    time.sleep(5)







