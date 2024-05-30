from selenium.webdriver.common.by import By


class HelpPageLocators:
    HEADER_HELP = (By.CSS_SELECTOR, '[data-test-id="summary-title-ads"]')
    INPUT_SEARCH = (By.XPATH, '//*[@data-test-id="fullscreen-search-vkads"]//input')
    WRAPPER_CATEGORIES = (By.XPATH, '//*[contains(@class, "Categories_wrapper")]')

    SIGN_SEARCH_FOUND_RESULTS = (By.CSS_SELECTOR, '[data-test-id="search-page-vkads"]')
    SIGN_SEARCH_NOT_FOUND_RESULTS = (By.CSS_SELECTOR, '[data-test-id="not-found-search-page-vkads"]')
    CARD_AUTHORIZATION = (By.CSS_SELECTOR, '[href="/help/categories/authorization"]')
    CARD_GENERAL = (By.CSS_SELECTOR, '[href="/help/categories/general"]')

    TITLE_ARTICLES = (By.CSS_SELECTOR, '[data-test-id="summary-title-ads"]')
    LIST_ARTICLES = (By.CSS_SELECTOR, '[data-test-id="category-page-articles-list-ads"]')
    SIDEBAR_ARTICLES = (By.CSS_SELECTOR, '[data-test-id="layout-sidebar-vkads"]')
    SEARCH_IN_SIDEBAR_ARTICLES = (By.XPATH, './/input')
    CATEGORIES_IN_SIDEBAR_ARTICLES = (By.CSS_SELECTOR, '[data-test-id="navigation-help-sidebar-ads"]')
