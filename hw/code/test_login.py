import pytest

from ui.pages.main_page import MainPage, URL_MAIN_PAGE
from cases import BaseCase


class TestLogin(BaseCase):
    def test_login(self, credentials):
        main_page = self.login_page.login(credentials)
        assert isinstance(main_page, MainPage)
        assert URL_MAIN_PAGE == self.driver.current_url
