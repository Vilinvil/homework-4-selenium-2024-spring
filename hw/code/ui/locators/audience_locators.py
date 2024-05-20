from selenium.webdriver.common.by import By


class AudiencePageLocators:
    BUTTON_CREATE_GROUP = (By.CSS_SELECTOR, '[data-testid="create-audience"]')
    ID_AUDIENCE = (By.ID, 'audience')
    INPUT_NAME_GROUP = (By.XPATH, '//*[@id="root"]//input')
    BUTTON_ADD_SOURCE = (By.XPATH, '//*[@id="root"]//button//*[contains(text(), "Добавить источник")]')
    BUTTON_SAVE_GROUP = (By.CSS_SELECTOR, '[data-testid="submit"]')
    BUTTON_CANCEL_GROUP = (By.CSS_SELECTOR, '[data-testid="cancel"]')
    ROOT = (By.ID, 'root')
    SUBSCRIBERS_SOURCE = (By.XPATH, '//*[contains(@class, "vkuiSimpleCell")]//*[contains(text(), "Подписчики сообществ")]')
    ADD_LIST = (By.XPATH, '//*[contains(text(), "Добавить списком")]')
    VK_COMMUNITY = (By.XPATH, '//*[contains(text(), "Сообщества ВКонтакте")]')
    TEXTAREA = (By.TAG_NAME, 'textarea')
    ADD = (By.XPATH, '//*[contains(text(), "Добавить")]')
