from ui.pages.base_page import BasePage, PageWithModalView, PageWithRedirectWindow
from ui.locators.lead_forms_locators import LeadFormsPageLocators

from selenium.webdriver.support import expected_conditions as EC


class LeadFormsPage(BasePage):
    locators = LeadFormsPageLocators()


    def add_click(button_getter):
        """Adds clicks method to button"""
        def decorator(self):
            button = button_getter(self)
            def __click():
                """Clicks button"""
                self.click(button)
            button.clicks = __click
            return button
        return decorator
    

    def add_enter(input_field_getter):
        """Adds enter method to input_field"""
        def decorator(self):
            input = input_field_getter(self)
            def __enter(text):
                """Enters text in input field"""
                input.clear()
                input.send_keys(text)

            input.enter = __enter
            return input
        return decorator
    

    @property
    @add_click
    def CREATE_LEAD_FORM_BUTTON(self):
        return self.find(self.locators.CREATE_FORM_BUTTON,
                                       until_EC=EC.visibility_of_element_located)


    @property
    @add_enter
    def SEARCH_LEAD_FORM_INPUT(self):
        return self.find(self.locators.SEARCH_INPUT,
                                       until_EC=EC.visibility_of_element_located)
    

    @property
    @add_click
    def LEAD_FORM_TAB(self):
        return self.find(self.locators.LEADFORMS_TAB,
                                       until_EC=EC.visibility_of_element_located)
    
    
    @property
    @add_click
    def YCLIENTS_TAB(self):
        return self.find(self.locators.YCLIENTS_TAB,
                                       until_EC=EC.visibility_of_element_located)
        

    @property
    @add_click
    def SURVEYS_TAB(self):
        return self.find(self.locators.SURVEYS_TAB,
                                       until_EC=EC.visibility_of_element_located)


    @property
    @add_enter
    def LEAD_FORM_NAME_INPUT(self):
        return self.find(self.locators.INPUT_FORM_NAME)
    

    @property
    @add_enter
    def COMPANY_NAME_INPUT(self):
        return self.find(self.locators.INPUT_COMPANY_NAME)


    @property
    @add_enter
    def HEADER_INPUT_FIELD(self):
        return self.find(self.locators.INPUT_HEADER)
    

    @property
    @add_enter
    def SURVEYS_INFO_INPUT(self):
        return self.find(self.locators.INPUT_SURVEYS_INFO)
    

    @property
    @add_click
    def CHOOSE_IMAGE_BUTTON(self):
        return self.find(self.locators.CHOOSE_IMAGE_BUTTON)
    

    @property
    @add_click
    def CANCEL_BUTTON(self):
        return self.find(self.locators.CANCEL_BUTTON)
    

    @property
    @add_click
    def CONTINUE_BUTTON(self):
        return self.find(self.locators.CONTINUE_BUTTON)
    

    @property
    @add_click
    def COMPACT_BUTTON(self):
        return self.find(self.locators.COMPACT_BUTTON)
    

    @property
    @add_click
    def MORE_TEXT_BUTTON(self):
        return self.find(self.locators.MORE_TEXT_BUTTON)
     
    