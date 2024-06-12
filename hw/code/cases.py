import pytest

from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.login_page import LoginPage


class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup_base_case(self, driver, config):
        self.driver = driver
        self.config = config

        self.base_page = BasePage(driver)
        self.login_page = LoginPage(driver)


@pytest.mark.usefixtures('setup_base_case')
class LoggedCase(BaseCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, setup_base_case, credentials):
        self.main_page = self.login_page.login(credentials)
        # self.login_page.click(self.base_page.locators.NAV_BUTTON_CABINET_LOCATOR)
        # self.login_page.click(self.base_page.locators.NAV_BUTTON_CABINET_LOCATOR)

        # self.login_page.click(self.base_page.BUTTON_MAILRU_AUTH_LOCATOR)

        # self.login_page.write_input(self.base_page.INPUT_EMAIL_LOCATOR, credentials.login)

        # self.login_page.click(self.base_page.BUTTON_NEXT_LOCATOR)

        # self.login_page.write_input(self.base_page.INPUT_PASSWORD_LOCATOR, credentials.password)

        # self.login_page.click(self.base_page.BUTTON_SUBMIT_LOCATOR)

        # self.main_page = MainPage(self.login_page)


@pytest.mark.usefixtures('setup_base_case')
class LoggedNewUserCase(BaseCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, setup_base_case, credentials_new_user):
        self.main_page = self.login_page.login(credentials_new_user)


@pytest.mark.usefixtures('setup_base_case')
class RegisteredUserCase(BaseCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, setup_base_case, credentials_user_without_cabinet):
        self.pre_registration_page = self.login_page.register(credentials_user_without_cabinet)
