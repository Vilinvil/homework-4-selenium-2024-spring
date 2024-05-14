from selenium.webdriver.common.by import By


class OverviewNewUserPageLocators:
    START_ACTIONS_WRAPPER = (By.XPATH, '//*[starts-with(@class, "StartActions_wrapper")]')
    START_ACTION = (By.XPATH,'//*[starts-with(@class, "StartAction_wrapper")]')
    BUTTON_IN_START_ACTION_WRAPPER = (By.XPATH, './/button')
