from ui.pages.base_page import BasePage
from ui.locators.main_locators import MainPageLocators

URL_MAIN_PAGE = 'https://ads.vk.com/hq/overview'


class MainPage(BasePage):
    url = URL_MAIN_PAGE
    locators = MainPageLocators()

    
    def click_redirect_to_site_page(self):
        self.click(self.locators.sidebar_locators.BUTTON_SITES)


    def click_redirect_to_lead_forms_page(self):
        self.click(self.locators.sidebar_locators.BUTTON_LEADS)