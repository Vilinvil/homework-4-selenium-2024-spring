from ui.pages.base_page import BasePage
from ui.locators.help_locators import HelpPageLocators

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class HelpPage(BasePage):
    url = "https://ads.vk.com/help"

    locators = HelpPageLocators()

    def search(self, query, timeout=None):
        query = query + Keys.ENTER

        self.write_input(self.locators.INPUT_SEARCH, query)

    def click_to_card(self, card_locator):
        self.click(card_locator)
        self.wait().until(EC.invisibility_of_element_located(card_locator))
