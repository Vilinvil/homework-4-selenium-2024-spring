from ui.pages.base_page_functionality import BasePageFunctionality, add_click, add_write
from ui.locators.leads_locators import LeadsPageLocators


class LeadsPage(BasePageFunctionality):
    url = "https://ads.vk.com/hq/leadads/leadforms"
    locators = LeadsPageLocators()

    @property
    @add_click(locators.BUTTON_CREATE_LEAD_FORM)
    def BUTTON_CREATE_LEAD_FORM(self):
        return self.find_with_check_visibility(self.locators.BUTTON_CREATE_LEAD_FORM)

    @property
    @add_write(locators.INPUT_LEAD_NAME)
    def INPUT_LEAD_NAME(self):
        return self.find_with_check_visibility(self.locators.INPUT_LEAD_NAME)
