import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



def test_action_buttons():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()
    action=ActionChains(driver)

    old_window=driver.current_window_handle
    main_window=driver.find_element(By.PARTIAL_LINK_TEXT,"Click").click()

    window_handle=driver.window_handles
    # print(window_handle)


    for window in window_handle:
        # this navigate to ua new window
        driver.switch_to.window(window)
        if "New Window" in driver.page_source:
            print("yes")
            break

    driver.switch_to.window(old_window)



    time.sleep(10)



