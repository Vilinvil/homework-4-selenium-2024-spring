from selenium.webdriver.common.by import By


class LeadsPageDesignLocators:
    HEADER = (By.XPATH, '//*[contains(@class, "ModalSidebarPage_header")]//*[contains(text(), "Новая лид-форма")]')
    INPUT_LEAD_NAME = (By.CSS_SELECTOR, '[placeholder="Название лид-формы"]')
    BUTTON_SET_GLOBAL_IMAGE = (By.CSS_SELECTOR, '[data-testid="set-global-image"]')
    INPUT_ORGANIZATION = (By.CSS_SELECTOR, '[placeholder="Название компании"]')
    RADIOGROUP_FIRST_SCREEN = (By.XPATH, '//*[contains(@class, "ModalSidebarPage_container")]'
                                         '//*[contains(text(), "Первый экран формы")]//..//*[@role="radiogroup"]')
    INPUT_TITLE = (By.CSS_SELECTOR, '[placeholder="Текст заголовка"]')
    INPUT_SHORT_DESCRIPTION = (By.CSS_SELECTOR, '[placeholder="Краткое описание опроса"]')
    PIPETTE_CHOICE_GRADIENT = (By.CSS_SELECTOR, '[data-id="101"]')
    BUTTON_SET_MAIN_IMAGE = (By.CSS_SELECTOR, '[data-testid="set-main-image"]')


class LeadsPageLocators:
    BUTTON_CREATE_LEAD_FORM = (By.CSS_SELECTOR, '[test-id="create-leadform-button"]')
    BUTTON_CANCEL = (By.CSS_SELECTOR, '[data-testid="cancel"]')
    BUTTON_SUBMIT = (By.CSS_SELECTOR, '[data-testid="submit"]')

