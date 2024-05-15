from selenium.webdriver.common.by import By


class OverviewNewUserPageLocators:
    START_ACTIONS_WRAPPER = (By.XPATH, '//*[starts-with(@class, "StartActions_wrapper")]')
    START_ACTION = (By.XPATH, './/*[starts-with(@class, "StartAction_wrapper")]')
    BUTTON_IN_START_ACTION_WRAPPER = (By.XPATH, './/button')

    BUTTON_CREATE_CAMPAIGN = \
        (By.XPATH, '//*[starts-with(@class, "StartAction_wrapper")]//button//*[contains(text(),"Создать вручную")]')
    BUTTON_START_TRAINING = \
        (By.XPATH, '//*[starts-with(@class, "StartAction_wrapper")]//button//*[contains(text(),"Пройти обучение")]')


class OverviewPageLocators:
    WIDGET_CAMPAIGNS = \
        (By.XPATH, '//*[starts-with(@class, "FeedWidgetWrapper_wrapper")]//*[contains(text(), "Кампании")]')
    WIDGET_BUDGET = (By.XPATH, '//*[starts-with(@class, "FeedWidgetWrapper_wrapper")]//*[contains(text(), "Бюджет")]')
    WIDGET_LIMIT = \
        (By.XPATH, '//*[starts-with(@class, "FeedWidgetWrapper_wrapper")]//*[contains(text(), "Лимит объявлений")]')
    WIDGET_FAVOURITES = (By.XPATH, '//*[starts-with(@class, "FavoritesWidget_wrapper")]//*[contains(text(),'
                                   ' "Избранные кампании")]')
    BUTTON_CREATE_CAMPAIGN = (By.CSS_SELECTOR, '[data-testid="create-button"]')
    BUTTON_BUDGET_REPLENISH = (By.XPATH, '//*[starts-with(@class, "FeedWidgetWrapper_wrapper")]'
                                         '//button//*[contains(text(), "Пополнить")]')
    BUTTON_CHOOSE_CAMPAIGNS = (By.XPATH, '//*[starts-with(@class, "FavoritesWidget_wrapper")]'
                                         '//button//*[contains(text(), "Выбрать кампании")]')
    BUTTON_LIMIT_ARTICLE = (By.CSS_SELECTOR, '[href="/help/articles/ad_limits"]')

    SIGN_OPENING_MODAL_PAGE_BUDGET = (By.ID, "_modal_17")
    BUTTON_CLOSE_MODAL_PAGE_BUDGET = (By.CSS_SELECTOR, '.vkuiModalDismissButton')

    BUTTON_OPEN_DATE_CHOOSE = (By.XPATH, '//*[starts-with(@class, "DatePicker_datePickerButton")]')
    SIGN_OPENING_DATE_CHOOSE = (By.XPATH, '//*[starts-with(@class, "RangeDatePicker_layout")]')
    BUTTON_CLOSE_DATE_CHOOSE = (By.XPATH, '//*[starts-with(@class, "RangeDatePicker_layout")]'
                                          '//button//*[contains(text(), "Отменить")]')
    BUTTON_APPLY_DATE_CHOOSE = (By.XPATH, '//*[starts-with(@class, "RangeDatePicker_layout")]'
                                          '//button//*[contains(text(), "Применить")]')
