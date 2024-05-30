from ui.pages.base_page import PageWithView, PageWithRedirectWindow
from ui.pages.campaign_page import CampaignSharedPage
from ui.locators.training_locators import TrainingPageSharedLocators, TrainingPageLocators
from utils.timeout import BASIC_TIMEOUT

from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TrainingPage(PageWithView, PageWithRedirectWindow):
    url = "https://ads.vk.com/hq/overview"
    locators = TrainingPageLocators()
    locators_shared = TrainingPageSharedLocators()

    def find_section_in_content_list(self, section_name):
        content_list = self.find(self.locators.CONTENT_LIST, until_EC=EC.visibility_of_element_located)
        return content_list.find_element(By.XPATH, f'.//*[@role="button"]//*[contains(text(), "{section_name}")]')

    def find_title(self):
        return self.find_with_check_visibility(self.locators.TITLE)

    def find_button_try_later(self):
        return self.find_with_check_visibility(self.locators.BUTTON_TRY_LATER)

    def find_button_close(self):
        return self.find_with_check_visibility(self.locators.BUTTON_CLOSE)

    def find_site_title(self):
        return self.find_with_check_visibility(self.locators.site_locators.TITLE)

    def find_site_button_video(self):
        return self.find_with_check_visibility(self.locators.site_locators.BUTTON_VIDEO)

    def find_site_button_articles(self):
        return self.find_with_check_visibility(self.locators.site_locators.BUTTON_ARTICLES)

    def find_site_button_step_by_step_training(self):
        return self.find_with_check_visibility(self.locators.site_locators.BUTTON_STEP_BY_STEP_TRAINING)

    def find_step1_button_create_campaign(self):
        return self.find_with_check_visibility(self.locators.campaign_page_shared_locators.STEP1_BUTTON_CREATE_CAMPAIGN)

    def find_step1_tooltip_create_campaign(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP1_TOOLTIP_CREATE_CAMPAIGN)

    def find_step2_tooltip_goals(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP2_TOOLTIP_GOALS)

    def find_step2_tooltip_object_ads(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP2_TOOLTIP_OBJECT_ADS)

    def find_step2_tooltip_site(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP2_TOOLTIP_SITE)

    def find_step2_tooltip_pixel(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP2_TOOLTIP_PIXEL)

    def find_step2_tooltip_action(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP2_TOOLTIP_ACTION)

    def find_step2_tooltip_optimize_budget(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP2_TOOLTIP_OPTIMIZE_BUDGET)

    def find_step2_tooltip_strategy(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP2_TOOLTIP_STRATEGY)

    def find_step2_tooltip_budget(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP2_TOOLTIP_BUDGET)

    def find_step2_tooltip_date(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP2_TOOLTIP_DATE)

    def find_step2_tooltip_end_step(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP2_TOOLTIP_END_STEP)

    def find_step3_tooltip_settings_target_audience(self):
        return self.find_with_check_visibility(
            self.locators.step_by_step_locators.STEP3_TOOLTIP_SETTINGS_TARGET_AUDIENCE)

    def find_step3_tooltip_schedule(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP3_TOOLTIP_SCHEDULE)

    def find_step3_tooltip_regions(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP3_TOOLTIP_REGIONS)

    def find_step3_tooltip_parameters_audience(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP3_TOOLTIP_PARAMETERS_AUDIENCE)

    def find_step3_tooltip_parameters_url(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP3_TOOLTIP_PARAMETERS_URL)

    def find_step3_tooltip_end_step(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP3_TOOLTIP_END_STEP)

    def find_step4_tooltip_ads(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP4_TOOLTIP_ADS)

    def find_step4_tooltip_logo(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP4_TOOLTIP_LOGO)

    def find_step4_tooltip_title(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP4_TOOLTIP_TITLE)

    def find_step4_tooltip_short_description(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP4_TOOLTIP_SHORT_DESCRIPTION)

    def find_step4_tooltip_long_description(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP4_TOOLTIP_LONG_DESCRIPTION)

    def find_step4_tooltip_href(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP4_TOOLTIP_HREF)

    def find_step4_tooltip_media(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP4_TOOLTIP_MEDIA)

    def find_step4_tooltip_legal_info(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP4_TOOLTIP_LEGAL_INFO)

    def find_step4_tooltip_preview(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP4_TOOLTIP_PREVIEW)

    def find_step4_tooltip_end_step(self):
        return self.find_with_check_visibility(self.locators.step_by_step_locators.STEP4_TOOLTIP_END_STEP)

    def open_site(self):
        self.open_view(self.locators.site_locators.BUTTON_SITE, self.locators.site_locators.SIGN_OPENING_SITE)

    def hover_step3_header_parameters_audience(self):
        self.hover_wrapper(self.locators.step_by_step_locators.STEP3_HEADER_PARAMETERS_URL)

    def click_button_step_by_step_training(self):
        self.click(self.locators.site_locators.BUTTON_STEP_BY_STEP_TRAINING)

    def click_step2_button_continue_goals(self):
        self.click(self.locators.step_by_step_locators.STEP2_BUTTON_CONTINUE_GOALS)

    def click_step3_button_continue_settings_target_audience(self):
        self.click(self.locators.step_by_step_locators.STEP3_BUTTON_CONTINUE_SETTINGS_TARGET_AUDIENCE)

    def click_step4_button_continue_ads(self):
        self.click(self.locators.step_by_step_locators.STEP4_BUTTON_CONTINUE_ADS)

    def click_continue(self):
        self.click(self.locators.step_by_step_locators.STEP2_BUTTON_CONTINUE)

    def click_back(self):
        self.click(self.locators.step_by_step_locators.STEP2_BUTTON_BACK)

    def cancel_interrupt(self):
        self.click(self.locators.step_by_step_locators.STEP1_BUTTON_TOOLTIP_CLOSE)
        self.click(self.locators.step_by_step_locators.STEP1_BUTTON_CONTINUE_TRAINING)

    def check_disable_of_locator(self, check_locator, timeout=BASIC_TIMEOUT):
        return self.wait(timeout).until(EC.element_attribute_to_include(attribute_='disabled', locator=check_locator))

    def check_disable_of_button_continue(self):
        return self.check_disable_of_locator(self.locators.step_by_step_locators.STEP2_BUTTON_CONTINUE)
