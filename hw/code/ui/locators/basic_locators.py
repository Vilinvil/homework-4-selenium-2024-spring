from selenium.webdriver.common.by import By


class BasePageLocators:
    NAV_BUTTON_HELP = (By.XPATH, '//*[@data-test-id="header-test-id:dark"]//*[@href="/help"]')
