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
        assert self.help_page.HEADER_HELP
        assert self.help_page.INPUT_SEARCH
        assert self.help_page.WRAPPER_CATEGORIES

    @pytest.mark.parametrize(
        'query,is_found_expected,result_articles',
        [
            pytest.param(
                'авторизация', True, ('Создание нового кабинета, авторизация', 'API VK Рекламы')
            ),
            pytest.param(
                'реклама', True, ('Запуск товарной рекламы для сайтов и мобильных приложений',
                                  'Продвижение сообществ', 'Добавление нового приложения')
            ),
            pytest.param(
                'статистика', True, ('Дашборд', 'Агентствам: статистика по клиентам',
                                     'Статистика из приложений для веб-кампаний')
            ),
            pytest.param(
                'сайт', True, ('Запуск товарной рекламы для сайтов и мобильных приложений',
                               'Запуск рекламы сайта', 'Блокировка рекламы')
            ),
            pytest.param(
                'таргетинг', True, ('Динамический ретаргетинг на базе мобильных событий',
                                    'Динамический ретаргетинг на базе веб-событий', 'Таргетинги')
            ),
            pytest.param(
                'asdfasdf', False, ()
            ),
            pytest.param(
                'Проверка xss “”></script><img src onerror=alert()>', False, ()
            ),
        ],
    )
    def test_search(self, query, is_found_expected, result_articles):
        self.help_page.search(query)

        if is_found_expected:
            assert self.help_page.SIGN_SEARCH_FOUND_RESULT

            for article in result_articles:
                assert self.help_page.ARTICLE_BY_TITLE(article)
        else:
            assert self.help_page.SIGN_SEARCH_NOT_FOUND_RESULT

    @pytest.mark.parametrize(
        'click_to_card,expected_title,expected_articles',
        [
            pytest.param(
                lambda help_page: help_page.click(help_page.CARD_AUTHORIZATION), 'Авторизация',
                ('Создание нового кабинета, авторизация', 'Обзор кабинета',
                 'Агентствам: регистрация и импорт кабинета агентств')
            ),
            pytest.param(
                lambda help_page: help_page.click(help_page.CARD_GENERAL), 'Как настроить рекламу',
                ('Продвижение видео и трансляций', 'Продвижение музыки',
                 'Продвижение мини-приложений (VK Mini Apps и игры ВКонтакте)')
            ),
        ],
    )
    def test_card_display(self, click_to_card, expected_title, expected_articles):
        click_to_card(self.help_page)

        assert self.help_page.TITLE_ARTICLES(expected_title)

        for article in expected_articles:
            assert self.help_page.ARTICLE_WITH_INNER_LIST_BY_TITLE(article)

        assert self.help_page.SEARCH_IN_SIDEBAR_ARTICLES
        assert self.help_page.CATEGORIES_IN_SIDEBAR_ARTICLES
