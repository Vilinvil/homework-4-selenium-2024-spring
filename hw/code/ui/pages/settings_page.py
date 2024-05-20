from ui.locators.settings_locators import SettingsPageLocators
from utils.timeout import BASIC_TIMEOUT
from ui.pages.base_page import PageWithModalView, PageWithRedirectWindow


class SettingsPage(PageWithRedirectWindow, PageWithModalView):
    url = "https://ads.vk.com/hq/settings"
    locators = SettingsPageLocators()

    def get_input_field_value(self, locator, timeout=BASIC_TIMEOUT):
        elem = self.find(locator, timeout=timeout)
        return elem.get_attribute('value')
