import pytest

from cases import LoggedNewUserCase, LoggedCase
from utils.parse_date import parse_date
from utils.redirect_window import redirect_window
from ui.pages.overview_page import OverviewNewUserPage, OverviewPage
from ui.locators.overview_locators import OverviewNewUserPageLocators, OverviewPageLocators
from ui.locators.campaigns_locators import CampaignsPageSharedLocators
from ui.locators.training_locators import TrainingPageSharedLocators


class TestNewUserOverview(LoggedNewUserCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_new_user_overview(self, driver, config):
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
    def setup_overview(self, driver, config):
        self.overview_page = OverviewPage(self.driver)

    def test_display(self):
        self.overview_page.check_display()

    def test_click_create_campaign(self):
        self.overview_page.click(self.overview_page.locators.BUTTON_CREATE_CAMPAIGN)
        assert self.driver.current_url == "https://ads.vk.com/hq/new_create/ad_plan"

    def test_click_new_tab_limit_article(self):
        redirect_window(self.overview_page, self.overview_page.locators.BUTTON_LIMIT_ARTICLE)

        assert self.driver.current_url == "https://ads.vk.com/help/articles/ad_limits"

    def test_modal_page_budget(self):
        self.overview_page.open_modal_view(self.overview_page.locators.BUTTON_BUDGET_REPLENISH,
                                           self.overview_page.locators.SIGN_OPENING_MODAL_PAGE_BUDGET)

        self.overview_page.close_modal_view(self.overview_page.locators.BUTTON_CLOSE_MODAL_PAGE_BUDGET,
                                            self.overview_page.locators.SIGN_OPENING_MODAL_PAGE_BUDGET)

    def test_date_picker(self):
        self.overview_page.open_modal_view(self.overview_page.locators.BUTTON_OPEN_DATE_CHOOSE,
                                           self.overview_page.locators.SIGN_OPENING_DATE_CHOOSE)
        self.overview_page.click(self.overview_page.locators.BUTTON_DATE_RANGE_TODAY)
        self.overview_page.close_modal_view(self.overview_page.locators.BUTTON_APPLY_DATE_CHOOSE)

        button_date_range = self.overview_page.find(self.overview_page.locators.BUTTON_OPEN_DATE_CHOOSE)

        today_date = \
            parse_date(button_date_range.find_element(*self.overview_page.locators.RANGE_TEXT_DATE_CHOOSE).text)

        self.overview_page.open_modal_view(self.overview_page.locators.BUTTON_OPEN_DATE_CHOOSE,
                                           self.overview_page.locators.SIGN_OPENING_DATE_CHOOSE)
        self.overview_page.click(self.overview_page.locators.BUTTON_DATE_RANGE_YESTERDAY)
        self.overview_page.close_modal_view(self.overview_page.locators.BUTTON_APPLY_DATE_CHOOSE)

        yesterday_date = \
            parse_date(button_date_range.find_element(*self.overview_page.locators.RANGE_TEXT_DATE_CHOOSE).text)

        assert (today_date - yesterday_date).days == 1

    @pytest.mark.parametrize('query, expected_locator',
                             [
                                 pytest.param(
                                     "asdfasdf",
                                     OverviewPageLocators.SIGN_SEARCH_NOT_FOUND_RESULTS,
                                 ),
                                 pytest.param(
                                     "Кампания",
                                     OverviewPageLocators.SIGN_SEARCH_FOUND_RESULTS,
                                 )
                             ], )
    def test_search_in_choose_campaigns(self, query, expected_locator):
        self.overview_page.open_modal_view(self.overview_page.locators.BUTTON_CHOOSE_CAMPAIGNS,
                                           self.overview_page.locators.SIGN_OPENING_CHOOSE_CAMPAIGNS)

        self.overview_page.write_input(self.overview_page.locators.INPUT_SEARCH_IN_CHOOSE_CAMPAIGNS, query)

        assert self.overview_page.find(expected_locator).is_displayed()
