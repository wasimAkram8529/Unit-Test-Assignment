import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


SELENIUM_REMOTE = os.getenv("SELENIUM_REMOTE_URL")


@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    if SELENIUM_REMOTE:
        driver = webdriver.Remote(
            command_executor=SELENIUM_REMOTE,
            options=options
        )
    else:
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        service = Service(ChromeDriverManager().install())
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
    assert result in ("15", "15.0")
