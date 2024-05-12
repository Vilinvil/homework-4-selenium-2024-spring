from ui.pages.base_page import BasePage
from ui.locators.main_locators import MainPageLocators

URL_MAIN_PAGE = 'https://ads.vk.com/hq/overview'

class MainPage(BasePage):
    url = URL_MAIN_PAGE
    locators = MainPageLocators()
