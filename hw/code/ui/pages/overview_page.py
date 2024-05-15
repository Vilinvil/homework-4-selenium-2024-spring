from ui.pages.base_page import BasePage, PageWithModalView
from ui.locators.overview_locators import OverviewNewUserPageLocators
from ui.locators.overview_locators import OverviewPageLocators
from ui.locators.training_locators import TrainingPageSharedLocators
from ui.locators.campaigns_locators import CampaignsPageSharedLocators

from selenium.webdriver.common.by import By


class OverviewNewUserPage(BasePage):
    url = "https://ads.vk.com/hq/overview"
    locators = OverviewNewUserPageLocators()
    locators_training = TrainingPageSharedLocators()
    locators_campaigns = CampaignsPageSharedLocators()

    def check_display_start_actions(self):
        start_actions_wrapper = (
            self.find(self.locators.START_ACTIONS_WRAPPER))

        start_actions = start_actions_wrapper.find_elements(*self.locators.START_ACTION)

        for start_action in start_actions:
            assert start_action.find_element(By.XPATH, './/button').is_displayed()


class OverviewPage(PageWithModalView):
    url = "https://ads.vk.com/hq/overview"
    locators = OverviewPageLocators()

    def check_display(self):
        assert self.find(self.locators.WIDGET_CAMPAIGNS).is_displayed()
        assert self.find(self.locators.WIDGET_BUDGET).is_displayed()
        assert self.find(self.locators.WIDGET_LIMIT).is_displayed()
        assert self.find(self.locators.WIDGET_FAVOURITES).is_displayed()
        assert self.find(self.locators.BUTTON_CREATE_CAMPAIGN).is_displayed()
        assert self.find(self.locators.BUTTON_BUDGET_REPLENISH).is_displayed()
        assert self.find(self.locators.BUTTON_CHOOSE_CAMPAIGNS).is_displayed()
        assert self.find(self.locators.BUTTON_LIMIT_ARTICLE).is_displayed()
