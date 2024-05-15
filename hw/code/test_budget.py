import pytest

from cases import LoggedCase
from utils.redirect_window import redirect_window
from ui.pages.budget_page import BudgetPage
from ui.locators.budget_locators import HINT_MIN_SUMM_URL

from selenium.webdriver.support import expected_conditions as EC


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
        assert self.budget_page.find(self.budget_page.locators.TITLE_CRETE_INVOICE_VAT).is_displayed()
        assert self.budget_page.find(self.budget_page.locators.BUTTON_CONTINUE_BUDGET_REPLENISH).is_displayed()

        self.budget_page.hover_wrapper(self.budget_page.locators.HINT_MIN_SUMM_TRIGGER)
        assert self.budget_page.find(self.budget_page.locators.TOOLTIP_MIN_SUMM).is_displayed()

    def test_error_min_sum(self):
        self.budget_page.open_modal_view(self.budget_page.locators.BUTTON_START_BUDGET_REPLENISH,
                                         self.budget_page.locators.SIGN_OPENING_MODAL_PAGE_BUDGET)

        self.budget_page.write_input(self.budget_page.locators.INPUT_AMOUNT, '599')
        self.budget_page.click(self.budget_page.locators.BUTTON_CONTINUE_BUDGET_REPLENISH)
        assert self.budget_page.find(self.budget_page.locators.ALERT_MIN_SUMM_REPLENISH).is_displayed()

        self.budget_page.write_input(self.budget_page.locators.INPUT_AMOUNT_WITHOUT_VAT, '499')
        self.budget_page.click(self.budget_page.locators.BUTTON_CONTINUE_BUDGET_REPLENISH)
        assert self.budget_page.find(self.budget_page.locators.ALERT_MIN_SUMM_REPLENISH).is_displayed()

    def test_hint_min_summ(self):
        self.budget_page.open_modal_view(self.budget_page.locators.BUTTON_START_BUDGET_REPLENISH,
                                         self.budget_page.locators.SIGN_OPENING_MODAL_PAGE_BUDGET)

        self.budget_page.hover_wrapper(self.budget_page.locators.HINT_MIN_SUMM_TRIGGER)

        redirect_window(self.budget_page, self.budget_page.locators.HINT_MIN_SUMM_REF)
        assert self.budget_page.wait().until(EC.url_to_be(HINT_MIN_SUMM_URL))

    def test_error_big_summ(self):
        self.budget_page.open_modal_view(self.budget_page.locators.BUTTON_START_BUDGET_REPLENISH,
                                         self.budget_page.locators.SIGN_OPENING_MODAL_PAGE_BUDGET)

        self.budget_page.write_input(self.budget_page.locators.INPUT_AMOUNT, '200001')
        self.budget_page.click(self.budget_page.locators.BUTTON_CONTINUE_BUDGET_REPLENISH)
        assert self.budget_page.find(self.budget_page.locators.ALERT_MAX_SUMM_REPLENISH).is_displayed()

        # TODO CREATE REPORT IN ADS.VK.COM
        # self.budget_page.write_input(self.budget_page.locators.INPUT_AMOUNT_WITHOUT_VAT, '166667')
        # self.budget_page.click(self.budget_page.locators.BUTTON_CONTINUE_BUDGET_REPLENISH)
        # assert self.budget_page.find(self.budget_page.locators.ALERT_MAX_SUMM_REPLENISH).is_displayed()

    def test_incorrect_input(self):
        self.budget_page.open_modal_view(self.budget_page.locators.BUTTON_START_BUDGET_REPLENISH,
                                         self.budget_page.locators.SIGN_OPENING_MODAL_PAGE_BUDGET)

        incorrect_value = 'asdf700.02asdf'
        expected_value = '700,02 ₽'

        self.budget_page.write_input(self.budget_page.locators.INPUT_AMOUNT,incorrect_value )
        assert self.budget_page.find(self.budget_page.locators.INPUT_AMOUNT).get_attribute('value') == expected_value

        self.budget_page.write_input(self.budget_page.locators.INPUT_AMOUNT_WITHOUT_VAT, incorrect_value)
        assert (self.budget_page.find(self.budget_page.locators.INPUT_AMOUNT_WITHOUT_VAT).get_attribute('value')
                == expected_value)

    def test_full_way(self):
        self.budget_page.open_modal_view(self.budget_page.locators.BUTTON_START_BUDGET_REPLENISH,
                                         self.budget_page.locators.SIGN_OPENING_MODAL_PAGE_BUDGET)

        value_invoice = '600'
        value_invoice_with_vat = '500'

        self.budget_page.write_input(self.budget_page.locators.INPUT_AMOUNT, value_invoice)

        assert (self.budget_page.find(self.budget_page.locators.INPUT_AMOUNT_WITHOUT_VAT).
                get_attribute('value').startswith(value_invoice_with_vat))

        self.budget_page.write_input(self.budget_page.locators.INPUT_AMOUNT_WITHOUT_VAT, value_invoice_with_vat)

        assert (self.budget_page.find(self.budget_page.locators.INPUT_AMOUNT).
                get_attribute('value').startswith(value_invoice))

        self.budget_page.click(self.budget_page.locators.BUTTON_CONTINUE_BUDGET_REPLENISH)

        (self.budget_page.wait().
         until(EC.visibility_of_element_located(self.budget_page.locators.SIGN_OPENING_INVOICE_END_IFRAME)))
