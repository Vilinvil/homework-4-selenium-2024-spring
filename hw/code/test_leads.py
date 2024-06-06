import pytest

from cases import LoggedCase
from ui.pages.leads_page import LeadsPage


class TestLeads(LoggedCase):
    @pytest.fixture(scope='function')
    def setup_create_leads(self):
        self.main_page.open_leads()
        self.leads_page = LeadsPage(self.driver)

    def check_design_display(self):
        assert self.leads_page.design_page.HEADER
        assert self.leads_page.design_page.INPUT_LEAD_NAME
        assert self.leads_page.design_page.BUTTON_SET_GLOBAL_IMAGE
        assert self.leads_page.design_page.INPUT_ORGANIZATION
        assert self.leads_page.design_page.RADIOGROUP_FIRST_SCREEN
        assert self.leads_page.design_page.INPUT_TITLE
        assert self.leads_page.design_page.INPUT_SHORT_DESCRIPTION
        assert self.leads_page.design_page.PIPETTE_CHOICE_GRADIENT
        assert self.leads_page.design_page.BUTTON_SET_MAIN_IMAGE
        assert self.leads_page.design_page.PREVIEW_CONTAINER
        assert self.leads_page.design_page.PREVIEW_TITLE_CONTACT_DETAILS

    def check_design_media(self):
        assert self.leads_page.design_page.MEDIA_HEADER
        assert self.leads_page.design_page.MEDIA_UPLOAD
        assert self.leads_page.design_page.MEDIA_DEFAULT_IMAGE

    def test_more_text(self, setup_create_leads):
        self.leads_page.BUTTON_CREATE_LEAD_FORM.click(timeout=5)

        self.check_design_display()

        lead_name = 'Лид-форма Лидер'
        self.leads_page.design_page.INPUT_LEAD_NAME.write(lead_name)
        assert self.leads_page.design_page.INPUT_LEAD_NAME.get_value() == lead_name

        self.leads_page.design_page.BUTTON_SET_GLOBAL_IMAGE.click()
        self.check_design_media()
        self.leads_page.design_page.MEDIA_DEFAULT_IMAGE.click()
        assert self.leads_page.design_page.PREVIEW_LOGO

        organization = 'ООО "Лидер"'
        self.leads_page.design_page.INPUT_ORGANIZATION.write(organization)
        assert self.leads_page.design_page.PREVIEW_TOP_PART_TITLE.text == organization

        self.leads_page.design_page.RADIOGROUP_BUTTON_MORE_TEXT.click()
        self.leads_page.design_page.check_active_RADIOGROUP_BUTTON_MORE_TEXT()

        title = 'Как вы оцениваете нашу работу?'
        self.leads_page.design_page.INPUT_TITLE.write(title)
        self.leads_page.design_page.check_HEADER_LEAD_FORM_TITLE(title)

        more_text = 'Ответьте, пожалуйста, на пару вопросов, так вы помогаете нам стать лучше.'
