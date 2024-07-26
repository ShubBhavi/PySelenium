import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException


def test_web_tables():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable1.html")

    # fp   //table[@id="customers"]/tbod//tr[
    #       2
    # sp    ]//td[
    #       2
    # tp    ]

    row_elements = driver.find_elements(By.XPATH, "//table[@border='1']/tbody/tr")
    row = len(row_elements)
    print(row)

    col_elements = driver.find_elements(By.XPATH, "//table[@border='1']/tbody/tr[1]/td")
    col = len(col_elements)
    print(col)

    for i in range(1, row + 1):
        for j in range(1, col + 1):
            path = f"//table[@border='1']/tbody/tr[{i}]/td[{j}]"
            value = driver.find_element(By.XPATH, path)
            print(value.text)

