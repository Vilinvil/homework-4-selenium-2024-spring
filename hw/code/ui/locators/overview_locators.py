from selenium.webdriver.common.by import By


class OverviewNewUserPageLocators:
    START_ACTIONS_WRAPPER = (By.XPATH, '//*[contains(@class, "StartActions_wrapper")]')
    START_ACTION = (By.XPATH, './/*[contains(@class, "StartAction_wrapper")]')
    BUTTON_IN_START_ACTION_WRAPPER = (By.XPATH, './/button')

    BUTTON_CREATE_CAMPAIGN = \
        (By.XPATH, '//*[contains(@class, "StartAction_wrapper")]//button//*[contains(text(),"Создать вручную")]')
    BUTTON_START_TRAINING = \
        (By.XPATH, '//*[contains(@class, "StartAction_wrapper")]//button//*[contains(text(),"Пройти обучение")]')


class OverviewPageDateChoose:
    BUTTON_OPEN_DATE_CHOOSE = (By.XPATH, '//*[contains(@class, "DatePicker_datePickerButton")]')
    SIGN_OPENING_DATE_CHOOSE = (By.XPATH, '//*[contains(@class, "RangeDatePicker_layout")]')
    BUTTON_CLOSE_DATE_CHOOSE = (By.XPATH, '//*[contains(@class, "RangeDatePicker_layout")]'
                                          '//button//*[contains(text(), "Отменить")]')
    BUTTON_APPLY_DATE_CHOOSE = (By.XPATH, '//*[contains(@class, "RangeDatePicker_layout")]'
                                          '//button//*[contains(text(), "Применить")]')
    BUTTON_DATE_RANGE_TODAY = (By.XPATH, '//*[(contains(@class, "rdrStaticRangeLabel") and text()="Сегодня")]')
    BUTTON_DATE_RANGE_YESTERDAY = (By.XPATH, '//*[(contains(@class, "rdrStaticRangeLabel") and text()="Вчера")]')
    RANGE_TEXT_DATE_CHOOSE = (By.XPATH, '//*[contains(@class, "RangeDatePickerManager_rangeText")]')


class OverviewPageChooseCampaign:
    INPUT_SEARCH_IN_CHOOSE_CAMPAIGNS = (By.CSS_SELECTOR, '[data-testid="search"')
    SIGN_SEARCH_NOT_FOUND_RESULTS = (By.XPATH, '//*[@id="_modal_30"]//*[contains(text(), "Ничего не нашлось")]')
    SIGN_SEARCH_FOUND_RESULTS = (By.XPATH, '//*[@id="_modal_30"]//*[contains(@class, "vkuiCheckbox__title")'
                                           ' and contains(text(), "Кампания")]')
    SIGN_OPENING_CHOOSE_CAMPAIGNS = (By.ID, '_modal_30')

    COUNTER_CHOOSE_CAMPAIGN = (By.XPATH, '//*[@id="_modal_30"]//*[contains(@class, "PlansSelector_desc")]')
    CHECKBOX_CHOOSE_CAMPAIGN = (By.XPATH, '//*[@id="_modal_30"]//*[contains(@class, "PlansSelector_list")]'
                                          '//*[contains(@class, "vkuiCheckbox__icon--off")]')
    CHECKBOX_CHOOSE_CAMPAIGN_FOR_TOOLTIP = (By.XPATH, '(//*[@id="_modal_30"]//*[contains(@class, "PlansSelector_list")]'
                                                      '//*[contains(@class, "vkuiCheckbox__icon--off")])[6]')
    TOOLTIP_MAX_COUNT_CHOOSE_CAMPAIGN = (By.XPATH, '//*[contains(@class, "Tooltip_tooltip") and'
                                                   ' contains(text(), "Выбрано максимальное количество кампаний")]')

    BUTTON_RESET_CHOOSE_CAMPAIGN = (By.XPATH, '//*[@id="_modal_30"]//*[contains(@class, "vkuiButton__content") and '
                                              'contains(text(), "Сбросить")]')

    BUTTON_SAVE_CHOOSE_CAMPAIGN = (By.XPATH, '//*[@id="_modal_30"]//*[contains(@class, "vkuiButton__content") and '
                                             'contains(text(), "Сохранить")]')
    COUNTER_CHOOSE_CAMPAIGN_IN_MAIN_VIEW = (By.XPATH, '//*[contains(@class, "FavoritesList_listItem")]')


class OverviewPageLocators(OverviewPageChooseCampaign, OverviewPageDateChoose):
    WIDGET_CAMPAIGNS = \
        (By.XPATH, '//*[contains(@class, "FeedWidgetWrapper_wrapper")]//*[contains(text(), "Кампании")]')
    WIDGET_BUDGET = (By.XPATH, '//*[contains(@class, "FeedWidgetWrapper_wrapper")]//*[contains(text(), "Бюджет")]')
    WIDGET_LIMIT = \
        (By.XPATH, '//*[contains(@class, "FeedWidgetWrapper_wrapper")]//*[contains(text(), "Лимит объявлений")]')
    WIDGET_FAVOURITES = (By.XPATH, '//*[contains(@class, "FavoritesWidget_wrapper")]//*[contains(text(),'
                                   ' "Избранные кампании")]')
    BUTTON_CREATE_CAMPAIGN = (By.CSS_SELECTOR, '[data-testid="create-button"]')
    BUTTON_BUDGET_REPLENISH = (By.XPATH, '//*[contains(@class, "FeedWidgetWrapper_wrapper")]'
                                         '//button//*[contains(text(), "Пополнить")]')
    BUTTON_CHOOSE_CAMPAIGNS = (By.XPATH, '//*[contains(@class, "FavoritesWidget_wrapper")]'
                                         '//button//*[contains(text(), "Выбрать кампании")]')
    BUTTON_LIMIT_ARTICLE = (By.CSS_SELECTOR, '[href="/help/articles/ad_limits"]')

    SIGN_OPENING_MODAL_PAGE_BUDGET = (By.ID, "_modal_17")
    BUTTON_CLOSE_MODAL_PAGE_BUDGET = (By.CSS_SELECTOR, '.vkuiModalDismissButton')
