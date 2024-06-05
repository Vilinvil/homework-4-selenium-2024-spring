import pytest

from cases import LoggedCase
from ui.pages.leads_page import LeadsPage


class TestLeads(LoggedCase):
    @pytest.fixture(scope='function')
    def setup_create_leads(self):
        self.main_page.open_leads()
        self.leads_page = LeadsPage(self.driver)

    def test_more_text(self, setup_create_leads):
        self.leads_page.BUTTON_CREATE_LEAD_FORM.click(timeout=5)

        name_lead_form = "Лид-форма Лидер"
        self.leads_page.INPUT_LEAD_NAME.write(name_lead_form, timeout=5)
