import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities.logger import LogGenerator
from config.config import Config
import os
from utilities.screenshot_utils import ScreenshotUtils

logger = LogGenerator.loggen()


@pytest.fixture()
def setup(request):

    logger.info("Launching Chrome Browser")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(Config.BASE_URL)
    yield driver

    if hasattr(request.node,"rep_call") and request.node.rep_call.failed:
        os.makedirs("screenshots",exist_ok=True)
        driver.save_screenshot(f"screenshots/{request.node.name}.png")
        logger.error(f"Screenshot captured:{request.node.name}.png")

    logger.info("Closing Chrome Browser")

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()
    if report.when=="call" and report.failed:
        driver = item.funcargs.get("setup")
        if driver:
            ScreenshotUtils.capture_screenshot(driver,item.name)











