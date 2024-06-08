from selenium.webdriver.common.by import By


class LeadsPageDesignLocators:
    HEADER = (By.XPATH, '//*[contains(@class, "ModalSidebarPage_header")]//*[contains(text(), "Новая лид-форма")]')
    INPUT_LEAD_NAME = (By.CSS_SELECTOR, '[placeholder="Название лид-формы"]')
    BUTTON_SET_GLOBAL_IMAGE = (By.CSS_SELECTOR, '[data-testid="set-global-image"]')
    INPUT_ORGANIZATION = (By.CSS_SELECTOR, '[placeholder="Название компании"]')

    RADIOGROUP_FIRST_SCREEN = (By.XPATH, '//*[contains(@class, "ModalSidebarPage_container")]'
                                         '//*[contains(text(), "Первый экран формы")]//..//*[@role="radiogroup"]')
    RADIOGROUP_BUTTON_MORE_TEXT = (By.XPATH, '//*[contains(@class, "vkuiSegmentedControlOption")]'
                                             '//*[contains(text(), "Больше текста")]',)

    INPUT_TITLE = (By.CSS_SELECTOR, '[placeholder="Текст заголовка"]')
    INPUT_SHORT_DESCRIPTION = (By.CSS_SELECTOR, '[placeholder="Краткое описание опроса"]')

    PIPETTE_CHOICE_GRADIENT = (By.CSS_SELECTOR, '[data-id="101"]')
    PIPETTE_INPUT_GRADIENT = (By.XPATH, '//*[contains(@class, "ColorMap_actions")]//input')
    PIPETTE_BUTTON_SUBMIT = (By.XPATH, '//*[contains(@class, "ColorMap_actions")]//button')
    PIPETTE_GRADIENT_RESULT = (By.XPATH, '//*[contains(@class, "ActionButtons-module_goNext")]')

    BUTTON_SET_MAIN_IMAGE = (By.CSS_SELECTOR, '[data-testid="set-main-image"]')

    PREVIEW_CONTAINER = (By.XPATH, '//*[contains(@class, "CreateLeadFormModal_previewContainer")]')
    PREVIEW_TITLE_CONTACT_DETAILS = By.XPATH, (f'//*[contains(@class, "CreateLeadFormModal_previewContainer")]'
                                               '//h3[contains(text(), "Введите свои контактные данные")]')
    PREVIEW_LOGO = (By.XPATH, '//*[contains(@class, "CreateLeadFormModal_previewContainer")]'
                              '//*[contains(@class, "TopPart-module_appLogo")]')
    PREVIEW_TOP_PART_TITLE = (By.XPATH, '//*[contains(@class, "TopPart-module_companyTitle")]')

    MEDIA_HEADER = (By.XPATH, '//*[contains(@class, "ModalSidebarPage_container")]//*[contains(text(), "Медиатека")]')
    MEDIA_UPLOAD = (By.XPATH, '//*[contains(@class, "ModalSidebarPage_container")]'
                              '//*[contains(@class, "LocalFileSelector_container")]')
    MEDIA_DEFAULT_IMAGE = (By.XPATH, '//*[contains(@class, "ModalSidebarPage_container")]'
                                     '//*[contains(@class, "ImageItems_imageItem")]')

    INPUT_MORE_TEXT = (By.CSS_SELECTOR, '[placeholder="Расскажите о вашем опросе или предложении"]')

    @staticmethod
    def PREVIEW_LEAD_FORM_TITLE(title):
        return By.XPATH, f'//*[contains(@class, "OnePageContentBlock-module_wrap")]//h2[contains(text(), "{title}")]'

    PREVIEW_LONG_DESCRIPTION = (By.XPATH, '//*[contains(@class, "LeadForm-module_long_description")]')


class LeadsPageQuestionsLocators:
    TITLE_QUESTION = (By.XPATH, '//*[contains(@class, "ModalSidebarPage_content")]//h4[contains(text(), "Вопросы")]')
    BUTTON_ADD_QUESTION = (By.XPATH, '//*[contains(@class, "ModalSidebarPage_content")]'
                                     '//button//*[contains(text(), "Добавить вопрос")]')

    @staticmethod
    def ADD_QUESTION_CONTAINER(number):
        return By.XPATH, f'//*[contains(@class, "Question_question_") and .//*[contains(text(), "Вопрос № {number}")]]'

    ADD_QUESTION_INPUT_TITLE = (By.XPATH, './/*[@placeholder="Напишите вопрос"]')
    ADD_QUESTION_SELECTOR_TYPE = (By.XPATH, './/*[contains(@class, "HintSelector_hintSelectorButton")]')
    ADD_QUESTION_SELECT_SEVERAL_ANSWERS = (By.XPATH, '//*[contains(@class, "HintSelector_list")]'
                                                     '//*[contains(text(), "Выбор нескольких ответов")]')
    ADD_QUESTION_SELECT_ANY_FORM_ANSWER = (By.XPATH, '//*[contains(@class, "HintSelector_list")]'
                                                     '//*[contains(text(), "Ответ в произвольной форме")]')
    ADD_QUESTION_INPUT_ANSWER = (By.XPATH, './/input[contains(@placeholder, "Введите ответ")]')
    ADD_QUESTION_BUTTON_ADD_ANSWER = (By.XPATH, './/button[.//*[contains(text(), "Добавить ответ")]]')
    ADD_QUESTION_BUTTON_ADD_MORE = (By.XPATH, './/button[contains(@class, "Question_buttonAddMore")]')
    ADD_QUESTION_BUTTON_ADD_MORE_OTHER = (By.XPATH, '//*[contains(@class, "Tooltip_tooltipContainer")]'
                                                    '//*[contains(text(), "Другое")]')

    @staticmethod
    def PREVIEW_TITLE_QUESTION(title):
        return By.XPATH, f'//*[contains(@class, "OnePageContentBlock-module_titleWrap") and .//*[contains(text(), "{title}")]]'

    @staticmethod
    def PREVIEW_QUESTION_BY_TITLE(title):
        return By.XPATH, f'//*[contains(@class, "OnePageContentBlock-module_wrap") and .//*[contains(text(), "{title}")]]'

    PREVIEW_ANSWERS_SIGN_RADIOGROUP = (By.XPATH, './/*[contains(@class, "vkuiRadioGroup")]')
    PREVIEW_ANSWERS_SIGN_CHECKBOX = (By.XPATH, './/*[contains(@class, "vkuiCheckbox")]')
    PREVIEW_ANSWERS_SIGN_ANY_FORM = (By.XPATH, './/*[contains(@placeholder, "Введите текст")]')

    @staticmethod
    def CHECKBOX_CONTENT(text):
        return By.XPATH, f'.//*[contains(@class, "vkuiCheckbox__content") and .//*[contains(text(), "{text}")]]'

    TITLE_CONTACT_INFO = (By.XPATH, '//*[contains(@class, "ModalSidebarPage_content")]'
                                    '//h4[contains(text(), "Контактная информация")]')
    BUTTON_ADD_CONTACT_INFO = (By.XPATH, '//*[contains(@class, "ModalSidebarPage_content")]'
                                         '//button//*[contains(text(), "Добавить контактные данные")]')

    BUTTON_DELETE_CONTACT_INFO_PHONE = (By.CSS_SELECTOR, '[data-id="phone"]')

    MODAL_VIEW_CONTACT_INFO = (By.XPATH, '//*[contains(@class, "ModalRoot_componentWrapper") and '
                                         './/h2[contains(text(), "Контактная информация")]]')
    MODAL_VIEW_CONTACT_INFO_BUTTON_SUBMIT = (By.XPATH, './/button[.//*[contains(text(), "Добавить")]]')

    @staticmethod
    def PREVIEW_ANSWER_CONTACT_INFO(answer):
        return By.XPATH, f'.//*[contains(@placeholder, "{answer}")]'


class LeadsPageResultLocators:
    HEADER_RESULT = (By.XPATH, '//*[contains(@class, "ModalSidebarPage_content")]'
                               '//*[contains(@class, "vkuiInternalGroup")]//*[contains(text(), "Результат")]')
    INPUT_TITLE = (By.XPATH, '//*[contains(@class, "ModalSidebarPage_content")]'
                             '//*[contains(@class, "vkuiFormItem") and .//*[contains(text(), "Заголовок")]]//input')
    INPUT_DESCRIPTION = (By.XPATH, '//*[contains(@class, "ModalSidebarPage_content")]'
                                   '//*[contains(@class, "vkuiFormItem") and'
                                   ' .//*[contains(text(), "Описание")]]//input')
    INPUT_SITE = (By.XPATH, '//*[contains(@class, "ModalSidebarPage_content")]'
                            '//*[contains(@class, "vkuiFormItem") and'
                            ' .//*[contains(text(), "Ссылка на сайт")]]//input')
    INPUT_PROMO_CODE = (By.XPATH, '//*[contains(@class, "ModalSidebarPage_content")]'
                                  '//*[contains(@class, "vkuiFormItem") and'
                                  ' .//*[contains(text(), "Промокод")]]//input')
    BUTTON_ADD_SITE = (By.CSS_SELECTOR, '[data-testid="add-site-btn"]')
    BUTTON_ADD_PHONE = (By.CSS_SELECTOR, '[data-testid="add-phone-btn"]')
    BUTTON_ADD_PROMO_CODE = (By.CSS_SELECTOR, '[data-testid="add-promo-code-btn"]')

    @staticmethod
    def PREVIEW_TEXT(text):
        return By.XPATH, (f'//*[contains(@class, "CreateLeadFormModal_preview")]'
                          f'//*[contains(@class, "FormPanel-module_formContent")]//*[contains(text(), "{text}")]')

    @staticmethod
    def PREVIEW_SITE(url):
        return By.XPATH, (f'//*[contains(@class, "CreateLeadFormModal_preview")]'
                          f'//*[contains(@class, "ActionButtons-module_actionBlock")]//*[contains(@href, "{url}")]')

    @staticmethod
    def PREVIEW_PROMO_CODE(promo_code):
        return By.XPATH, (f'//*[contains(@class, "CreateLeadFormModal_preview")]'
                          f'//*[contains(@class, "ActionButtons-module_actionBlock")]'
                          f'//input[contains(@value, "{promo_code}")]')


class LeadsPageSettingsLocators:
    HEADER = (By.XPATH, '//*[contains(@class, "ModalSidebarPage_content")]'
                        '//*[contains(@class, "vkuiInternalGroup")]'
                        '//*[contains(text(), "Настройки лид-формы")]')

    TITLE_NOTIFICATION = (By.XPATH, '//*[contains(@class, "ModalSidebarPage_content")]'
                                    '//*[contains(@class, "vkuiInternalGroup")]'
                                    '//*[contains(text(), "Уведомления")]')

    TITLE_AGREEMENT = (By.XPATH, '//*[contains(@class, "ModalSidebarPage_content")]'
                                 '//*[contains(@class, "vkuiInternalGroup")]'
                                 '//*[contains(text(), "Согласие на обработку персональных данных")]')

    INPUT_FULL_NAME = (By.CSS_SELECTOR, '[placeholder="Введите фамилию, имя и отчество"]')
    INPUT_ADDRESS = (By.CSS_SELECTOR, '[placeholder="Введите адрес"]')
    INPUT_EMAIL = (By.CSS_SELECTOR, '[placeholder="Введите email"]')
    INPUT_INN = (By.CSS_SELECTOR, '[placeholder="Введите ИНН"]')


class LeadsPageLocators:
    BUTTON_CREATE_LEAD_FORM = (By.CSS_SELECTOR, '[test-id="create-leadform-button"]')
    BUTTON_CANCEL = (By.CSS_SELECTOR, '[data-testid="cancel"]')
    BUTTON_SUBMIT = (By.CSS_SELECTOR, '[data-testid="submit"]')

    @staticmethod
    def NAME_LEAD_FORM(name):
        return By.XPATH, (f'//*[contains(@class, "LeadForms_tableContainer")]'
                          f'//*[contains(@class, "NameCell_wrapper") and .//*[contains(text(), "{name}")]]')

    BUTTON_REMOVE_LEAD_FORM = (By.XPATH, './/*[contains(text(), "Удалить")]')
    BUTTON_EDIT_LEAD_FORM = (By.XPATH, './/*[contains(text(), "Редактировать")]')

    HEADER_EDIT = (By.XPATH, ('//*[contains(@class, "ModalSidebarPage_header")]'
                              '//*[contains(text(), "Редактирование лид-формы")]'))
