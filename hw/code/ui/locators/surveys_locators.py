from selenium.webdriver.common.by import By


class SurveysLocators:
    @staticmethod
    def CHANGE_SURVEY(name):
        return By.XPATH, f'//div[text()="{name}"]'

    TO_SURVEYS = (By.XPATH, '//span[text()="Опросы"]')
    BUTTON_CREATE_SURVEYS = (By.XPATH, '//span[text()="Создать опрос"]')

    INPUT_NAME = (By.XPATH, '//input[@placeholder="Введите название"]')
    INPUT_COMPANY_NAME = (By.XPATH, '//input[@placeholder="Введите название компании"]')
    INPUT_SURVEYS_HEADER = (By.XPATH, '//input[@placeholder="Введите заголовок"]')
    INPUT_SURVEYS_DESCRIPTION = (By.XPATH, '//textarea[@placeholder="Введите описание опроса"]')
    BUTTON_LOAD_IMAGE = (By.XPATH, '//span[text()="Загрузить логотип"]')

    BUTTON_TO_QUESTIONS = (By.XPATH, '//span[text()="Вопросы"]')
    BUTTON_LOAD_MEDIAFILES = (By.XPATH, '//span[text()="Загрузите медиафайлы"]')
    FILE_INPUT_LOCATOR = (By.XPATH, '//input[@type="file"]')
    LOGO_IMG = (By.XPATH, '//div[contains(@class, "TitleBlock-module_appLogo__HXtKt")]')
    MODAL_VIEW_TRAINING = (By.XPATH, '//*[text()="Хотите пройти обучение?"]')
    CHOOSE_NO = (By.XPATH, '//*[text()="Не сейчас"]')

    @staticmethod
    def CHOOSE_IMAGE(i=1):
        return By.XPATH, f'(//div[contains(@class, "ImageItems_imageItem__jdlt3")])[{i}]'

    @staticmethod
    def SURVEYS_COMPANY_NAME(name):
        return By.XPATH, f'//span[text()="{name}"]'

    @staticmethod
    def SURVEYS_HEADER(header):
        return By.XPATH, f'//h2[text()="{header}"]'

    @staticmethod
    def SURVEYS_DESCRIPTION(desc):
        return By.XPATH, f'//h4[text()="{desc}"]'

    """index starts from 1"""

    @staticmethod
    def INPUT_QUESTION_TEXT(i=1):
        return By.XPATH, f'(//textarea[@placeholder="Текст вопроса"])[{i}]'

    """index starts from 1"""

    @staticmethod
    def INPUT_ANSWER(i=1):
        return By.XPATH, f'(//input[@placeholder="Введите ответ"])[{i}]'

    """index starts from 1"""

    @staticmethod
    def BUTTON_ADD_ANSWER(i=1):
        return By.XPATH, f'(//span[text()="Добавить вариант"])[{i}]'

    @staticmethod
    def BUTTON_ADD_CONDITION(i=1):
        return By.XPATH, f'(//button[contains(@class, "Question_conditionButton__pjBTk")])[{i}]'

    BUTTON_ADD_QUESTION = (By.XPATH, '//span[text()="Добавить вопрос"]')
    BUTTON_ADD_STOP_VIEW = (By.XPATH, '//span[text()="Добавить стоп-экран"]')

    @staticmethod
    def SPAN_CONDITION_OPTION_ANSWER(answer):
        return By.XPATH, f'//span[text()="{answer}"]'

    @staticmethod
    def SELECT_QUESTION(i=1):
        return By.XPATH, f'(//div[contains(@class, "vkuiCustomSelectInput__container")])[{i}]'

    @staticmethod
    def SELECT_ANSWER(i=1):
        return By.XPATH, '//input[@placeholder="Введите название"]'

    @staticmethod
    def SELECT_ANSWER_FOR_STOP_VIEW(i=1):
        return By.XPATH, f'(//input[@placeholder="содержит любой из"])[{i}]'

    INPUT_QUESTION_STOP_VIEW = (By.XPATH, '//input[@placeholder="Выбрать"]')

    @staticmethod
    def CHOOSE_ANSWER(i=1):
        return By.XPATH, f'(//div[contains(@class, "vkuiCustomSelectOption")])[{i}]'

    @staticmethod
    def CHOOSE_ANSWER_STOP_VIEW(answer_text):
        return (By.XPATH, f'//div[contains(@class, "vkuiCustomSelectOption__children") and text()="{answer_text}"]')

    INPUT_STOP_VIEW_HEADER = (By.XPATH, '//input[@placeholder="Введите заголовок"]')
    INPUT_STOP_VIEW_DESCRIPTION = (By.XPATH, '//input[@placeholder="Введите описание опроса"]')
    SURVEY_QUESTION_BLOCK = (By.XPATH, '//div[contains(@class, "SurveyQuestion-module_wrapper__L3nHm")]')

    @staticmethod
    def QUESTION_TEXT():
        return (By.XPATH, '(.//div[contains(@class, "SurveyQuestion-module_title__gwlrn")])')

    @staticmethod
    def QUESTION_ANSWER(i=1):
        return By.XPATH, f'(.//span[contains(@class, "vkuiText")])[{i}]'

    BUTTON_TO_RESULT = (By.XPATH, '//span[text()="Результат"]')
    INPUT_END_HEADER = (By.XPATH, '//input[@placeholder="Введите заголовок"]')
    INPUT_END_DESCRIPTION = (
        By.XPATH, '//input[@placeholder="Введите описание: например, поблагодарите за прохождение опроса"]')
    SURVEYS_SUCCESS_BLOCK = (By.XPATH, '//div[contains(@class, "Success-module_placeholder__zvamT")]')

    @staticmethod
    def RESULT_HEADER():
        return By.XPATH, './/h2'

    @staticmethod
    def RESULT_DESCRIPTION():
        return By.XPATH, './/h4'

    BUTTON_START_SURVEY = (By.XPATH, '//span[text()="Запустить опрос"]')

    @staticmethod
    def QUESTION_ANSWER_REMOVABLE_CHIP(i=1):
        return By.XPATH, f'(//div[contains(@class, "vkuiChip--removable")])[{i}]'

    INPUT = By.XPATH, './/input[]'

    @staticmethod
    def DESIGN_MESSAGE_ERROR(i):
        return By.XPATH, f'(//div[text()="Обязательное поле"])[{i}]'

    @staticmethod
    def QUESTIONS_MESSAGE_ERROR(i):
        return By.XPATH, f'(//span[text()="Вопрос должен быть не пустым и содержать минимум 2 ответа"])[{i}]'

    BUTTON_ADD_LINK = (By.XPATH, '//span[text()="Добавить ссылку"]')

    INPUT_ADD_LINK = (By.XPATH, '//input[@placeholder="Введите ссылку"]')

    LINK_ERROR_MESSAGE = (By.XPATH, '//div[text()="Необходимо указать протокол http(s)"]')
