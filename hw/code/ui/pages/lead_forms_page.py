from ui.pages.base_page import PageWithModalView, PageWithRedirectWindow
from ui.locators.lead_forms_locators import LeadFormsPageLocators

from selenium.webdriver.support import expected_conditions as EC


class LeadFormsPage(PageWithModalView, PageWithRedirectWindow):
    locators = LeadFormsPageLocators()


    def add_click(button_getter):
        """Adds click method to button"""
        def decorator(self):
            def click():
                """Clicks button"""
                self.click(button_getter(self))

            button_getter(self).click = click
            return button_getter(self)
        return decorator
    

    def add_enter(input_field_getter):
        """Adds enter method to input_field"""
        def decorator(self):
            def enter(text):
                """Enters text in input field"""
                input_field_getter(self).clear()
                input_field_getter(self).send_keys(text)

            input_field_getter(self).enter = enter
            return input_field_getter(self)
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
     
    
    