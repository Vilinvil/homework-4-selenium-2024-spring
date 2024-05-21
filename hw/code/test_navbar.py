import pytest

from cases import BaseCase
from ui.pages.base_page import BasePage, PageWithRedirectWindow


class TestNavbar(BaseCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_monetization(self, driver):
        self.redirect_page = PageWithRedirectWindow(self.driver)

    def test_display(self):
        assert self.base_page.find_nav_button_help()
        assert self.base_page.find_nav_button_monetization()
        assert self.base_page.find_nav_button_ideas()
        assert self.base_page.find_nav_button_cases()
        assert self.base_page.find_nav_button_news()
        assert self.base_page.find_nav_button_cabinet()
        assert self.base_page.find_nav_wrapper_education()

    @pytest.mark.parametrize(
        'click_to_nav_button,url',
        [
            pytest.param(
                BasePage.click_nav_button_help, 'https://ads.vk.com/help'
            ),
            pytest.param(
                BasePage.click_nav_button_ideas, 'https://ads.vk.com/upvote'
            ),
            pytest.param(
                BasePage.click_nav_button_cases, 'https://ads.vk.com/cases'
            ),
            pytest.param(
                BasePage.click_nav_button_news, 'https://ads.vk.com/news'
            ),
        ],
    )
    def test_open_pages(self, click_to_nav_button, url):
        click_to_nav_button(self.base_page)

        assert self.base_page.check_url(url)

    @pytest.mark.parametrize(
        'redirect_to_page,url',
        [
            pytest.param(
                BasePage.redirect_nav_monetization, 'https://ads.vk.com/partner'
            ),
        ],
    )
    def test_open_pages_with_redirect(self, redirect_to_page, url):
        redirect_to_page(self.base_page, self.redirect_page)

        assert self.base_page.check_url(url)

    def test_education_dropdown_display(self):
        self.base_page.hover_nav_wrapper_education()

        assert self.base_page.find_nav_wrapped_button_insights()
        assert self.base_page.find_nav_wrapped_button_events()
        assert self.base_page.find_nav_wrapped_button_video_courses()
        assert self.base_page.find_nav_wrapped_button_certification()

    @pytest.mark.parametrize(
        'click_to,url',
        [
            pytest.param(
                BasePage.click_nav_wrapped_button_insights, 'https://ads.vk.com/insights'
            ),
            pytest.param(
                BasePage.click_nav_wrapped_button_events, 'https://ads.vk.com/events'
            ),
        ],
    )
    def test_education_dropdown_buttons_open_pages(self, click_to, url):
        self.base_page.hover_nav_wrapper_education()

        click_to(self.base_page)

        self.base_page.check_url(url)

    @pytest.mark.parametrize(
        'redirect_to,url',
        [
            pytest.param(
                BasePage.redirect_nav_wrapped_button_video_courses, 'https://expert.vk.com/catalog/courses/'
            ),
            pytest.param(
                BasePage.redirect_nav_wrapped_button_certification, 'https://expert.vk.com/certification/'
            ),
        ],
    )
    def test_education_dropdown_buttons_open_pages_with_redirect(self, redirect_to, url):
        self.base_page.hover_wrapper(self.base_page.locators.NAV_WRAPPER_EDUCATION)

        redirect_to(self.base_page, self.redirect_page)

        self.base_page.check_url(url)

    def test_sequential_transition(self):
        self.base_page.click_nav_button_cases()
        self.base_page.check_url("https://ads.vk.com/cases")

        self.base_page.click_nav_button_ideas()
        self.base_page.check_url("https://ads.vk.com/upvote")

        self.base_page.click_nav_button_news()
        self.base_page.check_url("https://ads.vk.com/news")

        self.base_page.click_nav_button_cases()
        self.base_page.check_url("https://ads.vk.com/cases")

    def test_open_login_page(self):
        self.base_page.click_nav_button_cabinet()
        self.base_page.check_url("https://id.vk.com/auth")
