import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


SELENIUM_REMOTE = os.getenv("SELENIUM_REMOTE_URL")

@pytest.fixture(scope="module")
def driver():
    if SELENIUM_REMOTE:
        caps = {"browserName": "chrome"}
        driver = webdriver.Remote(command_executor=SELENIUM_REMOTE, desired_capabilities=caps)
    else:
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_add_via_ui(driver):
    url = os.getenv("APP_URL", "http://localhost:5000")
    driver.get(url)
    time.sleep(0.5)
    a = driver.find_element(By.ID, "a")
    b = driver.find_element(By.ID, "b")
    add_btn = driver.find_element(By.ID, "add-btn")
    a.send_keys("7")
    b.send_keys("8")
    add_btn.click()
    time.sleep(0.5)
    result = driver.find_element(By.ID, "result").text
    assert result == "15.0" or result == "15"
