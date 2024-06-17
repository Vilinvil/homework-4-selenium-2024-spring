from ui.locators.settings_locators import SettingsPageLocators
from utils.timeout import BASIC_TIMEOUT
from ui.pages.base_page import PageWithView, PageWithRedirectWindow

from selenium.webdriver.common.action_chains import ActionChains as AC


class SettingsPage(PageWithRedirectWindow, PageWithView):
    url = "https://ads.vk.com/hq/settings"
    locators = SettingsPageLocators()

    def get_input_field_value(self, locator, timeout=BASIC_TIMEOUT):
        elem = self.find(locator, timeout=timeout)
        return elem.get_attribute('value')

    def find_main_tab(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_MAIN_TAB)

    def find_notifications_tab(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_NOTIFICATIONS_TAB)

    def find_access_tab(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_ACCESS_TAB)

    def find_logs_tab(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_LOGS_TAB)

    def find_phone_field(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_PHONE_FIELD)

    def find_email_field(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_EMAIL_FIELD)

    def find_language_select(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_LANGUAGE_SELECT)

    def find_fio_field(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_FIO_FIELD)

    def find_inn_field(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_INN_FIELD)

    def find_cabinet_name_field(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_CABINET_NAME_FIELD)

    def find_delete_button(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_BUTTON_DELETE_CABINET)

    def find_logout_button(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_BUTTON_LOGOUT_FROM_ALL_DEVICES)

    def write_inn(self, input):
        self.write_input(self.locators.SETTINGS_INN_FIELD, input)

    def write_fio(self, input):
        self.write_input(self.locators.SETTINGS_FIO_FIELD, input)

    def write_phone(self, input):
        self.write_input(self.locators.SETTINGS_PHONE_FIELD, input)

    def write_extra_email(self, input):
        self.write_input(self.locators.SETTINGS_EMAIL_EXTRA_FIELD, input)

    def find_save_button(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_SAVE_BUTTON)

    def find_cancel_button(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_CANCEL_BUTTON)

    def find_logout_message(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_LOGOUT_FROM_ALL_DEVICES_MESSAGE)

    def click_save_button(self):
        elem = self.find_save_button()
        AC(self.driver).move_to_element(elem).click(elem).perform()

    def click_logout_button(self):
        elem = self.find_logout_button()
        AC(self.driver).move_to_element(elem).click(elem).perform()

    def click_cancel_button(self):
        elem = self.find_cancel_button()
        AC(self.driver).move_to_element(elem).click(elem).perform()

    def click_add_email_button(self):
        self.click(self.locators.SETTINGS_ADD_EMAIL_BUTTON)

    def get_fio(self):
        return self.get_input_field_value(self.locators.SETTINGS_FIO_FIELD)

    def find_phone_alert(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_WRONG_PHONE_ALERT)

    def find_email_alert(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_WRONG_EMAIL_ALERT)

    def find_email_extra_field(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_EMAIL_EXTRA_FIELD)

    def find_inn_alert(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_SHORT_INN_ALERT)

    def click_notifications_tab(self):
        self.click(self.locators.SETTINGS_NOTIFICATIONS_TAB)

    def find_finance_checkbox(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_NOTIFICATIONS_FINANCE_CHECKBOX)

    def find_sales_checkbox(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_NOTIFICATIONS_SALES_CHECKBOX)

    def find_campaigns_checkbox(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_NOTIFICATIONS_CAMPAIGNS_CHECKBOX)

    def find_moderation_checkbox(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_NOTIFICATIONS_MODERATION_CHECKBOX)

    def find_api_checkbox(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_NOTIFICATIONS_API_CHECKBOX)

    def find_email_switch(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_NOTIFICATIONS_EMAIL_SWITCH)

    def find_rules_checkbox(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_NOTIFICATIONS_RULES_CHECKBOX)

    def find_news_checkbox(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_NOTIFICATIONS_NEWS_CHECKBOX)

    def find_events_checkbox(self):
        return self.find_with_check_visibility(self.locators.SETTINGS_NOTIFICATIONS_EVENTS_CHECKBOX)

    def click_email_switch(self):
        self.click(self.locators.SETTINGS_NOTIFICATIONS_EMAIL_SWITCH)
