from ui.pages.base_page_functionality import BasePageFunctionality, add_click, add_write, add_get_value
from ui.locators.leads_locators import (
    LeadsPageLocators, LeadsPageDesignLocators, LeadsPageQuestionsLocators)
from utils.expected_conditions import element_has_background

from selenium.webdriver.support import expected_conditions as EC


class LeadsPageDesign(BasePageFunctionality):
    url = "https://ads.vk.com/hq/leadads/leadforms"
    locators = LeadsPageDesignLocators()

    @property
    def HEADER(self):
        return self.find_with_check_visibility(self.locators.HEADER)

    @property
    @add_write(locators.INPUT_LEAD_NAME)
    @add_get_value(locators.INPUT_LEAD_NAME)
    def INPUT_LEAD_NAME(self):
        return self.find_with_check_visibility(self.locators.INPUT_LEAD_NAME)

    @property
    @add_click(locators.BUTTON_SET_GLOBAL_IMAGE)
    def BUTTON_SET_GLOBAL_IMAGE(self):
        return self.find_with_check_visibility(self.locators.BUTTON_SET_GLOBAL_IMAGE)

    @property
    @add_write(locators.INPUT_ORGANIZATION)
    def INPUT_ORGANIZATION(self):
        return self.find_with_check_visibility(self.locators.INPUT_ORGANIZATION)

    @property
    def RADIOGROUP_FIRST_SCREEN(self):
        return self.find_with_check_visibility(self.locators.RADIOGROUP_FIRST_SCREEN)

    @property
    @add_click(locators.RADIOGROUP_BUTTON_MORE_TEXT)
    def RADIOGROUP_BUTTON_MORE_TEXT(self):
        return self.find_with_check_visibility(self.locators.RADIOGROUP_BUTTON_MORE_TEXT)

    def check_active_RADIOGROUP_BUTTON_MORE_TEXT(self):
        assert self.find(self.locators.INPUT_SHORT_DESCRIPTION, until_EC=EC.invisibility_of_element_located)
        assert self.find_with_check_visibility(self.locators.INPUT_MORE_TEXT)

    @property
    @add_write(locators.INPUT_TITLE)
    def INPUT_TITLE(self):
        return self.find_with_check_visibility(self.locators.INPUT_TITLE)

    @property
    @add_write(locators.INPUT_SHORT_DESCRIPTION)
    def INPUT_SHORT_DESCRIPTION(self):
        return self.find_with_check_visibility(self.locators.INPUT_SHORT_DESCRIPTION)

    @property
    @add_click(locators.PIPETTE_CHOICE_GRADIENT)
    def PIPETTE_CHOICE_GRADIENT(self):
        return self.find_with_check_visibility(self.locators.PIPETTE_CHOICE_GRADIENT)

    @property
    @add_write(locators.PIPETTE_INPUT_GRADIENT)
    def PIPETTE_INPUT_GRADIENT(self):
        return self.find_with_check_visibility(self.locators.PIPETTE_INPUT_GRADIENT)

    @property
    @add_click(locators.PIPETTE_BUTTON_SUBMIT)
    def PIPETTE_BUTTON_SUBMIT(self):
        return self.find_with_check_visibility(self.locators.PIPETTE_BUTTON_SUBMIT)

    def choose_gradient(self, gradient):
        self.PIPETTE_CHOICE_GRADIENT.click()
        self.PIPETTE_INPUT_GRADIENT.write(gradient)
        pipette_button_submit = self.PIPETTE_BUTTON_SUBMIT.click()

        self.wait().until(EC.invisibility_of_element(pipette_button_submit))

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
    @add_click(locators.BUTTON_SET_MAIN_IMAGE)
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
    @add_click(locators.MEDIA_DEFAULT_IMAGE)
    def MEDIA_DEFAULT_IMAGE(self):
        return self.find_with_check_visibility(self.locators.MEDIA_DEFAULT_IMAGE)

    @property
    @add_write(locators.INPUT_MORE_TEXT)
    def INPUT_MORE_TEXT(self):
        return self.find_with_check_visibility(self.locators.INPUT_MORE_TEXT)


class LeadsPageQuestions(BasePageFunctionality):
    url = "https://ads.vk.com/hq/leadads/leadforms"
    locators = LeadsPageQuestionsLocators()

    @property
    def TITLE_QUESTION(self):
        return self.find_with_check_visibility(self.locators.TITLE_QUESTION)

    @property
    @add_click(locators.BUTTON_ADD_QUESTION)
    def BUTTON_ADD_QUESTION(self):
        return self.find_with_check_visibility(self.locators.BUTTON_ADD_QUESTION)

    @property
    def TITLE_CONTACT_INFO(self):
        return self.find_with_check_visibility(self.locators.TITLE_CONTACT_INFO)

    @property
    @add_click(locators.BUTTON_ADD_CONTACT_INFO)
    def BUTTON_ADD_CONTACT_INFO(self):
        return self.find_with_check_visibility(self.locators.BUTTON_ADD_CONTACT_INFO)


class LeadsPage(BasePageFunctionality):
    url = "https://ads.vk.com/hq/leadads/leadforms"
    locators = LeadsPageLocators()

    def __init__(self, driver):
        super().__init__(driver)
        self.design_page = LeadsPageDesign(driver)
        self.question_page = LeadsPageQuestions(driver)

    @property
    @add_click(locators.BUTTON_CREATE_LEAD_FORM)
    def BUTTON_CREATE_LEAD_FORM(self):
        return self.find_with_check_visibility(self.locators.BUTTON_CREATE_LEAD_FORM)

    @property
    @add_click(locators.BUTTON_CANCEL)
    def BUTTON_CANCEL(self):
        return self.find_with_check_visibility(self.locators.BUTTON_CANCEL)

    @property
    @add_click(locators.BUTTON_SUBMIT)
    def BUTTON_SUBMIT(self):
        return self.find_with_check_visibility(self.locators.BUTTON_SUBMIT)
