from ui.pages.base_page import PageWithView
from ui.locators.main_locators import MainPageLocators
from ui.locators.training_locators import TrainingPageSharedLocators


URL_MAIN_PAGE = 'https://ads.vk.com/hq/overview'


class MainPage(PageWithView):
    url = URL_MAIN_PAGE
    locators = MainPageLocators()
    training_locators = TrainingPageSharedLocators()

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

    def open_training(self):
        self.open_view(self.locators.sidebar_locators.BUTTON_TRAINING, self.training_locators.SIGN_OPENING_MODAL_VIEW)
