from ui.pages.base_page import PageWithView, PageWithRedirectWindow, add_open_view
from ui.pages.base_page_functionality import add_hover
from ui.locators.training_locators import TrainingPageSharedLocators, TrainingPageLocators
from utils.timeout import BASIC_TIMEOUT
from ui.pages.campaign_page import CampaignSharedPage

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC


class TrainingPage(PageWithView, PageWithRedirectWindow):
    url = "https://ads.vk.com/hq/overview"
    locators = TrainingPageLocators()
    locators_shared = TrainingPageSharedLocators()

    @property
    def CONTENT_LIST(self):
        return self.find_with_check_visibility(self.locators.CONTENT_LIST)

    def SECTION_IN_CONTENT_LIST_BY_NAME(self, name):
        return self.CONTENT_LIST.find_element(*self.locators.SECTION_IN_CONTENT_LIST_BY_NAME(name))

    @property
    def TITLE(self):
        return self.find_with_check_visibility(self.locators.TITLE)

    @property
    def BUTTON_TRY_LATER(self):
        return self.find_with_check_visibility(self.locators.BUTTON_TRY_LATER)

    @property
    def BUTTON_CLOSE(self):
        return self.find_with_check_visibility(self.locators.BUTTON_CLOSE)

    @property
    @add_open_view(locators.site_locators.SIGN_OPENING_SITE)
    def BUTTON_SITE(self):
        return self.find_with_check_visibility(self.locators.site_locators.BUTTON_SITE)

    @property
    def SITE_TITLE(self):
        return self.find_with_check_visibility(self.locators.site_locators.TITLE)

    @property
    def SITE_BUTTON_VIDEO(self):
        return self.find_with_check_visibility(self.locators.site_locators.BUTTON_VIDEO)

    @property
    def SITE_BUTTON_ARTICLES(self):
        return self.find_with_check_visibility(self.locators.site_locators.BUTTON_ARTICLES)

    @property
    def SITE_BUTTON_STEP_BY_STEP_TRAINING(self):
        return self.find_with_check_visibility(self.locators.site_locators.BUTTON_STEP_BY_STEP_TRAINING)

    @property
    def STEP1_BUTTON_CREATE_CAMPAIGN(self):
        return self.find_step1_button_create_campaign()

    @property
    def STEP1_TOOLTIP_CREATE_CAMPAIGN(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP1_TOOLTIP_CREATE_CAMPAIGN)

    @property
    def STEP1_BUTTON_TOOLTIP_CLOSE(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP1_BUTTON_TOOLTIP_CLOSE)

    @property
    def STEP1_BUTTON_CONTINUE_TRAINING(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP1_BUTTON_CONTINUE_TRAINING)

    def cancel_interrupt(self):
        self.click(self.STEP1_BUTTON_TOOLTIP_CLOSE)
        self.click(self.STEP1_BUTTON_CONTINUE_TRAINING)

    @property
    def STEP2_TOOLTIP_GOALS(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP2_TOOLTIP_GOALS)

    @property
    def STEP2_TOOLTIP_OBJECT_ADS(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP2_TOOLTIP_OBJECT_ADS)

    @property
    def STEP2_TOOLTIP_SITE(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP2_TOOLTIP_SITE)

    @property
    def STEP2_TOOLTIP_PIXEL(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP2_TOOLTIP_PIXEL)

    @property
    def STEP2_TOOLTIP_ACTION(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP2_TOOLTIP_ACTION)

    @property
    def STEP2_TOOLTIP_OPTIMIZE_BUDGET(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP2_TOOLTIP_OPTIMIZE_BUDGET)

    @property
    def STEP2_TOOLTIP_STRATEGY(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP2_TOOLTIP_STRATEGY)

    @property
    def STEP2_TOOLTIP_BUDGET(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP2_TOOLTIP_BUDGET)

    @property
    def STEP2_TOOLTIP_DATE(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP2_TOOLTIP_DATE)

    @property
    def STEP2_TOOLTIP_END_STEP(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP2_TOOLTIP_END_STEP)

    @property
    def STEP2_BUTTON_CONTINUE_GOALS(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP2_BUTTON_CONTINUE_GOALS)

    @property
    def BUTTON_CONTINUE(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.BUTTON_CONTINUE)

    def check_disable_of_locator(self, check_locator, timeout=BASIC_TIMEOUT):
        return self.wait(timeout).until(EC.element_attribute_to_include(attribute_='disabled', locator=check_locator))

    def check_disable_of_button_continue(self):
        return self.check_disable_of_locator(self.locators.step_by_step_locators.BUTTON_CONTINUE)

    @property
    def STEP2_BUTTON_BACK(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP2_BUTTON_BACK)

    @property
    def STEP3_TOOLTIP_SETTINGS_TARGET_AUDIENCE(self):
        return self.find_with_check_visibility(
            self.locators.step_by_step_locators.STEP3_TOOLTIP_SETTINGS_TARGET_AUDIENCE)

    @property
    def STEP3_TOOLTIP_SCHEDULE(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP3_TOOLTIP_SCHEDULE)

    @property
    def STEP3_TOOLTIP_REGIONS(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP3_TOOLTIP_REGIONS)

    @property
    def STEP3_TOOLTIP_PARAMETERS_AUDIENCE(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP3_TOOLTIP_PARAMETERS_AUDIENCE)

    @property
    def STEP3_TOOLTIP_PARAMETERS_URL(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP3_TOOLTIP_PARAMETERS_URL)

    @property
    def STEP3_TOOLTIP_END_STEP(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP3_TOOLTIP_END_STEP)

    @property
    @add_hover
    def STEP3_HEADER_PARAMETERS_URL(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP3_HEADER_PARAMETERS_URL)

    @property
    def STEP3_BUTTON_CONTINUE_SETTINGS_TARGET_AUDIENCE(self):
        return self.find_with_check_visibility(
            self.locators.step_by_step_locators.STEP3_BUTTON_CONTINUE_SETTINGS_TARGET_AUDIENCE)

    @property
    def STEP4_TOOLTIP_ADS(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP4_TOOLTIP_ADS)

    @property
    def STEP4_TOOLTIP_LOGO(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP4_TOOLTIP_LOGO)

    @property
    def STEP4_TOOLTIP_TITLE(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP4_TOOLTIP_TITLE)

    @property
    def STEP4_TOOLTIP_SHORT_DESCRIPTION(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP4_TOOLTIP_SHORT_DESCRIPTION)

    @property
    def STEP4_TOOLTIP_LONG_DESCRIPTION(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP4_TOOLTIP_LONG_DESCRIPTION)

    @property
    def STEP4_TOOLTIP_HREF(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP4_TOOLTIP_HREF)

    @property
    def STEP4_TOOLTIP_MEDIA(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP4_TOOLTIP_MEDIA)

    @property
    def STEP4_TOOLTIP_LEGAL_INFO(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP4_TOOLTIP_LEGAL_INFO)

    @property
    def STEP4_TOOLTIP_PREVIEW(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP4_TOOLTIP_PREVIEW)

    @property
    def STEP4_TOOLTIP_END_STEP(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP4_TOOLTIP_END_STEP)

    @property
    def STEP4_BUTTON_CONTINUE_ADS(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP4_BUTTON_CONTINUE_ADS)

    # STEP 1 of full way step_by_step training. All before click on button STEP1_BUTTON_CREATE_CAMPAIGN.
    def step1_full_way_step_by_step(self) -> CampaignSharedPage:
        self.cancel_interrupt()

        campaign_shared_page = CampaignSharedPage(self.driver)

        assert self.STEP1_TOOLTIP_CREATE_CAMPAIGN
        campaign_shared_page.click(campaign_shared_page.STEP1_BUTTON_CREATE_CAMPAIGN)

        return campaign_shared_page

    # STEP 2 of full way step_by_step training. Settings of Campaign.
    def step2_of_full_way_step_by_step(self, campaign_shared_page: CampaignSharedPage) -> CampaignSharedPage:
        assert self.STEP2_TOOLTIP_GOALS
        self.click(self.STEP2_BUTTON_CONTINUE_GOALS)

        assert self.STEP2_TOOLTIP_OBJECT_ADS
        campaign_shared_page.click(campaign_shared_page.STEP2_BUTTON_CHOOSE_SITE)

        assert self.STEP2_TOOLTIP_SITE
        # check disable of continue button if input wrong url.
        campaign_shared_page.STEP2_INPUT_SITE_URL.write('wrong_url' + Keys.ENTER)
        assert campaign_shared_page.check_text_input_site_url('wrong_url')
        assert self.check_disable_of_button_continue()

        campaign_shared_page.STEP2_INPUT_SITE_URL.write('goods-galaxy.ru' + Keys.ENTER)
        assert campaign_shared_page.check_text_input_site_url('goods-galaxy.ru')
        self.click(self.BUTTON_CONTINUE)

        assert self.STEP2_TOOLTIP_PIXEL
        # check back in tooltips
        self.click(self.STEP2_BUTTON_BACK)
        assert self.STEP2_TOOLTIP_SITE
        self.click(self.BUTTON_CONTINUE)
        assert self.STEP2_TOOLTIP_PIXEL
        self.click(self.BUTTON_CONTINUE)

        assert self.STEP2_TOOLTIP_ACTION
        self.click(self.BUTTON_CONTINUE)
        assert self.STEP2_TOOLTIP_OPTIMIZE_BUDGET
        self.click(self.BUTTON_CONTINUE)
        assert self.STEP2_TOOLTIP_STRATEGY
        self.click(self.BUTTON_CONTINUE)

        assert self.STEP2_TOOLTIP_BUDGET
        self.check_disable_of_button_continue()
        campaign_shared_page.STEP2_INPUT_BUDGET.write('100')
        self.click(self.BUTTON_CONTINUE)

        self.click(self.BUTTON_CONTINUE)
        assert self.STEP2_TOOLTIP_DATE
        self.click(self.BUTTON_CONTINUE)

        assert self.STEP2_TOOLTIP_END_STEP
        campaign_shared_page.click(campaign_shared_page.STEP2_BUTTON_START_GROUP_STEP)

        return campaign_shared_page

    def step3_of_full_way_step_by_step(self, campaign_shared_page: CampaignSharedPage) -> CampaignSharedPage:
        assert self.STEP3_TOOLTIP_SETTINGS_TARGET_AUDIENCE
        self.click(self.STEP3_BUTTON_CONTINUE_SETTINGS_TARGET_AUDIENCE)

        assert self.STEP3_TOOLTIP_SCHEDULE
        self.click(self.BUTTON_CONTINUE)

        assert self.STEP3_TOOLTIP_REGIONS
        self.check_disable_of_button_continue()
        campaign_shared_page.choose_region_by_name('Москва')
        self.click(self.BUTTON_CONTINUE)

        assert self.STEP3_TOOLTIP_PARAMETERS_AUDIENCE
        self.click(self.BUTTON_CONTINUE)

        self.STEP3_HEADER_PARAMETERS_URL.hover()
        assert self.STEP3_TOOLTIP_PARAMETERS_URL

        assert self.STEP3_TOOLTIP_END_STEP
        campaign_shared_page.click(campaign_shared_page.STEP3_BUTTON_START_ADS_STEP)

        return campaign_shared_page

    def step4_of_full_way_step_by_step(self, campaign_shared_page: CampaignSharedPage) -> CampaignSharedPage:
        assert self.STEP4_TOOLTIP_ADS
        self.click(self.STEP4_BUTTON_CONTINUE_ADS)

        assert self.STEP4_TOOLTIP_LOGO
        self.check_disable_of_button_continue()
        campaign_shared_page.set_default_image()
        assert self.STEP4_TOOLTIP_LOGO
        self.click(self.BUTTON_CONTINUE)

        assert self.STEP4_TOOLTIP_TITLE
        self.check_disable_of_button_continue()
        campaign_shared_page.STEP4_INPUT_TITLE.write('Title')
        self.click(self.BUTTON_CONTINUE)

        assert self.STEP4_TOOLTIP_SHORT_DESCRIPTION
        self.check_disable_of_button_continue()
        campaign_shared_page.STEP4_INPUT_SHORT_DESCRIPTION.write('Description')
        self.click(self.BUTTON_CONTINUE)

        assert self.STEP4_TOOLTIP_LONG_DESCRIPTION
        self.check_disable_of_button_continue()
        campaign_shared_page.STEP4_INPUT_LONG_DESCRIPTION.write('Description')
        self.click(self.BUTTON_CONTINUE)

        assert self.STEP4_TOOLTIP_HREF
        self.click(self.BUTTON_CONTINUE)

        assert self.STEP4_TOOLTIP_MEDIA
        self.check_disable_of_button_continue()
        campaign_shared_page.set_default_media()
        self.click(self.BUTTON_CONTINUE)

        assert self.STEP4_TOOLTIP_LEGAL_INFO
        self.click(self.BUTTON_CONTINUE)

        assert self.STEP4_TOOLTIP_PREVIEW
        self.click(self.BUTTON_CONTINUE)

        assert self.STEP4_TOOLTIP_END_STEP

        return campaign_shared_page
