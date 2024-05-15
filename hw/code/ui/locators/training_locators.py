from selenium.webdriver.common.by import By


class TrainingPageSharedLocators:
    MODAL_PAGE = (By.ID, '_modal_24')


class TrainingPageLocators:
    BUTTON_START_TRAINING = (By.CSS_SELECTOR, '[data-entityid="onboarding"]')
    TITLE = (By.XPATH, '//*[@id="_modal_24"]//*[contains(text(), "С чего начнём обучение?")]')
    BUTTON_TRY_LATER = (By.XPATH, '//*[@id="_modal_24"]//button//*[contains(text(), "Попробовать позже")]')
    BUTTON_CLOSE = (By.CSS_SELECTOR, '.vkuiModalDismissButton')
    CONTENT_LIST = (By.CSS_SELECTOR, '.vkuiModalPage__content')
