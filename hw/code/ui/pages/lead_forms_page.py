from ui.pages.base_page import PageWithModalView, PageWithRedirectWindow
from ui.locators.lead_forms_locators import LeadFormsPageLocators

from selenium.webdriver.support import expected_conditions as EC


class LeadFormsPage(PageWithModalView, PageWithRedirectWindow):
    locators = LeadFormsPageLocators()


    def get_create_lead_form_button(self):
        return self.find(self.locators.CREATE_FORM_BUTTON,
                                       until_EC=EC.visibility_of_element_located)


    # def get_search_status_dropmenu(self):
        # return self.find(self.locators.DROP_MENU)
    

    def get_search_leadform_input_field(self):
        return self.find(self.locators.SEARCH_INPUT,
                                       until_EC=EC.visibility_of_element_located)
    

    def get_lead_forms_tab(self):
        return self.find(self.locators.LEADFORMS_TAB,
                                       until_EC=EC.visibility_of_element_located)
    

    def get_yclients_tab(self):
        return self.find(self.locators.YCLIENTS_TAB,
                                       until_EC=EC.visibility_of_element_located)
    
    
    def get_surveys_tab(self):
        return self.find(self.locators.SURVEYS_TAB,
                                       until_EC=EC.visibility_of_element_located)
    

    def click_create_lead_form_button(self):
        self.click(self.get_create_lead_form_button())


    def get_name_lead_form_input_field(self):
        return self.find(self.locators.INPUT_FORM_NAME)


    def get_name_company_input_field(self):
        return self.find(self.locators.INPUT_COMPANY_NAME)


    def get_header_input_field(self):
        return self.find(self.locators.INPUT_HEADER)
    

    def get_surveys_info_input_field(self):
        return self.find(self.locators.INPUT_SURVEYS_INFO)
    

    def get_choose_image_button(self):
        return self.find(self.locators.CHOOSE_IMAGE_BUTTON)
    

    def get_cancel_button(self):
        return self.find(self.locators.CANCEL_BUTTON)
    

    def get_continue_button(self):
        return self.find(self.locators.CONTINUE_BUTTON)
    

    def get_compact_button(self):
        return self.find(self.locators.COMPACT_BUTTON)
    

    def get_more_text_button(self):
        return self.find(self.locators.MORE_TEXT_BUTTON)
    
    
    