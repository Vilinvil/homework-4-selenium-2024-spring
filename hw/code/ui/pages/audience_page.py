from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage
from ui.locators.audience_locators import AudiencePageLocators

class AudiencePage(BasePage):
    url = "https://ads.vk.com/hq/audience"
    locators = AudiencePageLocators()

    def find_tabs_in_subnav(self, tab_name):
        id_audience = self.find(self.locators.ID_AUDIENCE, until_EC=EC.visibility_of_element_located)
        return id_audience.find_element(By.CSS_SELECTOR, f'[aria-controls="{tab_name}"]')

    def click_create_audience(self):
        self.click(self.locators.BUTTON_CREATE_GROUP)

    def find_source_items(self, source_items):
        root = self.find(self.locators.ROOT, until_EC=EC.visibility_of_element_located)
        return root.find_element(By.XPATH, f'//*[contains(@class, "vkuiSimpleCell")]//*[contains(text(), "{source_items}")]')
