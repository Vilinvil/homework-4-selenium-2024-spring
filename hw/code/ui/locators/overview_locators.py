from selenium.webdriver.common.by import By


class OverviewNewUserPageLocators:
    START_ACTIONS_WRAPPER = (By.XPATH, '//*[starts-with(@class, "StartActions_wrapper")]')
    START_ACTION = (By.XPATH,'.//*[starts-with(@class, "StartAction_wrapper")]')
    BUTTON_IN_START_ACTION_WRAPPER = (By.XPATH, './/button')

    BUTTON_CREATE_CAMPAIGN =\
        (By.XPATH, '//*[starts-with(@class, "StartAction_wrapper")]//button//*[contains(text(),"Создать вручную")]')
    BUTTON_START_TRAINING = \
        (By.XPATH, '//*[starts-with(@class, "StartAction_wrapper")]//button//*[contains(text(),"Пройти обучение")]')
