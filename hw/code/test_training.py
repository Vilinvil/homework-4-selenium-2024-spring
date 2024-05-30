import pytest

from cases import LoggedCase
from ui.pages.training_page import TrainingPage
from ui.pages.campaign_page import CampaignSharedPage

from selenium.webdriver import Keys


class TestTraining(LoggedCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_training(self, driver):
        self.training_page = TrainingPage(self.driver)
        self.main_page.open_training()

    def test_display(self):
        assert self.training_page.find_title()
        assert self.training_page.find_button_try_later()
        assert self.training_page.find_button_close()

    @pytest.mark.parametrize('section_name',
                             [
                                 'Сообщество ВКонтакте',
                                 'Сайт',
                                 'Каталог товаров',
                                 'VK Mini Apps'
                             ], )
    def test_display_content_list(self, section_name):
        assert self.training_page.find_section_in_content_list(section_name)

    @pytest.fixture(scope='function')
    def setup_training_site(self):
        self.training_page.open_site()

    def test_display_site_section(self, setup_training_site):
        assert self.training_page.find_site_title()
        assert self.training_page.find_site_button_video()
        assert self.training_page.find_site_button_articles()
        assert self.training_page.find_site_button_step_by_step_training()

    @pytest.fixture(scope="function")
    def setup_step_by_step(self, setup_training_site):
        self.training_page.click_button_step_by_step_training()

    def test_open_step_by_step(self, setup_step_by_step):
        assert self.training_page.find_step1_button_create_campaign()
        assert self.training_page.find_step1_tooltip_create_campaign()

    # STEP 1 of full way step_by_step training. All before click on button STEP1_BUTTON_CREATE_CAMPAIGN.
    def step1_full_way_step_by_step(self) -> CampaignSharedPage:
        self.training_page.cancel_interrupt()

        campaign_shared_page = CampaignSharedPage(self.driver)

        assert self.training_page.find_step1_tooltip_create_campaign()
        campaign_shared_page.click_create_campaign()

        return campaign_shared_page

    # STEP 2 of full way step_by_step training. Settings of Campaign.
    def step2_of_full_way_step_by_step(self, campaign_shared_page: CampaignSharedPage) -> CampaignSharedPage:
        assert self.training_page.find_step2_tooltip_goals()
        self.training_page.click_step2_button_continue_goals()

        assert self.training_page.find_step2_tooltip_object_ads()
        campaign_shared_page.click_choose_site()

        assert self.training_page.find_step2_tooltip_site()
        # check disable of continue button if input wrong url.
        campaign_shared_page.input_site_url('wrong_url' + Keys.ENTER)
        assert campaign_shared_page.check_text_input_site_url('wrong_url')
        assert self.training_page.check_disable_of_button_continue()

        campaign_shared_page.input_site_url('goods-galaxy.ru' + Keys.ENTER)
        assert campaign_shared_page.check_text_input_site_url('goods-galaxy.ru')
        self.training_page.click_continue()

        assert self.training_page.find_step2_tooltip_pixel()
        # check back in tooltips
        self.training_page.click_back()
        assert self.training_page.find_step2_tooltip_site()
        self.training_page.click_continue()
        assert self.training_page.find_step2_tooltip_pixel()
        self.training_page.click_continue()

        assert self.training_page.find_step2_tooltip_action()
        self.training_page.click_continue()
        assert self.training_page.find_step2_tooltip_optimize_budget()
        self.training_page.click_continue()
        assert self.training_page.find_step2_tooltip_strategy()
        self.training_page.click_continue()

        assert self.training_page.find_step2_tooltip_budget()
        self.training_page.check_disable_of_button_continue()
        campaign_shared_page.input_budget('100')
        self.training_page.click_continue()

        self.training_page.click_continue()
        assert self.training_page.find_step2_tooltip_date()
        self.training_page.click_continue()

        assert self.training_page.find_step2_tooltip_end_step()
        campaign_shared_page.click_start_group_step()

        return campaign_shared_page

    def step3_of_full_way_step_by_step(self, campaign_shared_page: CampaignSharedPage) -> CampaignSharedPage:
        assert self.training_page.find_step3_tooltip_settings_target_audience()
        self.training_page.click_step3_button_continue_settings_target_audience()

        assert self.training_page.find_step3_tooltip_schedule()
        self.training_page.click_continue()

        assert self.training_page.find_step3_tooltip_regions()
        self.training_page.check_disable_of_button_continue()
        campaign_shared_page.choose_region_by_name('Москва')
        self.training_page.click_continue()

        assert self.training_page.find_step3_tooltip_parameters_audience()
        self.training_page.click_continue()

        self.training_page.hover_step3_header_parameters_audience()
        assert self.training_page.find_step3_tooltip_parameters_url()

        assert self.training_page.find_step3_tooltip_end_step()
        campaign_shared_page.click_start_ads_step()

        return campaign_shared_page

    def step4_of_full_way_step_by_step(self, campaign_shared_page: CampaignSharedPage) -> CampaignSharedPage:
        assert self.training_page.find_step4_tooltip_ads()
        self.training_page.click_step4_button_continue_ads()

        assert self.training_page.find_step4_tooltip_logo()
        self.training_page.check_disable_of_button_continue()
        campaign_shared_page.set_default_image()
        assert self.training_page.find_step4_tooltip_logo()
        self.training_page.click_continue()

        assert self.training_page.find_step4_tooltip_title()
        self.training_page.check_disable_of_button_continue()
        campaign_shared_page.input_title('Title')
        self.training_page.click_continue()

        assert self.training_page.find_step4_tooltip_short_description()
        self.training_page.check_disable_of_button_continue()
        campaign_shared_page.input_short_description('Description')
        self.training_page.click_continue()

        assert self.training_page.find_step4_tooltip_long_description()
        self.training_page.check_disable_of_button_continue()
        campaign_shared_page.input_long_description('Description')
        self.training_page.click_continue()

        assert self.training_page.find_step4_tooltip_href()
        self.training_page.click_continue()

        assert self.training_page.find_step4_tooltip_media()
        self.training_page.check_disable_of_button_continue()
        campaign_shared_page.set_default_media()
        self.training_page.click_continue()

        assert self.training_page.find_step4_tooltip_legal_info()
        self.training_page.click_continue()

        assert self.training_page.find_step4_tooltip_preview()
        self.training_page.click_continue()

        assert self.training_page.find_step4_tooltip_end_step()

        return campaign_shared_page

    def test_full_way_step_by_step(self, setup_step_by_step):
        campaign_shared_page = self.step1_full_way_step_by_step()

        campaign_shared_page = self.step2_of_full_way_step_by_step(campaign_shared_page)

        campaign_shared_page = self.step3_of_full_way_step_by_step(campaign_shared_page)

        self.step4_of_full_way_step_by_step(campaign_shared_page)
