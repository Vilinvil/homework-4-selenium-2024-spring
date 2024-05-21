import pytest

from cases import BaseCase
from ui.locators.monetization_locators import MonetizationPageLocators
from ui.pages.base_page import PageWithRedirectWindow
from ui.pages.monetization_page import MonetizationPage
from utils.timeout import BASIC_TIMEOUT

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC


class TestMonetizationFooter(BaseCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_monetization(self, driver):
        self.redirect_page = PageWithRedirectWindow(self.driver)
        self.base_page.redirect_nav_monetization(self.redirect_page)

        self.monetization_page = MonetizationPage(self.driver)

    def test_display(self):
        self.monetization_page.go_to_footer()

        assert self.monetization_page.find_help_button()
        assert self.monetization_page.find_rules_button()
        assert self.monetization_page.find_main_button()
        assert self.monetization_page.find_language_wrapper()
        assert self.monetization_page.find_vk_business_logo()


    def test_vk_business_logo_redirect(self):
        self.monetization_page.redirect_to_vk_business(self.redirect_page)
        self.monetization_page.check_url('https://vk.company/ru/company/business/')


    @pytest.mark.parametrize(
        'button,url',
        [
            pytest.param(
                MonetizationPage.click_rules_button,
                'https://ads.vk.com/help/articles/partner_rules'
            ),
            pytest.param(
                MonetizationPage.click_main_button, 'https://ads.vk.com/'
            ),
            pytest.param(
                MonetizationPage.click_help_button,
                'https://ads.vk.com/help/categories/partner'
            ),
        ],
    )
    def test_open_pages(self, button, url):
        button(self.monetization_page)

        self.monetization_page.check_url(url)

    @pytest.mark.parametrize(
        'button,text_value',
        [
            pytest.param(
                MonetizationPage.click_ru_button, 'RU'
            ),
            pytest.param(
                MonetizationPage.click_en_button, 'EN'
            ),
        ],
    )
    def test_language_wrapped_buttons(self, button, text_value):
        self.monetization_page.click_language_wrapper()

        button(self.monetization_page)
        assert self.monetization_page.find_language_wrapper().text == text_value

