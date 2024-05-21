from ui.pages.base_page import BasePage
from ui.locators.campaigns_locators import CampaignsPageSharedLocators

from selenium.webdriver.support import expected_conditions as EC


class CampaignSharedPage(BasePage):
    url = "https://ads.vk.com/hq/dashboard/ad_plans"
    locators_shared = CampaignsPageSharedLocators()

    def click_create_campaign(self):
        self.click(self.locators_shared.STEP1_BUTTON_CREATE_CAMPAIGN)

    def click_choose_site(self):
        self.click(self.locators_shared.STEP2_BUTTON_CHOOSE_SITE)

    def click_start_group_step(self):
        self.click(self.locators_shared.STEP2_BUTTON_START_GROUP_STEP)

    def input_site_url(self, url):
        self.write_input(self.locators_shared.STEP2_INPUT_SITE_URL, url)

    def check_text_input_site_url(self, text):
        return self.wait(1).until(EC.text_to_be_present_in_element_value(
            self.locators_shared.STEP2_INPUT_SITE_URL, 'wrong_url'))

    def click_start_ads_step(self):
        self.click(self.locators_shared.STEP3_BUTTON_START_ADS_STEP)

    def input_budget(self, budget):
        self.write_input(self.locators_shared.STEP2_INPUT_BUDGET, budget)

    def choose_region_by_name(self, region_name):
        self.write_input(self.locators_shared.STEP3_INPUT_SEARCH_REGION, region_name)
        self.click(self.locators_shared.STEP3_CHECKBOXES_REGION)

    def input_title(self, title):
        self.write_input(self.locators_shared.STEP4_INPUT_TITLE, title)

    def input_short_description(self, description):
        self.write_input(self.locators_shared.STEP4_SHORT_DESCRIPTION, description)

    def input_long_description(self, description):
        self.write_input(self.locators_shared.STEP4_LONG_DESCRIPTION, description)

    def set_default_image(self):
        self.click(self.locators_shared.STEP4_BUTTON_SET_GLOBAL_IMAGE)
        self.click(self.locators_shared.STEP4_IMAGE_ITEM)

    def set_default_media(self):
        self.click(self.locators_shared.STEP4_BUTTON_SET_MEDIA)
        self.click(self.locators_shared.STEP4_IMAGE_ITEM)
        self.click(self.locators_shared.STEP4_BUTTON_SUBMIT_MEDIA)
