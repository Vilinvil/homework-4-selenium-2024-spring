import pytest

from cases import LoggedNewUserCase
from cases import LoggedCase
from ui.pages.overview_page import OverviewNewUserPage
from ui.pages.overview_page import OverviewPage
from ui.locators.overview_locators import OverviewNewUserPageLocators
from ui.locators.campaigns_locators import CampaignsPageSharedLocators
from ui.locators.training_locators import TrainingPageSharedLocators


class TestNewUserOverview(LoggedNewUserCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_help(self, driver, config):
        self.overview_new_user_page = OverviewNewUserPage(self.driver)

    def test_display(self):
        self.overview_new_user_page.check_display_start_actions()

    @pytest.mark.parametrize('button_locator, expected_locator',
                             [
                                 pytest.param(
                                     OverviewNewUserPageLocators.BUTTON_CREATE_CAMPAIGN,
                                     CampaignsPageSharedLocators.SIGN_NEW_AD_CREATE,
                                 ),
                                 pytest.param(
                                     OverviewNewUserPageLocators.BUTTON_START_TRAINING,
                                     TrainingPageSharedLocators.MODAL_PAGE,
                                 )
                             ], )
    def test_open_page_by_click(self, button_locator, expected_locator):
        self.overview_new_user_page.click(button_locator)
        assert self.overview_new_user_page.find(expected_locator).is_displayed()


class TestOverview(LoggedCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_help(self, driver, config):
        self.overview_page = OverviewPage(self.driver)

    def test_display(self):
        self.overview_page.check_display()

    def test_click_redirect_campaign(self):
        self.overview_page.click(self.overview_page.locators.BUTTON_CREATE_CAMPAIGN)
        assert self.driver.current_url == "https://ads.vk.com/hq/new_create/ad_plan"

    def test_click_new_tab_limit_article(self):
        self.overview_page.click_redirect_article_help()

        assert self.driver.current_url == "https://ads.vk.com/help/articles/ad_limits"

    def test_modal_page_budget(self):
        self.overview_page.open_modal_view(self.overview_page.locators.BUTTON_BUDGET_REPLENISH,
                                           self.overview_page.locators.SIGN_OPENING_MODAL_PAGE_BUDGET)

        self.overview_page.close_modal_view(self.overview_page.locators.BUTTON_CLOSE_MODAL_PAGE_BUDGET,
                                            self.overview_page.locators.SIGN_OPENING_MODAL_PAGE_BUDGET)
