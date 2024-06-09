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

    def test_negative(self, setup_create_leads):
        self.leads_page.click(self.leads_page.BUTTON_CREATE_LEAD_FORM)
        self.leads_page.click(self.leads_page.BUTTON_SUBMIT)

        assert self.leads_page.ERROR_REQUIRED_FIELD_BY_TITLE_ITEM('Логотип')
        assert self.leads_page.ERROR_REQUIRED_FIELD_BY_TITLE_ITEM('Название компании')
        assert self.leads_page.ERROR_REQUIRED_FIELD_BY_TITLE_ITEM('Заголовок')
        assert self.leads_page.ERROR_REQUIRED_FIELD_BY_TITLE_ITEM('Описание опроса')

        to_long_organization = "a" * 31
        self.leads_page.design_page.INPUT_ORGANIZATION.write(to_long_organization)
        assert self.leads_page.ERROR_BY_TITLE_ITEM('Название компании',
                                                   'Превышена максимальная длина поля')

        self.leads_page.design_page.fill_minimum()
        self.leads_page.click(self.leads_page.BUTTON_SUBMIT)
        self.leads_page.check_invisibility_any_error()

        self.leads_page.click(self.leads_page.question_page.BUTTON_ADD_QUESTION)
        self.leads_page.click(self.leads_page.BUTTON_SUBMIT)
        self.leads_page.question_page.check_error_question()

        self.leads_page.question_page.fill_minimum_first_question()
        self.leads_page.click(self.leads_page.BUTTON_SUBMIT)
        self.leads_page.check_invisibility_any_error()

        self.leads_page.click(self.leads_page.result_page.BUTTON_ADD_SITE)
        self.leads_page.result_page.INPUT_SITE.write('goods-galaxy')
        self.leads_page.click(self.leads_page.BUTTON_SUBMIT)
        assert self.leads_page.ERROR_BY_TITLE_ITEM('Ссылка на сайт', 'Невалидный url')

        self.leads_page.click(self.leads_page.result_page.BUTTON_ADD_PHONE)
        self.leads_page.result_page.INPUT_PHONE.write('++79809809898')
        self.leads_page.click(self.leads_page.BUTTON_SUBMIT)
        assert self.leads_page.ERROR_BY_TITLE_ITEM('Телефон для заказа',
                                                   'Телефон должен начинаться с + и содержать только цифры')

        self.leads_page.result_page.fill_minimum_title_site_phone()
        self.leads_page.click(self.leads_page.BUTTON_SUBMIT)
        self.leads_page.check_invisibility_any_error()

        self.leads_page.click(self.leads_page.BUTTON_SUBMIT)
        self.leads_page.click(self.leads_page.BUTTON_SUBMIT)
        self.leads_page.ERROR_REQUIRED_FIELD_BY_TITLE_ITEM('Фамилия, имя, отчество')
        self.leads_page.ERROR_REQUIRED_FIELD_BY_TITLE_ITEM('Адрес регистрации по месту жительства')
