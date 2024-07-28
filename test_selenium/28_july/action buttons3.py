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
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()
    action=ActionChains(driver)
    # WebDriverWait(driver,5).until(EC.alert_is_present())
    # alert=driver.switch_to.alert
    # alert.dismiss()
    time.sleep(3)
    from_city=driver.find_element(By.ID,"fromCity")

    action.move_to_element(from_city).click().send_keys("new Delhi").perform()

    time.sleep(20)



