import pytest

from cases import LoggedNewUserCase, LoggedCase
from utils.parse_date import parse_date
from ui.pages.overview_page import OverviewNewUserPage, OverviewPage
from ui.locators.overview_locators import OverviewNewUserPageLocators, OverviewPageLocators
from ui.locators.campaigns_locators import CampaignsPageSharedLocators
from ui.locators.training_locators import TrainingPageSharedLocators

from selenium.webdriver.support import expected_conditions as EC


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
        self.max_count_campaigns = 5

    def test_display(self):
        self.overview_page.check_display()

    def test_click_create_campaign(self):
        self.overview_page.click(self.overview_page.locators.BUTTON_CREATE_CAMPAIGN)
        assert self.overview_page.wait().until(EC.url_to_be("https://ads.vk.com/hq/new_create/ad_plan"))

    def test_click_new_tab_limit_article(self):
        self.overview_page.redirect_window(self.overview_page.locators.BUTTON_LIMIT_ARTICLE)

        assert self.overview_page.wait().until(EC.url_to_be("https://ads.vk.com/help/articles/ad_limits"))

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

    def test_tooltip_max_count_campaigns(self):
        self.overview_page.open_modal_view(self.overview_page.locators.BUTTON_CHOOSE_CAMPAIGNS,
                                           self.overview_page.locators.SIGN_OPENING_CHOOSE_CAMPAIGNS)

        count_choose_campaigns = self.overview_page.get_current_count_chose_campaigns()
        self.overview_page.activate_count_choose_campaigns(self.max_count_campaigns - count_choose_campaigns)

        self.overview_page.hover_wrapper(self.overview_page.locators.CHECKBOX_CHOOSE_CAMPAIGN_FOR_TOOLTIP)
        assert self.overview_page.find(self.overview_page.locators.TOOLTIP_MAX_COUNT_CHOOSE_CAMPAIGN)

    def test_reset_choose_campaigns(self):
        self.overview_page.open_modal_view(self.overview_page.locators.BUTTON_CHOOSE_CAMPAIGNS,
                                           self.overview_page.locators.SIGN_OPENING_CHOOSE_CAMPAIGNS)

        cur_count_chose_campaigns = self.overview_page.get_current_count_chose_campaigns()
        assert cur_count_chose_campaigns != 0

        self.overview_page.click(self.overview_page.locators.BUTTON_RESET_CHOOSE_CAMPAIGN)

        cur_count_chose_campaigns = self.overview_page.get_current_count_chose_campaigns()
        assert cur_count_chose_campaigns == 0

        checkboxes = self.driver.find_elements(*self.overview_page.locators.CHECKBOX_CHOOSE_CAMPAIGN)
        for checkbox in checkboxes:
            if checkbox.is_displayed():
                raise BaseException("Checkbox should not be displayed")

    def test_check_save_campaigns(self):
        self.overview_page.open_modal_view(self.overview_page.locators.BUTTON_CHOOSE_CAMPAIGNS,
                                           self.overview_page.locators.SIGN_OPENING_CHOOSE_CAMPAIGNS)

        expected_count_chose_campaigns = 2

        self.overview_page.click(self.overview_page.locators.BUTTON_RESET_CHOOSE_CAMPAIGN)
        self.overview_page.activate_count_choose_campaigns(expected_count_chose_campaigns)

        self.overview_page.close_modal_view(self.overview_page.locators.BUTTON_SAVE_CHOOSE_CAMPAIGN,
                                            self.overview_page.locators.SIGN_OPENING_CHOOSE_CAMPAIGNS)

        chose_campaigns = self.driver.find_elements(*self.overview_page.locators.COUNTER_CHOOSE_CAMPAIGN_IN_MAIN_VIEW)

        assert len(chose_campaigns) == expected_count_chose_campaigns
