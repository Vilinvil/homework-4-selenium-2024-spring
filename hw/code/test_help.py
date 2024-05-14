import pytest

from cases import BaseCase
from ui.locators.help_locators import HelpPageLocators
from ui.pages.help_page import HelpPage


class TestHelp(BaseCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_help(self, driver, config):
        self.base_page.click(self.base_page.locators.BUTTON_HELP)
        self.help_page = HelpPage(self.driver)

    def test_display(self):
        assert self.help_page.find(self.help_page.locators.HEADER_HELP)
        assert self.help_page.find(self.help_page.locators.INPUT_SEARCH)
        assert self.help_page.find(self.help_page.locators.WRAPPER_CATEGORIES)

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
            assert self.help_page.find(self.help_page.locators.SEARCH_FOUND_RESULTS)
        else:
            assert self.help_page.find(self.help_page.locators.SEARCH_NOT_FOUND_RESULTS)

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
        assert self.help_page.find(self.help_page.locators.LIST_ARTICLES)

        sidebar_articles = self.help_page.find(self.help_page.locators.SIDEBAR_ARTICLES)
        assert sidebar_articles.find_element(self.help_page.locators.SEARCH_IN_SIDEBAR_ARTICLES[0],
                                             self.help_page.locators.SEARCH_IN_SIDEBAR_ARTICLES[1])

        assert self.help_page.find(self.help_page.locators.CATEGORIES_IN_SIDEBAR_ARTICLES)
