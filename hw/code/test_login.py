from ui.pages.main_page import MainPage, URL_MAIN_PAGE
from cases import BaseCase

from selenium.webdriver.support import expected_conditions as EC


class TestLogin(BaseCase):
    def test_login(self, credentials):
        main_page = self.login_page.login(credentials)
        assert isinstance(main_page, MainPage)
        assert self.login_page.wait().until(EC.url_to_be(URL_MAIN_PAGE))
