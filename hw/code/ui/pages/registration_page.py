from ui.pages.base_page import BasePage
from ui.locators.registration_locators import RegistrationPageLocators
from ui.locators.main_locators import MainPageLocators
from ui.locators.settings_locators import SettingsPageLocators
from utils.timeout import BASIC_TIMEOUT

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC


class PreRegistrationPage(BasePage):
    url = 'https://ads.vk.com/hq/registration'
    locators = RegistrationPageLocators()

    def display_pre_registration(self):
        return self.find(self.locators.CREATE_NEW_CABINET_BUTTON,
                                        until_EC=EC.visibility_of_element_located)

    def open_registration_page(self):
        self.click(self.locators.CREATE_NEW_CABINET_BUTTON)
        self.wait().until(EC.url_to_be("https://ads.vk.com/hq/registration/new"))



class RegistrationPage(BasePage):
    url = 'https://ads.vk.com/hq/registration/new'
    locators = RegistrationPageLocators()

    def find_go_back_button(self):
        return self.find_with_check_visibility(self.locators.REGISTRATION_GO_BACK)

    def find_inn_alert(self):
        return self.find_with_check_visibility(self.locators.REGISTRATION_INN_ALERT)

    def find_fio_field(self):
        return self.find_with_check_visibility(self.locators.REGISTRATION_FIO_FIELD)

    def find_inn_field(self):
        return self.find_with_check_visibility(self.locators.REGISTRATION_INN_FIELD)

    def find_email_field(self):
        return self.find_with_check_visibility(self.locators.REGISTRATION_EMAIL_FIELD)

    def find_agency_button(self):
        return self.find_with_check_visibility(self.locators.REGISTRATION_AGENCY_BUTTON)

    def find_country_select(self):
        return self.find_with_check_visibility(self.locators.REGISTRATION_COUNTRY_SELECT)

    def find_advertiser_button(self):
        return self.find_with_check_visibility(self.locators.REGISTRATION_ADVERTISER_BUTTON)

    def find_create_button(self):
        return self.find_with_check_visibility(self.locators.REGISTRATION_CREATE_BUTTON)

    def find_currency_select(self):
        return self.find_with_check_visibility(self.locators.REGISTRATION_CURRENCY_SELECT)

    def find_english_button(self):
        return self.find_with_check_visibility(self.locators.REGISTRATION_ENGLISH_BUTTON)

    def find_russian_button(self):
        return self.find_with_check_visibility(self.locators.REGISTRATION_RUSSIAN_BUTTON)

    def find_entity_button(self):
        return self.find_with_check_visibility(self.locators.REGISTRATION_ENTITY_BUTTON)

    def find_individual_button(self):
        return self.find_with_check_visibility(self.locators.REGISTRATION_INDIVIDUAL_BUTTON)

    def find_offer_check_mark(self):
        return self.find_with_check_visibility(self.locators.REGISTRATION_OFFER_CHECK_MARK)

    def find_no_offer_alert(self):
        return self.find_with_check_visibility(self.locators.REGISTRATION_NO_OFFER_ALERT)

    def find_email_alert(self):
        return self.find_with_check_visibility(self.locators.REGISTRATION_EMAIL_ALERT)

    def click_offer_check_mark(self):
        elem = self.find(self.locators.REGISTRATION_OFFER_CHECK_MARK)
        AC(self.driver).move_to_element(elem).click(elem).perform()

    def click_create_button(self):
        elem = self.find(self.locators.REGISTRATION_CREATE_BUTTON)
        AC(self.driver).move_to_element(elem).click(elem).perform()

    def find_currency_select_rub(self):
        self.click(self.locators.REGISTRATION_CURRENCY_SELECT)
        return self.find_with_check_visibility(self.locators.REGISTRATION_CURRENCY_SELECT_RUB)

    def select_country_russia(self):
        self.click(self.locators.REGISTRATION_COUNTRY_SELECT)
        self.click(self.locators.REGISTRATION_COUNTRY_SELECT_RUSSIA)

    def select_country_belarus(self):
        self.click(self.locators.REGISTRATION_COUNTRY_SELECT)
        self.click(self.locators.REGISTRATION_COUNTRY_SELECT_BELARUS)

    def find_currency_select_usd_eur(self):
        self.click(self.locators.REGISTRATION_CURRENCY_SELECT)
        return (self.find_with_check_visibility(self.locators.REGISTRATION_CURRENCY_SELECT_USD) and
                self.find_with_check_visibility(self.locators.REGISTRATION_CURRENCY_SELECT_EUR))

    def write_email(self, input):
        self.write_input(self.locators.REGISTRATION_EMAIL_FIELD, input)

    def write_inn(self, input):
        self.write_input(self.locators.REGISTRATION_INN_FIELD, input)

    def write_fio(self, input):
        self.write_input(self.locators.REGISTRATION_FIO_FIELD, input)

    def click_agency_button(self):
        self.click(self.locators.REGISTRATION_AGENCY_BUTTON)

    def click_english_button(self):
        return self.click(self.locators.REGISTRATION_ENGLISH_BUTTON)

    def click_russian_button(self):
        return self.click(self.locators.REGISTRATION_RUSSIAN_BUTTON)

    def get_header_text(self):
        return self.find_with_check_visibility(self.locators.REGISTRATION_HEADER_TITLE).text

    def is_individual_button_invisible(self):
        return self.wait(BASIC_TIMEOUT).until(
            EC.invisibility_of_element(self.locators.REGISTRATION_INDIVIDUAL_BUTTON))

    def is_inn_field_invisible(self):
        return self.wait(BASIC_TIMEOUT).until(
            EC.invisibility_of_element(self.locators.REGISTRATION_INN_FIELD))

    def click_entity_button(self):
        self.click(self.locators.REGISTRATION_ENTITY_BUTTON)

    def delete_cabinet(self):
        self.click(MainPageLocators.sidebar_locators.BUTTON_SETTINGS)
        elem = self.wait(BASIC_TIMEOUT).until(
            EC.presence_of_element_located(SettingsPageLocators.SETTINGS_BUTTON_DELETE_CABINET))
        AC(self.driver).move_to_element(elem).click(elem).perform()
        self.click(SettingsPageLocators.SETTINGS_BUTTON_ACCEPT_DELETE_CABINET)

