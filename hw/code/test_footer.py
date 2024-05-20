import pytest

from cases import BaseCase
from ui.pages.base_page import PageWithRedirectWindow
from ui.locators.basic_locators import BasePageLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC


class TestFooter(BaseCase):
    def test_display(self):
        self.base_page.hover_wrapper((self.base_page.locators.FOOTER_LOCATOR))

        assert self.base_page.find(self.base_page.locators.FOOTER_WRAPPER_LANGUAGE, until_EC=EC.visibility_of_element_located)
        assert self.base_page.find(self.base_page.locators.FOOTER_LOGO_OK, until_EC=EC.visibility_of_element_located)
        assert self.base_page.find(self.base_page.locators.FOOTER_LOGO_TG, until_EC=EC.visibility_of_element_located)
        assert self.base_page.find(self.base_page.locators.FOOTER_LOGO_VK, until_EC=EC.visibility_of_element_located)
        assert self.base_page.find(self.base_page.locators.FOOTER_BUTTON_CASES,
                                   until_EC=EC.visibility_of_element_located)
        assert self.base_page.find(self.base_page.locators.FOOTER_ABOUT_COMPANY,
                                   until_EC=EC.visibility_of_element_located)
        assert self.base_page.find(self.base_page.locators.FOOTER_BUTTON_CABINET,
                                   until_EC=EC.visibility_of_element_located)
        assert self.base_page.find(self.base_page.locators.FOOTER_BUTTON_DOCUMENTS,
                                   until_EC=EC.visibility_of_element_located)
        assert self.base_page.find(self.base_page.locators.FOOTER_BUTTON_EVENTS,
                                   until_EC=EC.visibility_of_element_located)
        assert self.base_page.find(self.base_page.locators.FOOTER_BUTTON_EXPERTS,
                                   until_EC=EC.visibility_of_element_located)
        assert self.base_page.find(self.base_page.locators.FOOTER_BUTTON_HELP,
                                   until_EC=EC.visibility_of_element_located)
        assert self.base_page.find(self.base_page.locators.FOOTER_BUTTON_INSIGHTS,
                                   until_EC=EC.visibility_of_element_located)
        assert self.base_page.find(self.base_page.locators.FOOTER_BUTTON_MONETIZATION,
                                   until_EC=EC.visibility_of_element_located)
        assert self.base_page.find(self.base_page.locators.FOOTER_BUTTON_NEWS,
                                   until_EC=EC.visibility_of_element_located)
        assert self.base_page.find(self.base_page.locators.FOOTER_LOGO_VK_BUSINESS,
                                   until_EC=EC.visibility_of_element_located)

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
            page_with_redirect = PageWithRedirectWindow(self.driver)
            page_with_redirect.redirect_window_with_scroll(locator)
        else:
            elem = self.base_page.find(locator)
            AC(self.driver).move_to_element(elem).click(elem).perform()

        self.base_page.wait().until(EC.url_matches(url))

    def test_open_login_page(self):
        elem = self.base_page.find(self.base_page.locators.FOOTER_BUTTON_CABINET)
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
        elem = self.base_page.find(self.base_page.locators.FOOTER_WRAPPER_LANGUAGE)
        AC(self.driver).move_to_element(elem).click(elem).perform()

        self.base_page.click(locator)
        assert self.base_page.find(self.base_page.locators.FOOTER_WRAPPER_LANGUAGE).text == text_value
