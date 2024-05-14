import pytest

from cases import LoggedNewUserCase
from ui.pages.overview_page import OverviewNewUserPage


class TestNewUserOverview(LoggedNewUserCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_help(self, driver, config):
        self.overview_new_user_page = OverviewNewUserPage(self.driver)

    def test_display(self):
        self.overview_new_user_page.check_start_actions()
