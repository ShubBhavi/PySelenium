import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_chrome():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    driver.maximize_window()

    make_appoint=driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr")
    row=len(make_appoint)
    print(row)


    col=driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr[2]/td")
    length=len(col)
    print(length)

    # // table[ @ id = 'customers'] / tbody / tr[ -fp
    #     2
    #     ] / td[-sp
    #     1-
    #     ]-tp
    fp="//table[@id='customers']/tbody/tr["
    sp="]/td["
    tp="]"



    for i in range(2,row+1):
        for j in range(1,length+1):
            dynamic_path=f"{fp}{i}{sp}{j}{tp}"
            values=driver.find_element(By.XPATH,f"{dynamic_path}").text
            if "Helen Bennett" in values:
                country_path=f"{dynamic_path}/following-sibling::td"
                country_text=driver.find_element(By.XPATH,country_path).text
                print(f"elen in {country_text}")










    # username= driver.find_elements(By.NAME,"username")
    # username[0].send_keys("yzbdueuxgt@txcct.com")
    #
    # # username= driver.find_element(By.ID,"login-username")
    # # username.send_keys("yzbdueuxgt@txcct.com")
    #
    #
    # # username= driver.find_element(By.XPATH,"//input[@id='login-username']")
    # # username.send_keys("yzbdueuxgt@txcct.com")
    #
    # password=driver.find_element(By.ID,"login-password")
    # password.send_keys("Shubham@1980")

    # butn=driver.find_element(By.ID,"js-login-btn")
    # butn.click()

    # free_trail=driver.find_element(By.PARTIAL_LINK_TEXT,"Start a free")
    # free_trail.click()


    time.sleep(10)