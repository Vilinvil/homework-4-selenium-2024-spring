from ui.pages.base_page import PageWithView, PageWithRedirectWindow
from ui.locators.budget_locators import BudgetPageLocators
from ui.pages.base_page_functionality import add_hover, add_write, add_get_value
from ui.pages.base_page import add_open_view


class BudgetPage(PageWithView, PageWithRedirectWindow):
    url = "https://ads.vk.com/hq/budget/transactions"
    locators = BudgetPageLocators()

    @property
    def TITLE(self):
        return self.find_with_check_visibility(self.locators.TITLE)

    @property
    def TITLE_MODAL_PAGE_BUDGET(self):
        return self.find_with_check_visibility(self.locators.TITLE_MODAL_PAGE_BUDGET)

    @property
    def TITLE_CREATE_INVOICE_SUMM(self):
        return self.find_with_check_visibility(self.locators.TITLE_CREATE_INVOICE_SUMM)

    @property
    def TITLE_CREATE_INVOICE_VAT(self):
        return self.find_with_check_visibility(self.locators.TITLE_CREATE_INVOICE_VAT)

    @property
    def BUTTON_CONTINUE_BUDGET_REPLENISH(self):
        return self.find_with_check_visibility(self.locators.BUTTON_CONTINUE_BUDGET_REPLENISH)

    @property
    def ALERT_MIN_SUMM_REPLENISH(self):
        return self.find_with_check_visibility(self.locators.ALERT_MIN_SUMM_REPLENISH)

    @property
    def ALERT_MAX_SUMM_REPLENISH(self):
        return self.find_with_check_visibility(self.locators.ALERT_MAX_SUMM_REPLENISH)

    @property
    def SIGN_OPENING_INVOICE_END(self):
        return self.find_with_check_visibility(self.locators.SIGN_OPENING_INVOICE_END_IFRAME)

    @property
    @add_open_view(BudgetPageLocators.SIGN_OPENING_MODAL_PAGE_BUDGET)
    def BUTTON_START_BUDGET_REPLENISH(self):
        return self.find_with_check_visibility(self.locators.BUTTON_START_BUDGET_REPLENISH)

    @property
    @add_write
    @add_get_value
    def INPUT_AMOUNT(self):
        return self.find_with_check_visibility(self.locators.INPUT_AMOUNT)

    @property
    @add_write
    @add_get_value
    def INPUT_AMOUNT_WITHOUT_VAT(self):
        return self.find_with_check_visibility(self.locators.INPUT_AMOUNT_WITHOUT_VAT)

    @property
    @add_hover
    def HINT_MIN_SUMM_TRIGGER(self):
        return self.find_with_check_visibility(self.locators.HINT_MIN_SUMM_TRIGGER)

    @property
    def HINT_MIN_SUMM(self):
        return self.find_with_check_visibility(self.locators.HINT_MIN_SUMM)
