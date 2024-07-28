import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



def test_action_buttons():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    first_name=driver.find_element(By.XPATH,"//input[@name='firstname']")

    #take a variable and assign it.
    #Key down means press the shift key down,press the shift key button
    #Key up means release the key button,press the shift key button

    action_btn=ActionChains(driver)
    action_btn.key_down(Keys.SHIFT).send_keys_to_element(first_name,"shubham bhavi").key_up(Keys.SHIFT).perform()



    # context test is somthing when you right click and the options comes

    hyper_link=driver.find_element(By.XPATH,"//a[normalize-space()='Click here to Download File']")
    action_btn.context_click(hyper_link).perform()

    time.sleep(20)

