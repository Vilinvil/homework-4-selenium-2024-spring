from ui.pages.base_page import BasePage
from ui.locators.campaigns_locators import CampaignsPageSharedLocators


class CampaignSharedPage(BasePage):
    url = "https://ads.vk.com/hq/dashboard/ad_plans"
    locators_shared = CampaignsPageSharedLocators()

    def click_create_campaign(self):
        self.click(self.locators_shared.STEP1_BUTTON_CREATE_CAMPAIGN)

    def click_choose_site(self):
        self.click(self.locators_shared.STEP2_BUTTON_CHOOSE_SITE)

    def input_site_url(self, url):
        self.write_input(self.locators_shared.STEP2_INPUT_SITE_URL, url)

    def input_budget(self, budget):
        self.write_input(self.locators_shared.STEP2_INPUT_BUDGET, budget)

    def click_start_group_step(self):
        self.click(self.locators_shared.STEP2_BUTTON_START_GROUP_STEP)
