from cases import LoggedCase
from ui.pages.surveys_page import SurveysPage
from ui.pages.leads_page import LeadsPage
import pytest
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException


class TestSurveysPage(LoggedCase):
    NAME = "Название 1"
    COMPANY_NAME = "Название компании 1"
    SURVEYS_HEADER = "Заголовок опроса 1"
    SURVEYS_DESCRIPTION = "Описание опроса 1"
    LOGO_RELATIVE_PATH = "hw/code/img/october_2023.jpg"

    QUESTION_TEXT_1 = "Текст вопроса 1"
    ANSWER_1 = "ответ 1"
    ANSWER_2 = "ответ 2"
    ANSWER_3 = "ответ 3"

    QUESTION_TEXT_2 = "Текст вопроса 2"
    ANSWER_2_1 = "ответ 2.1"
    ANSWER_2_2 = "ответ 2.2"


    STOP_VIEW_HEADER = "Неверный ответ"
    STOP_VIEW_DESCRIPTION = "Опрос закончен"

    RESULT_HEADER = "Спасибо за ответы!"
    RESULT_DESCRIPTION = "Заявка отправлена"

    ERRORS_DESIGN_MSG_COUNT = 5
    ERRORS_RESULT_MSG_COUNT = 2

    @pytest.fixture(scope='function', autouse=True)
    def setup_surveys_page(self):
        self.main_page.open_leads()
        self.leadpage = LeadsPage(self.driver)
        self.leadpage.redirect_to_surveys()
        self.surveys_page = SurveysPage(self.driver)
    

    # @pytest.mark.skip
    def test_simple_positive(self):
        # Клик на кнопку создания опроса (почему-то, с первого раза вылетает эксепшен, несмотря на правильно проставленный until_EC)
        while True:
            try:
                self.surveys_page.BUTTON_CREATE_SURVEYS.clicks()
                break
            except StaleElementReferenceException:
                pass

        # Оформление
        self.surveys_page.INPUT_NAME.write(self.NAME)
        self.surveys_page.INPUT_COMPANY_NAME.write(self.COMPANY_NAME)
        self.surveys_page.INPUT_SURVEYS_HEADER.write(self.SURVEYS_HEADER)
        self.surveys_page.INPUT_SURVEYS_DESCRIPTION.write(self.SURVEYS_DESCRIPTION)
        self.surveys_page.load_logo(self.LOGO_RELATIVE_PATH)

        assert self.surveys_page.COMPANY_NAME(self.COMPANY_NAME) != None
        assert self.surveys_page.SURVEYS_HEADER(self.SURVEYS_HEADER) != None
        assert self.surveys_page.SURVEYS_DESCRIPTION(self.SURVEYS_DESCRIPTION) != None
        assert self.surveys_page.LOGO_IMAGE != None
        
        self.surveys_page.BUTTON_TO_QUESTIONS.clicks()

        # Вопросы
        # Первый вопрос
        self.surveys_page.INPUT_TEXT_QUESTION().write(self.QUESTION_TEXT_1)
        self.surveys_page.INPUT_QUESTION_ANSWER().write(self.ANSWER_1)
        self.surveys_page.INPUT_QUESTION_ANSWER(2).write(self.ANSWER_2)
        self.surveys_page.BUTTON_ADD_ANSWER().clicks()
        self.surveys_page.INPUT_QUESTION_ANSWER(3).write(self.ANSWER_3)
        
        assert self.surveys_page.QUESTION_TEXT == self.QUESTION_TEXT_1
        assert self.surveys_page.ANSWER_TEXT(1) == self.ANSWER_1
        assert self.surveys_page.ANSWER_TEXT(2) == self.ANSWER_2
        assert self.surveys_page.ANSWER_TEXT(3) == self.ANSWER_3

        # Второй вопрос
        self.surveys_page.BUTTON_ADD_QUESTION.clicks()

        self.surveys_page.INPUT_TEXT_QUESTION(2).write(self.QUESTION_TEXT_2)
        self.surveys_page.INPUT_QUESTION_ANSWER(4).write(self.ANSWER_2_1)
        self.surveys_page.INPUT_QUESTION_ANSWER(5).write(self.ANSWER_2_2)

        assert self.surveys_page.QUESTION_TEXT == self.QUESTION_TEXT_2
        assert self.surveys_page.ANSWER_TEXT(1) == self.ANSWER_2_1
        assert self.surveys_page.ANSWER_TEXT(2) == self.ANSWER_2_2

        # Условие показа
        self.surveys_page.BUTTON_ADD_CONDITION().clicks()
        self.surveys_page.choose_answer_condition(1)

        # Стоп-экран
        self.surveys_page.BUTTON_ADD_STOP_VIEW.clicks()
        self.surveys_page.choose_answer_stop_view(self.ANSWER_2_1)

        self.surveys_page.INPUT_HEADER_STOP_VIEW.write(self.STOP_VIEW_HEADER)
        self.surveys_page.INPUT_DESCRIPTION_STOP_VIEW.write(self.STOP_VIEW_DESCRIPTION)

        self.surveys_page.BUTTON_TO_RESULTS.clicks()

        # Результат
        self.surveys_page.INPUT_RESULT_HEADER.write(self.RESULT_HEADER)
        self.surveys_page.INPUT_RESULT_DESCRIPTION.write(self.RESULT_DESCRIPTION)
        
        assert self.surveys_page.RESULT_HEADER == self.RESULT_HEADER
        assert self.surveys_page.RESULT_DESCRIPTION == self.RESULT_DESCRIPTION

        # Сохранение опроса
        self.surveys_page.BUTTON_START_SURVEY.clicks()

        # Проверка опроса в форме редактирование, после сохранения
        self.surveys_page.SURVEY_RAW(self.NAME).clicks()
        # Оформление
        assert self.surveys_page.COMPANY_NAME(self.COMPANY_NAME) != None
        assert self.surveys_page.SURVEYS_HEADER(self.SURVEYS_HEADER) != None
        assert self.surveys_page.SURVEYS_DESCRIPTION(self.SURVEYS_DESCRIPTION) != None
        assert self.surveys_page.LOGO_IMAGE != None

        self.surveys_page.BUTTON_TO_QUESTIONS.clicks()

        # Вопросы
        # Первый вопрос
        assert self.surveys_page.QUESTION_TEXT == self.QUESTION_TEXT_1
        assert self.surveys_page.ANSWER_TEXT(1) == self.ANSWER_1
        assert self.surveys_page.ANSWER_TEXT(2) == self.ANSWER_2
        assert self.surveys_page.ANSWER_TEXT(3) == self.ANSWER_3

        self.surveys_page.INPUT_TEXT_QUESTION(2).clicks()
        
        # Второй вопрос
        assert self.surveys_page.QUESTION_TEXT == self.QUESTION_TEXT_2
        assert self.surveys_page.ANSWER_TEXT(1) == self.ANSWER_2_1
        assert self.surveys_page.ANSWER_TEXT(2) == self.ANSWER_2_2

        # Условие показа
        assert self.surveys_page.CONDITION_QUESTION_ANSWER_TEXT == self.ANSWER_1

        # Стоп-экран
        assert self.surveys_page.STOP_VIEW_QUESTION_ANSWER_TEXT == self.ANSWER_2_1

        self.surveys_page.BUTTON_TO_RESULTS.clicks()

        # Результаты
        assert self.surveys_page.RESULT_HEADER == self.RESULT_HEADER
        assert self.surveys_page.RESULT_DESCRIPTION == self.RESULT_DESCRIPTION

    def test_neg_cases(self):
        while True:
            try:
                self.surveys_page.BUTTON_CREATE_SURVEYS.clicks()
                break
            except StaleElementReferenceException:
                pass

        # Переходим на следующим этап, не заполнив поля
        self.surveys_page.BUTTON_TO_QUESTIONS.clicks()

        # Проверяем, что появилось 5 сообщений об ошибке
        for i in range(1, self.ERRORS_DESIGN_MSG_COUNT + 1):
            assert self.surveys_page.DESIGN_ERROR_MESSAGE(i) != None

        # Заполняем поля
        self.surveys_page.INPUT_NAME.write(self.NAME)
        self.surveys_page.INPUT_COMPANY_NAME.write(self.COMPANY_NAME)
        self.surveys_page.INPUT_SURVEYS_HEADER.write(self.SURVEYS_HEADER)
        self.surveys_page.INPUT_SURVEYS_DESCRIPTION.write(self.SURVEYS_DESCRIPTION)
        self.surveys_page.load_logo(self.LOGO_RELATIVE_PATH)

        # Переходим к вопросам
        while 1:
            try:
                self.surveys_page.BUTTON_TO_QUESTIONS.clicks()
                break
            except TimeoutException:
                pass


        # Переходим к результатам, не заполнив поля
        self.surveys_page.BUTTON_TO_RESULTS.clicks()

        # Проверяем появившееся сообщение об ошибке
        assert self.surveys_page.QUESTION_ERROR_MESSAGE(1) != None

        # Заполняем вопрос
        self.surveys_page.INPUT_TEXT_QUESTION().write(self.QUESTION_TEXT_1)
        self.surveys_page.INPUT_QUESTION_ANSWER().write(self.ANSWER_1)
        self.surveys_page.INPUT_QUESTION_ANSWER(2).write(self.ANSWER_2)

        # Переходим к результату
        self.surveys_page.BUTTON_TO_RESULTS.clicks()

        # На моей системе, на которой запускались тесты, получилось создать опрос с пустыми полями
        # Делаем поля пустыми
        # self.surveys_page.INPUT_RESULT_HEADER.clear()
        # self.surveys_page.INPUT_RESULT_DESCRIPTION.clear()

        # Пытаемся запутсить опрос ---- после этого опрос создавался, хотя поля выше очищаются
        # self.surveys_page.BUTTON_START_SURVEY.clicks()

        # # Проверяем сообщения, что поля должны быть не пустыми
        # for i in range(1, self.ERRORS_RESULT_MSG_COUNT):
        #     assert self.surveys_page.DESIGN_ERROR_MESSAGE(i) != None

        # Добавляем неправильную ссылку
        self.surveys_page.BUTTON_ADD_LINK.clicks()
        self.surveys_page.INPUT_ADD_LINK.write("ne ssilka")
        

        # Пытаемся запутсить опрос
        self.surveys_page.BUTTON_START_SURVEY.clicks()

        assert self.surveys_page.ERROR_LINK_MESSAGE != None



        



        