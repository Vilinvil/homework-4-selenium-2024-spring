import pytest

from cases import BaseCase
from ui.pages.help_page import HelpPage

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
class TestHelp(BaseCase):
    def test_searh(self, query, is_found_expected):
        self.base_page.click(self.base_page.locators.BUTTON_HELP)

        helpPage = HelpPage(self.driver)

        helpPage.search(query)

        if is_found_expected:
            assert helpPage.find(helpPage.locators.SEARCH_FOUND_RESULTS)
        else:
            assert helpPage.find(helpPage.locators.SEARCH_NOT_FOUND_RESULTS)
