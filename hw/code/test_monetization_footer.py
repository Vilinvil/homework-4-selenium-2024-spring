import pytest

from cases import BaseCase
from ui.locators.monetization_locators import MonetizationPageLocators
from ui.pages.monetization_page import MonetizationPage
from selenium.webdriver.support import expected_conditions as EC
from utils.redirect_window import redirect_window
from utils.timeout import BASIC_TIMEOUT
from selenium.webdriver.common.action_chains import ActionChains as AC


class TestMonetizationFooter(BaseCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_monetization(self, driver, config):
        redirect_window(self.base_page, self.base_page.locators.NAV_BUTTON_MONETIZATION)
        self.monetization_page = MonetizationPage(self.driver)

    def test_display(self):
        elem = self.monetization_page.wait(BASIC_TIMEOUT).until(
            EC.presence_of_element_located(self.monetization_page.locators.MONETIZATION_FOOTER_LOGO_VK_BUSINESS))
        AC(self.driver).move_to_element(elem).perform()

        assert self.monetization_page.find(self.monetization_page.locators.MONETIZATION_FOOTER_BUTTON_HELP)
        assert self.monetization_page.find(self.monetization_page.locators.MONETIZATION_FOOTER_BUTTON_RULES)
        assert self.monetization_page.find(self.monetization_page.locators.MONETIZATION_FOOTER_BUTTON_MAIN)
        assert self.monetization_page.find(self.monetization_page.locators.MONETIZATION_FOOTER_LANGUAGE_WRAPPER)
        assert self.monetization_page.find(self.monetization_page.locators.MONETIZATION_FOOTER_LOGO_VK_BUSINESS)
