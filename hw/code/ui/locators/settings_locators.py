from selenium.webdriver.common.by import By


class SettingsPageLocators:
    SETTINGS_BUTTON_DELETE_CABINET = (By.XPATH, '//*[contains(text(),"Удалить кабинет")]')
    SETTINGS_BUTTON_ACCEPT_DELETE_CABINET = (By.XPATH, '//*[contains(text(),"Да, удалить")]')