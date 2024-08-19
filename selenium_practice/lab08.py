import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton

def test_chrome():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()

    main_window=driver.current_window_handle
    print(main_window)
    print()
    clickable=driver.find_element(By.PARTIAL_LINK_TEXT,"Click He")
    clickable.click()

    window_handles=driver.window_handles
    print(window_handles)

    for handle in window_handles:
        driver.switch_to.window(handle)
        if "New Window" in driver.page_source:
            print("new winodw found")


    time.sleep(10)

