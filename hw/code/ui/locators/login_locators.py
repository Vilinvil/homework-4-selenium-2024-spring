from selenium.webdriver.common.by import By


class LoginPageLocators:
    BUTTON_MAILRU_AUTH_LOCATOR = (By.CSS_SELECTOR, '[data-test-id="oAuthService_mail_ru"]')
    INPUT_EMAIL_LOCATOR = (By.NAME, 'username')
    BUTTON_NEXT_LOCATOR = (By.CSS_SELECTOR, '[data-test-id="next-button"]')
    INPUT_PASSWORD_LOCATOR = (By.NAME, 'password')
    BUTTON_SUBMIT_LOCATOR = (By.CSS_SELECTOR, '[data-test-id="submit-button"]')
