import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities.logger import LogGenerator

logger = LogGenerator.loggen()


@pytest.fixture()
def setup():
    logger.info("Launching Chrome Browser")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    yield driver
    logger.info("Closing Chrome Browser")

    driver.quit()