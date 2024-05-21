from ui.pages.base_page import BasePage
from ui.locators.monetization_locators import MonetizationPageLocators


class MonetizationPage(BasePage):
    url = "https://ads.vk.com/partner"

    locators = MonetizationPageLocators()
