from ui.pages.base_page import PageWithModalView
from ui.locators.budget_locators import BudgetPageLocators


class BudgetPage(PageWithModalView):
    url = "https://ads.vk.com/hq/budget/transactions"
    locators = BudgetPageLocators()
