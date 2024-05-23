from cases import LoggedCase
from ui.pages.lead_forms_page import LeadFormsPage
import pytest
import random
import time

class TestLeadFormPage(LoggedCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_site_page(self):
        self.main_page.click_redirect_to_lead_forms_page()
        self.lead_forms_page = LeadFormsPage(self.driver)

    def test_display(self):
        self.lead_forms_page.CREATE_LEAD_FORM_BUTTON.click()
        self.lead_forms_page.LEAD_FORM_NAME_INPUT.enter("Test Name")
        self.lead_forms_page.CANCEL_BUTTON.click()
        # self.lead_forms_page.SEARCH_LEAD_FORM_INPUT.enter("test")
        # self.lead_forms_page.get_search_lead_form_input_field.enter("test")
        # assert self.lead_forms_page.create_lead_form_button != None
        # assert self.lead_forms_page.get_search_status_dropmenu() != None
        # assert self.lead_forms_page.get_search_lead_form_input_field != None
        # assert self.lead_forms_page.get_lead_forms_tab() != None
        # assert self.lead_forms_page.get_yclients_tab != None
        # assert self.lead_forms_page.get_surveys_tab != None

        # self.lead_forms_page.click_create_lead_form_button()

        # assert self.lead_forms_page.get_name_lead_form_input_field() != None

        # assert self.lead_forms_page.get_name_company_input_field() != None

        # assert self.lead_forms_page.get_header_input_field() != None
    
        # assert self.lead_forms_page.get_surveys_info_input_field() != None

        # # assert self.lead_forms_page.get_choose_image_button() != None
    
        # assert self.lead_forms_page.get_cancel_button() != None

        # assert self.lead_forms_page.get_continue_button() != None

        # assert self.lead_forms_page.get_compact_button() != None
    
        # assert self.lead_forms_page.get_more_text_button() != None

    