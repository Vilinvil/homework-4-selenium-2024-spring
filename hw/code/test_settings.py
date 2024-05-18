import pytest

from ui.pages.settings_page import SettingsPage
from selenium.webdriver.support import expected_conditions as EC
from cases import LoggedCase
from selenium.webdriver.common.action_chains import ActionChains as AC
from utils.timeout import BASIC_TIMEOUT
from ui.locators.settings_locators import SettingsPageLocators
from ui.pages.base_page import PageWithRedirectWindow

class TestSettingsBase(LoggedCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_new_settings(self, driver, config):
        self.main_page.click(self.main_page.locators.NAV_BUTTON_SETTINGS)
        self.settings_page = SettingsPage(self.driver)

    def test_display_tabs(self):
        assert self.settings_page.find(self.settings_page.locators.SETTINGS_MAIN_TAB).is_displayed()
        assert self.settings_page.find(self.settings_page.locators.SETTINGS_NOTIFICATIONS_TAB).is_displayed()
        assert self.settings_page.find(self.settings_page.locators.SETTINGS_ACCESS_TAB).is_displayed()
        assert self.settings_page.find(self.settings_page.locators.SETTINGS_LOGS_TAB).is_displayed()

    @pytest.mark.parametrize(
        'locator,url',
        [
            pytest.param(
                SettingsPageLocators.SETTINGS_MAIN_TAB, 'https://ads.vk.com/hq/settings'
            ),
            pytest.param(
                SettingsPageLocators.SETTINGS_NOTIFICATIONS_TAB, 'https://ads.vk.com/hq/settings/notifications'
            ),
            pytest.param(
                SettingsPageLocators.SETTINGS_ACCESS_TAB, 'https://ads.vk.com/hq/settings/access'
            ),
            pytest.param(
                SettingsPageLocators.SETTINGS_LOGS_TAB, 'https://ads.vk.com/hq/settings/logs'
            ),
        ],
    )
    def test_tabs_open_pages(self, locator, url):
        self.settings_page.click(locator)
        self.settings_page.wait().until(EC.url_to_be(url))

    def test_display(self):
        assert self.settings_page.find(self.settings_page.locators.SETTINGS_PHONE_FIELD).is_displayed()
        assert self.settings_page.find(self.settings_page.locators.SETTINGS_EMAIL_FIELD).is_displayed()

        elem = self.settings_page.wait(BASIC_TIMEOUT).until(
            EC.presence_of_element_located(self.settings_page.locators.SETTINGS_LANGUAGE_SELECT))
        AC(self.driver).move_to_element(elem).perform()

        assert self.settings_page.find(self.settings_page.locators.SETTINGS_FIO_FIELD).is_displayed()
        assert self.settings_page.find(self.settings_page.locators.SETTINGS_INN_FIELD).is_displayed()
        assert self.settings_page.find(self.settings_page.locators.SETTINGS_CABINET_NAME_FIELD).is_displayed()
        assert self.settings_page.find(self.settings_page.locators.SETTINGS_LANGUAGE_SELECT).is_displayed()

        elem = self.settings_page.wait(BASIC_TIMEOUT).until(
            EC.presence_of_element_located(self.settings_page.locators.SETTINGS_BUTTON_DELETE_CABINET))
        AC(self.driver).move_to_element(elem).perform()

        assert self.settings_page.find(self.settings_page.locators.SETTINGS_BUTTON_DELETE_CABINET).is_displayed()
        assert self.settings_page.find(self.settings_page.locators.SETTINGS_BUTTON_LOGOUT_FROM_ALL_DEVICES).is_displayed()

    def test_new_buttons_after_change_field(self):
        elem = self.settings_page.wait(BASIC_TIMEOUT).until(
            EC.presence_of_element_located(self.settings_page.locators.SETTINGS_INN_FIELD))
        AC(self.driver).move_to_element(elem).perform()

        self.settings_page.write_input(self.settings_page.locators.SETTINGS_INN_FIELD, "111111111111")

        assert self.settings_page.find(self.settings_page.locators.SETTINGS_SAVE_BUTTON).is_displayed()
        assert self.settings_page.find(
            self.settings_page.locators.SETTINGS_CANCEL_BUTTON).is_displayed()

    def test_save(self):
        elem = self.settings_page.wait(BASIC_TIMEOUT).until(
            EC.presence_of_element_located(self.settings_page.locators.SETTINGS_FIO_FIELD))
        AC(self.driver).move_to_element(elem).perform()

        self.settings_page.write_input(self.settings_page.locators.SETTINGS_FIO_FIELD, "Дзержинский Феликс Эдмундович")

        if self.settings_page.find(self.settings_page.locators.SETTINGS_SAVE_BUTTON).is_displayed():
            elem = self.settings_page.wait(BASIC_TIMEOUT).until(
                EC.presence_of_element_located(self.settings_page.locators.SETTINGS_SAVE_BUTTON))
            AC(self.driver).move_to_element(elem).click(elem).perform()
            assert (self.settings_page.get_input_field_value(self.settings_page.locators.SETTINGS_FIO_FIELD)
                    == "Дзержинский Феликс Эдмундович")

    def test_cancel(self):
        elem = self.settings_page.wait(BASIC_TIMEOUT).until(
            EC.presence_of_element_located(self.settings_page.locators.SETTINGS_FIO_FIELD))
        AC(self.driver).move_to_element(elem).perform()

        old_fio = self.settings_page.get_input_field_value(self.settings_page.locators.SETTINGS_FIO_FIELD)

        self.settings_page.write_input(self.settings_page.locators.SETTINGS_FIO_FIELD, "Дзержинский Феликс Эдмундович")

        if self.settings_page.find(self.settings_page.locators.SETTINGS_CANCEL_BUTTON).is_displayed():
            elem = self.settings_page.wait(BASIC_TIMEOUT).until(
                EC.presence_of_element_located(self.settings_page.locators.SETTINGS_CANCEL_BUTTON))
            AC(self.driver).move_to_element(elem).click(elem).perform()
            assert (self.settings_page.get_input_field_value(self.settings_page.locators.SETTINGS_FIO_FIELD) == old_fio)

    @pytest.mark.parametrize(
        'field_locator,new_value,alert_locator',
        [
            pytest.param(
                SettingsPageLocators.SETTINGS_PHONE_FIELD, 'not phone', SettingsPageLocators.SETTINGS_WRONG_PHONE_ALERT
            ),
            pytest.param(
                SettingsPageLocators.SETTINGS_INN_FIELD, '12122', SettingsPageLocators.SETTINGS_SHORT_INN_ALERT
            ),
        ],
    )
    def test_alerts(self, field_locator, new_value, alert_locator):
        self.settings_page.write_input(field_locator, new_value)
        elem = self.settings_page.wait(BASIC_TIMEOUT).until(
            EC.presence_of_element_located(self.settings_page.locators.SETTINGS_SAVE_BUTTON))
        AC(self.driver).move_to_element(elem).click(elem).perform()
        assert self.settings_page.find(alert_locator).is_displayed()

    def test_add_email_button(self):
        self.settings_page.click(self.settings_page.locators.SETTINGS_ADD_EMAIL_BUTTON)
        assert self.settings_page.find(self.settings_page.locators.SETTINGS_EMAIL_EXTRA_FIELD).is_displayed()

    def test_wrong_email(self):
        self.settings_page.click(self.settings_page.locators.SETTINGS_ADD_EMAIL_BUTTON)
        self.settings_page.write_input(self.settings_page.locators.SETTINGS_EMAIL_EXTRA_FIELD, "wrong_email")
        elem = self.settings_page.wait(BASIC_TIMEOUT).until(
            EC.presence_of_element_located(self.settings_page.locators.SETTINGS_SAVE_BUTTON))
        AC(self.driver).move_to_element(elem).click(elem).perform()
        assert self.settings_page.find(self.settings_page.locators.SETTINGS_WRONG_EMAIL_ALERT).is_displayed()

    def test_logout_from_all_devices(self):
        elem = self.settings_page.wait(BASIC_TIMEOUT).until(
            EC.presence_of_element_located(self.settings_page.locators.SETTINGS_BUTTON_LOGOUT_FROM_ALL_DEVICES))
        AC(self.driver).move_to_element(elem).click(elem).perform()
        assert self.settings_page.find(self.settings_page.locators.SETTINGS_LOGOUT_FROM_ALL_DEVICES_MESSAGE).is_displayed()

    @pytest.fixture(scope='function')
    def setup_notifications(self):
        self.settings_page.click(self.settings_page.locators.SETTINGS_NOTIFICATIONS_TAB)

    def test_display_notifications(self, setup_notifications):
        assert self.settings_page.find(self.settings_page.locators.SETTINGS_NOTIFICATIONS_FINANCE_CHECKBOX).is_displayed()
        assert self.settings_page.find(self.settings_page.locators.SETTINGS_NOTIFICATIONS_SALES_CHECKBOX).is_displayed()
        assert self.settings_page.find(self.settings_page.locators.SETTINGS_NOTIFICATIONS_CAMPAIGNS_CHECKBOX).is_displayed()
        assert self.settings_page.find(self.settings_page.locators.SETTINGS_NOTIFICATIONS_MODERATION_CHECKBOX).is_displayed()
        assert self.settings_page.find(self.settings_page.locators.SETTINGS_NOTIFICATIONS_API_CHECKBOX).is_displayed()
        assert self.settings_page.find(self.settings_page.locators.SETTINGS_NOTIFICATIONS_EMAIL_SWITCH).is_displayed()
        assert self.settings_page.find(self.settings_page.locators.SETTINGS_NOTIFICATIONS_RULES_CHECKBOX).is_displayed()
        assert self.settings_page.find(self.settings_page.locators.SETTINGS_NOTIFICATIONS_NEWS_CHECKBOX).is_displayed()
        assert self.settings_page.find(self.settings_page.locators.SETTINGS_NOTIFICATIONS_EVENTS_CHECKBOX).is_displayed()

    def test_new_buttons_after_change_notification(self, setup_notifications):
        self.settings_page.click(self.settings_page.locators.SETTINGS_NOTIFICATIONS_FINANCE_CHECKBOX)
        assert self.settings_page.find(
            self.settings_page.locators.SETTINGS_SAVE_BUTTON).is_displayed()
        assert self.settings_page.find(
            self.settings_page.locators.SETTINGS_CANCEL_BUTTON).is_displayed()

    @pytest.fixture(scope='function')
    def setup_access(self):
        self.settings_page.click(self.settings_page.locators.SETTINGS_ACCESS_TAB)

    def test_display_access(self, setup_access):
        assert self.settings_page.find(self.settings_page.locators.SETTINGS_ACCESS_ADD_USER_BUTTON).is_displayed()
        assert self.settings_page.find(self.settings_page.locators.SETTINGS_ACCESS_DETAILS_LINK).is_displayed()

    def test_details_link(self, setup_access):
        self.settings_page.redirect_window(self.settings_page.locators.SETTINGS_ACCESS_DETAILS_LINK)
        self.settings_page.wait().until(EC.url_to_be('https://ads.vk.com/help/articles/additionalaccounts'))



