from ui.pages.base_page import BasePage
from ui.locators.settings_locators import SettingsPageLocators
from utils.timeout import BASIC_TIMEOUT
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from ui.pages.base_page import PageWithModalView, PageWithRedirectWindow


class SettingsPage(PageWithRedirectWindow, PageWithModalView):
    url = "https://ads.vk.com/hq/settings"
    locators = SettingsPageLocators()

    def get_input_field_value(self, locator, timeout=BASIC_TIMEOUT):
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.presence_of_element_located(locator))
        return elem.get_attribute('value')