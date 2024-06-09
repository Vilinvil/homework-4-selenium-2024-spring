from ui.pages.base_page_functionality import BasePageFunctionality, add_write
from ui.locators.campaigns_locators import CampaignsPageSharedLocators

from selenium.webdriver.support import expected_conditions as EC


class CampaignSharedPage(BasePageFunctionality):
    url = "https://ads.vk.com/hq/dashboard/ad_plans"
    locators_shared = CampaignsPageSharedLocators()

    @property
    def STEP1_BUTTON_CREATE_CAMPAIGN(self):
        return self.find_with_check_visibility(self.locators_shared.STEP1_BUTTON_CREATE_CAMPAIGN)

    @property
    def STEP2_BUTTON_CHOOSE_SITE(self):
        return self.find_with_check_visibility(self.locators_shared.STEP2_BUTTON_CHOOSE_SITE)

    @property
    def STEP2_BUTTON_START_GROUP_STEP(self):
        return self.find_with_check_visibility(self.locators_shared.STEP2_BUTTON_START_GROUP_STEP)

    @property
    @add_write
    def STEP2_INPUT_SITE_URL(self):
        return self.find_with_check_visibility(self.locators_shared.STEP2_INPUT_SITE_URL)

    def check_text_input_site_url(self, text):
        return self.wait(1).until(EC.text_to_be_present_in_element_value(
            self.locators_shared.STEP2_INPUT_SITE_URL, text))

    @property
    def STEP3_BUTTON_START_ADS_STEP(self):
        return self.find_with_check_visibility(self.locators_shared.STEP3_BUTTON_START_ADS_STEP)

    @property
    @add_write
    def STEP2_INPUT_BUDGET(self):
        return self.find_with_check_visibility(self.locators_shared.STEP2_INPUT_BUDGET)

    @property
    @add_write
    def STEP3_INPUT_SEARCH_REGION(self):
        return self.find_with_check_visibility(self.locators_shared.STEP3_INPUT_SEARCH_REGION)

    @property
    def STEP3_CHECKBOXES_REGION(self):
        return self.find_with_check_visibility(self.locators_shared.STEP3_CHECKBOXES_REGION)

    def choose_region_by_name(self, region_name):
        self.STEP3_INPUT_SEARCH_REGION.write(region_name)
        self.click(self.STEP3_CHECKBOXES_REGION)

    @property
    @add_write
    def STEP4_INPUT_TITLE(self):
        return self.find_with_check_visibility(self.locators_shared.STEP4_INPUT_TITLE)

    @property
    @add_write
    def STEP4_INPUT_SHORT_DESCRIPTION(self):
        return self.find_with_check_visibility(self.locators_shared.STEP4_INPUT_SHORT_DESCRIPTION)

    @property
    @add_write
    def STEP4_INPUT_LONG_DESCRIPTION(self):
        return self.find_with_check_visibility(self.locators_shared.STEP4_INPUT_LONG_DESCRIPTION)

    @property
    def STEP4_BUTTON_SET_GLOBAL_IMAGE(self):
        return self.find_with_check_visibility(self.locators_shared.STEP4_BUTTON_SET_GLOBAL_IMAGE)

    @property
    def STEP4_IMAGE_ITEM(self):
        return self.find_with_check_visibility(self.locators_shared.STEP4_IMAGE_ITEM)

    @property
    def STEP4_BUTTON_SET_MEDIA(self):
        return self.find_with_check_visibility(self.locators_shared.STEP4_BUTTON_SET_MEDIA)

    @property
    def STEP4_BUTTON_SUBMIT_MEDIA(self):
        return self.find_with_check_visibility(self.locators_shared.STEP4_BUTTON_SUBMIT_MEDIA)

    def set_default_image(self):
        self.click(self.STEP4_BUTTON_SET_GLOBAL_IMAGE)
        self.click(self.STEP4_IMAGE_ITEM)

    def set_default_media(self):
        self.click(self.STEP4_BUTTON_SET_MEDIA)
        self.click(self.STEP4_IMAGE_ITEM)
        self.click(self.STEP4_BUTTON_SUBMIT_MEDIA)
