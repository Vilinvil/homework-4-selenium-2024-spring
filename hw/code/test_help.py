import pytest

from cases import BaseCase
from ui.locators.help_locators import HelpPageLocators
from ui.pages.help_page import HelpPage

from selenium.webdriver.support import expected_conditions as EC


class TestHelp(BaseCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_help(self, driver):
        self.base_page.click_nav_button_help()
        self.help_page = HelpPage(self.driver)

    def test_display(self):
        assert self.help_page.find_header_help()
        assert self.help_page.find_input_search()
        assert self.help_page.find_wrapper_categories()

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
            assert self.help_page.find_sign_found_result()
        else:
            assert self.help_page.find_sign_not_found_result()

    @pytest.mark.parametrize(
        'click_to_card,expected_title',
        [
            pytest.param(
                HelpPage.click_to_card_authorization, 'Авторизация'
            ),
            pytest.param(
                HelpPage.click_to_card_general, 'Как настроить рекламу'
            ),
        ],
    )
    def test_card_display(self, click_to_card, expected_title):
        click_to_card(self.help_page)

        title_articles = self.help_page.get_title_articles()

        assert expected_title == title_articles.text
        assert self.help_page.find_list_articles()

        assert self.help_page.find_sidebar_articles_search()
        assert self.help_page.find_sidebar_articles_categories()

    @pytest.mark.parametrize(
        'click_to_card',
        [
            pytest.param(
                HelpPage.click_to_card_authorization
            ),
            pytest.param(
                HelpPage.click_to_card_general
            ),
        ],
    )
    def test_card_go_to_article(self, click_to_card):
        click_to_card(self.help_page)

        list_articles = self.help_page.find_list_articles()
        self.help_page.click_href_in_list_articles(list_articles)

        assert self.help_page.find_article_page()
