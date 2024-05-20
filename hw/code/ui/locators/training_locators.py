from ui.locators.campaigns_locators import CampaignsPageSharedLocators

from selenium.webdriver.common.by import By


class TrainingPageSharedLocators:
    SIGN_OPENING_MODAL_VIEW = (By.ID, '_modal_24')


class TrainingPageSiteLocators:
    BUTTON_SITE = (By.XPATH, '//*[contains(@class, "ModalRoot_componentWrapper")]'
                             '//*[@role="button"]//*[contains(text(), "Сайт")]')
    TITLE = (By.XPATH, '//*[contains(@class, "ModalRoot_componentWrapper")]'
                       '//*[contains(text(), "Как хотите учиться?")]')
    BUTTON_VIDEO = (By.XPATH, '//*[contains(@class, "ModalRoot_componentWrapper")]//*[@role="button"]'
                              '//*[contains(text(), "Смотреть видеоурок")]')
    BUTTON_ARTICLES = (By.XPATH, '//*[contains(@class, "ModalRoot_componentWrapper")]//*[@role="button"]'
                                 '//*[contains(text(), "Смотреть курс")]')
    BUTTON_STEP_BY_STEP_TRAINING = (By.XPATH, '//*[contains(@class, "ModalRoot_componentWrapper")]//*[@role="button"]'
                                              '//*[contains(text(), "Пошаговое обучение")]')

    SIGN_OPENING_VIDEO = (By.XPATH, '//iframe[contains(@class, "VideoOnboardingModal")]')


def create_rich_tooltip(message):
    return By.XPATH, f'//*[contains(@class, "RichTooltop_wrapper")]//*[contains(text(), "{message}")]'


class TrainingPageStepByStepLocators:
    # STEP 1 of full way step_by_step training. All before click on button STEP1_BUTTON_CREATE_CAMPAIGN.
    STEP1_TOOLTIP_CREATE_CAMPAIGN = create_rich_tooltip('Создание кампании')

    STEP1_BUTTON_TOOLTIP_CLOSE = (By.XPATH, '//*[contains(@class, "RichTooltop_wrapper")]'
                                            '//*[contains(@class, "RichTooltop_closeBtn")]')
    STEP1_BUTTON_CLOSE_TRAINING = (By.XPATH, '//*[contains(@class, "StopOnboardingModal_content")]'
                                             '//button//*[contains(text(), "Прервать")]')

    STEP1_BUTTON_CONTINUE_TRAINING = (By.XPATH, '//*[contains(@class, "StopOnboardingModal_content")]'
                                                '//button//*[contains(text(), "Отмена")]')

    # STEP 2 of full way step_by_step training. Settings of Campaign.
    STEP2_TOOLTIP_GOALS = (By.XPATH, '//*[contains(@class, "Info_root")]//*[contains(text(), "Выбор объекта и цели рекламы")]')
    STEP2_BUTTON_CONTINUE_GOALS = (By.XPATH, '//*[contains(@class, "Info_firstButton")]')

    STEP2_TOOLTIP_OBJECT_ADS = create_rich_tooltip("Объект рекламы")

    STEP2_TOOLTIP_SITE = create_rich_tooltip("Рекламируемый сайт") # disabled
    STEP2_BUTTON_CONTINUE = (By.XPATH, '//*[contains(@class, "RichTooltop_wrapper")]'
                                       '//button[.//*[contains(text(), "Далее")]]')

    STEP2_TOOLTIP_PIXEL = (By.XPATH, '//*[contains(@class, "RichTooltop_wrapper")]'
                                     '//*[contains(text(), "Установить пиксель") or'
                                     ' contains(text(), "Вы можете выполнить настройку пикселя в разделе Сайты")]')
    STEP2_BUTTON_BACK = (By.XPATH, '//*[contains(@class, "RichTooltop_wrapper")]//button'
                                   '//*[contains(text(), "Назад")]')

    STEP2_TOOLTIP_ACTION = create_rich_tooltip("Целевое действие")

    STEP2_TOOLTIP_OPTIMIZE_BUDGET = create_rich_tooltip("Оптимизация бюджета кампании")

    STEP2_TOOLTIP_STRATEGY = create_rich_tooltip("Стратегия ставок кампании")

    STEP2_TOOLTIP_BUDGET = create_rich_tooltip("Бюджет") # disabled

    STEP2_TOOLTIP_DATE = create_rich_tooltip("Даты проведения")

    STEP2_TOOLTIP_END_STEP = create_rich_tooltip("Кампания настроена")

    # STEP 3 of full way step_by_step training. Groups of target audience.
    STEP3_TOOLTIP_SETTINGS_TARGET_AUDIENCE = (By.XPATH, '//*[contains(@class, "Info_root")]'
                                                        '//*[contains(text(), "Настройка целевой аудитории")]')
    STEP3_BUTTON_CONTINUE_SETTINGS_TARGET_AUDIENCE = (By.XPATH, '//*[contains(@class, "Info_firstButton")]')

    STEP3_TOOLTIP_SCHEDULE = create_rich_tooltip("Расписание показа")
    STEP3_BUTTON_CONTINUE = STEP2_BUTTON_CONTINUE

    STEP3_TOOLTIP_REGIONS = create_rich_tooltip("Регионы показа") # disabled

    STEP3_TOOLTIP_PARAMETERS_AUDIENCE = create_rich_tooltip("Параметры аудитории")

    STEP3_HEADER_PARAMETERS_URL = (By.XPATH, '//*[contains(@class, "vkuiGroup__header")]//*[contains(text(), "Параметры URL")]')
    STEP3_TOOLTIP_PARAMETERS_URL = create_rich_tooltip("Параметры URL")

    STEP3_TOOLTIP_END_STEP = create_rich_tooltip("Группа объявлений готова")

    # STEP 4 of full way step_by_step training. ADS.
    STEP4_TOOLTIP_ADS = (By.XPATH, '//*[contains(@class, "Info_root")]'
                                                        '//*[contains(text(), "Оформление объявления")]')
    STEP4_BUTTON_CONTINUE_ADS = (By.XPATH, '//*[contains(@class, "Info_firstButton")]')

    STEP4_TOOLTIP_LOGO = create_rich_tooltip("Логотип") # disabled

    STEP4_TOOLTIP_TITLE = create_rich_tooltip("Заголовок") # disabled
    STEP4_BUTTON_CONTINUE = STEP2_BUTTON_CONTINUE

    STEP4_TOOLTIP_SHORT_DESCRIPTION = create_rich_tooltip("Короткое описание") # disabled

    STEP4_TOOLTIP_LONG_DESCRIPTION = create_rich_tooltip("Длинное описание") # disabled

    STEP4_TOOLTIP_HREF = create_rich_tooltip("Укажите ссылку")

    STEP4_TOOLTIP_MEDIA = create_rich_tooltip("Медиафайлы")

    STEP4_TOOLTIP_LEGAL_INFO = create_rich_tooltip("Юридическая информация")

    STEP4_TOOLTIP_PREVIEW = create_rich_tooltip("Предпросмотр")

    STEP4_TOOLTIP_END_STEP = create_rich_tooltip("Объявление оформлено")


class TrainingPageLocators:
    site_locators = TrainingPageSiteLocators()
    campaign_page_shared_locators = CampaignsPageSharedLocators()
    step_by_step_locators = TrainingPageStepByStepLocators()

    TITLE = (By.XPATH, '//*[contains(@class, "ModalRoot_componentWrapper")]'
                       '//*[contains(text(), "С чего начнём обучение?")]')
    BUTTON_TRY_LATER = (By.XPATH, '//*[contains(@class, "ModalRoot_componentWrapper")]'
                                  '//button//*[contains(text(), "Попробовать позже")]')
    BUTTON_CLOSE = (By.CLASS_NAME, 'vkuiModalDismissButton')
    CONTENT_LIST = (By.CLASS_NAME, 'vkuiModalPage__content')
