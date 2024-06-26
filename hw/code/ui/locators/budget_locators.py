from selenium.webdriver.common.by import By

HINT_MIN_SUMM_URL = "https://ads.vk.com/help/articles/billing#min"


class BudgetPageLocators:
    BUTTON_BUDGET_SECTION = (By.CSS_SELECTOR, '[data-entityid="budget"]')
    TITLE = (By.XPATH, '//*[@id="budget"]//*[contains(text(), "Транзакций пока нет")]')
    BUTTON_START_BUDGET_REPLENISH = (By.XPATH, '//*[@id="budget"]//button//*[contains(text(), "Пополнить счёт")]')
    SIGN_OPENING_MODAL_PAGE_BUDGET = (By.XPATH, '//*[contains(@class, "CreateInvoiceModal_modal")]')
    BUTTON_CLOSE_MODAL_PAGE_BUDGET = (By.CSS_SELECTOR, '.vkuiModalDismissButton')

    TITLE_MODAL_PAGE_BUDGET = (By.XPATH, '//*[contains(@class, "CreateInvoiceModal_modal")]'
                                         '//*[contains(@class, "CreateInvoiceModal_desc")]'
                                         '//*[contains(text(), "Пополнение счёта")]')
    TITLE_CREATE_INVOICE_SUMM = (By.XPATH, '//*[contains(@class, "CreateInvoiceModal_modal")]'
                                           '//*[contains(@class, "CreateInvoiceModal_top")]'
                                           '//*[contains(text(), "Cумма к оплате")]')
    TITLE_CREATE_INVOICE_VAT = (By.XPATH, '//*[contains(@class, "CreateInvoiceModal_modal")]'
                                          '//*[contains(@class, "CreateInvoiceModal_top")]'
                                          '//*[contains(text(), "Сумма, поступающая на ваш счёт (НДС — 20%)")]')
    BUTTON_CONTINUE_BUDGET_REPLENISH = (By.XPATH, '//*[contains(@class, "CreateInvoiceModal_modal")]'
                                                  '//button//*[contains(text(), "Пополнить счёт")]')

    INPUT_AMOUNT = (By.NAME, 'amount')
    INPUT_AMOUNT_WITHOUT_VAT = (By.NAME, 'amountWithoutVat')
    ALERT_MIN_SUMM_REPLENISH = (By.XPATH, '//*[contains(@class, "CreateInvoiceModal_modal")]'
                                          '//*[@role="alert" and contains(text(), "Минимальная сумма 600,00")]')

    HINT_MIN_SUMM_TRIGGER = (By.XPATH, '//*[contains(@class, "CreateInvoiceModal_modal")]'
                                       '//*[contains(@class, "Hint_hintTrigger")]')
    TOOLTIP_MIN_SUMM = (By.XPATH, '//*[contains(@class, "Tooltip_tooltipContainer")]'
                                  '//*[contains(text(), "Сумма к оплате")]')
    HINT_MIN_SUMM_REF = (By.CSS_SELECTOR, f'[href="{HINT_MIN_SUMM_URL}"]')

    ALERT_MAX_SUMM_REPLENISH = (By.XPATH, '//*[contains(@class, "CreateInvoiceModal_modal")]'
                                          '//*[@role="alert" and contains(text(), "уменьшите сумму")]')

    SIGN_OPENING_INVOICE_END_IFRAME = \
        (By.XPATH, '//*[contains(@class, "CreateInvoiceModal")]//iframe[contains(@class, "CreateInvoiceModal")]')

    HINT_MIN_SUMM_TRIGGER = (By.XPATH, '//*[contains(@class, "CreateInvoiceModal_modal")]'
                                       '//*[contains(@class, "Hint_hintTrigger")]')

    HINT_MIN_SUMM = (By.XPATH, '//*[contains(@class, "Tooltip_tooltipContainer")]'
                               '//*[contains(text(), "Подробнее о минимальном платеже и НДС")]')
