from ui.pages.base_page import PageWithView
from ui.locators.main_locators import MainPageLocators
from ui.locators.training_locators import TrainingPageSharedLocators

from selenium.webdriver.support import expected_conditions as EC

URL_MAIN_PAGE = 'https://ads.vk.com/hq/overview'


class MainPage(PageWithView):
    url = URL_MAIN_PAGE
    locators = MainPageLocators()
    training_locators = TrainingPageSharedLocators()

    def find_button_overview(self):
        return self.find_with_check_visibility(self.locators.sidebar_locators.BUTTON_OVERVIEW)

    def find_button_campaigns(self):
        return self.find_with_check_visibility(self.locators.sidebar_locators.BUTTON_CAMPAIGN)

    def find_button_audience(self):
        return self.find_with_check_visibility(self.locators.sidebar_locators.BUTTON_AUDIENCE)

    def find_button_budget(self):
        return self.find_with_check_visibility(self.locators.sidebar_locators.BUTTON_BUDGET)

    def find_button_training(self):
        return self.find_with_check_visibility(self.locators.sidebar_locators.BUTTON_TRAINING)

    def find_button_catalogs(self):
        return self.find_with_check_visibility(self.locators.sidebar_locators.BUTTON_CATALOGS)

    def find_button_sites(self):
        return self.find_with_check_visibility(self.locators.sidebar_locators.BUTTON_SITES)

    def find_button_mobile_app(self):
        return self.find_with_check_visibility(self.locators.sidebar_locators.BUTTON_MOBILE_APPS)

    def find_button_leads(self):
        return self.find_with_check_visibility(self.locators.sidebar_locators.BUTTON_LEADS)

    def find_button_settings(self):
        return self.find_with_check_visibility(self.locators.sidebar_locators.BUTTON_SETTINGS)

    def find_button_help(self):
        return self.find_with_check_visibility(self.locators.sidebar_locators.BUTTON_HELP)

    def find_button_toggle(self):
        return self.find_with_check_visibility(self.locators.sidebar_locators.BUTTON_TOGGLE)

    def find_button_help_cases(self):
        return self.find_with_check_visibility(self.locators.sidebar_locators.BUTTON_HELP_CASES)

    def find_button_help_help(self):
        return self.find_with_check_visibility(self.locators.sidebar_locators.BUTTON_HELP_HELP)

    def find_button_help_ideas(self):
        return self.find_with_check_visibility(self.locators.sidebar_locators.BUTTON_HELP_IDEAS)

    def find_button_help_question(self):
        return self.find_with_check_visibility(self.locators.sidebar_locators.BUTTON_HELP_QUESTION)

    def find_ads_logo(self):
        return self.find_with_check_visibility(self.locators.navbar_locators.ADS_LOGO)

    def find_button_account_switch(self):
        return self.find_with_check_visibility(self.locators.navbar_locators.BUTTON_ACCOUNT_SWITCH)

    def find_button_balance(self):
        return self.find_with_check_visibility(self.locators.navbar_locators.BUTTON_BALANCE)

    def find_button_notifications(self):
        return self.find_with_check_visibility(self.locators.navbar_locators.BUTTON_NOTIFICATIONS)

    def find_button_user_menu(self):
        return self.find_with_check_visibility(self.locators.navbar_locators.BUTTON_USER_MENU)

    def click_ads_logo(self):
        self.click(self.locators.navbar_locators.ADS_LOGO)

    def click_user_menu_logout(self):
        self.click(self.locators.navbar_locators.BUTTON_USER_MENU_LOGOUT)

    def open_overview(self):
        self.open_view(self.locators.sidebar_locators.BUTTON_OVERVIEW,
                       self.locators.sidebar_locators.SIGN_OPENING_OVERVIEW)

    def open_campaigns(self):
        self.open_view(self.locators.sidebar_locators.BUTTON_CAMPAIGN,
                       self.locators.sidebar_locators.SIGN_OPENING_CAMPAIGN)

    def open_audience(self):
        self.open_view(self.locators.sidebar_locators.BUTTON_AUDIENCE,
                       self.locators.sidebar_locators.SIGN_OPENING_AUDIENCE)

    def open_budget(self):
        self.open_view(self.locators.sidebar_locators.BUTTON_BUDGET,
                       self.locators.sidebar_locators.SIGN_OPENING_BUDGET)

    def open_catalogs(self):
        self.open_view(self.locators.sidebar_locators.BUTTON_CATALOGS,
                       self.locators.sidebar_locators.SIGN_OPENING_CATALOGS)

    def open_sites(self):
        self.open_view(self.locators.sidebar_locators.BUTTON_SITES,
                       self.locators.sidebar_locators.SIGN_OPENING_SITES)

    def open_mobile_app(self):
        self.open_view(self.locators.sidebar_locators.BUTTON_MOBILE_APPS,
                       self.locators.sidebar_locators.SIGN_OPENING_MOBILE_APPS)

    def open_leads(self):
        self.open_view(self.locators.sidebar_locators.BUTTON_LEADS,
                       self.locators.sidebar_locators.SIGN_OPENING_LEADS)

    def open_settings(self):
        self.open_view(self.locators.sidebar_locators.BUTTON_SETTINGS,
                       self.locators.sidebar_locators.SIGN_OPENING_SETTINGS)

    def open_help(self):
        self.open_view(self.locators.sidebar_locators.BUTTON_HELP, self.locators.sidebar_locators.SIGN_OPENING_HELP)

    def collapse_sidebar(self):
        self.click(self.locators.sidebar_locators.BUTTON_TOGGLE)
        return self.find_with_check_visibility(self.locators.sidebar_locators.SIGN_TOGGLE)

    def open_sidebar(self):
        self.click(self.locators.sidebar_locators.BUTTON_TOGGLE)
        return self.find(self.locators.sidebar_locators.SIGN_TOGGLE, until_EC=EC.invisibility_of_element_located)

    def open_help_question(self):
        self.click(self.locators.sidebar_locators.BUTTON_HELP_QUESTION)
        return self.find_with_check_visibility(self.locators.sidebar_locators.SIGN_OPENING_HELP_QUESTION)

    def open_account_switch(self):
        self.open_view(self.locators.navbar_locators.BUTTON_ACCOUNT_SWITCH,
                       self.locators.navbar_locators.SIGN_OPENING_ACCOUNT_SWITCH)

    def open_balance(self):
        self.open_view(self.locators.navbar_locators.BUTTON_BALANCE,
                       self.locators.navbar_locators.SIGN_OPENING_BALANCE)

    def open_notifications(self):
        self.open_view(self.locators.navbar_locators.BUTTON_NOTIFICATIONS,
                       self.locators.navbar_locators.SIGN_OPENING_NOTIFICATIONS)

    def open_user_menu(self):
        self.open_view(self.locators.navbar_locators.BUTTON_USER_MENU,
                       self.locators.navbar_locators.SIGN_OPENING_USER_MENU)

    def open_training(self):
        self.open_view(self.locators.sidebar_locators.BUTTON_TRAINING, self.training_locators.SIGN_OPENING_MODAL_VIEW)

    def redirect_help_cases(self, redirect_page):
        redirect_page.redirect_window(self.locators.sidebar_locators.BUTTON_HELP_CASES, expected_number_of_windows_to_be=2)

    def redirect_help_help(self, redirect_page):
        redirect_page.redirect_window(self.locators.sidebar_locators.BUTTON_HELP_HELP, expected_number_of_windows_to_be=2)

    def redirect_help_ideas(self, redirect_page):
        redirect_page.redirect_window(self.locators.sidebar_locators.BUTTON_HELP_IDEAS, expected_number_of_windows_to_be=2)

    def redirect_user_menu_account(self, redirect_page):
        redirect_page.redirect_window(self.locators.navbar_locators.BUTTON_USER_MENU_ACCOUNT, expected_number_of_windows_to_be=2)
