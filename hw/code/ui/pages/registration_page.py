from ui.pages.base_page import BasePage
from ui.locators.registration_locators import RegistrationPageLocators


class PreRegistrationPage(BasePage):
    url = 'https://ads.vk.com/hq/registration'
    locators = RegistrationPageLocators()

class RegistrationPage(BasePage):
    url = 'https://ads.vk.com/hq/registration/new'
    locators = RegistrationPageLocators()
