from selenium.webdriver.common.by import By


class BudgetPageLocators:
    BUTTON_BUDGET_SECTION = (By.CSS_SELECTOR, '[data-entityid="budget"]')
    TITLE = (By.XPATH, '//*[@id="budget"]//*[contains(text(), "Транзакций пока нет")]')
    BUTTON_START_BUDGET_REPLENISH = (By.XPATH, '//*[@id="budget"]//button//*[contains(text(), "Пополнить счёт")]')
    SIGN_OPENING_MODAL_PAGE_BUDGET = (By.ID, "_modal_17")
    BUTTON_CLOSE_MODAL_PAGE_BUDGET = (By.CSS_SELECTOR, '.vkuiModalDismissButton')

    TITLE_MODAL_PAGE_BUDGET = (By.XPATH, '//*[@id="_modal_17"]//*[starts-with(@class, "CreateInvoiceModal_desc")]'
                                         '//*[contains(text(), "Пополнение счёта")]')
    TITLE_CRETE_INVOICE_SUMM = (By.XPATH, '//*[@id="_modal_17"]//*[starts-with(@class, "CreateInvoiceModal_top")]'
                                          '//*[contains(text(), "Cумма к оплате")]')
    TITLE_CRETE_INVOICE_TAX = (By.XPATH, '//*[@id="_modal_17"]//*[starts-with(@class, "CreateInvoiceModal_top")]'
                                         '//*[contains(text(), "Сумма, поступающая на ваш счёт (НДС — 20%)")]')
    BUTTON_CONTINUE_BUDGET_REPLENISH = (By.XPATH, '//*[@id="_modal_17"]//button//*[contains(text(), "Пополнить счёт")]')
