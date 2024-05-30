import pytest

from cases import LoggedCase
from ui.pages.budget_page import BudgetPage


class TestBudget(LoggedCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_training(self, driver, config):
        self.main_page.open_budget()
        self.budget_page = BudgetPage(self.driver)

    def test_display(self):
        assert self.budget_page.find_title()
        assert self.budget_page.find_button_start_budget_replenish()

        self.budget_page.open_modal_budget_replenish()

        assert self.budget_page.find_title_modal_page_budget()
        assert self.budget_page.find_title_create_invoice_summ()
        assert self.budget_page.find_title_create_invoice_vat()
        assert self.budget_page.find_button_continue_budget_replenish()

    @pytest.fixture(scope="function")
    def setup_budget_replenish(self):
        self.budget_page.open_modal_budget_replenish()

    def test_error_min_sum(self, setup_budget_replenish):
        self.budget_page.write_amount('599')
        self.budget_page.click_button_continue_budget_replenish()
        assert self.budget_page.find_alert_min_summ_replenish()

        self.budget_page.write_amount_without_vat('499')
        self.budget_page.click_button_continue_budget_replenish()
        assert self.budget_page.find_alert_min_summ_replenish()

    def test_error_big_summ(self, setup_budget_replenish):
        self.budget_page.write_amount('200001')
        self.budget_page.click_button_continue_budget_replenish()
        assert self.budget_page.find_alert_max_summ_replenish()

    def test_incorrect_input(self, setup_budget_replenish):
        incorrect_value = 'asdf700.02asdf'
        expected_value = '700,02 ₽'

        self.budget_page.write_amount(incorrect_value)
        assert self.budget_page.get_value_amount() == expected_value

        self.budget_page.write_amount_without_vat(incorrect_value)
        assert self.budget_page.get_value_amount_without_vat() == expected_value

    def test_full_way(self, setup_budget_replenish):
        value_invoice = '600'
        value_invoice_with_vat = '500'

        self.budget_page.write_amount(value_invoice)

        assert self.budget_page.get_value_amount_without_vat().startswith(value_invoice_with_vat)

        self.budget_page.write_amount_without_vat(value_invoice_with_vat)

        assert self.budget_page.get_value_amount().startswith(value_invoice)

        self.budget_page.click_button_continue_budget_replenish()

        assert self.budget_page.find_opening_invoice_end()
