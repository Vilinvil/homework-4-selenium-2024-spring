from selenium.webdriver.common.by import By


class BasePageLocators:
    NAV_BUTTON_HELP = (By.XPATH, '//*[@data-test-id="header-test-id:dark"]//*[@href="/help"]')
    NAV_BUTTON_CABINET_LOCATOR = (By.XPATH, '//*[@data-test-id="header-test-id:dark"]//*[@href="/hq?ref=main_landing"]')
