import pytest

from cases import RegisteredUserCase
from ui.pages.registration_page import PreRegistrationPage, RegistrationPage
from utils.timeout import BASIC_TIMEOUT
from utils.credentials import Credentials

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC


class TestPreRegistration(RegisteredUserCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_new_registration_window(self, driver):
        self.pre_registration_page = PreRegistrationPage(self.driver)

    def test_display_pre_registration(self):
        assert self.pre_registration_page.display_pre_registration()

    def test_new_cabinet_button_click(self):
        self.pre_registration_page.open_registration_page()


class TestRegistration(RegisteredUserCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_new_registration_window(self, driver):
        self.pre_registration_page = PreRegistrationPage(self.driver)
        self.pre_registration_page.open_registration_page()
        self.registration_page = RegistrationPage(self.driver)

    def test_display(self):
        assert self.registration_page.find_go_back_button()
        assert self.registration_page.find_fio_field()
        assert self.registration_page.find_inn_field()
        assert self.registration_page.find_email_field()
        assert self.registration_page.find_agency_button()
        assert self.registration_page.find_country_select()
        assert self.registration_page.find_advertiser_button()
        assert self.registration_page.find_create_button()
        assert self.registration_page.find_currency_select()
        assert self.registration_page.find_english_button()
        assert self.registration_page.find_russian_button()
        assert self.registration_page.find_entity_button()
        assert self.registration_page.find_individual_button()

    def test_create_without_offer(self):
        self.registration_page.click_offer_check_mark()

        self.registration_page.click_create_button()
        assert self.registration_page.find_no_offer_alert()

    @pytest.mark.parametrize(
        'button,expected_text',
        [
            pytest.param(
                RegistrationPage.click_english_button, 'Account registration'
            ),
            pytest.param(
                RegistrationPage.click_russian_button, 'Регистрация кабинета'
            ),
        ],
    )
    def test_change_language(self, button, expected_text):
        button(self.registration_page)
        assert self.registration_page.get_header_text() == expected_text

    def test_country_russia_currency_rub(self):
        self.registration_page.select_country_russia()

        assert self.registration_page.find_currency_select_rub()

    def test_country_belarus_currency_usd_eur(self):
        self.registration_page.select_country_belarus()

        assert self.registration_page.find_currency_select_usd_eur()

    def test_create_without_email(self):
        self.registration_page.click_create_button()
        assert self.registration_page.find_email_alert()

    def test_create_with_wrong_email(self):
        self.registration_page.write_email("aboba")

        self.registration_page.click_create_button()
        assert self.registration_page.find_email_alert()

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
        self.registration_page.write_inn(inn)
        elem = self.registration_page.find_create_button()
        AC(self.driver).move_to_element(elem).click(elem).perform()
        assert self.registration_page.find_inn_alert().text == expected_text

    def test_no_individual_with_agency(self):
        self.registration_page.click_agency_button()
        assert self.registration_page.is_individual_button_invisible()

    def test_no_inn_with_entity(self):
        self.registration_page.click_entity_button()
        assert self.registration_page.is_inn_field_invisible()

    def test_create_cabinet(self, credentials: Credentials):
        self.registration_page.write_email(credentials.login)
        self.registration_page.write_inn("473275643494")
        self.registration_page.write_fio("Иванов Валерий Ильич")

        self.registration_page.click_create_button()

        self.registration_page.check_url("https://ads.vk.com/hq/overview")

        self.registration_page.delete_cabinet()
