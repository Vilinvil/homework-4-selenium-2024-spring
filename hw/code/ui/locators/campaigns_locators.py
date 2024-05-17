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
