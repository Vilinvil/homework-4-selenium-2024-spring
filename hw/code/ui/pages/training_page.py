from ui.pages.base_page import PageWithModalView, PageWithRedirectWindow
from ui.pages.campaign_page import CampaignSharedPage
from ui.locators.training_locators import TrainingPageSharedLocators, TrainingPageLocators

from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC


class TrainingPage(PageWithModalView, PageWithRedirectWindow):
    url = "https://ads.vk.com/hq/overview"
    locators = TrainingPageLocators()
    locators_shared = TrainingPageSharedLocators()

    def find_section_in_content_list(self, section_name):
        content_list = self.find(self.locators.CONTENT_LIST, until_EC=EC.visibility_of_element_located)
        return content_list.find_element(By.XPATH, f'.//*[@role="button"]//*[contains(text(), "{section_name}")]')

    def click_zero_coordinate(self):
        ActionBuilder(self.driver).pointer_action.move_to_location(0, 0).click()

    def cancel_interrupt(self, button_interrupt_locator, button_cancel_locator):
        self.click(button_interrupt_locator)
        self.click(button_cancel_locator)

    def check_disable_of_locator(self, check_locator):
        assert self.find(check_locator).get_attribute('disabled')

    # STEP 1 of full way step_by_step training. All before click on button STEP1_BUTTON_CREATE_CAMPAIGN.
    def test_step1_of_full_way_step_by_step(self) -> CampaignSharedPage:
        self.cancel_interrupt(self.locators.step_by_step_locators.STEP1_BUTTON_TOOLTIP_CLOSE,
                              self.locators.step_by_step_locators.
                              STEP1_BUTTON_CONTINUE_TRAINING)

        campaign_shared_page = CampaignSharedPage(self.driver)

        assert self.find(self.locators.step_by_step_locators.STEP1_TOOLTIP_CREATE_CAMPAIGN,
                         until_EC=EC.visibility_of_element_located)
        campaign_shared_page.click_create_campaign()

        return campaign_shared_page

    def test_standard_tooltip(self, tooltip_locator, button_continue_locator):
        assert (self.find(tooltip_locator, until_EC=EC.visibility_of_element_located))
        self.click(button_continue_locator)

    # STEP 2 of full way step_by_step training. Settings of Campaign.
    def test_step2_of_full_way_step_by_step(self, campaign_shared_page: CampaignSharedPage):
        self.test_standard_tooltip(self.locators.step_by_step_locators.STEP2_TOOLTIP_GOALS,
                                   self.locators.step_by_step_locators.STEP2_BUTTON_CONTINUE_GOALS)

        assert (self.find(self.locators.step_by_step_locators.STEP2_TOOLTIP_OBJECT_ADS,
                          until_EC=EC.visibility_of_element_located))
        campaign_shared_page.click_choose_site()

        assert (self.find(self.locators.step_by_step_locators.STEP2_TOOLTIP_SITE,
                          until_EC=EC.visibility_of_element_located))
        # check disable of continue button if input wrong url. # TODO create bug_report because
        #  not always BUTTON_CONTINUE is disabled
        # campaign_shared_page.input_site_url('wrong_url///' + Keys.ENTER)
        # campaign_shared_page.find(campaign_shared_page.locators_shared.STEP2_ALERT_WRONG_URL,
        #                          until_EC=EC.visibility_of_element_located)
        # self.check_disable_of_locator(self.locators.step_by_step_locators.STEP2_BUTTON_CONTINUE)
        campaign_shared_page.input_site_url('goods-galaxy.ru' + Keys.ENTER)
        campaign_shared_page.wait().until(EC.text_to_be_present_in_element_value(
            campaign_shared_page.locators_shared.STEP2_INPUT_SITE_URL, 'goods-galaxy.ru'))
        self.click(self.locators.step_by_step_locators.STEP2_BUTTON_CONTINUE)

        assert (self.find(self.locators.step_by_step_locators.STEP2_TOOLTIP_PIXEL,
                          until_EC=EC.visibility_of_element_located))
        # check back in tooltips
        self.click(self.locators.step_by_step_locators.STEP2_BUTTON_BACK)
        self.test_standard_tooltip(self.locators.step_by_step_locators.STEP2_TOOLTIP_SITE,
                                   self.locators.step_by_step_locators.STEP2_BUTTON_CONTINUE)
        self.test_standard_tooltip(self.locators.step_by_step_locators.STEP2_TOOLTIP_PIXEL,
                                   self.locators.step_by_step_locators.STEP2_BUTTON_CONTINUE)

        self.test_standard_tooltip(self.locators.step_by_step_locators.STEP2_TOOLTIP_ACTION,
                                   self.locators.step_by_step_locators.STEP2_BUTTON_CONTINUE)
        self.test_standard_tooltip(self.locators.step_by_step_locators.STEP2_TOOLTIP_OPTIMIZE_BUDGET,
                                   self.locators.step_by_step_locators.STEP2_BUTTON_CONTINUE)
        self.test_standard_tooltip(self.locators.step_by_step_locators.STEP2_TOOLTIP_STRATEGY,
                                   self.locators.step_by_step_locators.STEP2_BUTTON_CONTINUE)

        assert (self.find(self.locators.step_by_step_locators.STEP2_TOOLTIP_BUDGET,
                          until_EC=EC.visibility_of_element_located))
        campaign_shared_page.input_budget('100')
        self.click(self.locators.step_by_step_locators.STEP2_BUTTON_CONTINUE)

        self.click(self.locators.step_by_step_locators.STEP2_BUTTON_CONTINUE)
        self.test_standard_tooltip(self.locators.step_by_step_locators.STEP2_TOOLTIP_DATE,
                                   self.locators.step_by_step_locators.STEP2_BUTTON_CONTINUE)

        assert (self.find(self.locators.step_by_step_locators.STEP2_TOOLTIP_END_STEP,
                          until_EC=EC.visibility_of_element_located))
        campaign_shared_page.click_start_group_step()
