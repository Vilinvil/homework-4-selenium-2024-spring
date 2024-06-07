from ui.pages.base_page_functionality import BasePageFunctionality, add_write, add_get_value
from ui.locators.leads_locators import (
    LeadsPageLocators, LeadsPageDesignLocators, LeadsPageQuestionsLocators)
from utils.expected_conditions import element_has_background
from hw.code.utils.timeout import BASIC_TIMEOUT

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class LeadsPageDesign(BasePageFunctionality):
    url = "https://ads.vk.com/hq/leadads/leadforms"
    locators = LeadsPageDesignLocators()

    @property
    def HEADER(self):
        return self.find_with_check_visibility(self.locators.HEADER)

    @property
    @add_write
    @add_get_value
    def INPUT_LEAD_NAME(self):
        return self.find_with_check_visibility(self.locators.INPUT_LEAD_NAME)

    @property
    def BUTTON_SET_GLOBAL_IMAGE(self):
        return self.find(self.locators.BUTTON_SET_GLOBAL_IMAGE, until_EC=EC.element_to_be_clickable)

    def check_design_media(self):
        assert self.MEDIA_HEADER
        assert self.MEDIA_UPLOAD
        assert self.MEDIA_DEFAULT_IMAGE

    @property
    @add_write
    def INPUT_ORGANIZATION(self):
        return self.find_with_check_visibility(self.locators.INPUT_ORGANIZATION)

    @property
    def RADIOGROUP_FIRST_SCREEN(self):
        return self.find_with_check_visibility(self.locators.RADIOGROUP_FIRST_SCREEN)

    @property
    def RADIOGROUP_BUTTON_MORE_TEXT(self):
        return self.find_with_check_visibility(self.locators.RADIOGROUP_BUTTON_MORE_TEXT)

    def check_active_RADIOGROUP_BUTTON_MORE_TEXT(self):
        assert self.find(self.locators.INPUT_SHORT_DESCRIPTION, until_EC=EC.invisibility_of_element_located)
        assert self.find_with_check_visibility(self.locators.INPUT_MORE_TEXT)

    @property
    @add_write
    def INPUT_TITLE(self):
        return self.find_with_check_visibility(self.locators.INPUT_TITLE)

    @property
    @add_write
    def INPUT_SHORT_DESCRIPTION(self):
        return self.find_with_check_visibility(self.locators.INPUT_SHORT_DESCRIPTION)

    @property
    def PIPETTE_CHOICE_GRADIENT(self):
        return self.find_with_check_visibility(self.locators.PIPETTE_CHOICE_GRADIENT)

    @property
    @add_write
    def PIPETTE_INPUT_GRADIENT(self):
        return self.find_with_check_visibility(self.locators.PIPETTE_INPUT_GRADIENT)

    def choose_gradient(self, gradient):
        self.PIPETTE_CHOICE_GRADIENT.click()
        self.PIPETTE_INPUT_GRADIENT.write(gradient)
        pipette_button_submit = self.click(self.PIPETTE_BUTTON_SUBMIT)

        self.wait().until(EC.invisibility_of_element(pipette_button_submit))

    @property
    def PIPETTE_BUTTON_SUBMIT(self):
        return self.find_with_check_visibility(self.locators.PIPETTE_BUTTON_SUBMIT)

    @property
    def PIPETTE_GRADIENT_RESULT(self):
        return self.find_with_check_visibility(self.locators.PIPETTE_GRADIENT_RESULT)

    def rgb_from_hex(self, hex_code) -> str:
        red = int(hex_code[1:2])*16 + int(hex_code[2:3])
        green = int(hex_code[3:4])*16 + int(hex_code[4:5])
        blue = int(hex_code[5:6])*16 + int(hex_code[6:7])

        return f'rgb({red}, {green}, {blue})'

    def check_pipette_gradient_result(self, gradient):
        rgb = self.rgb_from_hex(gradient)

        assert self.wait().until(element_has_background(self.locators.PIPETTE_GRADIENT_RESULT, rgb))

    @property
    def BUTTON_SET_MAIN_IMAGE(self):
        return self.find_with_check_visibility(self.locators.BUTTON_SET_MAIN_IMAGE)

    @property
    def PREVIEW_CONTAINER(self):
        return self.find_with_check_visibility(self.locators.PREVIEW_CONTAINER)

    @property
    def PREVIEW_TITLE_CONTACT_DETAILS(self):
        return self.find_with_check_visibility(self.locators.PREVIEW_TITLE_CONTACT_DETAILS)

    @property
    def PREVIEW_LOGO(self):
        return self.find_with_check_visibility(self.locators.PREVIEW_LOGO)

    @property
    def PREVIEW_TOP_PART_TITLE(self):
        return self.find_with_check_visibility(self.locators.PREVIEW_TOP_PART_TITLE)

    @property
    def PREVIEW_LONG_DESCRIPTION(self):
        return self.find_with_check_visibility(self.locators.PREVIEW_LONG_DESCRIPTION)

    def check_PREVIEW_LEAD_FORM_TITLE(self, title):
        assert self.find_with_check_visibility(self.locators.PREVIEW_LEAD_FORM_TITLE(title))

    @property
    def MEDIA_HEADER(self):
        return self.find_with_check_visibility(self.locators.MEDIA_HEADER)

    @property
    def MEDIA_UPLOAD(self):
        return self.find_with_check_visibility(self.locators.MEDIA_UPLOAD)

    @property
    def MEDIA_DEFAULT_IMAGE(self):
        return self.find_with_check_visibility(self.locators.MEDIA_DEFAULT_IMAGE)

    @property
    @add_write
    def INPUT_MORE_TEXT(self):
        return self.find_with_check_visibility(self.locators.INPUT_MORE_TEXT)

    def check_design_display(self):
        assert self.HEADER
        assert self.INPUT_LEAD_NAME
        assert self.BUTTON_SET_GLOBAL_IMAGE
        assert self.INPUT_ORGANIZATION
        assert self.RADIOGROUP_FIRST_SCREEN
        assert self.INPUT_TITLE
        assert self.INPUT_SHORT_DESCRIPTION
        assert self.PIPETTE_CHOICE_GRADIENT
        assert self.BUTTON_SET_MAIN_IMAGE
        assert self.PREVIEW_CONTAINER
        assert self.PREVIEW_TITLE_CONTACT_DETAILS

    def check_design(self):
        self.check_design_display()

        lead_name = 'Лид-форма Лидер'
        self.INPUT_LEAD_NAME.write(lead_name)
        assert self.INPUT_LEAD_NAME.get_value() == lead_name

        self.BUTTON_SET_GLOBAL_IMAGE.click()
        self.check_design_media()
        self.MEDIA_DEFAULT_IMAGE.click()
        assert self.PREVIEW_LOGO

        organization = 'ООО "Лидер"'
        self.INPUT_ORGANIZATION.write(organization)
        assert self.PREVIEW_TOP_PART_TITLE.text == organization

        self.RADIOGROUP_BUTTON_MORE_TEXT.click()
        self.check_active_RADIOGROUP_BUTTON_MORE_TEXT()

        title = 'Как вы оцениваете нашу работу?'
        self.INPUT_TITLE.write(title)
        self.check_PREVIEW_LEAD_FORM_TITLE(title)

        more_text = 'Ответьте, пожалуйста, на пару вопросов, так вы помогаете нам стать лучше.'
        self.INPUT_MORE_TEXT.write(more_text)
        assert self.PREVIEW_LONG_DESCRIPTION.text == more_text

        gradient = '#800080'
        self.choose_gradient(gradient)
        self.check_pipette_gradient_result(gradient)


class LeadsPageQuestions(BasePageFunctionality):
    url = "https://ads.vk.com/hq/leadads/leadforms"
    locators = LeadsPageQuestionsLocators()

    def get_ADD_QUESTION_CONTAINER(self, title):
        return self.find_with_check_visibility(self.locators.ADD_QUESTION_CONTAINER(title))

    @property
    def TITLE_QUESTION(self):
        return self.find_with_check_visibility(self.locators.TITLE_QUESTION)

    @property
    def BUTTON_ADD_QUESTION(self):
        return self.find_with_check_visibility(self.locators.BUTTON_ADD_QUESTION)

    @add_write
    def ADD_QUESTION_INPUT_TITLE(self, question_num):
        question = self.get_ADD_QUESTION_CONTAINER(question_num)
        return question.find_element(*self.locators.ADD_QUESTION_INPUT_TITLE)

    def ADD_QUESTION_SELECTOR_TYPE(self, question_num):
        question = self.get_ADD_QUESTION_CONTAINER(question_num)
        return question.find_element(*self.locators.ADD_QUESTION_SELECTOR_TYPE)

    @property
    def ADD_QUESTION_SELECT_SEVERAL_ANSWERS(self):
        return self.find_with_check_visibility(self.locators.ADD_QUESTION_SELECT_SEVERAL_ANSWERS)

    @property
    def ADD_QUESTION_SELECT_ANY_FORM_ANSWER(self):
        return self.find_with_check_visibility(self.locators.ADD_QUESTION_SELECT_ANY_FORM_ANSWER)

    def ADD_QUESTION_INPUTS_ANSWER(self, question_num):
        question = self.get_ADD_QUESTION_CONTAINER(question_num)
        return question.find_elements(*self.locators.ADD_QUESTION_INPUT_ANSWER)

    def ADD_QUESTION_BUTTON_ADD_ANSWER(self, question_num):
        question = self.get_ADD_QUESTION_CONTAINER(question_num)
        return question.find_element(*self.locators.ADD_QUESTION_BUTTON_ADD_ANSWER)

    def ADD_QUESTION_BUTTON_ADD_MORE(self, question_num):
        question = self.get_ADD_QUESTION_CONTAINER(question_num)
        return question.find_element(*self.locators.ADD_QUESTION_BUTTON_ADD_MORE)

    @property
    def ADD_QUESTION_BUTTON_ADD_MORE_OTHER(self):
        return self.find_with_check_visibility(self.locators.ADD_QUESTION_BUTTON_ADD_MORE_OTHER)

    def check_added_question(self, question_num):
        assert self.get_ADD_QUESTION_CONTAINER(question_num)
        assert self.ADD_QUESTION_INPUT_TITLE(question_num)
        assert self.ADD_QUESTION_SELECTOR_TYPE(question_num)

        inputs_answer = self.ADD_QUESTION_INPUTS_ANSWER(question_num)
        assert len(inputs_answer) == 2

        assert self.ADD_QUESTION_BUTTON_ADD_ANSWER
        assert self.ADD_QUESTION_BUTTON_ADD_MORE(question_num)

    @property
    def TITLE_CONTACT_INFO(self):
        return self.find_with_check_visibility(self.locators.TITLE_CONTACT_INFO)

    @property
    def BUTTON_ADD_CONTACT_INFO(self):
        return self.find_with_check_visibility(self.locators.BUTTON_ADD_CONTACT_INFO)

    def PREVIEW_TITLE_QUESTION(self, title):
        assert self.find_with_check_visibility(self.locators.PREVIEW_TITLE_QUESTION(title))

    def PREVIEW_QUESTION_BY_TITLE(self, title):
        return self.find_with_check_visibility(self.locators.PREVIEW_QUESTION_BY_TITLE(title))

    def get_preview_radiogroup_by_title_question(self, question_title) -> WebElement:
        question = self.PREVIEW_QUESTION_BY_TITLE(question_title)
        return question.find_element(*self.locators.PREVIEW_ANSWERS_SIGN_RADIOGROUP)

    def check_preview_invisibility_radiogroup(self, radiogroup):
        assert self.wait().until(EC.invisibility_of_element(radiogroup))

    def get_preview_checkbox_by_title_question(self, question_title) -> WebElement:
        question = self.PREVIEW_QUESTION_BY_TITLE(question_title)
        return question.find_element(*self.locators.PREVIEW_ANSWERS_SIGN_CHECKBOX)

    def check_preview_visibility_checkbox(self, checkbox):
        assert self.wait().until(EC.visibility_of(checkbox))

    def get_preview_any_form_answer_by_title_question(self, question_title) -> WebElement:
        question = self.PREVIEW_QUESTION_BY_TITLE(question_title)
        return question.find_element(*self.locators.PREVIEW_ANSWERS_SIGN_ANY_FORM)

    def check_preview_visibility_any_form_answer(self, any_form_answer):
        assert self.wait().until(EC.visibility_of(any_form_answer))

    def check_preview_checkbox_answer_in_question_by_title(self, title, answer):
        question = self.PREVIEW_QUESTION_BY_TITLE(title)
        assert question.find_element(*self.locators.CHECKBOX_CONTENT(answer))

    def get_preview_contact_info_by_question_title(self, title, contact_info):
        question = self.PREVIEW_QUESTION_BY_TITLE(title)

        return question.find_element(*self.locators.PREVIEW_ANSWER_CONTACT_INFO(contact_info))

    def check_preview_invisibility_contact_info_element(self, contact_info_element):
        assert self.wait().until(EC.invisibility_of_element(contact_info_element))

    @property
    def BUTTON_DELETE_CONTACT_INFO_PHONE(self):
        return self.find_with_check_visibility(self.locators.BUTTON_DELETE_CONTACT_INFO_PHONE)

    @property
    def MODAL_VIEW_CONTACT_INFO(self):
        return self.find_with_check_visibility(self.locators.MODAL_VIEW_CONTACT_INFO)

    @property
    def MODAL_VIEW_CONTACT_INFO_BUTTON_SUBMIT(self):
        return self.MODAL_VIEW_CONTACT_INFO.find_element(*self.locators.MODAL_VIEW_CONTACT_INFO_BUTTON_SUBMIT)

    def click_checkbox_contact_info_by_title(self, title):
        self.click(self.locators.CHECKBOX_CONTENT(title))

    def check_question_display(self):
        assert self.TITLE_QUESTION
        assert self.BUTTON_ADD_QUESTION
        assert self.TITLE_CONTACT_INFO
        assert self.BUTTON_ADD_CONTACT_INFO

    def check_questions(self):
        self.check_question_display()

        self.BUTTON_ADD_QUESTION.click()
        first_question_num = 1
        self.check_added_question(first_question_num)

        first_question_title = 'Что вам понравилось?'
        self.ADD_QUESTION_INPUT_TITLE(first_question_num).write(first_question_title)
        self.PREVIEW_TITLE_QUESTION(first_question_title)

        first_question_radiogroup = self.get_preview_radiogroup_by_title_question(first_question_title)
        self.ADD_QUESTION_SELECTOR_TYPE(first_question_num).click()
        self.ADD_QUESTION_SELECT_SEVERAL_ANSWERS.click()
        self.check_preview_invisibility_radiogroup(first_question_radiogroup)
        first_question_checkbox = self.get_preview_checkbox_by_title_question(first_question_title)
        self.check_preview_visibility_checkbox(first_question_checkbox)

        inputs_answer = self.ADD_QUESTION_INPUTS_ANSWER(first_question_num)
        first_question_first_answer = "Время выполнения"
        self.write_input_to_element(inputs_answer[0], first_question_first_answer)
        self.check_preview_checkbox_answer_in_question_by_title(
            first_question_title, first_question_first_answer)

        first_question_second_answer = "Качество"
        self.write_input_to_element(inputs_answer[1], first_question_second_answer)
        self.check_preview_checkbox_answer_in_question_by_title(
            first_question_title, first_question_second_answer)

        self.ADD_QUESTION_BUTTON_ADD_ANSWER(first_question_num).click()
        inputs_answer = self.ADD_QUESTION_INPUTS_ANSWER(first_question_num)
        assert len(inputs_answer) == 3

        first_question_third_answer = "Цена"
        self.write_input_to_element(inputs_answer[2], first_question_third_answer)
        self.check_preview_checkbox_answer_in_question_by_title(
            first_question_title, first_question_third_answer)

        first_question_other_answer = 'Другое'
        self.ADD_QUESTION_BUTTON_ADD_MORE(first_question_num).click()
        self.ADD_QUESTION_BUTTON_ADD_MORE_OTHER.click()
        self.ADD_QUESTION_BUTTON_ADD_MORE(first_question_num).click()
        self.check_preview_checkbox_answer_in_question_by_title(
            first_question_title, first_question_other_answer)

        self.BUTTON_ADD_QUESTION.click()
        second_question_num = 2
        self.check_added_question(second_question_num)

        second_question_title = 'Что вам не понравилось в нашей работе?'
        self.ADD_QUESTION_INPUT_TITLE(second_question_num).write(second_question_title)
        self.PREVIEW_TITLE_QUESTION(second_question_title)

        second_question_radiogroup = self.get_preview_radiogroup_by_title_question(second_question_title)
        self.ADD_QUESTION_SELECTOR_TYPE(second_question_num).click()
        self.ADD_QUESTION_SELECT_ANY_FORM_ANSWER.click()
        self.check_preview_invisibility_radiogroup(second_question_radiogroup)
        second_question_any_form = self.get_preview_any_form_answer_by_title_question(second_question_title)
        self.check_preview_visibility_any_form_answer(second_question_any_form)

        contact_info_title = 'Введите свои контактные данные'
        assert self.PREVIEW_QUESTION_BY_TITLE(contact_info_title)
        name_contact_info = 'Введите имя'
        assert self.get_preview_contact_info_by_question_title(contact_info_title, name_contact_info)
        phone_contact_info = '(___) ___-____'
        phone_contact_info_element = self.get_preview_contact_info_by_question_title(
            contact_info_title, phone_contact_info)
        assert phone_contact_info_element

        self.click(self.BUTTON_DELETE_CONTACT_INFO_PHONE)
        assert self.get_preview_contact_info_by_question_title(contact_info_title, 'Введите имя')
        self.check_preview_invisibility_contact_info_element(phone_contact_info_element)

        self.BUTTON_ADD_CONTACT_INFO.click()
        self.click_checkbox_contact_info_by_title('Номер телефона')
        self.click_checkbox_contact_info_by_title('Город')
        self.click(self.MODAL_VIEW_CONTACT_INFO_BUTTON_SUBMIT)
        city_contact_info = 'Введите город'
        assert self.get_preview_contact_info_by_question_title(contact_info_title, name_contact_info)
        assert self.get_preview_contact_info_by_question_title(contact_info_title, phone_contact_info)
        assert self.get_preview_contact_info_by_question_title(contact_info_title, city_contact_info)


class LeadsPage(BasePageFunctionality):
    url = "https://ads.vk.com/hq/leadads/leadforms"
    locators = LeadsPageLocators()

    def __init__(self, driver):
        super().__init__(driver)
        self.design_page = LeadsPageDesign(driver)
        self.question_page = LeadsPageQuestions(driver)

    @property
    def BUTTON_CREATE_LEAD_FORM(self):
        return self.find(self.locators.BUTTON_CREATE_LEAD_FORM, until_EC=EC.element_to_be_clickable)

    @property
    def BUTTON_CANCEL(self):
        return self.find_with_check_visibility(self.locators.BUTTON_CANCEL)

    @property
    def BUTTON_SUBMIT(self):
        return self.find_with_check_visibility(self.locators.BUTTON_SUBMIT)
