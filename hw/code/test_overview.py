import pytest

from cases import LoggedNewUserCase
from ui.pages.overview_page import OverviewNewUserPage
from ui.locators.overview_locators import OverviewNewUserPageLocators
from ui.locators.campaigns_locators import CampaignsPageSharedLocators
from ui.locators.training_locators import TrainingPageSharedLocators


class TestNewUserOverview(LoggedNewUserCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_help(self, driver, config):
        self.overview_new_user_page = OverviewNewUserPage(self.driver)

    def test_display(self):
        self.overview_new_user_page.check_start_actions()

    @pytest.mark.parametrize('button_locator, expected_locator',
                             [
                                 pytest.param(
                                     OverviewNewUserPageLocators.BUTTON_CREATE_CAMPAIGN,
                                     CampaignsPageSharedLocators.SIGN_NEW_AD_CREATE
                                 ),
                                 pytest.param(
                                     OverviewNewUserPageLocators.BUTTON_START_TRAINING,
                                     TrainingPageSharedLocators.MODAL_PAGE,
                                 )
                             ], )
    def test_open_page_by_click(self, button_locator, expected_locator):
        self.overview_new_user_page.click(button_locator)
        assert self.overview_new_user_page.find(expected_locator).is_displayed()
