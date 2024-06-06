import pytest

from cases import LoggedCase
from ui.pages.leads_page import LeadsPage


class TestLeads(LoggedCase):
    @pytest.fixture(scope='function')
    def setup_create_leads(self):
        self.main_page.open_leads()
        self.leads_page = LeadsPage(self.driver)

    def check_display_design(self):
        assert self.leads_page.design_page.HEADER
        assert self.leads_page.design_page.INPUT_LEAD_NAME
        assert self.leads_page.design_page.BUTTON_SET_GLOBAL_IMAGE
        assert self.leads_page.design_page.INPUT_ORGANIZATION
        assert self.leads_page.design_page.RADIOGROUP_FIRST_SCREEN
        assert self.leads_page.design_page.INPUT_TITLE
        assert self.leads_page.design_page.INPUT_SHORT_DESCRIPTION
        assert self.leads_page.design_page.PIPETTE_CHOICE_GRADIENT
        assert self.leads_page.design_page.BUTTON_SET_MAIN_IMAGE

    def test_more_text(self, setup_create_leads):
        self.leads_page.BUTTON_CREATE_LEAD_FORM.click(timeout=5)

        self.check_display_design()
