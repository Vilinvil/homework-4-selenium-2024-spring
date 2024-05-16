import pytest

from cases import LoggedNewUserCase, LoggedCase, RegisteredUserCase
from ui.pages.registration_page import PreRegistrationPage, RegistrationPage
from selenium.webdriver.support import expected_conditions as EC
from ui.locators.registration_locators import RegistrationPageLocators
from ui.locators.navigation_locators import NavigationPageLocators
from ui.locators.settings_locators import SettingsPageLocators
from utils.timeout import BASIC_TIMEOUT
from selenium.webdriver.common.action_chains import ActionChains as AC
from utils.credentials import Credentials

class TestPreRegistration(RegisteredUserCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_new_registration_window(self, driver, config):
        self.pre_registration_page = PreRegistrationPage(self.driver)

    def test_display_pre_registration(self):
        assert self.pre_registration_page.find(self.pre_registration_page.locators.CREATE_NEW_CABINET_BUTTON).is_displayed()

    def test_new_cabinet_button_click(self):
        self.pre_registration_page.click(self.pre_registration_page.locators.CREATE_NEW_CABINET_BUTTON)
        self.pre_registration_page.wait().until(EC.url_to_be("https://ads.vk.com/hq/registration/new"))

class TestRegistration(RegisteredUserCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_new_registration_window(self, driver, config):
        self.pre_registration_page = PreRegistrationPage(self.driver)
        self.pre_registration_page.click(self.pre_registration_page.locators.CREATE_NEW_CABINET_BUTTON)
        self.registration_page = RegistrationPage(self.driver)

    def test_display(self):
        assert self.registration_page.find(self.registration_page.locators.REGISTRATION_GO_BACK).is_displayed()
        assert self.registration_page.find(self.registration_page.locators.REGISTRATION_FIO_FIELD).is_displayed()
        assert self.registration_page.find(self.registration_page.locators.REGISTRATION_INN_FIELD).is_displayed()
        assert self.registration_page.find(self.registration_page.locators.REGISTRATION_EMAIL_FIELD).is_displayed()
        assert self.registration_page.find(self.registration_page.locators.REGISTRATION_AGENCY_BUTTON).is_displayed()
        assert self.registration_page.find(self.registration_page.locators.REGISTRATION_COUNTRY_SELECT).is_displayed()
        assert self.registration_page.find(
            self.registration_page.locators.REGISTRATION_ADVERTISER_BUTTON).is_displayed()
        assert self.registration_page.find(self.registration_page.locators.REGISTRATION_CREATE_BUTTON).is_displayed()
        assert self.registration_page.find(self.registration_page.locators.REGISTRATION_CURRENCY_SELECT).is_displayed()
        assert self.registration_page.find(self.registration_page.locators.REGISTRATION_ENGLISH_BUTTON).is_displayed()
        assert self.registration_page.find(self.registration_page.locators.REGISTRATION_RUSSIAN_BUTTON).is_displayed()
        assert self.registration_page.find(self.registration_page.locators.REGISTRATION_ENTITY_BUTTON).is_displayed()
        assert self.registration_page.find(self.registration_page.locators.REGISTRATION_INDIVIDUAL_BUTTON).is_displayed()

    def test_create_without_offer(self):
        elem = self.registration_page.wait(BASIC_TIMEOUT).until(
            EC.presence_of_element_located(self.registration_page.locators.REGISTRATION_OFFER_CHECK_MARK))
        AC(self.driver).move_to_element(elem).click(elem).perform()

        elem = self.registration_page.wait(BASIC_TIMEOUT).until(
            EC.presence_of_element_located(self.registration_page.locators.REGISTRATION_CREATE_BUTTON))
        AC(self.driver).move_to_element(elem).click(elem).perform()
        assert self.registration_page.find(self.registration_page.locators.REGISTRATION_NO_OFFER_ALERT).is_displayed()

    @pytest.mark.parametrize(
        'locator,expected_text',
        [
            pytest.param(
                RegistrationPageLocators.REGISTRATION_ENGLISH_BUTTON, 'Account registration'
            ),
            pytest.param(
                RegistrationPageLocators.REGISTRATION_RUSSIAN_BUTTON, 'Регистрация кабинета'
            ),
        ],
    )
    def test_change_language(self, locator, expected_text):
        self.registration_page.click(locator)
        assert self.registration_page.find(self.registration_page.locators.REGISTRATION_HEADER_TITLE).text == expected_text

    def test_country_russia_currency_rub(self):
        self.registration_page.click(self.registration_page.locators.REGISTRATION_COUNTRY_SELECT)
        self.registration_page.click(self.registration_page.locators.REGISTRATION_COUNTRY_SELECT_RUSSIA)
        self.registration_page.click(self.registration_page.locators.REGISTRATION_CURRENCY_SELECT)
        assert self.registration_page.find(self.registration_page.locators.REGISTRATION_CURRENCY_SELECT_RUB).is_displayed()

    def test_country_belarus_currency_usd_eur(self):
        self.registration_page.click(self.registration_page.locators.REGISTRATION_COUNTRY_SELECT)
        self.registration_page.click(self.registration_page.locators.REGISTRATION_COUNTRY_SELECT_BELARUS)
        self.registration_page.click(self.registration_page.locators.REGISTRATION_CURRENCY_SELECT)
        assert self.registration_page.find(
            self.registration_page.locators.REGISTRATION_CURRENCY_SELECT_USD).is_displayed()
        assert self.registration_page.find(
            self.registration_page.locators.REGISTRATION_CURRENCY_SELECT_EUR).is_displayed()

    def test_create_without_email(self):
        elem = self.registration_page.wait(BASIC_TIMEOUT).until(
            EC.presence_of_element_located(self.registration_page.locators.REGISTRATION_CREATE_BUTTON))
        AC(self.driver).move_to_element(elem).click(elem).perform()
        assert self.registration_page.find(self.registration_page.locators.REGISTRATION_EMAIL_ALERT).is_displayed()

    def test_create_with_wrong_email(self):
        self.registration_page.write_input(self.registration_page.locators.REGISTRATION_EMAIL_FIELD, "aboba")

        elem = self.registration_page.wait(BASIC_TIMEOUT).until(
            EC.presence_of_element_located(self.registration_page.locators.REGISTRATION_CREATE_BUTTON))
        AC(self.driver).move_to_element(elem).click(elem).perform()
        assert self.registration_page.find(self.registration_page.locators.REGISTRATION_EMAIL_ALERT).is_displayed()

    @pytest.mark.parametrize(
        'inn,expected_text',
        [
            pytest.param(
                '111', 'Минимальная длина 12'
            ),
            pytest.param(
                '111111111111111111111111111111111111111', 'Максимальная длина 12 символов'
            ),
        ],
    )
    def test_long_short_inn(self, inn, expected_text):
        self.registration_page.write_input(self.registration_page.locators.REGISTRATION_INN_FIELD, inn)
        elem = self.registration_page.wait(BASIC_TIMEOUT).until(
            EC.presence_of_element_located(self.registration_page.locators.REGISTRATION_CREATE_BUTTON))
        AC(self.driver).move_to_element(elem).click(elem).perform()
        assert self.registration_page.find(
            self.registration_page.locators.REGISTRATION_INN_ALERT).text == expected_text

    def test_no_individual_with_agency(self):
        self.registration_page.click(self.registration_page.locators.REGISTRATION_AGENCY_BUTTON)
        assert self.registration_page.wait(BASIC_TIMEOUT).until(EC.invisibility_of_element(self.registration_page.locators.REGISTRATION_INDIVIDUAL_BUTTON))

    def test_no_inn_with_entity(self):
        self.registration_page.click(self.registration_page.locators.REGISTRATION_ENTITY_BUTTON)
        assert self.registration_page.wait(BASIC_TIMEOUT).until(EC.invisibility_of_element(self.registration_page.locators.REGISTRATION_INN_FIELD))

    def test_create_cabinet(self, credentials: Credentials):
        self.registration_page.write_input(
            self.registration_page.locators.REGISTRATION_EMAIL_FIELD, credentials.login)
        self.registration_page.write_input(
            self.registration_page.locators.REGISTRATION_INN_FIELD, "473275643494")
        self.registration_page.write_input(
            self.registration_page.locators.REGISTRATION_FIO_FIELD, "Иванов Валерий Ильич")

        elem = self.registration_page.wait(BASIC_TIMEOUT).until(
            EC.presence_of_element_located(self.registration_page.locators.REGISTRATION_CREATE_BUTTON))
        AC(self.driver).move_to_element(elem).click(elem).perform()

        self.registration_page.wait().until(EC.url_matches("https://ads.vk.com/hq/overview"))

        self.registration_page.click(NavigationPageLocators.NAVIGATION_BUTTON_SETTINGS)
        elem = self.registration_page.wait(BASIC_TIMEOUT).until(
            EC.presence_of_element_located(SettingsPageLocators.SETTINGS_BUTTON_DELETE_CABINET))
        AC(self.driver).move_to_element(elem).click(elem).perform()
        self.registration_page.click(SettingsPageLocators.SETTINGS_BUTTON_ACCEPT_DELETE_CABINET)

