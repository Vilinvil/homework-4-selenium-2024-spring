from selenium.webdriver.common.by import By


class BasePageLocators:
    BUTTON_CABINET_LOCATOR = (By.CLASS_NAME, 'ButtonCabinet_primary__LCfol')
    BUTTON_HELP = (By.CSS_SELECTOR, '[href="/help"]')
