import pytest

from cases import LoggedCase
from ui.pages.leads_page import LeadsPage


class TestLeads(LoggedCase):
    @pytest.fixture(scope='function')
    def setup_create_leads(self):
        self.main_page.open_leads()
        self.leads_page = LeadsPage(self.driver)
        yield
        self.tear_down_create_leads()

    def tear_down_create_leads(self):
        pass

    def test_more_text(self, setup_create_leads):
        self.leads_page.click(self.leads_page.BUTTON_CREATE_LEAD_FORM)
        leads_form_design = self.leads_page.design_page.check_more_text()

        self.leads_page.click(self.leads_page.BUTTON_SUBMIT)
        leads_form_question = self.leads_page.question_page.check_more_text()

        self.leads_page.click(self.leads_page.BUTTON_SUBMIT)
        leads_form_result = self.leads_page.result_page.check_more_text()

        self.leads_page.click(self.leads_page.BUTTON_SUBMIT)
        leads_form_settings = self.leads_page.settings_page.check_more_text()

        self.leads_page.click(self.leads_page.BUTTON_SUBMIT)

        def tear_down_create_lead_form():
            self.leads_page.remove_lead_form(name=leads_form_design.lead_name)

        self.tear_down_create_leads = tear_down_create_lead_form

        assert self.leads_page.NAME_LEAD_FORM(leads_form_design.lead_name)

        self.leads_page.click(self.leads_page.get_button_edit_by_name_lead_form(leads_form_design.lead_name))
        assert self.leads_page.HEADER_EDIT
        self.leads_page.design_page.check_leads_form(leads_form_design)

        self.leads_page.click(self.leads_page.BUTTON_SUBMIT)
        self.leads_page.question_page.check_leads_form(leads_form_question)

        self.leads_page.click(self.leads_page.BUTTON_SUBMIT)
        self.leads_page.result_page.check_leads_form(leads_form_result)

        self.leads_page.click(self.leads_page.BUTTON_SUBMIT)
        self.leads_page.settings_page.check_leads_form(leads_form_settings)

