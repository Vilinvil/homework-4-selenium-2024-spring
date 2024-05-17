from ui.pages.base_page import PageWithModalView, PageWithRedirectWindow
from ui.locators.training_locators import TrainingPageSharedLocators, TrainingPageLocators

from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.by import By


class TrainingPage(PageWithModalView, PageWithRedirectWindow):
    url = "https://ads.vk.com/hq/overview"
    locators = TrainingPageLocators()
    locators_shared = TrainingPageSharedLocators()

    def find_section_in_content_list(self, section_name):
        content_list = self.find(self.locators.CONTENT_LIST)
        return content_list.find_element(By.XPATH, f'.//*[@role="button"]//*[contains(text(), "{section_name}")]')

    def click_zero_coordinate(self):
        ActionBuilder(self.driver).pointer_action.move_to_location(0, 0).click()
