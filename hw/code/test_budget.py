import pytest

from cases import LoggedCase
from ui.pages.budget_page import BudgetPage


class TestBudget(LoggedCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_training(self, driver, config):
        self.main_page.open_budget()
        self.budget_page = BudgetPage(self.driver)

    def test_display(self):
        assert self.budget_page.TITLE
        assert self.budget_page.BUTTON_START_BUDGET_REPLENISH

        self.budget_page.BUTTON_START_BUDGET_REPLENISH.open_view()

        assert self.budget_page.TITLE_MODAL_PAGE_BUDGET
        assert self.budget_page.TITLE_CREATE_INVOICE_SUMM
        assert self.budget_page.TITLE_CREATE_INVOICE_VAT
        assert self.budget_page.BUTTON_CONTINUE_BUDGET_REPLENISH

    @pytest.fixture(scope="function")
    def setup_budget_replenish(self):
        self.budget_page.BUTTON_START_BUDGET_REPLENISH.open_view()

    def test_full_way(self, setup_budget_replenish):
        value_invoice = '600'
        value_invoice_with_vat = '500'

        self.budget_page.INPUT_AMOUNT.write(value_invoice)

        assert self.budget_page.INPUT_AMOUNT_WITHOUT_VAT.get_value().startswith(value_invoice_with_vat)

        self.budget_page.INPUT_AMOUNT_WITHOUT_VAT.write(value_invoice_with_vat)

        assert self.budget_page.INPUT_AMOUNT.get_value().startswith(value_invoice)

        self.budget_page.click(self.budget_page.BUTTON_CONTINUE_BUDGET_REPLENISH)

        assert self.budget_page.SIGN_OPENING_INVOICE_END

    def test_error_min_sum(self, setup_budget_replenish):
        self.budget_page.INPUT_AMOUNT.write('599')
        self.budget_page.click(self.budget_page.BUTTON_CONTINUE_BUDGET_REPLENISH)
        assert self.budget_page.ALERT_MIN_SUMM_REPLENISH

        self.budget_page.INPUT_AMOUNT_WITHOUT_VAT.write('499')
        self.budget_page.click(self.budget_page.BUTTON_CONTINUE_BUDGET_REPLENISH)
        assert self.budget_page.ALERT_MIN_SUMM_REPLENISH

    def test_hint_min_summ(self, setup_budget_replenish):
        self.budget_page.HINT_MIN_SUMM_TRIGGER.hover()
        assert self.budget_page.HINT_MIN_SUMM

    def test_error_big_summ(self, setup_budget_replenish):
        self.budget_page.INPUT_AMOUNT.write('200001')
        self.budget_page.click(self.budget_page.BUTTON_CONTINUE_BUDGET_REPLENISH)
        assert self.budget_page.ALERT_MAX_SUMM_REPLENISH

    def test_incorrect_input(self, setup_budget_replenish):
        incorrect_value = 'asdf700.02asdf'
        expected_value = '700,02 ₽'

        self.budget_page.INPUT_AMOUNT.write(incorrect_value)
        assert self.budget_page.INPUT_AMOUNT.get_value() == expected_value

        self.budget_page.INPUT_AMOUNT_WITHOUT_VAT.write(incorrect_value)
        assert self.budget_page.INPUT_AMOUNT_WITHOUT_VAT.get_value() == expected_value
