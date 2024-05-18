from selenium.webdriver.common.by import By


class SettingsPageLocators:
    SETTINGS_BUTTON_DELETE_CABINET = (By.XPATH, '//*[contains(text(),"Удалить кабинет")]')
    SETTINGS_BUTTON_LOGOUT_FROM_ALL_DEVICES = (By.XPATH, '//*[contains(text(),"Выйти из других устройств")]')
    SETTINGS_LOGOUT_FROM_ALL_DEVICES_MESSAGE = (By.XPATH, '//*[contains(@class, "Snackbar_success_")]')
    SETTINGS_BUTTON_ACCEPT_DELETE_CABINET = (By.XPATH, '//*[contains(text(),"Да, удалить")]')

    SETTINGS_MAIN_TAB = (By.ID, "tab-settings")
    SETTINGS_NOTIFICATIONS_TAB = (By.ID, "tab-settings.notifications")
    SETTINGS_ACCESS_TAB = (By.ID, "tab-settings.access")
    SETTINGS_LOGS_TAB = (By.ID, "tab-settings.logs")

    SETTINGS_PHONE_FIELD = (By.XPATH, '//*[@data-testid="general-phone"]')
    SETTINGS_EMAIL_FIELD = (By.XPATH, '//*[@data-testid="general-email"]')
    SETTINGS_ADD_EMAIL_BUTTON = (By.XPATH, '//*[@data-testid="add-email"]')
    SETTINGS_EMAIL_EXTRA_FIELD = (By.XPATH, '//*[@data-testid="email-0"]')
    SETTINGS_FIO_FIELD = (By.XPATH, '//*[@data-testid="general-ord-name"]')
    SETTINGS_INN_FIELD = (By.XPATH, '//*[@data-testid="general-ord-inn"]')
    SETTINGS_CABINET_NAME_FIELD = (By.XPATH, '//*[@data-testid="account-item"]')
    SETTINGS_WRONG_PHONE_ALERT = (By.XPATH, '//*[contains(text(),"Некорректный номер телефона")]')
    SETTINGS_SHORT_INN_ALERT = (By.XPATH, '//*[contains(text(),"Длина ИНН должна быть 12 символов")]')
    SETTINGS_WRONG_EMAIL_ALERT = (By.XPATH, '//*[contains(text(),"Некорректный email адрес")]')


    SETTINGS_LANGUAGE_SELECT = (By.XPATH, '//*[@data-testid="interface-language"]')

    SETTINGS_SAVE_BUTTON = (By.XPATH, '//*[@data-testid="settings-save"]')
    SETTINGS_CANCEL_BUTTON = (By.XPATH, '//*[@data-testid="settings-cancel"]')

    SETTINGS_NOTIFICATIONS_EMAIL_SWITCH = (By.XPATH, '//*[contains(@class, "vkuiSwitch")]')
    SETTINGS_NOTIFICATIONS_FINANCE_CHECKBOX = (By.XPATH, '//*[contains(text(),"Финансы")]')
    SETTINGS_NOTIFICATIONS_MODERATION_CHECKBOX = (By.XPATH, '//*[contains(text(),"Модерация")]')
    SETTINGS_NOTIFICATIONS_CAMPAIGNS_CHECKBOX = (By.XPATH, '//*[contains(text(),"Рекламные кампании")]')
    SETTINGS_NOTIFICATIONS_RULES_CHECKBOX = (By.XPATH, '//*[contains(text(),"Правила для объявлений")]')
    SETTINGS_NOTIFICATIONS_API_CHECKBOX = (By.XPATH, '//*[contains(text(),"Изменения в API")]')
    SETTINGS_NOTIFICATIONS_NEWS_CHECKBOX = (By.XPATH, '//*[contains(text(),"Новости")]')
    SETTINGS_NOTIFICATIONS_EVENTS_CHECKBOX = (By.XPATH, '//*[contains(text(),"Мероприятия")]')
    SETTINGS_NOTIFICATIONS_SALES_CHECKBOX = (By.XPATH, '//*[contains(text(),"Акции, спецпредложения и прочие")]')

    SETTINGS_ACCESS_DETAILS_LINK = (By.XPATH, '//*[@href="/help/articles/additionalaccounts"]')
    SETTINGS_ACCESS_ADD_USER_BUTTON = (By.XPATH, '//*[@data-testid="add-user"]')



