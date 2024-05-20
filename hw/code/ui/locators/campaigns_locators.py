from selenium.webdriver.common.by import By


class CampaignsPageSharedLocators:
    # STEP 1 of full way step_by_step create campaign. Before click on button STEP1_BUTTON_CREATE_CAMPAIGN.
    STEP1_SIGN_NEW_AD_CREATE = (By.ID, 'new_ad_create')
    STEP1_BUTTON_CREATE_CAMPAIGN = (By.CSS_SELECTOR, '[data-testid="create-button"]')
    STEP1_DASHBOARD_TAB_ITEM = (By.CSS_SELECTOR, '[aria-controls="dashboardV2.plans"]')
    STEP1_GROUP_TAB_ITEM = (By.CSS_SELECTOR, '[aria-controls="dashboardV2.groups"]')
    STEP1_AD_TAB_ITEM = (By.CSS_SELECTOR, '[aria-controls="dashboardV2.ads"]')
    STEP1_BASE_TABLE = (By.CLASS_NAME, 'BaseTable')

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

    STEP4_SHORT_DESCRIPTION = (By.NAME, 'заголовок, макс. 90 символов')

    STEP4_LONG_DESCRIPTION = (By.NAME, 'Длинный текст для использования в лентах соцсетей (2000 знаков)')

    STEP4_BUTTON_SET_MEDIA = (By.XPATH, '//*[@data-testid="set-global-image" and'
                                                                        ' contains(@class, "UnionMediaContentGroup")]')
    STEP4_BUTTON_SUBMIT_MEDIA = (By.CSS_SELECTOR, '[data-testid="submit"]')


class CampaignPageLocators(CampaignsPageSharedLocators):
    STEP2_BUTTON_START_GROUP_STEP_DISABLED = (By.XPATH, '//*[@id="footer"]//button//*[contains(text(), "Продолжить")]//*[@disabled=""]')
    STEP2_SUBNAV_CAMPAIGN = (By.XPATH, '//*[@id="subnav"]//*[@data-testid="steps"]//*[contains(text(), "Настройка кампании")]')
    STEP2_SUBNAV_GROUP = (By.XPATH, '//*[@id="subnav"]//*[@data-testid="steps"]//*[contains(text(), "Группы объявлений")]')
    STEP2_SUBNAV_AD = (By.XPATH, '//*[@id="subnav"]//*[@data-testid="steps"]//*[contains(text(), "Объявления")]')
    STEP2_HEADER = (By.XPATH, '//*[@id="new_ad_create"]//section//*[contains(@class, "vkuiGroup__header")]')
    STEP2_AD_TYPE_LIST = (By.XPATH, '//*[@id="new_ad_create"]//section//*[@data-name="objective"]')

    STEP3_GEO_SECTION = (By.CSS_SELECTOR, '[data-testid=""]')
    SAVE_SNIPEPT_BUTTON = (By.XPATH, '//*[@id="footer"]//button//*[contains(text(), "Сохранить как черновик")]')
    BACK_STEP_BUTTON = (By.XPATH, '//*[@id="footer"]//button//*[contains(text(), "Назад")]')