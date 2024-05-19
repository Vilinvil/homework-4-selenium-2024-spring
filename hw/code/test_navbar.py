import pytest
from cases import BaseCase
from ui.locators.basic_locators import BasePageLocators
from ui.pages.base_page import PageWithRedirectWindow
from selenium.webdriver.support import expected_conditions as EC


class TestNavbar(BaseCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_monetization(self, driver, config):
        self.redirect_page = PageWithRedirectWindow(self.driver)

    def test_display(self):
        assert self.base_page.find(self.base_page.locators.NAV_BUTTON_HELP,
                                   until_EC=EC.visibility_of_element_located)
        assert self.base_page.find(self.base_page.locators.NAV_BUTTON_MONETIZATION,
                                   until_EC=EC.visibility_of_element_located)
        assert self.base_page.find(self.base_page.locators.NAV_BUTTON_IDEAS,
                                   until_EC=EC.visibility_of_element_located)
        assert self.base_page.find(self.base_page.locators.NAV_BUTTON_CASES,
                                   until_EC=EC.visibility_of_element_located)
        assert self.base_page.find(self.base_page.locators.NAV_BUTTON_NEWS,
                                   until_EC=EC.visibility_of_element_located)
        assert self.base_page.find(self.base_page.locators.NAV_BUTTON_CABINET_LOCATOR,
                                   until_EC=EC.visibility_of_element_located)
        assert self.base_page.find(self.base_page.locators.NAV_WRAPPER_EDUCATION,
                                   until_EC=EC.visibility_of_element_located)

    @pytest.mark.parametrize(
        'locator,url,redirect',
        [
            pytest.param(
                BasePageLocators.NAV_BUTTON_HELP, 'https://ads.vk.com/help', False
            ),
            pytest.param(
                BasePageLocators.NAV_BUTTON_MONETIZATION, 'https://ads.vk.com/partner', True
            ),
            pytest.param(
                BasePageLocators.NAV_BUTTON_IDEAS, 'https://ads.vk.com/upvote', False
            ),
            pytest.param(
                BasePageLocators.NAV_BUTTON_CASES, 'https://ads.vk.com/cases', False
            ),
            pytest.param(
                BasePageLocators.NAV_BUTTON_NEWS, 'https://ads.vk.com/news', False
            ),
        ],
    )
    def test_open_pages(self, locator, url, redirect):
        if redirect:
            self.redirect_page.redirect_window(locator)
        else:
            self.base_page.click(locator)

        self.base_page.wait().until(EC.url_to_be(url))

    def test_education_dropdown_display(self):
        self.base_page.hover_wrapper(self.base_page.locators.NAV_WRAPPER_EDUCATION)

        assert self.base_page.find(self.base_page.locators.BUTTON_INSIGHTS, until_EC=EC.visibility_of_element_located)
        assert self.base_page.find(self.base_page.locators.BUTTON_EVENTS, until_EC=EC.visibility_of_element_located)
        assert self.base_page.find(self.base_page.locators.BUTTON_VIDEO_COURSES,
                                   until_EC=EC.visibility_of_element_located)
        assert self.base_page.find(self.base_page.locators.BUTTON_CERTIFICATION,
                                   until_EC=EC.visibility_of_element_located)

    @pytest.mark.parametrize(
        'locator,url,redirect',
        [
            pytest.param(
                BasePageLocators.BUTTON_INSIGHTS, 'https://ads.vk.com/insights', False
            ),
            pytest.param(
                BasePageLocators.BUTTON_EVENTS, 'https://ads.vk.com/events', False
            ),
            pytest.param(
                BasePageLocators.BUTTON_VIDEO_COURSES, 'https://expert.vk.com/catalog/courses/', True
            ),
            pytest.param(
                BasePageLocators.BUTTON_CERTIFICATION, 'https://expert.vk.com/certification/', True
            ),
        ],
    )
    def test_education_dropdown_buttons_open_pages(self, locator, url, redirect):
        self.base_page.hover_wrapper(self.base_page.locators.NAV_WRAPPER_EDUCATION)

        if redirect:
            self.redirect_page.redirect_window(locator)
        else:
            self.base_page.click(locator)

        self.base_page.wait().until(EC.url_to_be(url))

    def test_sequential_transition(self):
        self.base_page.click(self.base_page.locators.NAV_BUTTON_CASES)
        self.base_page.wait().until(EC.url_matches("https://ads.vk.com/cases"))

        self.base_page.click(self.base_page.locators.NAV_BUTTON_IDEAS)
        self.base_page.wait().until(EC.url_matches("https://ads.vk.com/upvote"))

        self.base_page.click(self.base_page.locators.NAV_BUTTON_NEWS)
        self.base_page.wait().until(EC.url_matches("https://ads.vk.com/news"))

        self.base_page.click(self.base_page.locators.NAV_BUTTON_CASES)
        self.base_page.wait().until(EC.url_matches("https://ads.vk.com/cases"))

    def test_open_login_page(self):
        self.base_page.click(self.base_page.locators.NAV_BUTTON_CABINET_LOCATOR)
        self.base_page.wait().until(EC.url_matches("https://id.vk.com/auth"))
