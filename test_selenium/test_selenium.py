import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver=webdriver.Chrome()
    yield driver

def test_open_url(driver):
    driver.get("https://app.vwo.com/")
    print(driver.title)
    assert driver.title=="Login - VWO","Its correct"
