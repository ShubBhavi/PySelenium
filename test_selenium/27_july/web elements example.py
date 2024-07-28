import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException


def test_web_elements():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")

    row_elemnts=driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr")
    row=len(row_elemnts)
    print(row)

    col_elements=driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr[2]/td")
    col=len(col_elements)
    print(col)

    for i in range(2,row+1):
        for j in range(1,col+1):
            path=f"//table[@id='customers']/tbody/tr[{i}]/td[{j}]"
            elem=driver.find_element(By.XPATH,path)
            data=elem.text
            if "Helen Bennett" in data:
                path1=(f"{path}/following-sibling::td")
                el=driver.find_element(By.XPATH,path1)
                print(el.text)