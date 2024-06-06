from selenium.webdriver.common.by import By


class LeadsPageDesignLocators:
    HEADER = (By.XPATH, '//*[contains(@class, "ModalSidebarPage_header")]//*[contains(text(), "Новая лид-форма")]')
    INPUT_LEAD_NAME = (By.CSS_SELECTOR, '[placeholder="Название лид-формы"]')
    BUTTON_SET_GLOBAL_IMAGE = (By.CSS_SELECTOR, '[data-testid="set-global-image"]')
    INPUT_ORGANIZATION = (By.CSS_SELECTOR, '[placeholder="Название компании"]')
    RADIOGROUP_FIRST_SCREEN = (By.XPATH, '//*[contains(@class, "ModalSidebarPage_container")]'
                                         '//*[contains(text(), "Первый экран формы")]//..//*[@role="radiogroup"]')
    INPUT_TITLE = (By.CSS_SELECTOR, '[placeholder="Текст заголовка"]')
    INPUT_SHORT_DESCRIPTION = (By.CSS_SELECTOR, '[placeholder="Краткое описание опроса"]')
    PIPETTE_CHOICE_GRADIENT = (By.CSS_SELECTOR, '[data-id="101"]')
    BUTTON_SET_MAIN_IMAGE = (By.CSS_SELECTOR, '[data-testid="set-main-image"]')

    PREVIEW_CONTAINER = (By.XPATH, '//*[contains(@class, "CreateLeadFormModal_previewContainer")]')
    PREVIEW_TITLE_CONTACT_DETAILS = By.XPATH, (f'//*[contains(@class, "CreateLeadFormModal_previewContainer")]'
                                               '//h3[contains(text(), "Введите свои контактные данные")]')
    MEDIA_HEADER = (By.XPATH, '//*[contains(@class, "ModalSidebarPage_container")]//*[contains(text(), "Медиатека")]')
    MEDIA_UPLOAD = (By.XPATH, '//*[contains(@class, "ModalSidebarPage_container")]'
                              '//*[contains(@class, "LocalFileSelector_container")]')
    MEDIA_DEFAULT_IMAGE = (By.XPATH, '//*[contains(@class, "ModalSidebarPage_container")]'
                                     '//*[contains(@class, "ImageItems_imageItem")]')
    PREVIEW_LOGO = (By.XPATH, '//*[contains(@class, "CreateLeadFormModal_previewContainer")]'
                              '//*[contains(@class, "TopPart-module_appLogo")]')
    PREVIEW_TOP_PART_TITLE = (By.XPATH, '//*[contains(@class, "TopPart-module_companyTitle")]')

    RADIOGROUP_BUTTON_MORE_TEXT = (By.XPATH, '//*[contains(@class, "vkuiSegmentedControlOption")]'
                                             '//*[contains(text(), "Больше текста")]')
    INPUT_MORE_TEXT = (By.CSS_SELECTOR, '[placeholder="Расскажите о вашем опросе или предложении"]')

    def HEADER_LEAD_FORM_TITLE(self, title):
        return By.XPATH, f'//*[contains(@class, "OnePageContentBlock-module_wrap")]//h2[contains(text(), "{title}")]'


class LeadsPageLocators:
    BUTTON_CREATE_LEAD_FORM = (By.CSS_SELECTOR, '[test-id="create-leadform-button"]')
    BUTTON_CANCEL = (By.CSS_SELECTOR, '[data-testid="cancel"]')
    BUTTON_SUBMIT = (By.CSS_SELECTOR, '[data-testid="submit"]')
