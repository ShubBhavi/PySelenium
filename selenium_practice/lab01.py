import time

from selenium import webdriver

def test_open_chrome():
    driver1=webdriver.ChromeOptions()
    extension_path=r"C:\Users\233004\Documents\cookie.crx"
    driver1.add_extension(extension_path)
    driver=webdriver.Chrome(options=driver1)
    driver.get("https:google.com")
    time.sleep(5)
