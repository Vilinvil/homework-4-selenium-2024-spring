from selenium.webdriver.common.by import By


class BasePageLocators:
    NAV_BUTTON_HELP = (By.XPATH, '//*[@data-test-id="header-test-id:dark"]//*[@href="/help"]')
    NAV_BUTTON_MONETIZATION = (By.XPATH, '//*[@data-test-id="header-test-id:dark"]//*[@href="/partner"]')
    NAV_BUTTON_IDEAS = (By.XPATH, '//*[@data-test-id="header-test-id:dark"]//*[@href="/upvote"]')
    NAV_BUTTON_CASES = (By.XPATH, '//*[@data-test-id="header-test-id:dark"]//*[@href="/cases"]')
    NAV_BUTTON_NEWS = (By.XPATH, '//*[@data-test-id="header-test-id:dark"]//*[@href="/news"]')
    NAV_ICON_ADS_VK = (By.XPATH, '//*[@data-test-id="header-test-id:dark"]//*[@href="/"]')
    NAV_BUTTON_CABINET_LOCATOR = (By.XPATH, '//*[@data-test-id="header-test-id:dark"]//*[@href="/hq?ref=main_landing&v=1"]')

    NAV_WRAPPER_EDUCATION = (By.XPATH, '//*[contains(@class, "NavigationVKAds_hasChildren")]')
    NAV_WRAPPED_BUTTON_INSIGHTS = (By.CSS_SELECTOR, '[href="/insights"]')
    NAV_WRAPPED_BUTTON_EVENTS = (By.CSS_SELECTOR, '[href="/events"]')
    NAV_WRAPPED_BUTTON_VIDEO_COURSES = (By.CSS_SELECTOR, '[href="https://expert.vk.com/catalog/courses/"]')
    NAV_WRAPPED_BUTTON_CERTIFICATION = (By.CSS_SELECTOR, '[href="https://expert.vk.com/certification/"]')

    FOOTER_LOCATOR = (By.CSS_SELECTOR, '[data-test-id="footer-test-id"]')
    FOOTER_BUTTON_NEWS = (By.XPATH, '//*[@data-test-id="footer-test-id"]//*[@href="/news"]')
    FOOTER_BUTTON_INSIGHTS = (By.XPATH, '//*[@data-test-id="footer-test-id"]//*[@href="/insights"]')
    FOOTER_BUTTON_EVENTS = (By.XPATH, '//*[@data-test-id="footer-test-id"]//*[@href="/events"]')
    FOOTER_BUTTON_DOCUMENTS = (By.XPATH, '//*[@data-test-id="footer-test-id"]//*[@href="/documents"]')
    FOOTER_BUTTON_EXPERTS = (By.XPATH, '//*[@data-test-id="footer-test-id"]//*[contains(text(),"Обучение для бизнеса")]')
    FOOTER_BUTTON_CASES = (By.XPATH, '//*[@data-test-id="footer-test-id"]//*[@href="/cases"]')
    FOOTER_BUTTON_HELP = (By.XPATH, '//*[@data-test-id="footer-test-id"]//*[@href="/help"]')
    FOOTER_BUTTON_MONETIZATION = (By.XPATH, '//*[@data-test-id="footer-test-id"]//*[@href="/partner"]')
    FOOTER_BUTTON_CABINET = (By.XPATH, '//*[@data-test-id="footer-test-id"]//*[@href="/hq?ref=main_landing"]')
    FOOTER_LOGO_VK_BUSINESS = (
        By.XPATH, '//*[@data-test-id="footer-test-id"]//*[@href="https://vk.company/ru/company/business/"]')
    FOOTER_LOGO_VK = (By.XPATH, '//*[@data-test-id="footer-test-id"]//*[@href="https://vk.com/vk_ads"]')
    FOOTER_LOGO_OK = (By.XPATH, '//*[@data-test-id="footer-test-id"]//*[@href="https://ok.ru/group/64279825940712"]')
    FOOTER_LOGO_TG = (By.XPATH, '//*[@data-test-id="footer-test-id"]//*[@href="https://t.me/vk_ads"]')
    FOOTER_ABOUT_COMPANY = (By.XPATH, '//*[contains(@class, "Footer_about")]')
    FOOTER_WRAPPER_LANGUAGE = (By.XPATH, '//*[contains(@class, "SelectLanguage_wrapper")]')
    FOOTER_LANGUAGE_BUTTON_ENGLISH = (
        By.XPATH, '//*[contains(@class,"SelectLanguage_selectElem_") and contains(text(),"English")]')
    FOOTER_LANGUAGE_BUTTON_RUSSIAN = (
        By.XPATH, '//*[contains(@class,"SelectLanguage_selectElem_") and contains(text(),"Русский")]')
