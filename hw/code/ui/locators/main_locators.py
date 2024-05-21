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
    SIGN_OPENING_HELP = (By.XPATH, '//*[contains(@class, "Tooltip_tooltipContainer")]'
                                   '//*[@href="https://ads.vk.com/cases"]')
    BUTTON_HELP_CASES = (By.CSS_SELECTOR, '[href="https://ads.vk.com/cases"]')
    BUTTON_HELP_HELP = (By.CSS_SELECTOR, '[href="https://ads.vk.com/help"]')
    BUTTON_HELP_IDEAS = (By.CSS_SELECTOR, '[href="https://ads.vk.com/upvote"]')
    BUTTON_HELP_QUESTION = (By.XPATH, '//*[contains(@class, "Tooltip_tooltipContainer")]'
                                      '//*[@role="button"]//*[contains(text(), "Задать вопрос")]')
    SIGN_OPENING_HELP_QUESTION = (By.XPATH, '//iframe[contains(@src, "https://id.vk.com/messenger")] |'
                                            ' //*[contains(@class, "vkuiModalPage__header")]'
                                            '//*[contains(text(), "Служба заботы")]')

    BUTTON_TOGGLE = (By.XPATH, '//*[contains(@class, "sidebar_toggleButton")]')
    SIGN_TOGGLE = (By.XPATH, '//*[contains(@class, "layout_sidebarShort")]')


class NavBarLocators:
    ADS_LOGO = (By.XPATH, '//*[contains(@class, "header_left")]//img[@alt="Logo"]')

    BUTTON_ACCOUNT_SWITCH = (By.XPATH, '//*[contains(@class, "AccountSwitch_changeAccount")]')
    SIGN_OPENING_ACCOUNT_SWITCH = (By.XPATH, '//*[contains(@class, "AccountSwitch_accountsDropdown")]')

    BUTTON_BALANCE = (By.XPATH, '//*[contains(@class, "balance_balanceWithAction")]')
    SIGN_OPENING_BALANCE = (By.XPATH, '//*[contains(@class, "CreateInvoiceModal")]')

    BUTTON_NOTIFICATIONS = (By.XPATH, '//*[contains(@class, "header_bellNotifications")]')
    SIGN_OPENING_NOTIFICATIONS = (By.XPATH, '//*[contains(@class, "BellNotificationsContent")]')

    BUTTON_USER_MENU = (By.XPATH, '//*[contains(@class, "userMenu")]')
    BUTTON_USER_MENU_ACCOUNT = (By.CSS_SELECTOR, '[href="https://id.vk.com/account"]')
    SIGN_OPENING_USER_MENU = BUTTON_USER_MENU_ACCOUNT
    BUTTON_USER_MENU_LOGOUT = (By.XPATH, '//*[contains(@class, "vkuiPopper")]'
                                         '//*[@role="button"]//*[contains(text(), "Выйти")]')


class MainPageLocators:
    sidebar_locators = SidebarLocators()
    navbar_locators = NavBarLocators()
