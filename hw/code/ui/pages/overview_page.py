from ui.pages.base_page import BasePage, PageWithView, PageWithRedirectWindow
from ui.locators.overview_locators import OverviewNewUserPageLocators
from ui.locators.overview_locators import OverviewPageLocators
from ui.locators.training_locators import TrainingPageSharedLocators
from ui.locators.campaigns_locators import CampaignsPageSharedLocators
from utils.parse_date import parse_date

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class OverviewNewUserPage(BasePage):
    url = "https://ads.vk.com/hq/overview"
    locators = OverviewNewUserPageLocators()
    locators_training = TrainingPageSharedLocators()
    locators_campaigns = CampaignsPageSharedLocators()

    def check_display_start_actions(self):
        start_actions_wrapper = self.find_with_check_visibility(self.locators.START_ACTIONS_WRAPPER)

        start_actions = start_actions_wrapper.find_elements(*self.locators.START_ACTION)

        for start_action in start_actions:
            elem = start_action.find_element(By.XPATH, './/button')
            self.wait().until(EC.visibility_of(elem))

    def open_create_campaign(self):
        self.click(self.locators.BUTTON_CREATE_CAMPAIGN)
        self.find_with_check_visibility(self.locators_campaigns.STEP1_SIGN_NEW_AD_CREATE)

    def open_start_training(self):
        self.click(self.locators.BUTTON_START_TRAINING)
        self.find_with_check_visibility(self.locators_training.SIGN_OPENING_MODAL_VIEW)


class OverviewPage(PageWithView, PageWithRedirectWindow):
    url = "https://ads.vk.com/hq/overview"
    locators = OverviewPageLocators()
    locators_campaigns = CampaignsPageSharedLocators()

    def check_display(self):
        assert self.find_with_check_visibility(self.locators.WIDGET_CAMPAIGNS)
        assert self.find_with_check_visibility(self.locators.WIDGET_BUDGET)
        assert self.find_with_check_visibility(self.locators.WIDGET_LIMIT)
        assert self.find_with_check_visibility(self.locators.WIDGET_FAVOURITES)
        assert self.find_with_check_visibility(self.locators.BUTTON_CREATE_CAMPAIGN)
        assert self.find_with_check_visibility(self.locators.BUTTON_BUDGET_REPLENISH)
        assert self.find_with_check_visibility(self.locators.choose_campaign_locators.BUTTON_CHOOSE_CAMPAIGNS)
        assert self.find_with_check_visibility(self.locators.BUTTON_LIMIT_ARTICLE)

    def activate_amount_campaigns(self, expected_count_chose_campaigns):
        self.find(self.locators.choose_campaign_locators.CHECKBOX_CHOOSE_CAMPAIGN_OFF)
        checkboxes = self.driver.find_elements(*self.locators.choose_campaign_locators.CHECKBOX_CHOOSE_CAMPAIGN_OFF)

        cur_count_clicked_checkboxes = 0
        while len(checkboxes) != 0 and cur_count_clicked_checkboxes < expected_count_chose_campaigns:
            if checkboxes[0].is_displayed():
                checkboxes[0].click()
                cur_count_clicked_checkboxes += 1
            checkboxes = checkboxes[1:]

        if cur_count_clicked_checkboxes < expected_count_chose_campaigns:
            raise BaseException("Not enough checkboxes to click")

    def find_sign_not_found_result_in_choose_campaign(self):
        return self.find_with_check_visibility(self.locators.choose_campaign_locators.SIGN_SEARCH_NOT_FOUND_RESULTS)

    def find_sign_found_result_in_choose_campaign(self):
        return self.find_with_check_visibility(self.locators.choose_campaign_locators.SIGN_SEARCH_FOUND_RESULTS)

    def find_tooltip_max_choose_campaign(self):
        return self.find_with_check_visibility(self.locators.choose_campaign_locators.TOOLTIP_MAX_COUNT_CHOOSE_CAMPAIGN)

    def open_create_campaign(self):
        self.click(self.locators.BUTTON_CREATE_CAMPAIGN)
        self.find_with_check_visibility(self.locators_campaigns.STEP1_SIGN_NEW_AD_CREATE)

    def open_budget_replenish(self):
        self.open_view(self.locators.BUTTON_BUDGET_REPLENISH,
                       self.locators.SIGN_OPENING_MODAL_PAGE_BUDGET)

    def open_date_choose(self):
        self.open_view(self.locators.choose_date_locators.BUTTON_OPEN_DATE_CHOOSE,
                       self.locators.choose_date_locators.SIGN_OPENING_DATE_CHOOSE)

    def open_campaign_choose(self):
        self.open_view(self.locators.choose_campaign_locators.BUTTON_CHOOSE_CAMPAIGNS,
                       self.locators.choose_campaign_locators.SIGN_OPENING_CHOOSE_CAMPAIGNS)

    def open_settings_graph(self):
        self.open_view(self.locators.settings_graph_locators.BUTTON_OPEN_SETTINGS_GRAPH,
                       self.locators.settings_graph_locators.SIGN_OPENING_CHOOSE)

    def apply_date_choose(self):
        self.close_view(self.locators.choose_date_locators.BUTTON_APPLY_DATE_CHOOSE,
                        self.locators.choose_date_locators.SIGN_OPENING_DATE_CHOOSE)

    def apply_campaign_choose(self):
        self.close_view(self.locators.choose_campaign_locators.BUTTON_SAVE_CHOOSE_CAMPAIGN,
                              self.locators.choose_campaign_locators.SIGN_OPENING_CHOOSE_CAMPAIGNS)

    def apply_settings_graph(self):
        self.close_view(self.locators.settings_graph_locators.BUTTON_SAVE,
                        self.locators.settings_graph_locators.SIGN_OPENING_CHOOSE)

    def close_budget_replenish(self):
        self.close_view(self.locators.BUTTON_CLOSE_MODAL_PAGE_BUDGET,
                        self.locators.SIGN_OPENING_MODAL_PAGE_BUDGET)

    def redirect_limit_article(self):
        self.redirect_window(self.locators.BUTTON_LIMIT_ARTICLE)

    def hover_checkbox_choose_campaign(self):
        self.hover_wrapper(self.locators.choose_campaign_locators.CHECKBOX_CHOOSE_CAMPAIGN_FOR_TOOLTIP)

    def write_search_in_choose_campaign(self, query):
        self.write_input(self.locators.choose_campaign_locators.
                                       INPUT_SEARCH_IN_CHOOSE_CAMPAIGNS, query)

    def click_budget_date_yesterday(self):
        self.click(self.locators.BUTTON_CHOOSE_BUDGET_DATE_YESTERDAY)

    def click_date_choose_today(self):
        self.click(self.locators.choose_date_locators.BUTTON_DATE_RANGE_TODAY)

    def click_date_choose_yesterday(self):
        self.click(self.locators.choose_date_locators.BUTTON_DATE_RANGE_YESTERDAY)

    def click_reset_choose_campaign(self):
        self.click(self.locators.choose_campaign_locators.BUTTON_RESET_CHOOSE_CAMPAIGN)

    def click_choose_setting_graph_clicks(self):
        self.click(self.locators.settings_graph_locators.BUTTON_CHOOSE_CLICKS)

    def click_button_cases(self):
        self.click(self.locators.useful_articles_locators.BUTTON_CASES)

    def click_button_news(self):
        self.click(self.locators.useful_articles_locators.BUTTON_NEWS)

    def get_current_count_chosen_campaigns(self):
        text_choose_campaign = self.find(self.locators.choose_campaign_locators.COUNTER_CHOOSE_CAMPAIGN).text
        idx_counter = text_choose_campaign.find(' ')

        try:
            result = int(text_choose_campaign[idx_counter:idx_counter + 2])
        except ValueError:
            result = 0

        return result

    def get_budget_date(self):
        return self.find(self.locators.BUTTON_CHOOSE_BUDGET_DATE)

    def get_date(self):
        button_date_range = self.find(self.locators.choose_date_locators.BUTTON_OPEN_DATE_CHOOSE)

        text_date = button_date_range.find_element(*self.locators.choose_date_locators.RANGE_TEXT_DATE_CHOOSE).text

        return parse_date(text_date)

    def get_counter_choose_campaign_in_main_view(self):
        chose_campaigns = self.driver.find_elements(*self.locators.choose_campaign_locators.
                                                    COUNTER_CHOOSE_CAMPAIGN_IN_MAIN_VIEW)

        return len(chose_campaigns)

    def get_graph_settings_text(self):
        return self.find(self.locators.settings_graph_locators.BUTTON_OPEN_SETTINGS_GRAPH).text

    def get_screenshot_useful_articles(self):
        return self.find(self.locators.useful_articles_locators.USEFUL_ARTICLES).screenshot_as_base64

    def is_not_display_checkboxes(self):
        checkboxes = self.driver.find_elements(*self.locators.choose_campaign_locators.
                                               CHECKBOX_CHOOSE_CAMPAIGN_ON)
        for checkbox in checkboxes:
            if checkbox.is_displayed():
                return False

        return True
