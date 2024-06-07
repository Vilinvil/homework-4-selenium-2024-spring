import pytest

from cases import LoggedCase
from ui.pages.leads_page import LeadsPage


class TestLeads(LoggedCase):
    @pytest.fixture(scope='function')
    def setup_create_leads(self):
        self.main_page.open_leads()
        self.leads_page = LeadsPage(self.driver)

    def test_more_text(self, setup_create_leads):
        self.leads_page.BUTTON_CREATE_LEAD_FORM.click()
        self.leads_page.design_page.check_design()

        self.leads_page.BUTTON_SUBMIT.click()
        self.leads_page.question_page.check_questions()
