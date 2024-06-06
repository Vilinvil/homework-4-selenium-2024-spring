from ui.pages.base_page_functionality import BasePageFunctionality, add_click, add_write, add_hover
from ui.locators.leads_locators import LeadsPageLocators, LeadsPageDesignLocators


class LeadsPageDesign(BasePageFunctionality):
    url = "https://ads.vk.com/hq/leadads/leadforms"
    locators = LeadsPageDesignLocators()

    @property
    def HEADER(self):
        return self.find_with_check_visibility(self.locators.HEADER)

    @property
    @add_write(locators.INPUT_LEAD_NAME)
    def INPUT_LEAD_NAME(self):
        return self.find_with_check_visibility(self.locators.INPUT_LEAD_NAME)

    @property
    @add_click(locators.BUTTON_SET_GLOBAL_IMAGE)
    def BUTTON_SET_GLOBAL_IMAGE(self):
        return self.find_with_check_visibility(self.locators.BUTTON_SET_GLOBAL_IMAGE)

    @property
    @add_write(locators.INPUT_ORGANIZATION)
    def INPUT_ORGANIZATION(self):
        return self.find_with_check_visibility(self.locators.INPUT_ORGANIZATION)

    @property
    def RADIOGROUP_FIRST_SCREEN(self):
        return self.find_with_check_visibility(self.locators.RADIOGROUP_FIRST_SCREEN)

    @property
    @add_write(locators.INPUT_TITLE)
    def INPUT_TITLE(self):
        return self.find_with_check_visibility(self.locators.INPUT_TITLE)

    @property
    @add_write(locators.INPUT_SHORT_DESCRIPTION)
    def INPUT_SHORT_DESCRIPTION(self):
        return self.find_with_check_visibility(self.locators.INPUT_SHORT_DESCRIPTION)

    @property
    @add_click(locators.PIPETTE_CHOICE_GRADIENT)
    def PIPETTE_CHOICE_GRADIENT(self):
        return self.find_with_check_visibility(self.locators.PIPETTE_CHOICE_GRADIENT)

    @property
    @add_click(locators.BUTTON_SET_MAIN_IMAGE)
    def BUTTON_SET_MAIN_IMAGE(self):
        return self.find_with_check_visibility(self.locators.BUTTON_SET_MAIN_IMAGE)


class LeadsPage(BasePageFunctionality):
    url = "https://ads.vk.com/hq/leadads/leadforms"
    locators = LeadsPageLocators()

    def __init__(self, driver):
        super().__init__(driver)
        self.design_page = LeadsPageDesign(driver)

    @property
    @add_click(locators.BUTTON_CREATE_LEAD_FORM)
    def BUTTON_CREATE_LEAD_FORM(self):
        return self.find_with_check_visibility(self.locators.BUTTON_CREATE_LEAD_FORM)

    @property
    @add_click(locators.BUTTON_CANCEL)
    def BUTTON_CANCEL(self):
        return self.find_with_check_visibility(self.locators.BUTTON_CANCEL)

    @property
    @add_click(locators.BUTTON_SUBMIT)
    def BUTTON_SUBMIT(self):
        return self.find_with_check_visibility(self.locators.BUTTON_SUBMIT)
