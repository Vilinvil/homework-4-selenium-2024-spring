import pytest

from cases import BaseCase
from ui.locators.help_locators import HelpPageLocators
from ui.pages.help_page import HelpPage

from selenium.webdriver.support import expected_conditions as EC


class TestHelp(BaseCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_help(self, driver):
        self.base_page.click(self.base_page.locators.NAV_BUTTON_HELP)
        self.help_page = HelpPage(self.driver)

    def test_display(self):
        assert self.help_page.find(self.help_page.locators.HEADER_HELP, until_EC=EC.visibility_of_element_located)
        assert self.help_page.find(self.help_page.locators.INPUT_SEARCH, until_EC=EC.visibility_of_element_located)
        assert self.help_page.find(self.help_page.locators.WRAPPER_CATEGORIES,
                                   until_EC=EC.visibility_of_element_located)

    @pytest.mark.parametrize(
        'query,is_found_expected',
        [
            pytest.param(
                'авторизация', True
            ),
            pytest.param(
                'реклама', True
            ),
            pytest.param(
                'asdfasdf', False
            ),
            pytest.param(
                'Проверка xss “”></script><img src onerror=alert()>', False
            ),
        ],
    )
    def test_search(self, query, is_found_expected):
        self.help_page.search(query)

        if is_found_expected:
            assert self.help_page.find(self.help_page.locators.SEARCH_FOUND_RESULTS,
                                       until_EC=EC.visibility_of_element_located)
        else:
            assert self.help_page.find(self.help_page.locators.SEARCH_NOT_FOUND_RESULTS,
                                       until_EC=EC.visibility_of_element_located)

    @pytest.mark.parametrize(
        'card_locator,expected_title',
        [
            pytest.param(
                HelpPageLocators.CARD_AUTHORIZATION, 'Авторизация'
            ),
            pytest.param(
                HelpPageLocators.CARD_GENERAL, 'Как настроить рекламу'
            ),
        ],
    )
    def test_card_display(self, card_locator, expected_title):
        self.help_page.click_to_card(card_locator)

        title_articles = self.help_page.find(self.help_page.locators.TITLE_ARTICLES)

        assert expected_title == title_articles.text
        assert self.help_page.find(self.help_page.locators.LIST_ARTICLES, until_EC=EC.visibility_of_element_located)

        sidebar_articles = self.help_page.find(self.help_page.locators.SIDEBAR_ARTICLES)

        search_elem = sidebar_articles.find_element(*self.help_page.locators.SEARCH_IN_SIDEBAR_ARTICLES)
        self.help_page.wait().until(EC.visibility_of(search_elem))

        categories_elem = sidebar_articles.find_element(*self.help_page.locators.CATEGORIES_IN_SIDEBAR_ARTICLES)
        self.help_page.wait().until(EC.visibility_of(categories_elem))

    @pytest.mark.parametrize(
        'card_locator',
        [
            pytest.param(
                HelpPageLocators.CARD_AUTHORIZATION
            ),
            pytest.param(
                HelpPageLocators.CARD_GENERAL
            ),
        ],
    )
    def test_card_go_to_article(self, card_locator):
        self.help_page.click_to_card(card_locator)

        list_articles = self.help_page.find(self.help_page.locators.LIST_ARTICLES)

        href_article = list_articles.find_element(*self.help_page.locators.ARTICLE_HREF_IN_PAGE)
        href_article.click()

        assert self.help_page.find(self.help_page.locators.ARTICLE_PAGE, until_EC=EC.visibility_of_element_located)
