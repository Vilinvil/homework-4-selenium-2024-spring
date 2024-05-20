from ui.pages.base_page import PageWithModalView, PageWithRedirectWindow
from ui.locators.budget_locators import BudgetPageLocators


class BudgetPage(PageWithModalView, PageWithRedirectWindow):
    url = "https://ads.vk.com/hq/budget/transactions"
    locators = BudgetPageLocators()
