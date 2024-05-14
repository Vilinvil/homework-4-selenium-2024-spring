from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.locators import login_locators
from utils.credentials import Credentials


class LoginPage(BasePage):
    locators = login_locators.LoginPageLocators()
    
    def login(self, credentials: Credentials):
        self.click(super().locators.BUTTON_CABINET_LOCATOR)

        self.click(self.locators.BUTTON_MAILRU_AUTH_LOCATOR)

        self.write_input(self.locators.INPUT_EMAIL_LOCATOR, credentials.login)

        self.click(self.locators.BUTTON_NEXT_LOCATOR)

        self.write_input(self.locators.INPUT_PASSWORD_LOCATOR, credentials.password)

        self.click(self.locators.BUTTON_SUBMIT_LOCATOR)

        self.mainPage = MainPage(self.driver)

        return self.mainPage
