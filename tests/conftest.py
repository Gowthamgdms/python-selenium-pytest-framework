import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities.logger import LogGenerator
from config.config import Config
import os
from utilities.screenshot_utils import ScreenshotUtils
from datetime import datetime


def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",help="Browser Name")


logger = LogGenerator.loggen()


@pytest.fixture()
def setup(request):
    browser=request.config.getoption("--browser")

    if browser.lower() == "chrome":
        logger.info("Launching Chrome Browser")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    elif browser.lower() == "firefox":
        logger.info("Launching Firefox Browser")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    elif browser.lower() == "edge":
        logger.info("Launching Edge Browser")
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    else:
        raise Exception(f"Browser '{browser}' is not supported.")

    driver.maximize_window()
    driver.get(Config.BASE_URL)
    yield driver

    if hasattr(request.node,"rep_call") and request.node.rep_call.failed:
        os.makedirs("screenshots",exist_ok=True)
        driver.save_screenshot(f"screenshots/{request.node.name}.png")
        logger.error(f"Screenshot captured:{request.node.name}.png")

    logger.info(f"Closing {browser}Browser")

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()
    if report.when=="call" and report.failed:
        driver = item.funcargs.get("setup")
        if driver:
            ScreenshotUtils.capture_screenshot(driver,item.name)


def pytest_html_report_title(report):
    report.title = "Python Selenium Pytest Automation Report"

def pytest_configure(config):
    config.stash["framework"] = "Python Selenium Pytest Framework"
    config.stash["tester"] = "Gowtham"
    config.stash["execution_time"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")









