from config.config import Config
from pages.login_page import LoginPage
from utilities.excel_reader import ExcelReader
from utilities.json_reader import JsonReader

#test_data=JsonReader.read_json("testdata/login_data.json")

test_data=ExcelReader.read_data("testdata/login_data.xlsx","login_data")

class TestLogin:
 def test_login(self,setup):
    driver = setup

    driver.get(Config.BASE_URL)

    login_page = LoginPage(driver)

    # JSON version
    #login_page.login(test_data[0]["username"],test_data[0]["password"])

    # Excel version
    login_page.login(test_data[0][0],test_data[0][1])


    assert "inventory" in driver.current_url
