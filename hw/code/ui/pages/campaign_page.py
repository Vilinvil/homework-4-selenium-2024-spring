from ui.pages.base_page_functionality import BasePageFunctionality, add_write
from ui.locators.campaigns_locators import CampaignsPageSharedLocators
from utils.timeout import BASIC_TIMEOUT

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.common import TimeoutException


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

    def click_create_campaign(self):
        self.click(self.locators_shared.STEP1_BUTTON_CREATE_CAMPAIGN)

    def click_choose_site(self):
        self.click(self.locators_shared.STEP2_BUTTON_CHOOSE_SITE)

    def input_site_url(self, url):
        self.write_input(self.locators_shared.STEP2_INPUT_SITE_URL, url)

    def input_budget(self, budget):
        self.write_input(self.locators_shared.STEP2_INPUT_BUDGET, budget)

    def find_branding_tab(self):
        return self.find_with_check_visibility(self.locators_shared.TAB_BRANDING)

    def find_targeting_actions_tab(self):
        return self.find_with_check_visibility(self.locators_shared.TAB_TARGETED_ACTIONS)

    def find_site_button(self):
        return self.find_with_check_visibility(self.locators_shared.STEP2_BUTTON_CHOOSE_SITE)

    def find_ok_button(self):
        return self.find_with_check_visibility(self.locators_shared.BUTTON_OK)

    def find_dzen_button(self):
        return self.find_with_check_visibility(self.locators_shared.BUTTON_DZEN)

    def find_music_button(self):
        return self.find_with_check_visibility(self.locators_shared.BUTTON_MUSIC)

    def find_video_button(self):
        return self.find_with_check_visibility(self.locators_shared.BUTTON_VIDEO)

    def find_catalog_button(self):
        return self.find_with_check_visibility(self.locators_shared.BUTTON_CATALOG)

    def find_lead_ads_button(self):
        return self.find_with_check_visibility(self.locators_shared.BUTTON_LEAD_ADS)

    def find_mini_apps_button(self):
        return self.find_with_check_visibility(self.locators_shared.BUTTON_MINI_APPS)

    def find_mobile_apps_button(self):
        return self.find_with_check_visibility(self.locators_shared.BUTTON_MOBILE_APPS)

    def find_social_button(self):
        return self.find_with_check_visibility(self.locators_shared.BUTTON_SOCIAL)

    def find_close_training_button(self, timeout=BASIC_TIMEOUT):
        return self.find_with_check_visibility(self.locators_shared.BUTTON_CLOSE_TRAINING, timeout)

    def click_close_training_button(self):
        self.click(self.locators_shared.BUTTON_CLOSE_TRAINING)

    def find_input_site(self):
        return self.find_with_check_visibility(self.locators_shared.STEP2_INPUT_SITE_URL)

    def find_continue_button(self):
        return self.find_with_check_visibility(self.locators_shared.BUTTON_CONTINUE)

    def click_continue_button(self, timeout=BASIC_TIMEOUT):
        return self.click(self.locators_shared.BUTTON_CONTINUE, timeout)

    def find_budget_field(self):
        return self.find_with_check_visibility(self.locators_shared.FIELD_BUDGET)

    def find_optimize_budget_field(self):
        return self.find_with_check_visibility(self.locators_shared.FIELD_OPTIMIZE_BUDGET)

    def find_goal_action_field(self):
        return self.find_with_check_visibility(self.locators_shared.FIELD_GOAL_ACTION)

    def find_betting_strategy_field(self):
        return self.find_with_check_visibility(self.locators_shared.FIELD_BETTING_STRATEGY)

    def find_start_date_field(self):
        return self.find_with_check_visibility(self.locators_shared.FIELD_BETTING_STRATEGY)

    def find_campaign_name_field(self):
        return self.find_with_check_visibility(self.locators_shared.CAMPAIGN_NAME_FIELD)

    def input_campaign_name(self, name):
        self.click(self.locators_shared.CAMPAIGN_NAME_FIELD)
        self.write_input_without_clearing(self.locators_shared.CAMPAIGN_NAME_FIELD_EDIT, name)

    def find_group_start_date_field(self):
        return self.find_with_check_visibility(self.locators_shared.GROUP_FIELD_START_DATE)

    def find_group_name_field(self, timeout=BASIC_TIMEOUT):
        return self.find_with_check_visibility(self.locators_shared.GROUP_NAME_FIELD, timeout)

    def find_geo_tab(self):
        return self.find(self.locators_shared.GEO_TAB)

    def find_placement_tab(self):
        return self.find_with_check_visibility(self.locators_shared.PLACEMENT_TAB)

    def find_url_tab(self):
        return self.find_with_check_visibility(self.locators_shared.URL_TAB)

    def find_audience_tab(self):
        return self.find_with_check_visibility(self.locators_shared.AUDIENCE_TAB)

    def find_demography_tab(self):
        return self.find_with_check_visibility(self.locators_shared.DEMOGRAPHY_TAB)

    def find_interests_tab(self):
        return self.find_with_check_visibility(self.locators_shared.INTERESTS_TAB)

    def find_devices_tab(self):
        return self.find_with_check_visibility(self.locators_shared.DEVICES_TAB)

    def get_budget(self):
        elem = self.find(self.locators_shared.FIELD_BUDGET, timeout=BASIC_TIMEOUT)
        return elem.get_attribute('value')

    def input_group_name(self, name):
        self.click(self.locators_shared.GROUP_NAME_FIELD)
        self.write_input_without_clearing(self.locators_shared.GROUP_NAME_FIELD_EDIT, name)

    def click_moscow_region_button(self):
        self.click(self.locators_shared.MOSCOW_REGION_BUTTON)

    def open_interests_field(self):
        self.click(self.locators_shared.INTERESTS_TAB)
        self.click(self.locators_shared.INTERESTS_TAB_INTERESTS_SUBTAB)

    def chose_interest(self):
        elem = self.find_with_check_visibility(self.locators_shared.INTERESTS_TAB_COMMUNITIES_SUBTAB)
        AC(self.driver).move_to_element(elem).perform()

        self.click(self.locators_shared.INTERESTS_INPUT)
        self.click(self.locators_shared.INTEREST_AUTO)
        self.click(self.locators_shared.INTERESTS_CLOSE_INPUT_BUTTON)

    def open_devices_tab(self):
        self.click(self.locators_shared.DEVICES_TAB)

    def click_mobile_checkbox(self):
        elem = self.find(self.locators_shared.DEVICES_MOBILE_CHECKBOX)
        AC(self.driver).move_to_element(elem).perform()

        self.click(self.locators_shared.DEVICES_MOBILE_CHECKBOX)

    def find_ad_name_field(self):
        return self.find_with_check_visibility(self.locators_shared.AD_NAME_FIELD)

    def input_ad_name(self, name):
        self.click(self.locators_shared.AD_NAME_FIELD)
        self.write_input_without_clearing(self.locators_shared.AD_NAME_FIELD_EDIT, name)

    def find_ad_short_descr_field(self):
        return self.find_with_check_visibility(self.locators_shared.AD_FIELD_SHORT_DESCR)

    def find_ad_long_descr_field(self):
        return self.find_with_check_visibility(self.locators_shared.AD_FIELD_LONG_DESCR)

    def find_ad_title_field(self):
        return self.find_with_check_visibility(self.locators_shared.AD_FIELD_TITLE)

    def find_ad_extra_title_field(self):
        return self.find_with_check_visibility(self.locators_shared.AD_FIELD_EXTRA_TITLE)

    def find_ad_ai_image_button(self):
        return self.find_with_check_visibility(self.locators_shared.AD_AI_IMAGE_BUTTON)

    def find_ad_ai_preview(self):
        return self.find_with_check_visibility(self.locators_shared.AD_AI_PREVIEW)

    def input_ad_title(self, text):
        self.write_input(self.locators_shared.AD_FIELD_TITLE, text)

    def input_ad_short_descr(self, text):
        self.write_input(self.locators_shared.AD_FIELD_SHORT_DESCR, text)

    def input_ad_long_descr(self, text):
        self.write_input(self.locators_shared.AD_FIELD_LONG_DESCR, text)

    def input_ad_extra_title(self, text):
        self.write_input(self.locators_shared.AD_FIELD_EXTRA_TITLE, text)

    def click_ai_image_button(self):
        self.click(self.locators_shared.AD_AI_IMAGE_BUTTON)

    def click_publish_button(self):
        self.click(self.locators_shared.BUTTON_PUBLISH)

    def click_ai_image(self):
        elem = self.find_with_check_visibility(self.locators_shared.AD_AI_IMAGE)
        elem.click()

    def click_ai_image_submit_button(self, timeout=BASIC_TIMEOUT):
        self.click(self.locators_shared.AD_AI_IMAGE_SUBMIT_BUTTON, timeout)

    def click_edit_button(self):
        elem = self.find_with_check_visibility(self.locators_shared.CAMPAIGN_TITLE)
        self.hover_to_element(elem)
        elem = self.find_with_check_visibility(self.locators_shared.EDIT_BUTTON)
        elem.click()

    def find_element_with_text(self, text):
        return self.find_with_check_visibility(self.locators_shared.LOCATOR_WITH_TEXT(text))

    def click_group_button(self):
        self.click(self.locators_shared.GROUP_BUTTON)

    def click_ad_button(self):
        self.click(self.locators_shared.AD_BUTTON)

    def click_cancel_button(self):
        self.click(self.locators_shared.CANCEL_BUTTON)

    def click_dont_save_button(self):
        self.click(self.locators_shared.DONT_SAVE_BUTTON)

    def click_delete_button(self, name):
        self.click(self.locators_shared.CHECKBOX_OF_CAMPAIGN(name))
        self.click(self.locators_shared.ACTIONS_BUTTON)
        self.click(self.locators_shared.DELETE_BUTTON)

    def close_training_button_if_exist(self):
        try:
            self.find_close_training_button(2)
            self.click_close_training_button()
        except TimeoutException:
            pass
