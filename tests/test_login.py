from pages.login_page import LoginPage
from utilities.excel_reader import ExcelReader
from utilities.json_reader import JsonReader
import pytest

# JSON Version
test_data = JsonReader.read_json("testdata/login_data.json")

# Excel Version
# test_data = ExcelReader.read_data("testdata/login_data.xlsx", "login_data")


class TestLogin:

    # Excel Version
    # @pytest.mark.parametrize("username,password", test_data)

    # JSON Version
    @pytest.mark.parametrize("data", test_data)

    # Excel Version
    # def test_login(self, setup, username, password):

    # JSON Version
    def test_login(self, setup, data):

        driver = setup

        login_page = LoginPage(driver)

        # JSON Version
        login_page.login(data["username"], data["password"])

        # Excel Version
        # login_page.login(username, password)

        assert "inventory" in driver.current_url