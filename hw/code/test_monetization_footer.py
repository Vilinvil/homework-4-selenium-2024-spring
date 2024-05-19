import pytest

from cases import BaseCase
from ui.locators.monetization_locators import MonetizationPageLocators
from ui.pages.base_page import PageWithRedirectWindow
from ui.pages.monetization_page import MonetizationPage
from selenium.webdriver.support import expected_conditions as EC
from utils.timeout import BASIC_TIMEOUT
from selenium.webdriver.common.action_chains import ActionChains as AC


class TestMonetizationFooter(BaseCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_monetization(self, driver):
        self.redirect_page = PageWithRedirectWindow(self.driver)
        self.redirect_page.redirect_window(self.base_page.locators.NAV_BUTTON_MONETIZATION)

        self.monetization_page = MonetizationPage(self.driver)

    def test_display(self):
        elem = self.monetization_page.wait(BASIC_TIMEOUT).until(
            EC.presence_of_element_located(self.monetization_page.locators.MONETIZATION_FOOTER_LOGO_VK_BUSINESS))
        AC(self.driver).move_to_element(elem).perform()

        assert self.monetization_page.find(self.monetization_page.locators.MONETIZATION_FOOTER_BUTTON_HELP)
        assert self.monetization_page.find(self.monetization_page.locators.MONETIZATION_FOOTER_BUTTON_RULES)
        assert self.monetization_page.find(self.monetization_page.locators.MONETIZATION_FOOTER_BUTTON_MAIN)
        assert self.monetization_page.find(self.monetization_page.locators.MONETIZATION_FOOTER_LANGUAGE_WRAPPER)
        assert self.monetization_page.find(self.monetization_page.locators.MONETIZATION_FOOTER_LOGO_VK_BUSINESS)

    @pytest.mark.parametrize(
        'locator,url,redirect',
        [
            pytest.param(
                MonetizationPageLocators.MONETIZATION_FOOTER_LOGO_VK_BUSINESS,
                'https://vk.company/ru/company/business/', True
            ),
            pytest.param(
                MonetizationPageLocators.MONETIZATION_FOOTER_BUTTON_RULES,
                'https://ads.vk.com/help/articles/partner_rules', False
            ),
            pytest.param(
                MonetizationPageLocators.MONETIZATION_FOOTER_BUTTON_MAIN, 'https://ads.vk.com/', False
            ),
            pytest.param(
                MonetizationPageLocators.MONETIZATION_FOOTER_BUTTON_HELP,
                'https://ads.vk.com/help/categories/partner', False
            ),
        ],
    )
    def test_open_pages(self, locator, url, redirect):
        if redirect:
            self.redirect_page.redirect_window_with_scroll(locator, 3)
        else:
            elem = self.monetization_page.wait(BASIC_TIMEOUT).until(
                EC.presence_of_element_located(locator))
            AC(self.driver).move_to_element(elem).click(elem).perform()

        self.monetization_page.wait().until(EC.url_to_be(url))

    @pytest.mark.parametrize(
        'locator,text_value',
        [
            pytest.param(
                MonetizationPageLocators.MONETIZATION_FOOTER_LANGUAGE_BUTTON_RUSSIAN, 'RU'
            ),
            pytest.param(
                MonetizationPageLocators.MONETIZATION_FOOTER_LANGUAGE_BUTTON_ENGLISH, 'EN'
            ),
        ],
    )
    def test_language_wrapped_buttons(self, locator, text_value):
        elem = self.monetization_page.wait(BASIC_TIMEOUT).until(
            EC.presence_of_element_located(self.monetization_page.locators.MONETIZATION_FOOTER_LANGUAGE_WRAPPER))
        AC(self.driver).move_to_element(elem).click(elem).perform()

        self.monetization_page.click(locator)
        assert self.monetization_page.find(
            self.monetization_page.locators.MONETIZATION_FOOTER_LANGUAGE_WRAPPER).text == text_value
