import pytest

from cases import LoggedCase
from ui.locators.main_locators import MainPageLocators
from ui.pages.base_page import PageWithRedirectWindow

from selenium.webdriver.support import expected_conditions as EC


class TestSidebarLogged(LoggedCase):
    def test_display(self):
        assert self.main_page.find(self.main_page.locators.sidebar_locators.BUTTON_OVERVIEW,
                                   until_EC=EC.visibility_of_element_located)
        assert self.main_page.find(self.main_page.locators.sidebar_locators.BUTTON_CAMPAIGN,
                                   until_EC=EC.visibility_of_element_located)
        assert self.main_page.find(self.main_page.locators.sidebar_locators.BUTTON_AUDIENCE,
                                   until_EC=EC.visibility_of_element_located)
        assert self.main_page.find(self.main_page.locators.sidebar_locators.BUTTON_BUDGET,
                                   until_EC=EC.visibility_of_element_located)
        assert self.main_page.find(self.main_page.locators.sidebar_locators.BUTTON_TRAINING,
                                   until_EC=EC.visibility_of_element_located)
        assert self.main_page.find(self.main_page.locators.sidebar_locators.BUTTON_CATALOGS,
                                   until_EC=EC.visibility_of_element_located)
        assert self.main_page.find(self.main_page.locators.sidebar_locators.BUTTON_SITES,
                                   until_EC=EC.visibility_of_element_located)
        assert self.main_page.find(self.main_page.locators.sidebar_locators.BUTTON_MOBILE_APPS,
                                   until_EC=EC.visibility_of_element_located)
        assert self.main_page.find(self.main_page.locators.sidebar_locators.BUTTON_LEADS,
                                   until_EC=EC.visibility_of_element_located)
        assert self.main_page.find(self.main_page.locators.sidebar_locators.BUTTON_SETTINGS,
                                   until_EC=EC.visibility_of_element_located)
        assert self.main_page.find(self.main_page.locators.sidebar_locators.BUTTON_HELP,
                                   until_EC=EC.visibility_of_element_located)
        assert self.main_page.find(self.main_page.locators.sidebar_locators.BUTTON_TOGGLE,
                                   until_EC=EC.visibility_of_element_located)

    @pytest.mark.parametrize(
        'button_locator, sign_opening, expected_url',
        [
            pytest.param(MainPageLocators.sidebar_locators.BUTTON_OVERVIEW,
                         MainPageLocators.sidebar_locators.SIGN_OPENING_OVERVIEW,
                         'https://ads.vk.com/hq/overview'),
            pytest.param(MainPageLocators.sidebar_locators.BUTTON_CAMPAIGN,
                         MainPageLocators.sidebar_locators.SIGN_OPENING_CAMPAIGN,
                         'https://ads.vk.com/hq/dashboard/ad_plans'),
            pytest.param(MainPageLocators.sidebar_locators.BUTTON_AUDIENCE,
                         MainPageLocators.sidebar_locators.SIGN_OPENING_AUDIENCE,
                         'https://ads.vk.com/hq/audience'),
            pytest.param(MainPageLocators.sidebar_locators.BUTTON_BUDGET,
                         MainPageLocators.sidebar_locators.SIGN_OPENING_BUDGET,
                         'https://ads.vk.com/hq/budget/transactions'),
            pytest.param(MainPageLocators.sidebar_locators.BUTTON_CATALOGS,
                         MainPageLocators.sidebar_locators.SIGN_OPENING_CATALOGS,
                         'https://ads.vk.com/hq/ecomm/catalogs'),
            pytest.param(MainPageLocators.sidebar_locators.BUTTON_SITES,
                         MainPageLocators.sidebar_locators.SIGN_OPENING_SITES,
                         'https://ads.vk.com/hq/pixels'),
            pytest.param(MainPageLocators.sidebar_locators.BUTTON_MOBILE_APPS,
                         MainPageLocators.sidebar_locators.SIGN_OPENING_MOBILE_APPS,
                         'https://ads.vk.com/hq/apps'),
            pytest.param(MainPageLocators.sidebar_locators.BUTTON_LEADS,
                         MainPageLocators.sidebar_locators.SIGN_OPENING_LEADS,
                         'https://ads.vk.com/hq/leadads/leadforms'),
            pytest.param(MainPageLocators.sidebar_locators.BUTTON_SETTINGS,
                         MainPageLocators.sidebar_locators.SIGN_OPENING_SETTINGS,
                         'https://ads.vk.com/hq/settings'),
        ],
    )
    def test_opening(self, button_locator, sign_opening, expected_url):
        self.main_page.click(button_locator)
        assert self.main_page.find(sign_opening, until_EC=EC.visibility_of_element_located)
        assert self.main_page.wait(5).until(EC.url_matches(expected_url))

    def test_toggle(self):
        self.main_page.click(self.main_page.locators.sidebar_locators.BUTTON_TOGGLE)
        assert self.main_page.find(self.main_page.locators.sidebar_locators.SIGN_TOGGLE,
                                   until_EC=EC.visibility_of_element_located)

        self.main_page.click(self.main_page.locators.sidebar_locators.BUTTON_TOGGLE)
        assert self.main_page.find(self.main_page.locators.sidebar_locators.SIGN_TOGGLE,
                                   until_EC=EC.invisibility_of_element_located)

    @pytest.fixture(scope='function')
    def setup_help_section(self):
        self.main_page.click(self.main_page.locators.sidebar_locators.BUTTON_HELP)

    def test_help_section_display(self, setup_help_section):
        assert self.main_page.find(self.main_page.locators.sidebar_locators.BUTTON_HELP_CASES,
                                   until_EC=EC.visibility_of_element_located)
        assert self.main_page.find(self.main_page.locators.sidebar_locators.BUTTON_HELP_HELP,
                                   until_EC=EC.visibility_of_element_located)
        assert self.main_page.find(self.main_page.locators.sidebar_locators.BUTTON_HELP_IDEAS,
                                   until_EC=EC.visibility_of_element_located)
        assert self.main_page.find(self.main_page.locators.sidebar_locators.BUTTON_HELP_QUESTION,
                                   until_EC=EC.visibility_of_element_located)

    def test_help_section_question(self, setup_help_section):
        self.main_page.click(self.main_page.locators.sidebar_locators.BUTTON_HELP_QUESTION)
        assert self.main_page.find(self.main_page.locators.sidebar_locators.SIGN_OPENING_HELP_QUESTION,
                                   until_EC=EC.visibility_of_element_located)

    @pytest.mark.parametrize('button_locator, expected_url',
                             [
                                 pytest.param(MainPageLocators.sidebar_locators.BUTTON_HELP_CASES,
                                              'https://ads.vk.com/cases'),
                                 pytest.param(MainPageLocators.sidebar_locators.BUTTON_HELP_HELP,
                                              'https://ads.vk.com/help'),
                                 pytest.param(MainPageLocators.sidebar_locators.BUTTON_HELP_IDEAS,
                                              'https://ads.vk.com/upvote'),

                             ])
    def test_help_section_redirect(self, button_locator, expected_url, setup_help_section):
        page_with_redirect = PageWithRedirectWindow(self.driver)
        page_with_redirect.redirect_window(button_locator, expected_number_of_windows_to_be=2)
        assert self.main_page.wait(5).until(EC.url_matches(expected_url))

    def test_sequential_transition(self):
        self.main_page.click(self.main_page.locators.sidebar_locators.BUTTON_OVERVIEW)
        assert self.main_page.find(self.main_page.locators.sidebar_locators.SIGN_OPENING_OVERVIEW,
                                   until_EC=EC.visibility_of_element_located)

        self.main_page.click(self.main_page.locators.sidebar_locators.BUTTON_CAMPAIGN)
        assert self.main_page.find(self.main_page.locators.sidebar_locators.SIGN_OPENING_CAMPAIGN,
                                   until_EC=EC.visibility_of_element_located)

        self.main_page.click(self.main_page.locators.sidebar_locators.BUTTON_AUDIENCE)
        assert self.main_page.find(self.main_page.locators.sidebar_locators.SIGN_OPENING_AUDIENCE,
                                   until_EC=EC.visibility_of_element_located)

        self.main_page.click(self.main_page.locators.sidebar_locators.BUTTON_OVERVIEW)
        assert self.main_page.find(self.main_page.locators.sidebar_locators.SIGN_OPENING_OVERVIEW,
                                   until_EC=EC.visibility_of_element_located)


class TestNavBarLogged(LoggedCase):
    def test_display(self):
        assert self.main_page.find(self.main_page.locators.navbar_locators.ADS_LOGO,
                                   until_EC=EC.visibility_of_element_located)
        assert self.main_page.find(self.main_page.locators.navbar_locators.BUTTON_ACCOUNT_SWITCH,
                                   until_EC=EC.visibility_of_element_located)
        assert self.main_page.find(self.main_page.locators.navbar_locators.BUTTON_BALANCE,
                                   until_EC=EC.visibility_of_element_located)
        assert self.main_page.find(self.main_page.locators.navbar_locators.BUTTON_NOTIFICATIONS,
                                   until_EC=EC.visibility_of_element_located)
        assert self.main_page.find(self.main_page.locators.navbar_locators.BUTTON_USER_MENU,
                                   until_EC=EC.visibility_of_element_located)

    def test_click_logo(self):
        self.main_page.click(self.main_page.locators.navbar_locators.ADS_LOGO)
        assert self.main_page.wait(5).until(EC.url_matches('https://ads.vk.com/hq/overview'))

    @pytest.mark.parametrize('button_locator, sign_opening',
                             [
                                 pytest.param(MainPageLocators.navbar_locators.BUTTON_ACCOUNT_SWITCH,
                                              MainPageLocators.navbar_locators.SIGN_OPENING_ACCOUNT_SWITCH),
                                 pytest.param(MainPageLocators.navbar_locators.BUTTON_BALANCE,
                                              MainPageLocators.navbar_locators.SIGN_OPENING_BALANCE),
                                 pytest.param(MainPageLocators.navbar_locators.BUTTON_NOTIFICATIONS,
                                              MainPageLocators.navbar_locators.SIGN_OPENING_NOTIFICATIONS),
                                 pytest.param(MainPageLocators.navbar_locators.BUTTON_USER_MENU,
                                              MainPageLocators.navbar_locators.SIGN_OPENING_USER_MENU),

                             ], )
    def test_navigation_buttons(self, button_locator, sign_opening):
        self.main_page.click(button_locator)
        assert self.main_page.find(sign_opening, until_EC=EC.visibility_of_element_located)

    @pytest.fixture(scope="function")
    def setup_user_menu(self):
        self.main_page.click(self.main_page.locators.navbar_locators.BUTTON_USER_MENU)

    def test_user_menu_redirect_account(self, setup_user_menu):
        page_with_redirect = PageWithRedirectWindow(self.driver)
        page_with_redirect.redirect_window(self.main_page.locators.navbar_locators.BUTTON_USER_MENU_ACCOUNT,
                                           expected_number_of_windows_to_be=2)
        assert self.main_page.wait(5).until(EC.url_matches('https://id.vk.com/about/id'))

    def test_user_menu_logout(self, setup_user_menu):
        self.main_page.click(self.main_page.locators.navbar_locators.BUTTON_USER_MENU_LOGOUT)
        assert self.main_page.wait(5).until(EC.url_matches('https://ads.vk.com/'))
