import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException


def test_web_tables():
    driver = webdriver.Chrome()
#     another method

    driver.get("https://awesomeqa.com/webtable1.html")
    # get the table
    table=driver.find_element(By.XPATH,"//table[@border='1']/tbody")
    row_table=table.find_elements(By.TAG_NAME,"tr")
    print(len(row_table))

    for i in row_table:
        cols= i.find_elements(By.TAG_NAME,"td")
        for j in cols:
            data=j.text


            if "UAE" in data:
                print("test is passed")
            print(data)
