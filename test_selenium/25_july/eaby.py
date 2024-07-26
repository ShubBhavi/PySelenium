import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_site_login():
    driver=webdriver.Chrome()
    driver.get("https://www.ebay.com")

    search_engine=driver.find_element(By.XPATH,"//input[@id='gh-ac']")
    search_engine.send_keys("16gb")

    click_button=driver.find_element(By.XPATH,"//input[@id='gh-btn']")
    click_button.click()

    list_gb=driver.find_elements(By.XPATH,"//span[@role='heading']")
    for i in list_gb:
        print(i.text)

    # price_tag = driver.find_elements(By.XPATH, "li[id='item341da8b1fe'] span[class='s-item__price']")
    # for j in price_tag:
    #     print(j.text)



    time.sleep(5)
    driver.quit()
