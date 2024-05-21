import pytest

from cases import LoggedCase
from ui.pages.base_page import PageWithRedirectWindow
from ui.pages.main_page import MainPage


class TestSidebarLogged(LoggedCase):
    def test_display(self):
        assert self.main_page.find_button_overview()
        assert self.main_page.find_button_campaigns()
        assert self.main_page.find_button_audience()
        assert self.main_page.find_button_budget()
        assert self.main_page.find_button_training()
        assert self.main_page.find_button_catalogs()
        assert self.main_page.find_button_sites()
        assert self.main_page.find_button_mobile_app()
        assert self.main_page.find_button_leads()
        assert self.main_page.find_button_settings()
        assert self.main_page.find_button_help()
        assert self.main_page.find_button_toggle()

    @pytest.mark.parametrize(
        'open_view, expected_url',
        [
            pytest.param(MainPage.open_overview,
                         'https://ads.vk.com/hq/overview'),
            pytest.param(MainPage.open_campaigns,
                         'https://ads.vk.com/hq/dashboard/ad_plans'),
            pytest.param(MainPage.open_audience,
                         'https://ads.vk.com/hq/audience'),
            pytest.param(MainPage.open_budget,
                         'https://ads.vk.com/hq/budget/transactions'),
            pytest.param(MainPage.open_catalogs,
                         'https://ads.vk.com/hq/ecomm/catalogs'),
            pytest.param(MainPage.open_sites,
                         'https://ads.vk.com/hq/pixels'),
            pytest.param(MainPage.open_mobile_app,
                         'https://ads.vk.com/hq/apps'),
            pytest.param(MainPage.open_leads,
                         'https://ads.vk.com/hq/leadads/leadforms'),
            pytest.param(MainPage.open_settings,
                         'https://ads.vk.com/hq/settings'),
        ],
    )
    def test_opening(self, open_view, expected_url):
        open_view(self.main_page)
        assert self.base_page.check_url(expected_url)

    def test_toggle(self):
        assert self.main_page.collapse_sidebar()

        assert self.main_page.open_sidebar()

    @pytest.fixture(scope='function')
    def setup_help_section(self):
        self.main_page.open_help()

    def test_help_section_display(self, setup_help_section):
        assert self.main_page.find_button_help_cases()
        assert self.main_page.find_button_help_help()
        assert self.main_page.find_button_help_ideas()
        assert self.main_page.find_button_help_question()

    def test_help_section_question(self, setup_help_section):
        assert self.main_page.open_help_question()

    @pytest.mark.parametrize('redirect_by_button, expected_url',
                             [
                                 pytest.param(MainPage.redirect_help_cases,
                                              'https://ads.vk.com/cases'),
                                 pytest.param(MainPage.redirect_help_help,
                                              'https://ads.vk.com/help'),
                                 pytest.param(MainPage.redirect_help_ideas,
                                              'https://ads.vk.com/upvote'),

                             ])
    def test_help_section_redirect(self, redirect_by_button, expected_url, setup_help_section):
        page_with_redirect = PageWithRedirectWindow(self.driver)
        redirect_by_button(self.main_page, page_with_redirect)

        assert self.main_page.check_url(expected_url)

    def test_sequential_transition(self):
        self.main_page.open_overview()
        assert self.base_page.check_url('https://ads.vk.com/hq/overview')

        self.main_page.open_campaigns()
        assert self.base_page.check_url('https://ads.vk.com/hq/dashboard/ad_plans')

        self.main_page.open_audience()
        assert self.base_page.check_url('https://ads.vk.com/hq/audience')

        self.main_page.open_overview()
        assert self.base_page.check_url('https://ads.vk.com/hq/overview')


class TestNavBarLogged(LoggedCase):
    def test_display(self):
        assert self.main_page.find_ads_logo()
        assert self.main_page.find_account_switch()
        assert self.main_page.find_balance()
        assert self.main_page.find_notifications()
        assert self.main_page.find_user_menu()

    def test_click_logo(self):
        self.main_page.click_ads_logo()
        assert self.main_page.check_url('https://ads.vk.com/hq/overview')

    @pytest.mark.parametrize('open_view',
                             [
                                 pytest.param(MainPage.open_account_switch),
                                 pytest.param(MainPage.open_balance),
                                 pytest.param(MainPage.open_notifications),
                                 pytest.param(MainPage.open_user_menu),

                             ], )
    def test_navigation_buttons(self, open_view):
        open_view(self.main_page)

    @pytest.fixture(scope="function")
    def setup_user_menu(self):
        self.main_page.open_user_menu()

    def test_user_menu_redirect_account(self, setup_user_menu):
        page_with_redirect = PageWithRedirectWindow(self.driver)
        self.main_page.redirect_user_menu_account(page_with_redirect)
        assert self.main_page.check_url('https://id.vk.com/about/id')

    def test_user_menu_logout(self, setup_user_menu):
        self.main_page.click_user_menu_logout()
        assert self.main_page.check_url('https://ads.vk.com/')
