import pytest
from cases import BaseCase
from ui.locators.basic_locators import BasePageLocators
from ui.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from utils.redirect_window import redirect_window_with_scroll
from utils.timeout import BASIC_TIMEOUT
from selenium.webdriver.common.action_chains import ActionChains as AC
import time


class TestFooter(BaseCase):
    def test_display(self):
        elem = self.base_page.wait(BASIC_TIMEOUT).until(EC.presence_of_element_located(self.base_page.locators.FOOTER_LOCATOR))
        AC(self.driver).move_to_element(elem).perform()

        assert self.base_page.find(self.base_page.locators.FOOTER_WRAPPER_LANGUAGE)
        assert self.base_page.find(self.base_page.locators.FOOTER_LOGO_OK).is_displayed()
        assert self.base_page.find(self.base_page.locators.FOOTER_LOGO_TG).is_displayed()
        assert self.base_page.find(self.base_page.locators.FOOTER_LOGO_VK).is_displayed()
        assert self.base_page.find(self.base_page.locators.FOOTER_BUTTON_CASES).is_displayed()
        assert self.base_page.find(self.base_page.locators.FOOTER_ABOUT_COMPANY).is_displayed()
        assert self.base_page.find(self.base_page.locators.FOOTER_BUTTON_CABINET).is_displayed()
        assert self.base_page.find(self.base_page.locators.FOOTER_BUTTON_DOCUMENTS).is_displayed()
        assert self.base_page.find(self.base_page.locators.FOOTER_BUTTON_EVENTS).is_displayed()
        assert self.base_page.find(self.base_page.locators.FOOTER_BUTTON_EXPERTS).is_displayed()
        assert self.base_page.find(self.base_page.locators.FOOTER_BUTTON_HELP).is_displayed()
        assert self.base_page.find(self.base_page.locators.FOOTER_BUTTON_INSIGHTS).is_displayed()
        assert self.base_page.find(self.base_page.locators.FOOTER_BUTTON_MONETIZATION).is_displayed()
        assert self.base_page.find(self.base_page.locators.FOOTER_BUTTON_NEWS).is_displayed()
        assert self.base_page.find(self.base_page.locators.FOOTER_LOGO_VK_BUSINESS).is_displayed()

    @pytest.mark.parametrize(
        'locator,url,redirect',
        [
            pytest.param(
                BasePageLocators.FOOTER_BUTTON_NEWS, 'https://ads.vk.com/news', False
            ),
            pytest.param(
                BasePageLocators.FOOTER_BUTTON_INSIGHTS, 'https://ads.vk.com/insights', False
            ),
            pytest.param(
                BasePageLocators.FOOTER_BUTTON_EVENTS, 'https://ads.vk.com/events', False
            ),
            pytest.param(
                BasePageLocators.FOOTER_BUTTON_DOCUMENTS, 'https://ads.vk.com/documents', False
            ),
            pytest.param(
                BasePageLocators.FOOTER_BUTTON_EXPERTS, 'https://expert.vk.com/', True
            ),
            pytest.param(
                BasePageLocators.FOOTER_BUTTON_CASES, 'https://ads.vk.com/cases', False
            ),
            pytest.param(
                BasePageLocators.FOOTER_BUTTON_HELP, 'https://ads.vk.com/help', False
            ),
            pytest.param(
                BasePageLocators.FOOTER_BUTTON_MONETIZATION, 'https://ads.vk.com/partner', True
            ),
            pytest.param(
                BasePageLocators.FOOTER_LOGO_VK_BUSINESS, 'https://vk.company/ru/company/business/', True
            ),
            pytest.param(
                BasePageLocators.FOOTER_LOGO_VK, 'https://vk.com/vk_ads', True
            ),
            pytest.param(
                BasePageLocators.FOOTER_LOGO_OK, 'https://ok.ru/group/64279825940712', True
            ),
            pytest.param(
                BasePageLocators.FOOTER_LOGO_TG, 'https://t.me/vk_ads', True
            ),
            pytest.param(
                BasePageLocators.FOOTER_ABOUT_COMPANY, 'https://vk.company/ru/', True
            ),
        ],
    )
    def test_open_pages(self, locator, url, redirect):
        if redirect:
            redirect_window_with_scroll(self.base_page, locator)
        else:
            elem = self.base_page.wait(BASIC_TIMEOUT).until(
                EC.presence_of_element_located(locator))
            AC(self.driver).move_to_element(elem).click(elem).perform()

        self.base_page.wait().until(EC.url_to_be(url))

    def test_open_login_page(self):
        elem = self.base_page.wait(BASIC_TIMEOUT).until(
            EC.presence_of_element_located(self.base_page.locators.FOOTER_BUTTON_CABINET))
        AC(self.driver).move_to_element(elem).click(elem).perform()

        self.base_page.wait().until(EC.url_matches("https://id.vk.com/auth"))

    @pytest.mark.parametrize(
        'locator,text_value',
        [
            pytest.param(
                BasePageLocators.FOOTER_LANGUAGE_BUTTON_RUSSIAN, 'RU'
            ),
            pytest.param(
                BasePageLocators.FOOTER_LANGUAGE_BUTTON_ENGLISH, 'EN'
            ),
        ],
    )
    def test_language_wrapped_buttons(self, locator, text_value):
        elem = self.base_page.wait(BASIC_TIMEOUT).until(
            EC.presence_of_element_located(self.base_page.locators.FOOTER_WRAPPER_LANGUAGE))
        AC(self.driver).move_to_element(elem).click(elem).perform()

        self.base_page.click(locator)
        assert self.base_page.find(self.base_page.locators.FOOTER_WRAPPER_LANGUAGE).text == text_value
