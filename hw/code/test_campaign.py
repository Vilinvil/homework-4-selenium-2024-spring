import time

import pytest

from cases import LoggedCase
from ui.pages.base_page import PageWithRedirectWindow
from ui.pages.main_page import MainPage
from ui.pages.campaign_page import CampaignSharedPage
from selenium.webdriver.common.action_chains import ActionChains as AC


class TestCampaign(LoggedCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_new_campaign(self, driver):
        self.main_page.open_campaigns()
        self.campaign_page = CampaignSharedPage(self.driver)
        if self.campaign_page.find_close_training_button():
            self.campaign_page.click_close_training_button()


    def test_create_campaign(self):
        self.campaign_page.click_create_campaign()

        assert self.campaign_page.find_ok_button()
        assert self.campaign_page.find_lead_ads_button()
        assert self.campaign_page.find_mini_apps_button()
        assert self.campaign_page.find_mobile_apps_button()
        assert self.campaign_page.find_dzen_button()
        assert self.campaign_page.find_site_button()
        assert self.campaign_page.find_music_button()
        assert self.campaign_page.find_social_button()
        assert self.campaign_page.find_video_button()
        assert self.campaign_page.find_catalog_button()
        assert self.campaign_page.find_branding_tab()
        assert self.campaign_page.find_targeting_actions_tab()
        assert self.campaign_page.find_campaign_name_field()

        self.campaign_page.input_campaign_name("Реклама сайта тп")
        self.campaign_page.click_choose_site()
        assert self.campaign_page.find_input_site()
        assert self.campaign_page.find_continue_button()

        self.campaign_page.input_site_url("https://park.vk.company/")
        self.campaign_page.click_continue_button()

        assert self.campaign_page.find_goal_action_field()
        assert self.campaign_page.find_budget_field()
        assert self.campaign_page.find_betting_strategy_field()
        assert self.campaign_page.find_optimize_budget_field()
        assert self.campaign_page.find_start_date_field()

        self.campaign_page.input_budget(100)
        time.sleep(2)
        self.campaign_page.click_continue_button()

        assert self.campaign_page.find_group_name_field()
        assert self.campaign_page.find_group_start_date_field()
        assert self.campaign_page.find_geo_tab()
        assert self.campaign_page.find_url_tab()
        assert self.campaign_page.find_interests_tab()
        assert self.campaign_page.find_devices_tab()
        assert self.campaign_page.find_placement_tab()
        assert self.campaign_page.find_demography_tab()
        assert self.campaign_page.find_audience_tab()

        self.campaign_page.input_campaign_name("Группа рекламы сайта тп")
        self.campaign_page.click_moscow_region_button()

        self.campaign_page.open_interests_field()
        self.campaign_page.input_interest("Компьютерная техника")
        self.campaign_page.click_autocompleted_variant()


