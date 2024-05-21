from ui.pages.base_page import PageWithlView, PageWithRedirectWindow
from ui.locators.budget_locators import BudgetPageLocators, HINT_MIN_SUMM_URL


class BudgetPage(PageWithlView, PageWithRedirectWindow):
    url = "https://ads.vk.com/hq/budget/transactions"
    locators = BudgetPageLocators()

    def find_title(self):
        return self.find_with_check_visibility(self.locators.TITLE)

    def find_button_start_budget_replenish(self):
        return self.find_with_check_visibility(self.locators.BUTTON_START_BUDGET_REPLENISH)

    def find_title_modal_page_budget(self):
        return self.find_with_check_visibility(self.locators.TITLE_MODAL_PAGE_BUDGET)

    def find_title_create_invoice_summ(self):
        return self.find_with_check_visibility(self.locators.TITLE_CRETE_INVOICE_SUMM)

    def find_title_create_invoice_vat(self):
        return self.find_with_check_visibility(self.locators.TITLE_CRETE_INVOICE_VAT)

    def find_button_continue_budget_replenish(self):
        return self.find_with_check_visibility(self.locators.BUTTON_CONTINUE_BUDGET_REPLENISH)

    def find_tooltip_min_summ(self):
        return self.find_with_check_visibility(self.locators.TOOLTIP_MIN_SUMM)

    def find_alert_min_summ_replenish(self):
        return self.find_with_check_visibility(self.locators.ALERT_MIN_SUMM_REPLENISH)

    def find_alert_max_summ_replenish(self):
        return self.find_with_check_visibility(self.locators.ALERT_MAX_SUMM_REPLENISH)

    def find_opening_invoice_end(self):
        return self.find_with_check_visibility(self.locators.SIGN_OPENING_INVOICE_END_IFRAME)

    def open_modal_budget_replenish(self):
        self.open_view(self.locators.BUTTON_START_BUDGET_REPLENISH, self.locators.SIGN_OPENING_MODAL_PAGE_BUDGET)

    def hover_hint_min_summ_trigger(self):
        self.hover_wrapper(self.locators.HINT_MIN_SUMM_TRIGGER)

    def write_amount(self, amount):
        self.write_input(self.locators.INPUT_AMOUNT, amount)

    def write_amount_without_vat(self, amount):
        self.write_input(self.locators.INPUT_AMOUNT_WITHOUT_VAT, amount)

    def click_button_continue_budget_replenish(self):
        self.click(self.locators.BUTTON_CONTINUE_BUDGET_REPLENISH)

    def redirect_min_summ_ref(self):
        self.redirect_window(self.locators.HINT_MIN_SUMM_REF)

    def check_url_hint_min_summ(self):
        return self.check_url(HINT_MIN_SUMM_URL)

    def get_value_amount(self):
        return self.find(self.locators.INPUT_AMOUNT).get_attribute('value')

    def get_value_amount_without_vat(self):
        return self.find(self.locators.INPUT_AMOUNT_WITHOUT_VAT).get_attribute('value')
