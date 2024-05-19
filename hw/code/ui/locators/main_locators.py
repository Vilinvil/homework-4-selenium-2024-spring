from selenium.webdriver.common.by import By


class SidebarLocators:
    BUTTON_OVERVIEW = (By.CSS_SELECTOR, '[data-entityid="overview"]')
    SIGN_OPENING_OVERVIEW = (By.ID, 'overview')

    BUTTON_CAMPAIGN = (By.CSS_SELECTOR, '[data-entityid="dashboardV2"]')
    SIGN_OPENING_CAMPAIGN = (By.ID, 'dashboardV2')

    BUTTON_AUDIENCE = (By.CSS_SELECTOR, '[data-entityid="audience"]')
    SIGN_OPENING_AUDIENCE = (By.ID, 'audience')

    BUTTON_BUDGET = (By.CSS_SELECTOR, '[data-entityid="budget"]')
    SIGN_OPENING_BUDGET = (By.ID, 'budget')

    BUTTON_TRAINING = (By.CSS_SELECTOR, '[data-entityid="onboarding"]')
    SIGN_OPENING_TRAINING = (By.XPATH, '//*[contains(@class, "ModalRoot_componentWrapper")]'
                                       '//*[contains(text(), "С чего начнём обучение?")]')

    BUTTON_CATALOGS = (By.CSS_SELECTOR, '[data-entityid="catalogs"]')
    SIGN_OPENING_CATALOGS = (By.ID, 'catalogs')

    BUTTON_SITES = (By.CSS_SELECTOR, '[data-entityid="pixels"]')
    SIGN_OPENING_SITES = (By.ID, 'pixels')

    BUTTON_MOBILE_APPS = (By.CSS_SELECTOR, '[data-entityid="mobApps"]')
    SIGN_OPENING_MOBILE_APPS = (By.ID, 'mobApps')

    BUTTON_LEADS = (By.CSS_SELECTOR, '[data-entityid="leadads"]')
    SIGN_OPENING_LEADS = (By.ID, 'leadads')

    BUTTON_SETTINGS = (By.CSS_SELECTOR, '[data-entityid="settings"]')
    SIGN_OPENING_SETTINGS = (By.ID, 'settings')

    BUTTON_HELP = (By.XPATH, '//*[contains(@class, "sidebar_portalMenuTrigger")]')
    BUTTON_HELP_CASES = (By.CSS_SELECTOR, '[href="https://ads.vk.com/cases"]')
    BUTTON_HELP_HELP = (By.CSS_SELECTOR, '[href="https://ads.vk.com/help"]')
    BUTTON_HELP_IDEAS = (By.CSS_SELECTOR, '[href="https://ads.vk.com/upvote"]')
    BUTTON_HELP_QUESTION = (By.XPATH, '//*[contains(@class, "Tooltip_tooltipContainer")]'
                                      '//*[@role="button"]//*[contains(text(), "Задать вопрос")]')
    SIGN_OPENING_HELP_QUESTION = (By.XPATH, '//iframe[contains(@src, "https://id.vk.com/messenger")]')

    BUTTON_TOGGLE = (By.XPATH, '//*[contains(@class, "sidebar_toggleButton")]')
    SIGN_TOGGLE = (By.XPATH, '//*[contains(@class, "layout_sidebarShort")]')


class MainPageLocators:
    sidebar_locators = SidebarLocators()

