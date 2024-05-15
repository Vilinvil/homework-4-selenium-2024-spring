import time

import pytest

from cases import BaseCase
from ui.locators.basic_locators import BasePageLocators
from ui.pages.base_page import BasePage



class TestNavbar(BaseCase):
    def test_display(self):
        assert self.base_page.find(self.base_page.locators.NAV_BUTTON_HELP).is_displayed()
        assert self.base_page.find(self.base_page.locators.NAV_BUTTON_MONETIZATION).is_displayed()
        assert self.base_page.find(self.base_page.locators.NAV_BUTTON_IDEAS).is_displayed()
        assert self.base_page.find(self.base_page.locators.NAV_BUTTON_CASES).is_displayed()
        assert self.base_page.find(self.base_page.locators.NAV_BUTTON_NEWS).is_displayed()
        assert self.base_page.find(self.base_page.locators.BUTTON_CABINET_LOCATOR).is_displayed()
        assert self.base_page.find(self.base_page.locators.NAV_WRAPPER_EDUCATION).is_displayed()

    @pytest.mark.parametrize(
        'locator,url',
        [
            pytest.param(
                BasePageLocators.NAV_BUTTON_HELP, 'https://ads.vk.com/help'
            ),
            pytest.param(
                BasePageLocators.NAV_BUTTON_MONETIZATION, 'https://ads.vk.com/partner'
            ),
            pytest.param(
                BasePageLocators.NAV_BUTTON_IDEAS, 'https://ads.vk.com/upvote'
            ),
            pytest.param(
                BasePageLocators.NAV_BUTTON_CASES, 'https://ads.vk.com/cases'
            ),
            pytest.param(
                BasePageLocators.NAV_BUTTON_NEWS, 'https://ads.vk.com/news'
            ),
        ],
    )
    def test_open_pages(self, locator, url):
        self.base_page.click(locator)
        assert self.base_page.is_opened(url, 60)


    def test_education_dropdown_display(self):
        self.base_page.hover_wrapper(self.base_page.locators.NAV_WRAPPER_EDUCATION)

        assert self.base_page.find(self.base_page.locators.BUTTON_INSIGHTS).is_displayed()
        assert self.base_page.find(self.base_page.locators.BUTTON_EVENTS).is_displayed()
        assert self.base_page.find(self.base_page.locators.BUTTON_VIDEO_COURSES).is_displayed()
        assert self.base_page.find(self.base_page.locators.BUTTON_CERTIFICATION).is_displayed()

    @pytest.mark.parametrize(
        'locator,url',
        [
            pytest.param(
                BasePageLocators.BUTTON_INSIGHTS, 'https://ads.vk.com/insights'
            ),
            pytest.param(
                BasePageLocators.BUTTON_EVENTS, 'https://ads.vk.com/events'
            ),
            pytest.param(
                BasePageLocators.BUTTON_VIDEO_COURSES, 'https://expert.vk.com/catalog/courses/'
            ),
            pytest.param(
                BasePageLocators.BUTTON_CERTIFICATION, 'https://expert.vk.com/certification/'
            ),
        ],
    )
    def test_education_dropdown_buttons_open_pages(self, locator, url):
        self.base_page.hover_wrapper(self.base_page.locators.NAV_WRAPPER_EDUCATION)

        self.base_page.click(locator)
        assert self.base_page.is_opened(url)

    def test_sequential_transition(self):
        self.base_page.click(self.base_page.locators.NAV_BUTTON_CASES)
        assert self.base_page.is_opened('https://ads.vk.com/cases')

        self.base_page.click(self.base_page.locators.NAV_BUTTON_IDEAS)
        assert self.base_page.is_opened('https://ads.vk.com/upvote')

        self.base_page.click(self.base_page.locators.NAV_BUTTON_NEWS)
        assert self.base_page.is_opened('https://ads.vk.com/news')

        self.base_page.click(self.base_page.locators.NAV_BUTTON_CASES)
        assert self.base_page.is_opened('https://ads.vk.com/cases')


