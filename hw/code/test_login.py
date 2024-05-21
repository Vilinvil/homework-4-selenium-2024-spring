from cases import BaseCase
from ui.pages.main_page import MainPage


class TestLogin(BaseCase):
    def test_login(self, credentials):
        main_page = self.login_page.login(credentials)
        assert isinstance(main_page, MainPage)
