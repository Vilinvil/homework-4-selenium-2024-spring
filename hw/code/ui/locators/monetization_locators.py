from selenium.webdriver.common.by import By

class MonetizationPageLocators:
    MONETIZATION_FOOTER_LOGO_VK_BUSINESS = (By.XPATH, '//*[starts-with(@class, "PartnerContent_footerLogoImage")]')
    MONETIZATION_FOOTER_BUTTON_RULES = \
        (By.XPATH, '//*[starts-with(@class, "PartnerContent_footer")]//*[@href="/help/articles/partner_rules"]')
    MONETIZATION_FOOTER_BUTTON_MAIN = (By.XPATH, '//*[starts-with(@class, "PartnerContent_footer")]//*[@href="/"]')
    MONETIZATION_FOOTER_BUTTON_HELP = \
        (By.XPATH, '//*[starts-with(@class, "PartnerContent_footer")]//*[contains(text(),"Справка")]')
    MONETIZATION_FOOTER_LANGUAGE_WRAPPER = (By.XPATH, '//*[starts-with(@class, "SelectLanguage_desktopSelect")]')
    MONETIZATION_FOOTER_LANGUAGE_BUTTON_ENGLISH = \
        (By.XPATH, '//*[starts-with(@class, "SelectLanguage_desktopSelect")]//*[contains(text(),"English")]')
    MONETIZATION_FOOTER_LANGUAGE_BUTTON_RUSSIAN = \
        (By.XPATH, '//*[starts-with(@class, "SelectLanguage_desktopSelect")]//*[contains(text(),"Русский")]')