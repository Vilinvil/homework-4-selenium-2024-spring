from ui.pages.base_page_functionality import BasePageFunctionality, add_write, add_clicks
from ui.locators.surveys_locators import SurveysLocators

from selenium.webdriver.support import expected_conditions as EC
from os import path

from selenium.common import TimeoutException


class SurveysPage(BasePageFunctionality):
    url = "https://ads.vk.com/hq/leadads/surveys"
    locators = SurveysLocators()

    @property
    @add_clicks
    def BUTTON_CREATE_SURVEYS(self):
        return self.find_with_check_visibility(self.locators.BUTTON_CREATE_SURVEYS)

    @property
    @add_write
    def INPUT_NAME(self):
        return self.find_with_check_visibility(self.locators.INPUT_NAME)

    @property
    @add_write
    def INPUT_COMPANY_NAME(self):
        return self.find_with_check_visibility(self.locators.INPUT_COMPANY_NAME)

    def COMPANY_NAME(self, name):
        return self.find(self.locators.SURVEYS_COMPANY_NAME(name))

    @property
    @add_write
    def INPUT_SURVEYS_HEADER(self):
        return self.find_with_check_visibility(self.locators.INPUT_SURVEYS_HEADER)

    def SURVEYS_HEADER(self, header):
        return self.find(self.locators.SURVEYS_HEADER(header))

    @property
    @add_write
    def INPUT_SURVEYS_DESCRIPTION(self):
        return self.find_with_check_visibility(self.locators.INPUT_SURVEYS_DESCRIPTION)

    def SURVEYS_DESCRIPTION(self, desc):
        return self.find(self.locators.SURVEYS_DESCRIPTION(desc))

    @property
    @add_clicks
    def BUTTON_TO_QUESTIONS(self):
        return self.find_with_check_visibility(self.locators.BUTTON_TO_QUESTIONS)

    @property
    @add_clicks
    def BUTTON_LOAD_IMAGE(self):
        return self.find_with_check_visibility(self.locators.BUTTON_LOAD_IMAGE)

    @property
    @add_clicks
    def BUTTON_LOAD_MEDIAFILES(self):
        return self.find_with_check_visibility(self.locators.BUTTON_LOAD_MEDIAFILES)

    @property
    @add_clicks
    def CHOOSE_IMAGE(self):
        return self.find(self.locators.CHOOSE_IMAGE())

    @property
    def LOGO_IMAGE(self):
        return self.find_with_check_visibility(self.locators.LOGO_IMG)

    def load_logo(self, filepath):
        self.BUTTON_LOAD_IMAGE.clicks()
        file_input = self.find(self.locators.FILE_INPUT_LOCATOR)
        file_input.send_keys(path.abspath(filepath))
        self.CHOOSE_IMAGE.clicks()

    @add_clicks
    @add_write
    def INPUT_TEXT_QUESTION(self, i=1):
        return self.find_with_check_visibility(self.locators.INPUT_QUESTION_TEXT(i))

    @add_write
    def INPUT_QUESTION_ANSWER(self, i=1):
        return self.find_with_check_visibility(self.locators.INPUT_ANSWER(i))

    @property
    @add_clicks
    def BUTTON_ADD_QUESTION(self):
        return self.find_with_check_visibility(self.locators.BUTTON_ADD_QUESTION)

    @add_clicks
    def BUTTON_ADD_ANSWER(self, i=1):
        return self.find_with_check_visibility(self.locators.BUTTON_ADD_ANSWER(i))

    @property
    def QUESTION_TEXT(self):
        parent = self.find(self.locators.SURVEY_QUESTION_BLOCK)
        return self.find_child(parent, self.locators.QUESTION_TEXT()).text

    def ANSWER_TEXT(self, i=1):
        parent = self.find(self.locators.SURVEY_QUESTION_BLOCK)
        return self.find_child(parent, self.locators.QUESTION_ANSWER(i)).text

    @add_clicks
    def BUTTON_ADD_CONDITION(self, i=1):
        return self.find(self.locators.BUTTON_ADD_CONDITION(i))

    @add_clicks
    def BUTTON_SELECT_ANSWER(self):
        return self.find_with_check_visibility(self.locators.SELECT_ANSWER(1))

    @add_clicks
    def CONDITION_ANSWER_OPTION(self, i=1):
        return self.find(self.locators.CHOOSE_ANSWER(i))

    def choose_answer_condition(self, answer_num=1):
        self.BUTTON_SELECT_ANSWER().clicks()
        self.CONDITION_ANSWER_OPTION(answer_num).clicks()

    @property
    @add_clicks
    def BUTTON_ADD_STOP_VIEW(self):
        return self.find(self.locators.BUTTON_ADD_STOP_VIEW)

    @property
    @add_clicks
    def BUTTON_SELECT_QUESTION_STOP_VIEW(self):
        parent = self.find(self.locators.SELECT_QUESTION(2))
        return self.find_child(parent, self.locators.INPUT)

    @add_clicks
    def QUESTION_OPTION_STOP_VIEW(self, question_num):
        return self.find_with_check_visibility(self.locators.SELECT_QUESTION(question_num))

    def choose_question_stop_view(self, question_num=1):
        self.BUTTON_SELECT_QUESTION_STOP_VIEW.clicks()
        self.QUESTION_OPTION_STOP_VIEW(question_num)

    @property
    @add_clicks
    def BUTTON_SELECT_ANSWER_STOP_VIEW(self):
        return self.find(self.locators.SELECT_ANSWER_FOR_STOP_VIEW())

    @add_clicks
    def ANSWER_OPTION_STOP_VIEW(self, answer_text=""):
        return self.find_with_check_visibility(self.locators.CHOOSE_ANSWER_STOP_VIEW(answer_text))

    def choose_answer_stop_view(self, answer_text):
        self.BUTTON_SELECT_ANSWER_STOP_VIEW.clicks()
        self.ANSWER_OPTION_STOP_VIEW(answer_text=answer_text).clicks()

    @property
    @add_write
    def INPUT_HEADER_STOP_VIEW(self):
        return self.find(self.locators.INPUT_STOP_VIEW_HEADER)

    @property
    @add_write
    def INPUT_DESCRIPTION_STOP_VIEW(self):
        return self.find(self.locators.INPUT_STOP_VIEW_DESCRIPTION)

    @property
    @add_clicks
    def BUTTON_TO_RESULTS(self):
        return self.find(self.locators.BUTTON_TO_RESULT)

    @property
    @add_write
    def INPUT_RESULT_HEADER(self):
        return self.find(self.locators.INPUT_END_HEADER)

    @property
    @add_write
    def INPUT_RESULT_DESCRIPTION(self):
        return self.find(self.locators.INPUT_END_DESCRIPTION)

    @property
    def RESULT_HEADER(self):
        parent = self.find(self.locators.SURVEYS_SUCCESS_BLOCK)
        return self.find_child(parent, self.locators.RESULT_HEADER(), until_EC=EC.visibility_of_element_located).text

    @property
    def RESULT_DESCRIPTION(self):
        parent = self.find(self.locators.SURVEYS_SUCCESS_BLOCK)
        return self.find_child(parent, self.locators.RESULT_DESCRIPTION(),
                               until_EC=EC.visibility_of_element_located).text

    @property
    @add_clicks
    def BUTTON_START_SURVEY(self):
        return self.find(self.locators.BUTTON_START_SURVEY)

    @add_clicks
    def SURVEY_RAW(self, name):
        return self.find_with_check_visibility(self.locators.CHANGE_SURVEY(name))

    @property
    def CONDITION_QUESTION_ANSWER_TEXT(self):
        return self.find_with_check_visibility(self.locators.QUESTION_ANSWER_REMOVABLE_CHIP(1)).text

    @property
    def STOP_VIEW_QUESTION_ANSWER_TEXT(self):
        return self.find_with_check_visibility(self.locators.QUESTION_ANSWER_REMOVABLE_CHIP(2)).text

    def DESIGN_ERROR_MESSAGE(self, i):
        return self.find_with_check_visibility(self.locators.DESIGN_MESSAGE_ERROR(i)).text

    def QUESTION_ERROR_MESSAGE(self, i):
        return self.find_with_check_visibility(self.locators.QUESTIONS_MESSAGE_ERROR(i)).text

    @property
    @add_clicks
    def BUTTON_ADD_LINK(self):
        return self.find_with_check_visibility(self.locators.BUTTON_ADD_LINK)

    @property
    @add_write
    def INPUT_ADD_LINK(self):
        return self.find_with_check_visibility(self.locators.INPUT_ADD_LINK)

    @property
    def ERROR_LINK_MESSAGE(self):
        return self.find_with_check_visibility(self.locators.INPUT_ADD_LINK)
    
    def close_training_if_shown(self):
        try:
            self.find_with_check_visibility(self.locators.MODAL_VIEW_TRAINING)
            self.click(self.find(self.locators.CHOOSE_NO))
        except TimeoutException:
            pass
