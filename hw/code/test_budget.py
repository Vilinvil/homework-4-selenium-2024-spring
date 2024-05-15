import pytest

from cases import LoggedCase
from ui.pages.budget_page import BudgetPage


class TestBudget(LoggedCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_training(self, driver, config):
        self.main_page.click(self.main_page.locators.NAV_BUTTON_BUDGET_SECTION)
        self.budget_page = BudgetPage(self.driver)

    def test_display(self):
        assert self.budget_page.find(self.budget_page.locators.TITLE).is_displayed()
        assert self.budget_page.find(self.budget_page.locators.BUTTON_START_BUDGET_REPLENISH).is_displayed()

        self.budget_page.open_modal_view(self.budget_page.locators.BUTTON_START_BUDGET_REPLENISH,
                                         self.budget_page.locators.SIGN_OPENING_MODAL_PAGE_BUDGET)

        assert self.budget_page.find(self.budget_page.locators.TITLE_MODAL_PAGE_BUDGET).is_displayed()
        assert self.budget_page.find(self.budget_page.locators.TITLE_CRETE_INVOICE_SUMM).is_displayed()
        assert self.budget_page.find(self.budget_page.locators.TITLE_CRETE_INVOICE_TAX).is_displayed()
        assert self.budget_page.find(self.budget_page.locators.BUTTON_CONTINUE_BUDGET_REPLENISH).is_displayed()
