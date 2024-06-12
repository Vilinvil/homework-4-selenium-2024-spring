from ui.pages.base_page import BasePage
from ui.locators.monetization_locators import MonetizationPageLocators
from utils.timeout import BASIC_TIMEOUT

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC


class MonetizationPage(BasePage):
    url = "https://ads.vk.com/partner"

    locators = MonetizationPageLocators()

    def go_to_footer(self):
        elem = self.wait(BASIC_TIMEOUT).until(
            EC.presence_of_element_located(self.locators.MONETIZATION_FOOTER_LOGO_VK_BUSINESS))
        AC(self.driver).move_to_element(elem).perform()

    def find_help_button(self):
        return self.find_with_check_visibility(self.locators.MONETIZATION_FOOTER_BUTTON_HELP)

    def find_rules_button(self):
        return self.find_with_check_visibility(self.locators.MONETIZATION_FOOTER_BUTTON_RULES)

    def find_main_button(self):
        return self.find_with_check_visibility(self.locators.MONETIZATION_FOOTER_BUTTON_MAIN)

    def find_language_wrapper(self):
        return self.find_with_check_visibility(self.locators.MONETIZATION_FOOTER_LANGUAGE_WRAPPER)

    def find_vk_business_logo(self):
        return self.find_with_check_visibility(self.locators.MONETIZATION_FOOTER_LOGO_VK_BUSINESS)

    def redirect_to_vk_business(self, redirect_page):
        redirect_page.redirect_window_with_scroll(self.locators.MONETIZATION_FOOTER_LOGO_VK_BUSINESS, 3)

    def click_rules_button(self):
        elem = self.find(self.locators.MONETIZATION_FOOTER_BUTTON_RULES)
        AC(self.driver).move_to_element(elem).click(elem).perform()

    def click_main_button(self):
        elem = self.find(self.locators.MONETIZATION_FOOTER_BUTTON_MAIN)
        AC(self.driver).move_to_element(elem).click(elem).perform()

    def click_help_button(self):
        elem = self.find(self.locators.MONETIZATION_FOOTER_BUTTON_HELP)
        AC(self.driver).move_to_element(elem).click(elem).perform()

    def click_language_wrapper(self):
        elem = self.find(self.locators.MONETIZATION_FOOTER_LANGUAGE_WRAPPER)
        AC(self.driver).move_to_element(elem).click(elem).perform()

    def click_en_button(self):
        self.click(self.locators.MONETIZATION_FOOTER_LANGUAGE_BUTTON_ENGLISH)

    def click_ru_button(self):
        self.click(self.locators.MONETIZATION_FOOTER_LANGUAGE_BUTTON_RUSSIAN)