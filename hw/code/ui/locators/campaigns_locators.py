from selenium.webdriver.common.by import By


class CampaignsPageSharedLocators:
    # STEP 1 of full way step_by_step create campaign. Before click on button STEP1_BUTTON_CREATE_CAMPAIGN.
    STEP1_SIGN_NEW_AD_CREATE = (By.ID, 'new_ad_create')
    STEP1_BUTTON_CREATE_CAMPAIGN = (By.CSS_SELECTOR, '[data-testid="create-button"]')

    # STEP 2 of full way step_by_step create campaign. Settings of Campaign.
    STEP2_BUTTON_CHOOSE_SITE = (By.CSS_SELECTOR, '[data-id="site_conversions"]')
    STEP2_ALERT_WRONG_URL = (By.XPATH, '//*[contains(@class, "SiteObject_formItemWrapper")]'
                                       '//*[@role="alert"]//*[contains(text(), "Неверный формат URL")]')
    STEP2_INPUT_SITE_URL = (By.XPATH, '//*[contains(@class, "SiteObject_formItemWrapper")]//input')

    STEP2_INPUT_BUDGET = (By.CSS_SELECTOR, '[data-testid="targeting-not-set"]')

    STEP2_BUTTON_START_GROUP_STEP = (By.XPATH, '//*[@id="footer"]//button//*[contains(text(), "Продолжить")]')

    # STEP 3 of full way step_by_step training. Groups of target audience.
    STEP3_INPUT_SEARCH_REGION = (By.CSS_SELECTOR, '[data-testid="search"]')
    STEP3_CHECKBOXES_REGION = (By.XPATH, '//*[contains(@class, "RegionsTree_group")]'
                                         '//*[contains(@class, "vkuiCheckbox__icon--off")]')

    STEP3_BUTTON_START_ADS_STEP = (By.XPATH, '//*[@id="footer"]//button//*[contains(text(), "Продолжить")]')

    # STEP 4 of full way step_by_step training. ADS.
    STEP4_BUTTON_SET_GLOBAL_IMAGE = (By.XPATH, '//*[@data-testid="set-global-image" and'
                                               ' contains(@class, "UploadMediaButton_buttonLogo")]')
    STEP4_IMAGE_ITEM = (By.XPATH, '//*[contains(@class, "ImageItems_image")]')

    STEP4_INPUT_TITLE = (By.NAME, 'заголовок, макс. 40 символов')

    STEP4_INPUT_SHORT_DESCRIPTION = (By.NAME, 'заголовок, макс. 90 символов')

    STEP4_INPUT_LONG_DESCRIPTION = (By.NAME, 'Длинный текст для использования в лентах соцсетей (2000 знаков)')

    STEP4_BUTTON_SET_MEDIA = (By.XPATH, '//*[@data-testid="set-global-image" and'
                                                                        ' contains(@class, "UnionMediaContentGroup")]')
    STEP4_BUTTON_SUBMIT_MEDIA = (By.CSS_SELECTOR, '[data-testid="submit"]')

    # not shared locators for campaign tests
    TAB_TARGETED_ACTIONS = (By.ID, 'tab_conversion')
    TAB_BRANDING = (By.ID, 'tab_branding')
    BUTTON_MOBILE_APPS = (By.CSS_SELECTOR, '[data-id="mobapps"]')
    BUTTON_CATALOG = (By.CSS_SELECTOR, '[data-id="ecomm"]')
    BUTTON_SOCIAL = (By.CSS_SELECTOR, '[data-id="social"]')
    BUTTON_OK = (By.CSS_SELECTOR, '[data-id="odkl"]')
    BUTTON_LEAD_ADS = (By.CSS_SELECTOR, '[data-id="leadads"]')
    BUTTON_MINI_APPS = (By.CSS_SELECTOR, '[data-id="miniapps"]')
    BUTTON_MUSIC = (By.CSS_SELECTOR, '[data-id="socialmusic"]')
    BUTTON_VIDEO = (By.CSS_SELECTOR, '[data-id="socialvideo"]')
    BUTTON_DZEN = (By.CSS_SELECTOR, '[data-id="dzen"]')

    BUTTON_CLOSE_TRAINING = (By.XPATH, '//*[contains(text(),"Попробовать позже")]')
    BUTTON_CONTINUE = (By.XPATH, '//*[@id="footer"]//button//*[contains(text(), "Продолжить")]')

    FIELD_GOAL_ACTION = (By.CSS_SELECTOR, '[data-testid="priced-goal"]')
    FIELD_OPTIMIZE_BUDGET = (By.CSS_SELECTOR, '[data-name="budgetOptimization"]')
    FIELD_BETTING_STRATEGY = (By.CSS_SELECTOR, '[data-testid="autobidding-mode"]')
    FIELD_BUDGET = (By.CSS_SELECTOR, '[data-testid="targeting-not-set"]')
    FIELD_START_DATE = (By.CSS_SELECTOR, '[data-testid="start-date"]')
    CAMPAIGN_NAME_FIELD = (By.XPATH, "//*[contains(@class, 'EditableTitle')]")
    CAMPAIGN_NAME_FIELD_EDIT = (By.XPATH, "//*[contains(@class, 'EditableTitle')]//textarea")

    GROUP_NAME_FIELD = (By.XPATH, "//*[contains(@class, 'EditableTitle')]")
    GROUP_NAME_FIELD_EDIT = (By.XPATH, "//*[contains(@class, 'EditableTitle')]//textarea")
    GROUP_FIELD_START_DATE = (By.CSS_SELECTOR, '[data-testid="start-date"]')
    GEO_TAB = (By.CSS_SELECTOR, '[data-testid="section-geo"]')
    DEMOGRAPHY_TAB = (By.CSS_SELECTOR, '[data-testid="section-demography"]')
    AUDIENCE_TAB = (By.CSS_SELECTOR, '[data-testid="section-audience"]')
    INTERESTS_TAB = (By.CSS_SELECTOR, '[data-testid="section-interests"]')
    DEVICES_TAB = (By.CSS_SELECTOR, '[data-testid="section-devices"]')
    URL_TAB = (By.CSS_SELECTOR, '[data-testid="section-urlUtm"]')
    PLACEMENT_TAB = (By.CSS_SELECTOR, '[data-testid="section-placement"]')
    MOSCOW_REGION_BUTTON = (By.XPATH, '//*[@data-testid="section-geo"]//button//*[contains(text(), "Москва")]')

    INTERESTS_TAB_INTERESTS_SUBTAB = (By.XPATH, "//*[contains(@class, 'InterestsSubSection')]")
    INTERESTS_INPUT = (By.XPATH, '//*[@id="10_3"]')
    INTERESTS_AUTOCOMPLETED_VARIANT = (By.XPATH, '//*[contains(text(),"Компьютерная техника и программы")]')
