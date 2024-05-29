import pytest

from ui.pages.settings_page import SettingsPage
from cases import LoggedCase
from utils.timeout import BASIC_TIMEOUT
from ui.locators.settings_locators import SettingsPageLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC


class TestSettings(LoggedCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_new_settings(self, driver):
        self.main_page.open_settings()
        self.settings_page = SettingsPage(self.driver)

    def test_display_tabs(self):
        assert self.settings_page.find_main_tab()
        assert self.settings_page.find_notifications_tab()
        assert self.settings_page.find_access_tab()
        assert self.settings_page.find_logs_tab()


    def test_display(self):
        assert self.settings_page.find_phone_field()
        assert self.settings_page.find_email_field()

        elem = self.settings_page.find_language_select()
        AC(self.driver).move_to_element(elem).perform()

        assert self.settings_page.find_fio_field()
        assert self.settings_page.find_inn_field()
        assert self.settings_page.find_cabinet_name_field()
        assert self.settings_page.find_language_select()

        elem = self.settings_page.find_delete_button()
        AC(self.driver).move_to_element(elem).perform()

        assert self.settings_page.find_delete_button()
        assert self.settings_page.find_logout_button()

    def test_new_buttons_after_change_field(self):
        elem = self.settings_page.find_inn_field()
        AC(self.driver).move_to_element(elem).perform()

        self.settings_page.write_inn("111111111111")

        assert self.settings_page.find_save_button()
        assert self.settings_page.find_cancel_button()

    def test_save(self):
        elem = self.settings_page.find_fio_field()
        AC(self.driver).move_to_element(elem).perform()

        self.settings_page.write_fio("Дзержинский Феликс Эдмундович")

        self.settings_page.click_save_button()
        assert self.settings_page.get_fio() == "Дзержинский Феликс Эдмундович"

    def test_cancel(self):
        elem = self.settings_page.find_fio_field()
        AC(self.driver).move_to_element(elem).perform()

        old_fio = self.settings_page.get_fio()

        self.settings_page.write_fio("Дзержинский Феликс Эдмундович")

        self.settings_page.click_cancel_button()
        assert self.settings_page.get_fio() == old_fio

    @pytest.mark.parametrize(
        'write_func,new_value,find_alert',
        [
            pytest.param(
                SettingsPage.write_phone, 'not phone', SettingsPage.find_phone_alert
            ),
            pytest.param(
                SettingsPage.write_inn, '12122', SettingsPage.find_inn_alert
            ),
        ],
    )
    def test_alerts(self, write_func, new_value, find_alert):
        write_func(self.settings_page, new_value)
        self.settings_page.click_save_button()
        assert find_alert(self.settings_page)

    def test_add_email_button(self):
        self.settings_page.click_add_email_button()
        assert self.settings_page.find_email_extra_field()

    def test_wrong_email(self):
        self.settings_page.click_add_email_button()
        self.settings_page.write_extra_email("wrong_email")
        self.settings_page.click_save_button()
        assert self.settings_page.find_email_alert()

    def test_logout_from_all_devices(self):
        self.settings_page.click_logout_button()
        assert self.settings_page.find_logout_message()

    @pytest.fixture(scope='function')
    def setup_notifications(self):
        self.settings_page.click_notifications_tab()

    def test_display_notifications(self, setup_notifications):
        assert self.settings_page.find_finance_checkbox()
        assert self.settings_page.find_sales_checkbox()
        assert self.settings_page.find_campaigns_checkbox()
        assert self.settings_page.find_moderation_checkbox()
        assert self.settings_page.find_api_checkbox()
        assert self.settings_page.find_email_switch()
        assert self.settings_page.find_rules_checkbox()
        assert self.settings_page.find_news_checkbox()
        assert self.settings_page.find_events_checkbox()

    def test_new_buttons_after_change_notification(self, setup_notifications):
        self.settings_page.click_email_switch()
        assert self.settings_page.find_save_button()
        assert self.settings_page.find_cancel_button()
