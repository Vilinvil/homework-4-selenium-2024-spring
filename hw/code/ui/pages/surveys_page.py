from selenium.common import TimeoutException
from ui.pages.base_page_functionality import BasePageFunctionality, add_write, add_get_value, add_hover, add_click
from ui.locators.surveys_locators import SurveysLocators
from utils.expected_conditions import element_has_background

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.alert import Alert
from os import path


class SurveysPage(BasePageFunctionality):
    url = "https://ads.vk.com/hq/leadads/surveys"
    locators = SurveysLocators()

    @property
    @add_click
    def BUTTON_CREATE_SURVEYS(self):
        return self.find(self.locators.BUTTON_CREATE_SURVEYS, until_EC=EC.visibility_of_element_located)

    @property
    @add_write
    def INPUT_NAME(self):
        return self.find(self.locators.INPUT_NAME, until_EC=EC.visibility_of_element_located)
         

    @property
    @add_write
    def INPUT_COMPANY_NAME(self):
        return self.find(self.locators.INPUT_COMPANY_NAME, until_EC=EC.visibility_of_element_located)

    # @property
    def COMPANY_NAME(self, name):
        # parent = self.find(self.locators.SURVEYS_MAIN_BLOCK)
        # return self.find_child(parent, self.locators.SURVEYS_COMPANY_NAME).text
        return self.find(self.locators.SURVEYS_COMPANY_NAME(name))


    @property
    @add_write
    def INPUT_SURVEYS_HEADER(self):
        return self.find(self.locators.INPUT_SURVEYS_HEADER, until_EC=EC.visibility_of_element_located)


    # @property
    def SURVEYS_HEADER(self, header):
        # parent = self.find(self.locators.SURVEYS_MAIN_BLOCK)
        # return self.find_child(parent, self.locators.SURVEYS_HEADER).text
        return self.find(self.locators.SURVEYS_HEADER(header))

    @property
    @add_write
    def INPUT_SURVEYS_DESCRIPTION(self):
        return self.find(self.locators.INPUT_SURVEYS_DESCRIPTION, until_EC=EC.visibility_of_element_located)

    
    # @property
    def SURVEYS_DESCRIPTION(self, desc):
        # parent = self.find(self.locators.SURVEYS_MAIN_BLOCK)
        # return self.find_child(parent, self.locators.SURVEYS_DESCRIPTION).text
        return self.find(self.locators.SURVEYS_DESCRIPTION(desc))


    @property
    @add_click
    def BUTTON_TO_QUESTIONS(self):
        return self.find(self.locators.BUTTON_TO_QUESTIONS, until_EC=EC.visibility_of_element_located)
    

    @property
    @add_click 
    def BUTTON_LOAD_IMAGE(self):
        return self.find(self.locators.BUTTON_LOAD_IMAGE, until_EC=EC.visibility_of_element_located)

    @property
    @add_click
    def BUTTON_LOAD_MEDIAFILES(self):
        return self.find(self.locators.BUTTON_LOAD_MEDIAFILES, until_EC=EC.visibility_of_element_located)
    

    @property
    @add_click
    def CHOOSE_IMAGE(self):
        return self.find(self.locators.CHOOSE_IMAGE())


    @property
    def LOGO_IMAGE(self):
        return self.find(self.locators.LOGO_IMG, until_EC=EC.visibility_of_element_located)

    def load_logo(self, filepath):
        self.BUTTON_LOAD_IMAGE.clicks()
        file_input = self.find(self.locators.FILE_INPUT_LOCATOR)
        file_input.send_keys(path.abspath(filepath))
        self.CHOOSE_IMAGE.clicks()


    # @property
    @add_click
    @add_write
    def INPUT_TEXT_QUESTION(self, i=1):
        return self.find(self.locators.INPUT_QUESTION_TEXT(i), until_EC=EC.visibility_of_element_located)
        

    @add_write
    def INPUT_QUESTION_ANSWER(self, i=1):
        return self.find(self.locators.INPUT_ANSWER(i), until_EC=EC.visibility_of_element_located)
    

    @property
    @add_click
    def BUTTON_ADD_QUESTION(self):
        return self.find(self.locators.BUTTON_ADD_QUESTION, until_EC=EC.visibility_of_element_located)
    

    @add_click
    def BUTTON_ADD_ANSWER(self, i=1):
        return self.find(self.locators.BUTTON_ADD_ANSWER(i), until_EC=EC.visibility_of_element_located)
    

    @property
    def QUESTION_TEXT(self):
        parent = self.find(self.locators.SURVEY_QUESTION_BLOCK)
        return self.find_child(parent, self.locators.QUESTION_TEXT()).text
    

    def ANSWER_TEXT(self, i=1):
        parent = self.find(self.locators.SURVEY_QUESTION_BLOCK)
        return self.find_child(parent, self.locators.QUESTION_ANSWER(i)).text
    

    # @property
    @add_click
    def BUTTON_ADD_CONDITION(self, i=1):
        return self.find(self.locators.BUTTON_ADD_CONDITION(i))
    

    @add_click
    def BUTTON_SELECT_ANSWER(self):
        return self.find(self.locators.SELECT_ANSWER(1), until_EC=EC.visibility_of_element_located)
    

    @add_click
    def CONDITION_ANSWER_OPTION(self, i=1):
        return self.find(self.locators.CHOOSE_ANSWER(i))
    

    def choose_answer_condition(self, answer_num=1):
        self.BUTTON_SELECT_ANSWER().clicks()
        self.CONDITION_ANSWER_OPTION(answer_num).clicks()
        # self.find(self.locators.CHOOSE_ANSWER)
        # self.BUTTON_LOAD_MEDIAFILES.clicks()

    @property
    @add_click
    def BUTTON_ADD_STOP_VIEW(self):
        return self.find(self.locators.BUTTON_ADD_STOP_VIEW)
    

    @property
    @add_click
    def BUTTON_SELECT_QUESTION_STOP_VIEW(self):
        parent = self.find(self.locators.SELECT_QUESTION(2))
        return self.find_child(parent, self.locators.INPUT)
    

    # @property
    @add_click
    def QUESTION_OPTION_STOP_VIEW(self, question_num):
        return self.find(self.locators.SELECT_QUESTION(question_num), until_EC=EC.visibility_of_element_located)
    

    def choose_question_stop_view(self, question_num=1):
        self.BUTTON_SELECT_QUESTION_STOP_VIEW.clicks()
        self.QUESTION_OPTION_STOP_VIEW(question_num)


    @property
    @add_click
    def BUTTON_SELECT_ANSWER_STOP_VIEW(self):
        return self.find(self.locators.SELECT_ANSWER_FOR_STOP_VIEW())
    
    
    # @property
    @add_click
    def ANSWER_OPTION_STOP_VIEW(self, answer_text=""):
        return self.find(self.locators.CHOOSE_ANSWER_STOP_VIEW(answer_text), until_EC=EC.visibility_of_element_located)
    

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
    @add_click
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
        # return self.find(self.locators.RESULT_HEADER(header), until_EC=EC.presence_of_element_located)
    

    @property
    def RESULT_DESCRIPTION(self):
        parent = self.find(self.locators.SURVEYS_SUCCESS_BLOCK)
        return self.find_child(parent, self.locators.RESULT_DESCRIPTION(), until_EC=EC.visibility_of_element_located).text
        # return self.find(self.locators.RESULT_DESCRIPTION(), until_EC=EC.presence_of_element_located)


    @property
    @add_click
    def BUTTON_START_SURVEY(self):
        return self.find(self.locators.BUTTON_START_SURVEY) 
    

    # @property
    @add_click
    def SURVEY_RAW(self, name):
        return self.find(self.locators.CHANGE_SURVEY(name), until_EC=EC.visibility_of_element_located)
    

    @property
    def CONDITION_QUESTION_ANSWER_TEXT(self):
        return self.find(self.locators.QUESTION_ANSWER_REMOVABLE_CHIP(1), until_EC=EC.visibility_of_element_located).text
    

    @property
    def STOP_VIEW_QUESTION_ANSWER_TEXT(self):
        return self.find(self.locators.QUESTION_ANSWER_REMOVABLE_CHIP(2), until_EC=EC.visibility_of_element_located).text
    