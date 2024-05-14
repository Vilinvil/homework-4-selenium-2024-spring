from ui.pages.base_page import BasePage
from ui.locators.overview_locators import OverviewNewUserPageLocators
from ui.locators.training_locators import TrainingPageSharedLocators
from ui.locators.campaigns_locators import CampaignsPageSharedLocators

from selenium.webdriver.common.by import By


class OverviewNewUserPage(BasePage):
    url = "https://ads.vk.com/hq/overview"
    locators = OverviewNewUserPageLocators()
    locators_training = TrainingPageSharedLocators()
    locators_campaigns = CampaignsPageSharedLocators()

    def check_start_actions(self):
        start_actions_wrapper = (
            self.find(self.locators.START_ACTIONS_WRAPPER))

        start_actions = start_actions_wrapper.find_elements(self.locators.START_ACTION[0],
                                                            self.locators.START_ACTION[1])

        for start_action in start_actions:
            assert start_action.find_element(By.XPATH, './/button').is_displayed()
