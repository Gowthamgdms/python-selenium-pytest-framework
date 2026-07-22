from selenium.webdriver.common.by import By
from utilities.base_page import BasePage


class LoginPage(BasePage):

    username_textbox = (By.ID, "user-name")
    password_textbox = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        self.enter_text(self.username_textbox, username)

    def enter_password(self, password):
        self.enter_text(self.password_textbox, password)

    def click_login(self):
        self.click(self.login_button)