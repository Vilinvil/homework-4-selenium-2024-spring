from ui.pages.base_page_functionality import BasePageFunctionality, add_click, add_write, add_get_value
from ui.locators.leads_locators import LeadsPageLocators, LeadsPageDesignLocators

from selenium.webdriver.support import expected_conditions as EC


class LeadsPageDesign(BasePageFunctionality):
    url = "https://ads.vk.com/hq/leadads/leadforms"
    locators = LeadsPageDesignLocators()

    @property
    def HEADER(self):
        return self.find_with_check_visibility(self.locators.HEADER)

    @property
    @add_write(locators.INPUT_LEAD_NAME)
    @add_get_value(locators.INPUT_LEAD_NAME)
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

    @property
    def PREVIEW_CONTAINER(self):
        return self.find_with_check_visibility(self.locators.PREVIEW_CONTAINER)

    @property
    def PREVIEW_TITLE_CONTACT_DETAILS(self):
        return self.find_with_check_visibility(self.locators.PREVIEW_TITLE_CONTACT_DETAILS)

    @property
    def MEDIA_HEADER(self):
        return self.find_with_check_visibility(self.locators.MEDIA_HEADER)

    @property
    def MEDIA_UPLOAD(self):
        return self.find_with_check_visibility(self.locators.MEDIA_UPLOAD)

    @property
    @add_click(locators.MEDIA_DEFAULT_IMAGE)
    def MEDIA_DEFAULT_IMAGE(self):
        return self.find_with_check_visibility(self.locators.MEDIA_DEFAULT_IMAGE)

    @property
    def PREVIEW_LOGO(self):
        return self.find_with_check_visibility(self.locators.PREVIEW_LOGO)

    @property
    def PREVIEW_TOP_PART_TITLE(self):
        return self.find_with_check_visibility(self.locators.PREVIEW_TOP_PART_TITLE)

    @property
    @add_click(locators.RADIOGROUP_BUTTON_MORE_TEXT)
    def RADIOGROUP_BUTTON_MORE_TEXT(self):
        return self.find_with_check_visibility(self.locators.RADIOGROUP_BUTTON_MORE_TEXT)

    def check_active_RADIOGROUP_BUTTON_MORE_TEXT(self):
        assert self.find(self.locators.INPUT_SHORT_DESCRIPTION, until_EC=EC.invisibility_of_element_located)
        assert self.find_with_check_visibility(self.locators.INPUT_MORE_TEXT)

    def check_HEADER_LEAD_FORM_TITLE(self, title):
        assert self.find_with_check_visibility(self.locators.HEADER_LEAD_FORM_TITLE(title))


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
