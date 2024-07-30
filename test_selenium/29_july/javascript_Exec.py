import time

from  selenium.webdriver.common.by import By
from selenium import webdriver
import pytest


def test_login():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")


    butn_path=driver.find_element(By.CSS_SELECTOR,"button[onclick='addElement()']")

    #driver.executor is a module which executes the scripts of java
    js_executor=driver.execute_script
    # here arguments is replaced by the butn path
    js_executor("arguments[0].click()",butn_path)
    # return document is a java script , we have to learn the scripts of java
    title=js_executor("return document.title")
    print(title)

    time.sleep(5)