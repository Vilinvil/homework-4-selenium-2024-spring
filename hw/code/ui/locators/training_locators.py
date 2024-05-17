from selenium.webdriver.common.by import By


class TrainingPageSharedLocators:
    SIGN_OPENING_MODAL_VIEW = (By.ID, '_modal_24')


class TrainingPageSiteLocators:
    BUTTON_SITE = (By.XPATH, '//*[contains(@class, "ModalRoot_componentWrapper")]'
                             '//*[@role="button"]//*[contains(text(), "Сайт")]')
    TITLE = (By.XPATH, '//*[contains(@class, "ModalRoot_componentWrapper")]'
                       '//*[contains(text(), "Как хотите учиться?")]')
    BUTTON_VIDEO = (By.XPATH, '//*[contains(@class, "ModalRoot_componentWrapper")]//*[@role="button"]'
                              '//*[contains(text(), "Смотреть видеоурок")]')
    BUTTON_ARTICLES = (By.XPATH, '//*[contains(@class, "ModalRoot_componentWrapper")]//*[@role="button"]'
                                 '//*[contains(text(), "Смотреть курс")]')
    BUTTON_STEP_BY_STEP_TRAINING = (By.XPATH, '//*[contains(@class, "ModalRoot_componentWrapper")]//*[@role="button"]'
                                    '//*[contains(text(), "Пошаговое обучение")]')

    SIGN_OPENING_VIDEO = (By.XPATH, '//iframe[contains(@class, "VideoOnboardingModal")]')


class TrainingPageLocators:
    site_locators = TrainingPageSiteLocators()

    BUTTON_START_TRAINING = (By.CSS_SELECTOR, '[data-entityid="onboarding"]')
    TITLE = (By.XPATH, '//*[contains(@class, "ModalRoot_componentWrapper")]'
                       '//*[contains(text(), "С чего начнём обучение?")]')
    BUTTON_TRY_LATER = (By.XPATH, '//*[contains(@class, "ModalRoot_componentWrapper")]'
                                  '//button//*[contains(text(), "Попробовать позже")]')
    BUTTON_CLOSE = (By.CLASS_NAME, 'vkuiModalDismissButton')
    CONTENT_LIST = (By.CLASS_NAME, 'vkuiModalPage__content')
