import pytest

from cases import LoggedCase
from ui.pages.campaign_page import CampaignSharedPage

from selenium.common import TimeoutException


class TestCampaign(LoggedCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_new_campaign(self, driver):
        self.main_page.open_campaigns()
        self.campaign_page = CampaignSharedPage(self.driver)
        self.campaign_page.close_training_button_if_exist()

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

        self.campaign_page.input_budget('100')

        self.campaign_page.click_continue_button()
        try:
            assert self.campaign_page.find_group_name_field(2)
        except TimeoutException:
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

        self.campaign_page.input_group_name("Группа рекламы сайта тп")
        self.campaign_page.click_moscow_region_button()
        self.campaign_page.open_interests_field()
        self.campaign_page.chose_interest()
        self.campaign_page.click_continue_button()

        assert self.campaign_page.find_ad_name_field()
        assert self.campaign_page.find_ad_title_field()
        assert self.campaign_page.find_ad_extra_title_field()
        assert self.campaign_page.find_ad_long_descr_field()
        assert self.campaign_page.find_ad_short_descr_field()
        assert self.campaign_page.find_ad_ai_image_button()

        self.campaign_page.input_ad_name("Объявление рекламы сайта тп")
        self.campaign_page.input_ad_title("Технопарк")
        self.campaign_page.input_ad_short_descr("короткое описание рекламы сайта тп")
        self.campaign_page.input_ad_long_descr("длинное описание рекламы сайта технопарка")
        self.campaign_page.input_ad_extra_title("тп")
        self.campaign_page.click_ai_image_button()
        self.campaign_page.click_ai_image()
        self.campaign_page.click_ai_image_submit_button()

        self.campaign_page.click_publish_button()
        try:
            self.campaign_page.check_url('https://ads.vk.com/hq/dashboard')
            self.campaign_page.click_edit_button()
        except TimeoutException:
            self.campaign_page.click_publish_button()
            self.campaign_page.check_url('https://ads.vk.com/hq/dashboard')
            self.campaign_page.click_edit_button()

        assert self.campaign_page.find_element_with_text("park.vk.company")
        assert self.campaign_page.find_element_with_text("Клики по рекламе")
        assert self.campaign_page.find_element_with_text("Минимальная цена")
        self.campaign_page.click_group_button()
        assert self.campaign_page.find_element_with_text("Москва")
        assert self.campaign_page.find_element_with_text("Авто внедорожники")
        self.campaign_page.click_ad_button()
        assert self.campaign_page.find_element_with_text("Технопарк")
        assert self.campaign_page.find_element_with_text("короткое описание рекламы сайта тп")
        assert self.campaign_page.find_element_with_text("длинное описание рекламы сайта технопарка")
        assert self.campaign_page.find_element_with_text("тп")
        assert self.campaign_page.find_element_with_text("Перейти")

        self.campaign_page.click_cancel_button()
        self.campaign_page.click_dont_save_button()
        self.campaign_page.click_delete_button("Реклама сайта тп")
