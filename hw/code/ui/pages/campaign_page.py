from ui.pages.base_page_functionality import BasePageFunctionality, add_write
from ui.locators.campaigns_locators import CampaignsPageSharedLocators
from utils.timeout import BASIC_TIMEOUT
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC

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

    def find_close_training_button(self):
        return self.find_with_check_visibility(self.locators_shared.BUTTON_CLOSE_TRAINING)

    def click_close_training_button(self):
        self.click(self.locators_shared.BUTTON_CLOSE_TRAINING)

    def find_input_site(self):
        return self.find_with_check_visibility(self.locators_shared.STEP2_INPUT_SITE_URL)

    def find_continue_button(self):
        return self.find_with_check_visibility(self.locators_shared.BUTTON_CONTINUE)

    def click_continue_button(self):
        elem = self.find(self.locators_shared.BUTTON_CONTINUE, timeout=BASIC_TIMEOUT, until_EC=EC.presence_of_element_located)
        elem.click()

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

    def find_group_name_field(self):
        return self.find_with_check_visibility(self.locators_shared.GROUP_NAME_FIELD)

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
        # elem = self.find(self.locators_shared.INTERESTS_TAB, timeout=BASIC_TIMEOUT,
        #                  until_EC=EC.presence_of_element_located)
        # AC(self.driver).move_to_element(elem).click(elem).perform()
        # elem = self.find(self.locators_shared.INTERESTS_TAB_INTERESTS_SUBTAB, timeout=BASIC_TIMEOUT,
        #                  until_EC=EC.presence_of_element_located)
        # AC(self.driver).move_to_element(elem).click(elem).perform()
        self.click(self.locators_shared.INTERESTS_TAB)
        self.click(self.locators_shared.INTERESTS_TAB_INTERESTS_SUBTAB)

    def input_interest(self, text):
        elem = self.find(self.locators_shared.INTERESTS_INPUT, timeout=BASIC_TIMEOUT,
            until_EC=EC.presence_of_element_located)
        AC(self.driver).move_to_element(elem).perform()

        self.write_input(self.locators_shared.INTERESTS_INPUT, text)

    def click_autocompleted_variant(self):
        elem = self.find(self.locators_shared.INTERESTS_AUTOCOMPLETED_VARIANT, timeout=BASIC_TIMEOUT,
                         until_EC=EC.presence_of_element_located)
        AC(self.driver).move_to_element(elem).perform()

        self.click(self.locators_shared.INTERESTS_AUTOCOMPLETED_VARIANT)
