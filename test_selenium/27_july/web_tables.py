import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException,ElementNotSelectableException

def test_web_tables():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")

# fp   //table[@id="customers"]/tbod//tr[
#       2
# sp    ]//td[
#       2
# tp    ]

    row_elements=driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr")
    row=len(row_elements)
    print(row)

    col_elements=driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr/th")
    col=len(col_elements)
    print(col)

    for i in range(2,row+1):
        for j in range(1,col+1):
            path = f"//table[@id='customers']/tbody/tr[{i}]/td[{j}]"
            # value = driver.find_element(By.XPATH,path)
            # print(value.text,end='')
            # print(path)
            data = driver.find_element(By.XPATH,path)
            data1=data.text
            if "Roland Mendel" in data1:
                country_path=f"{path}/following-sibling::td"
                country=driver.find_element(By.XPATH,country_path)
                print(country.text)








