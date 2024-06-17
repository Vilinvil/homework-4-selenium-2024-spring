from ui.pages.base_page_functionality import BasePageFunctionality, add_write
from ui.locators.help_locators import HelpPageLocators

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class HelpPage(BasePageFunctionality):
    url = "https://ads.vk.com/help"

    locators = HelpPageLocators()

    @property
    def HEADER_HELP(self):
        return self.find_with_check_visibility(self.locators.HEADER_HELP)

    @property
    @add_write
    def INPUT_SEARCH(self):
        return self.find_with_check_visibility(self.locators.INPUT_SEARCH)

    def search(self, query):
        query = query + Keys.ENTER

        self.INPUT_SEARCH.write(query)

    @property
    def WRAPPER_CATEGORIES(self):
        return self.find_with_check_visibility(self.locators.WRAPPER_CATEGORIES)

    @property
    def SIGN_SEARCH_FOUND_RESULT(self):
        return self.find_with_check_visibility(self.locators.SIGN_SEARCH_FOUND_RESULTS)

    def ARTICLE_BY_TITLE(self, title):
        return self.find_with_check_visibility(self.locators.ARTICLE_BY_TITLE(title))

    @property
    def SIGN_SEARCH_NOT_FOUND_RESULT(self):
        return self.find_with_check_visibility(self.locators.SIGN_SEARCH_NOT_FOUND_RESULTS)

    def ARTICLE_WITH_INNER_LIST_BY_TITLE(self, title):
        return self.find_with_check_visibility(self.locators.ARTICLE_WITH_INNER_LIST_BY_TITLE(title))

    @property
    def SIDEBAR_ARTICLES(self):
        return self.find_with_check_visibility(self.locators.SIDEBAR_ARTICLES)

    @property
    def SEARCH_IN_SIDEBAR_ARTICLES(self):
        search_elem = self.SIDEBAR_ARTICLES.find_element(*self.locators.SEARCH_IN_SIDEBAR_ARTICLES)
        return self.wait().until(EC.visibility_of(search_elem))

    @property
    def CATEGORIES_IN_SIDEBAR_ARTICLES(self):
        categories_elem = self.SIDEBAR_ARTICLES.find_element(*self.locators.CATEGORIES_IN_SIDEBAR_ARTICLES)
        return self.wait().until(EC.visibility_of(categories_elem))

    @property
    def CARD_AUTHORIZATION(self):
        return self.find_with_check_visibility(self.locators.CARD_AUTHORIZATION)

    @property
    def CARD_GENERAL(self):
        return self.find_with_check_visibility(self.locators.CARD_GENERAL)

    def TITLE_ARTICLES(self, title):
        return self.wait().until(EC.text_to_be_present_in_element(self.locators.TITLE_ARTICLES, title))
