import time

from selenium import webdriver
import logging


def test_login_to_google():
    chrome_options=webdriver.ChromeOptions()
    file_path=r"\Users\SHUBHAM\Downloads\chrome_extension.crx"
    chrome_options.add_extension(file_path)
    chrome_options.add_argument("--start-maximiazed")
    driver=webdriver.Chrome(options=chrome_options)
    driver.get("https://www.google.com")
    logging.info(driver.title)
    time.sleep(10)
    # driver.close()
    # close will close the tab which it ha opend and the manually tabs which we have opened will not close
    driver.quit()

    # time.sleep(400)