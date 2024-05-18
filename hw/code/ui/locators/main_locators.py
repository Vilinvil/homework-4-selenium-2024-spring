from selenium.webdriver.common.by import By


class MainPageLocators:
    NAV_BUTTON_SECTION_OVERVIEW = (By.CSS_SELECTOR, '[data-entityid: "overview"]')
    NAV_BUTTON_BUDGET_SECTION = (By.CSS_SELECTOR, '[data-entityid="budget"]')
    NAV_BUTTON_SETTINGS = (By.XPATH, '//*[@href="/hq/settings"]')
