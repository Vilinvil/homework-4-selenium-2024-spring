from ui.pages.base_page import BasePage
from ui.locators.campaigns_locators import CampaignsPageSharedLocators, CampaignPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class CampaignSharedPage(BasePage):
    url = "https://ads.vk.com/hq/dashboard/ad_plans"
    locators_shared = CampaignsPageSharedLocators()

    def click_create_campaign(self):
        self.click(self.locators_shared.STEP1_BUTTON_CREATE_CAMPAIGN)

    def click_choose_site(self):
        self.click(self.locators_shared.STEP2_BUTTON_CHOOSE_SITE)

    def input_site_url(self, url):
        self.write_input(self.locators_shared.STEP2_INPUT_SITE_URL, url)

    def input_budget(self, budget):
        self.write_input(self.locators_shared.STEP2_INPUT_BUDGET, budget)

    def click_start_group_step(self):
        self.click(self.locators_shared.STEP2_BUTTON_START_GROUP_STEP)

    def choose_region_by_name(self, region_name):
        self.write_input(self.locators_shared.STEP3_INPUT_SEARCH_REGION, region_name)
        self.click(self.locators_shared.STEP3_CHECKBOXES_REGION)

    def click_start_ads_step(self):
        self.click(self.locators_shared.STEP3_BUTTON_START_ADS_STEP)

    def set_image(self):
        self.click(self.locators_shared.STEP4_BUTTON_SET_GLOBAL_IMAGE)
        self.click(self.locators_shared.STEP4_IMAGE_ITEM)

    def input_title(self, title):
        self.write_input(self.locators_shared.STEP4_INPUT_TITLE, title)

    def input_short_description(self, description):
        self.write_input(self.locators_shared.STEP4_SHORT_DESCRIPTION, description)

    def input_long_description(self, description):
        self.write_input(self.locators_shared.STEP4_LONG_DESCRIPTION, description)

    def set_media(self):
        self.click(self.locators_shared.STEP4_BUTTON_SET_MEDIA)
        self.click(self.locators_shared.STEP4_IMAGE_ITEM)
        self.click(self.locators_shared.STEP4_BUTTON_SUBMIT_MEDIA)


class CampaignPage(CampaignSharedPage):
    url = "https://ads.vk.com/hq/dashboard"
    campaign_locators = CampaignPageLocators()

    def find_section_in_ad_list(self, section_name):
        ad_list = self.find(self.campaign_locators.STEP2_AD_TYPE_LIST, until_EC=EC.visibility_of_element_located)
        return ad_list.find_element(By.XPATH, f'.//*[@data-id="{section_name}"]')

    def find_section_in_group_list(self, section_name):
        group_list = self.find(self.locators_shared.STEP1_SIGN_NEW_AD_CREATE, until_EC=EC.visibility_of_element_located)
        return group_list.find_element(By.XPATH, f'.//*[@data-testid="{section_name}"]')