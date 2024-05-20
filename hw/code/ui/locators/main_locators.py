from selenium.webdriver.common.by import By


class MainPageLocators:
    NAV_BUTTON_SECTION_OVERVIEW = (By.CSS_SELECTOR, '[data-entityid: "overview"]')
    NAV_BUTTON_BUDGET_SECTION = (By.CSS_SELECTOR, '[data-entityid="budget"]')
    NAV_BUTTON_CAMPAIGN_SECTION = (By.CSS_SELECTOR, '[data-entityid="dashboardV2"]')
    NAV_BUTTON_AUDIENCE_SECTION = (By.CSS_SELECTOR, '[data-entityid="audience"]')
