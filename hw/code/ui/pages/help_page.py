from selenium.webdriver.common.by import By

from ui.pages.base_page import BasePage
from ui.locators.help_locators import HelpPageLocators
from selenium.webdriver.common.keys import Keys

class HelpPage(BasePage):
    url = "https://ads.vk.com/help"

    locators = HelpPageLocators()

    def search(self, query, timeout=None):
        query = query + Keys.ENTER

        self.write_input(self.locators.INPUT_SEARCH, query)
