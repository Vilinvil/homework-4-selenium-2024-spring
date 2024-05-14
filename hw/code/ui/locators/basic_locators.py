from selenium.webdriver.common.by import By


class BasePageLocators:
    BUTTON_HELP = (By.CSS_SELECTOR, '[href="/help"]')
    BUTTON_CABINET_LOCATOR = (By.CSS_SELECTOR, '[href="/hq?ref=main_landing"]')
