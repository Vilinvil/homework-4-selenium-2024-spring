import pytest

from cases import LoggedCase
from ui.pages.campaign_page import CampaignPage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


class TestCampaign(LoggedCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_training(self, driver, config):
        self.main_page.click(self.main_page.locators.NAV_BUTTON_CAMPAIGN_SECTION)
        self.campaign_page = CampaignPage(self.driver)

    def test_display_start(self):
        assert self.campaign_page.find(self.campaign_page.locators_shared.STEP1_BUTTON_CREATE_CAMPAIGN,
                                       until_EC=EC.visibility_of_element_located)
        assert self.campaign_page.find(self.campaign_page.locators_shared.STEP1_DASHBOARD_TAB_ITEM,
                                       until_EC=EC.visibility_of_element_located)
        assert self.campaign_page.find(self.campaign_page.locators_shared.STEP1_GROUP_TAB_ITEM,
                                       until_EC=EC.visibility_of_element_located)
        assert self.campaign_page.find(self.campaign_page.locators_shared.STEP1_AD_TAB_ITEM,
                                       until_EC=EC.visibility_of_element_located)
        assert self.campaign_page.find(self.campaign_page.locators_shared.STEP1_BASE_TABLE,
                                       until_EC=EC.visibility_of_element_located)

    @pytest.mark.parametrize('section_name, group_section_name',
                             [
                                 pytest.param(
                                     'site_conversions',
                                     'ecomm',
                                     'mobapps',
                                     'social',
                                     'odkl',
                                     'leadads',
                                     'miniapps',
                                     'socialmusic',
                                     'socialvideo',
                                     'dzen'
                                 ),
                                 pytest.param(
                                    'section-geo',
                                     'section-demography',
                                     'section-interests',
                                     'section-audience',
                                     'section-devices',
                                     'section-urlUtm',
                                     'section-placement'
                                 )
                             ], )
    def test_display_step1(self, section_name, group_section_name):
        self.campaign_page.click_create_campaign()
        assert self.campaign_page.find(self.campaign_page.campaign_locators.STEP2_SUBNAV_CAMPAIGN,
                                       until_EC=EC.visibility_of_element_located)
        assert self.campaign_page.find(self.campaign_page.campaign_locators.STEP2_SUBNAV_GROUP,
                                       until_EC=EC.visibility_of_element_located)
        assert self.campaign_page.find(self.campaign_page.campaign_locators.STEP2_SUBNAV_AD,
                                       until_EC=EC.visibility_of_element_located)
        assert self.campaign_page.find(self.campaign_page.campaign_locators.STEP2_HEADER,
                                       until_EC=EC.visibility_of_element_located)
        assert self.campaign_page.find_section_in_ad_list(section_name)
        self.campaign_page.click_choose_site()
        self.campaign_page.input_site_url("vk.com" + Keys.ENTER)
        self.campaign_page.input_budget("100")
        self.campaign_page.click_start_group_step()
        self.campaign_page.choose_region_by_name('Москва')

        assert self.campaign_page.find_section_in_group_list(group_section_name)
        assert self.campaign_page.find(self.campaign_page.campaign_locators.SAVE_SNIPEPT_BUTTON,
                                       until_EC=EC.visibility_of_element_located)
        assert self.campaign_page.find(self.campaign_page.campaign_locators.BACK_STEP_BUTTON,
                                       until_EC=EC.visibility_of_element_located)

    def test_create(self):
        self.campaign_page.click_create_campaign()
        self.campaign_page.click_choose_site()
        self.campaign_page.input_site_url("vk.com"+ Keys.ENTER)
        self.campaign_page.input_budget("100")
        self.campaign_page.click_start_group_step()
        self.campaign_page.choose_region_by_name('Москва')
        self.campaign_page.click_start_ads_step()
        self.campaign_page.set_image()
        self.campaign_page.set_media()
        self.campaign_page.input_title("dsada")
        self.campaign_page.input_short_description("dsadadsa")
        self.campaign_page.input_long_description("dsadadsads")
        self.campaign_page.click_create_campaign()

    def test_check_continue_button(self):
        self.campaign_page.click_create_campaign()
        assert self.campaign_page.find(self.campaign_page.campaign_locators.STEP2_BUTTON_START_GROUP_STEP_DISABLED,
                                       until_EC=EC.visibility_of_element_located)
        self.campaign_page.click_choose_site()
        assert self.campaign_page.find(self.campaign_page.locators_shared.STEP2_BUTTON_START_GROUP_STEP,
                                       until_EC=EC.visibility_of_element_located)
