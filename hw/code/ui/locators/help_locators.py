from selenium.webdriver.common.by import By


class HelpPageLocators:
    INPUT_SEARCH = (By.XPATH, "//*[@data-test-id='fullscreen-search-vkads']//input")
    SEARCH_FOUND_RESULTS = (By.CSS_SELECTOR, '[data-test-id="search-page-vkads"]')
    SEARCH_NOT_FOUND_RESULTS = (By.CSS_SELECTOR, '[data-test-id="not-found-search-page-vkads"]')
    CARD_AUTHORIZATION = (By.CSS_SELECTOR, '[href="/help/categories/authorization"]')
    CARD_GENERAL = (By.CSS_SELECTOR, '[href="/help/categories/general"]')
