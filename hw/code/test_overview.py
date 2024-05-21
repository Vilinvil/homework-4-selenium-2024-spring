import pytest

from cases import LoggedNewUserCase, LoggedCase
from utils.parse_date import parse_date
from ui.pages.overview_page import OverviewNewUserPage, OverviewPage
from ui.locators.overview_locators import OverviewNewUserPageLocators, \
    OverviewPageLocators
from ui.locators.campaigns_locators import CampaignsPageSharedLocators
from ui.locators.training_locators import TrainingPageSharedLocators

from selenium.webdriver.support import expected_conditions as EC


class TestNewUserOverview(LoggedNewUserCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_new_user_overview(self, driver):
        self.overview_new_user_page = OverviewNewUserPage(self.driver)

    def test_display(self):
        self.overview_new_user_page.check_display_start_actions()

    @pytest.mark.parametrize('button_locator, expected_locator',
                             [
                                 pytest.param(
                                     OverviewNewUserPageLocators.BUTTON_CREATE_CAMPAIGN,
                                     CampaignsPageSharedLocators.STEP1_SIGN_NEW_AD_CREATE,
                                 ),
                                 pytest.param(
                                     OverviewNewUserPageLocators.BUTTON_START_TRAINING,
                                     TrainingPageSharedLocators.SIGN_OPENING_MODAL_VIEW,
                                 )
                             ], )
    def test_open_page_by_click(self, button_locator, expected_locator):
        self.overview_new_user_page.click(button_locator)
        assert self.overview_new_user_page.find(expected_locator, until_EC=EC.visibility_of_element_located)


class TestOverview(LoggedCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_overview(self, driver):
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

    def test_change_budget_date(self):
        budget_date_elem = self.overview_page.find(self.overview_page.locators.BUTTON_CHOOSE_BUDGET_DATE)
        assert budget_date_elem.text.find("cегодня")

        budget_date_elem.click()

        self.overview_page.click(self.overview_page.locators.BUTTON_CHOOSE_BUDGET_DATE_YESTERDAY)
        budget_date_elem = self.overview_page.find(self.overview_page.locators.BUTTON_CHOOSE_BUDGET_DATE)
        assert budget_date_elem.text.find("Вчера")

    def test_modal_page_budget(self):
        self.overview_page.open_modal_view(self.overview_page.locators.BUTTON_BUDGET_REPLENISH,
                                           self.overview_page.locators.SIGN_OPENING_MODAL_PAGE_BUDGET)

        self.overview_page.close_modal_view(self.overview_page.locators.BUTTON_CLOSE_MODAL_PAGE_BUDGET,
                                            self.overview_page.locators.SIGN_OPENING_MODAL_PAGE_BUDGET)

    def test_date_picker(self):
        self.overview_page.open_modal_view(self.overview_page.locators.choose_date_locators.BUTTON_OPEN_DATE_CHOOSE,
                                           self.overview_page.locators.choose_date_locators.SIGN_OPENING_DATE_CHOOSE)
        self.overview_page.click(self.overview_page.locators.choose_date_locators.BUTTON_DATE_RANGE_TODAY)
        self.overview_page.close_modal_view(self.overview_page.locators.choose_date_locators.BUTTON_APPLY_DATE_CHOOSE,
                                            self.overview_page.locators.choose_date_locators.SIGN_OPENING_DATE_CHOOSE)

        button_date_range = self.overview_page.find(self.overview_page.locators.choose_date_locators.
                                                    BUTTON_OPEN_DATE_CHOOSE)

        today_date = \
            parse_date(button_date_range.find_element(*self.overview_page.locators.
                                                      choose_date_locators.RANGE_TEXT_DATE_CHOOSE).text)

        self.overview_page.open_modal_view(self.overview_page.locators.choose_date_locators.BUTTON_OPEN_DATE_CHOOSE,
                                           self.overview_page.locators.choose_date_locators.SIGN_OPENING_DATE_CHOOSE)
        self.overview_page.click(self.overview_page.locators.choose_date_locators.BUTTON_DATE_RANGE_YESTERDAY)
        self.overview_page.close_modal_view(self.overview_page.locators.choose_date_locators.BUTTON_APPLY_DATE_CHOOSE,
                                            self.overview_page.locators.choose_date_locators.SIGN_OPENING_DATE_CHOOSE)

        yesterday_date = \
            parse_date(button_date_range.find_element(*self.overview_page.locators.choose_date_locators.
                                                      RANGE_TEXT_DATE_CHOOSE).text)

        assert (today_date - yesterday_date).days == 1

    @pytest.fixture(scope="function")
    def setup_choose_campaigns(self):
        self.overview_page.open_modal_view(self.overview_page.locators.choose_campaign_locators.BUTTON_CHOOSE_CAMPAIGNS,
                                           self.overview_page.locators.choose_campaign_locators.
                                           SIGN_OPENING_CHOOSE_CAMPAIGNS)

    @pytest.mark.parametrize('query, expected_locator',
                             [
                                 pytest.param(
                                     "asdfasdf",
                                     OverviewPageLocators.choose_campaign_locators
                                     .SIGN_SEARCH_NOT_FOUND_RESULTS,
                                 ),
                                 pytest.param(
                                     "Кампания",
                                     OverviewPageLocators.choose_campaign_locators
                                     .SIGN_SEARCH_FOUND_RESULTS,
                                 )
                             ], )
    def test_search_in_choose_campaigns(self,setup_choose_campaigns, query, expected_locator):
        self.overview_page.write_input(self.overview_page.locators.choose_campaign_locators.
                                       INPUT_SEARCH_IN_CHOOSE_CAMPAIGNS, query)

        assert self.overview_page.find(expected_locator, until_EC=EC.visibility_of_element_located)

    def test_tooltip_max_count_campaigns(self, setup_choose_campaigns):
        count_choose_campaigns = self.overview_page.get_current_count_chosen_campaigns()
        self.overview_page.activate_amount_campaigns(self.max_count_campaigns - count_choose_campaigns)

        self.overview_page.hover_wrapper(self.overview_page.locators.choose_campaign_locators.
                                         CHECKBOX_CHOOSE_CAMPAIGN_FOR_TOOLTIP)
        assert self.overview_page.find(self.overview_page.locators.choose_campaign_locators.
                                       TOOLTIP_MAX_COUNT_CHOOSE_CAMPAIGN)

    def test_reset_choose_campaigns(self, setup_choose_campaigns):
        cur_count_chose_campaigns = self.overview_page.get_current_count_chosen_campaigns()
        assert cur_count_chose_campaigns != 0

        self.overview_page.click(self.overview_page.locators.choose_campaign_locators.
                                 BUTTON_RESET_CHOOSE_CAMPAIGN)

        cur_count_chose_campaigns = self.overview_page.get_current_count_chosen_campaigns()
        assert cur_count_chose_campaigns == 0

        checkboxes = self.driver.find_elements(*self.overview_page.locators.choose_campaign_locators.
                                               CHECKBOX_CHOOSE_CAMPAIGN_ON)
        for checkbox in checkboxes:
            if checkbox.is_displayed():
                raise BaseException("Checkbox should not be displayed")

    def test_check_save_campaigns(self, setup_choose_campaigns):
        expected_count_chose_campaigns = 2

        self.overview_page.click(self.overview_page.locators.choose_campaign_locators
                                 .BUTTON_RESET_CHOOSE_CAMPAIGN)
        self.overview_page.activate_amount_campaigns(expected_count_chose_campaigns)

        self.overview_page.close_modal_view(self.overview_page.locators.choose_campaign_locators
                                            .BUTTON_SAVE_CHOOSE_CAMPAIGN,
                                            self.overview_page.locators.choose_campaign_locators.
                                            SIGN_OPENING_CHOOSE_CAMPAIGNS)

        chose_campaigns = self.driver.find_elements(*self.overview_page.locators.choose_campaign_locators.
                                                    COUNTER_CHOOSE_CAMPAIGN_IN_MAIN_VIEW)

        assert len(chose_campaigns) == expected_count_chose_campaigns

    def test_choose_settings_graph(self):
        begin_graph_settings = self.overview_page.find(self.overview_page.locators.settings_graph_locators.
                                                       BUTTON_OPEN_SETTINGS_GRAPH).text

        self.overview_page.open_modal_view(self.overview_page.locators.settings_graph_locators.BUTTON_OPEN_SETTINGS_GRAPH,
                                           self.overview_page.locators.settings_graph_locators.
                                           SIGN_OPENING_CHOOSE)

        self.overview_page.click(self.overview_page.locators.settings_graph_locators.BUTTON_CHOOSE_CLICKS)

        self.overview_page.close_modal_view(self.overview_page.locators.settings_graph_locators.
                                            BUTTON_SAVE,
                                            self.overview_page.locators.settings_graph_locators.
                                            SIGN_OPENING_CHOOSE)

        end_graph_settings = self.overview_page.find(self.overview_page.locators.settings_graph_locators.
                                                     BUTTON_OPEN_SETTINGS_GRAPH).text

        assert begin_graph_settings != end_graph_settings and end_graph_settings == "Клики"

    def test_useful_articles(self):
        self.overview_page.click(self.overview_page.locators.useful_articles_locators.BUTTON_CASES)
        begin_useful_articles = self.overview_page.find(self.overview_page.locators.useful_articles_locators.
                                                        USEFUL_ARTICLES).screenshot_as_base64

        self.overview_page.click(self.overview_page.locators.useful_articles_locators.BUTTON_NEWS)

        end_useful_articles = self.overview_page.find(self.overview_page.locators.useful_articles_locators.
                                                      USEFUL_ARTICLES).screenshot_as_base64

        assert begin_useful_articles != end_useful_articles
