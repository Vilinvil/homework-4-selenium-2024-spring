from selenium.webdriver.common.by import By


class BasePageLocators:
    NAV_BUTTON_HELP = (By.XPATH, '//*[@data-test-id="header-test-id:dark"]//*[@href="/help"]')
    NAV_BUTTON_MONETIZATION = (By.XPATH, '//*[@data-test-id="header-test-id:dark"]//*[@href="/partner"]')
    NAV_BUTTON_IDEAS = (By.XPATH, '//*[@data-test-id="header-test-id:dark"]//*[@href="/upvote"]')
    NAV_BUTTON_CASES = (By.XPATH, '//*[@data-test-id="header-test-id:dark"]//*[@href="/cases"]')
    NAV_BUTTON_NEWS = (By.XPATH, '//*[@data-test-id="header-test-id:dark"]//*[@href="/news"]')
    NAV_ICON_ADS_VK = (By.XPATH, '//*[@data-test-id="header-test-id:dark"]//*[@href="/"]')
    BUTTON_CABINET_LOCATOR = (By.CSS_SELECTOR, '[href="/hq?ref=main_landing"]')

    NAV_WRAPPER_EDUCATION = (By.XPATH, '//*[starts-with(@class, "NavigationVKAds_hasChildren")]')
    BUTTON_INSIGHTS = (By.CSS_SELECTOR, '[href="/insights"]')
    BUTTON_EVENTS = (By.CSS_SELECTOR, '[href="/events"]')
    BUTTON_VIDEO_COURSES = (By.CSS_SELECTOR, '[href="https://expert.vk.com/catalog/courses/"]')
    BUTTON_CERTIFICATION = (By.CSS_SELECTOR, '[href="https://expert.vk.com/certification/"]')

