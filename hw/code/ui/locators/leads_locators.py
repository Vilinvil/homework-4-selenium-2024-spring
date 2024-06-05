from selenium.webdriver.common.by import By


class LeadsPageLocators:
    BUTTON_CREATE_LEAD_FORM = (By.CSS_SELECTOR, '[test-id="create-leadform-button"]')
    INPUT_LEAD_NAME = (By.XPATH, '//*[contains(@class, "ModalSidebarPage_container")]'
                                 '//*[contains(text(), "Название лид-формы")]//..//input')
