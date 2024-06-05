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

    def find_header_help(self):
        return self.find_with_check_visibility(self.locators.HEADER_HELP)

    def find_input_search(self):
        return self.find_with_check_visibility(self.locators.INPUT_SEARCH)

    def find_wrapper_categories(self):
        return self.find_with_check_visibility(self.locators.WRAPPER_CATEGORIES)

    def find_sign_found_result(self):
        return self.find_with_check_visibility(self.locators.SIGN_SEARCH_FOUND_RESULTS)

    def find_sign_not_found_result(self):
        return self.find_with_check_visibility(self.locators.SIGN_SEARCH_NOT_FOUND_RESULTS)

    def find_list_articles(self):
        return self.find_with_check_visibility(self.locators.LIST_ARTICLES)

    def find_sidebar_articles_search(self):
        sidebar_articles = self.find(self.locators.SIDEBAR_ARTICLES)

        search_elem = sidebar_articles.find_element(*self.locators.SEARCH_IN_SIDEBAR_ARTICLES)
        return self.wait().until(EC.visibility_of(search_elem))

    def find_sidebar_articles_categories(self):
        sidebar_articles = self.find(self.locators.SIDEBAR_ARTICLES)

        categories_elem = sidebar_articles.find_element(*self.locators.CATEGORIES_IN_SIDEBAR_ARTICLES)
        return self.wait().until(EC.visibility_of(categories_elem))

    def click_to_card(self, card_locator):
        self.click(card_locator)
        self.wait().until(EC.invisibility_of_element_located(card_locator))

    def click_to_card_authorization(self):
        self.click_to_card(self.locators.CARD_AUTHORIZATION)

    def click_to_card_general(self):
        self.click_to_card(self.locators.CARD_GENERAL)

    def get_title_articles(self):
        return self.find_with_check_visibility(self.locators.TITLE_ARTICLES)