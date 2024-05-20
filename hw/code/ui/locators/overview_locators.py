from selenium.webdriver.common.by import By


class OverviewNewUserPageLocators:
    START_ACTIONS_WRAPPER = (By.XPATH, '//*[contains(@class, "StartActions_wrapper")]')
    START_ACTION = (By.XPATH, './/*[contains(@class, "StartAction_wrapper")]')
    BUTTON_IN_START_ACTION_WRAPPER = (By.XPATH, './/button')

    BUTTON_CREATE_CAMPAIGN = \
        (By.XPATH, '//*[contains(@class, "StartAction_wrapper")]//button//*[contains(text(),"Создать вручную")]')
    BUTTON_START_TRAINING = \
        (By.XPATH, '//*[contains(@class, "StartAction_wrapper")]//button//*[contains(text(),"Пройти обучение")]')


class OverviewPageChooseDateLocators:
    BUTTON_OPEN_DATE_CHOOSE = (By.XPATH, '//*[contains(@class, "DatePicker_datePickerButton")]')
    SIGN_OPENING_DATE_CHOOSE = (By.XPATH, '//*[contains(@class, "RangeDatePicker_layout")]')
    BUTTON_CLOSE_DATE_CHOOSE = (By.XPATH, '//*[contains(@class, "RangeDatePicker_layout")]'
                                          '//button//*[contains(text(), "Отменить")]')
    BUTTON_APPLY_DATE_CHOOSE = (By.XPATH, '//*[contains(@class, "RangeDatePicker_layout")]'
                                          '//button//*[contains(text(), "Применить")]')
    BUTTON_DATE_RANGE_TODAY = (By.XPATH, '//*[(contains(@class, "rdrStaticRangeLabel") and text()="Сегодня")]')
    BUTTON_DATE_RANGE_YESTERDAY = (By.XPATH, '//*[(contains(@class, "rdrStaticRangeLabel") and text()="Вчера")]')
    RANGE_TEXT_DATE_CHOOSE = (By.XPATH, '//*[contains(@class, "RangeDatePickerManager_rangeText")]')


class OverviewPageChooseCampaignLocators:
    BUTTON_CHOOSE_CAMPAIGNS = (By.XPATH, '//*[contains(@class, "FavoritesWidget_wrapper")]'
                                         '//button//*[contains(text(), "Выбрать кампании")]')
    SIGN_OPENING_CHOOSE_CAMPAIGNS = (By.XPATH, '//*[contains(@class, "PlansSelector_modal")]')

    INPUT_SEARCH_IN_CHOOSE_CAMPAIGNS = (By.CSS_SELECTOR, '[data-testid="search"')
    SIGN_SEARCH_NOT_FOUND_RESULTS = (By.XPATH, '//*[contains(@class, "PlansSelector_modal")]'
                                               '//*[contains(text(), "Ничего не нашлось")]')
    SIGN_SEARCH_FOUND_RESULTS = (By.XPATH, '//*[contains(@class, "PlansSelector_modal")]'
                                           '//*[contains(@class, "vkuiCheckbox__title")'
                                           ' and contains(text(), "Кампания")]')

    COUNTER_CHOOSE_CAMPAIGN = (By.XPATH, '//*[contains(@class, "PlansSelector_modal")]'
                                         '//*[contains(@class, "PlansSelector_desc")]')
    CHECKBOX_CHOOSE_CAMPAIGN = (By.XPATH, '//*[contains(@class, "PlansSelector_modal")]'
                                          '//*[contains(@class, "PlansSelector_list")]'
                                          '//*[contains(@class, "vkuiCheckbox__icon--off")]')
    CHECKBOX_CHOOSE_CAMPAIGN_FOR_TOOLTIP = (By.XPATH, '(//*[contains(@class, "PlansSelector_modal")]'
                                                      '//*[contains(@class, "PlansSelector_list")]'
                                                      '//*[contains(@class, "vkuiCheckbox__icon--off")])[6]')
    TOOLTIP_MAX_COUNT_CHOOSE_CAMPAIGN = (By.XPATH, '//*[contains(@class, "Tooltip_tooltip") and'
                                                   ' contains(text(), "Выбрано максимальное количество кампаний")]')

    BUTTON_RESET_CHOOSE_CAMPAIGN = (By.XPATH, '//*[contains(@class, "PlansSelector_modal")]'
                                              '//*[contains(@class, "vkuiButton__content") and '
                                              'contains(text(), "Сбросить")]')

    BUTTON_SAVE_CHOOSE_CAMPAIGN = (By.XPATH, '//*[contains(@class, "PlansSelector_modal")]'
                                             '//*[contains(@class, "vkuiButton__content") and '
                                             'contains(text(), "Сохранить")]')
    COUNTER_CHOOSE_CAMPAIGN_IN_MAIN_VIEW = (By.XPATH, '//*[contains(@class, "FavoritesList_listItem")]')


class OverviewPageSettingsGraphLocators:
    BUTTON_OPEN_SETTINGS_GRAPH = (By.XPATH, '//*[contains(@class, "FavoritesWidget_actions")]'
                                       '//*[contains(@class, "vkuiButton")]')
    SIGN_OPENING_CHOOSE = (By.XPATH, '//*[contains(@class, "Control_modalRoot")]')
    BUTTON_CHOOSE_CLICKS = (By.XPATH, '//*[contains(@class, "Control_modalRoot")]'
                                                     '//*[@role="button"]//*[contains(text(), "Клики")]')
    BUTTON_SAVE = (By.XPATH, '//*[contains(@class, "Control_modalRoot")]'
                                            '//*[contains(@class, "vkuiButton__content") and'
                                            ' contains(text(), "Применить")]')


class OverviewPageUsefulArticlesLocators:
    USEFUL_ARTICLES = (By.XPATH, '//*[contains(@class, "UsefulArticlesWidget_wrapper")]'
                                 '//*[contains(@class, "vkuiBaseGallery__viewport")]')
    BUTTON_CASES = (By.XPATH, '//*[@class="vkuiSegmentedControl__in"]//*[contains(text(), "Кейсы")]')
    BUTTON_NEWS = (By.XPATH, '//*[@class="vkuiSegmentedControl__in"]//*[contains(text(), "Новости")]')


class OverviewPageLocators:
    choose_date_locators = OverviewPageChooseDateLocators()
    choose_campaign_locators = OverviewPageChooseCampaignLocators()
    settings_graph_locators = OverviewPageSettingsGraphLocators()
    useful_articles_locators = OverviewPageUsefulArticlesLocators()

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
    BUTTON_LIMIT_ARTICLE = (By.CSS_SELECTOR, '[href="/help/articles/ad_limits"]')

    BUTTON_CHOOSE_BUDGET_DATE = (By.XPATH, '//*[contains(@class, "BudgetWidget")]'
                                           '//*[contains(@class, "OutcomeTypeSelector_icon")]')
    BUTTON_CHOOSE_BUDGET_DATE_YESTERDAY = (By.XPATH, '//*[contains(@class, "OutcomeTypeSelector_menuList")'
                                                     ']//*[contains(text(), "Вчера")]')

    SIGN_OPENING_MODAL_PAGE_BUDGET = (By.XPATH, '//*[contains(@class, "CreateInvoiceModal_modal")]')
    BUTTON_CLOSE_MODAL_PAGE_BUDGET = (By.CSS_SELECTOR, '.vkuiModalDismissButton')