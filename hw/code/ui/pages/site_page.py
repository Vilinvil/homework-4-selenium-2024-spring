from ui.pages.base_page import BasePage
from ui.locators.site_locators import SitePageLocators

class SitePage(BasePage):
    url = "https://ads.vk.com/hq/pixels"
    locators = SitePageLocators()

    def click_create_pixel_button(self):
        self.click(self.locators.BUTTON_CREATE_NEW_PIXEL)

    def get_error_message(self):
        return self.find(self.locators.ERROR_DOMAIN_INPUT).text

    def enter_pixel_id(self):
        return self.find(self.locators.PIXEL_ID_INPUT)

    def input_email_owner(self):
        return self.find(self.locators.EMAIL_INPUT, 3)

    def click_frame_button(self):
        self.click(self.locators.BUTTON_GROUP_IFRAME, 5)

    def get_pixel_found_message(self):
        return self.find(self.locators.MESSAGE_PIXEL_FOUND).text

    def enter_domain_name(self):
        return self.find(self.locators.DOMAIN_INPUT)

    def find_add_pixel_header(self):
        return self.find(self.locators.TEXT_ADD_PIXEL_HEADER).text

    def open_more_menu(self):
        self.scroll_and_click(self.locators.BUTTON_MENU_MORE)

    def submit_update_button(self):
        self.click(self.locators.BUTTON_SUBMIT_UPDATE)

    def update_name_input(self):
        return self.find(self.locators.INPUT_PIXEL_NAME_UPDATE)

    def open_update_modal(self):
        self.open_more_menu()
        self.click(self.locators.DROPDOWN_MENU_UPDATE)

    def open_delete_modal(self):
        self.open_more_menu()
        self.click(self.locators.DROPDOWN_MENU_DELETE)

    def click_delete_button(self):
        self.click(self.locators.BUTTON_DELETE_CONFIRM)

    def verify_no_pixels_message(self):
        return self.find(self.locators.TEXT_NO_PIXELS_FOUND).text

    def create_new_pixel(self, domain_name):
        self.click_create_pixel_button()

        domain_input = self.enter_domain_name()
        domain_input.clear()
        domain_input.send_keys(domain_name)

        self.click_frame_button()
        self.click_create_pixel_button()
        self.click(self.locators.BUTTON_CLOSE_MODAL)

    def search_for_pixel(self, domain_name):
        return self.find(self.locators.find_element(domain_name))

    def verify_update_successful(self):
        return self.find(self.locators.TEXT_UPDATE_CONFIRM).text

    def verify_nothing_found(self):
        return self.find(self.locators.TEXT_NOTHING_FOUND).text

    def verify_domain_found(self):
        return self.find(self.locators.TEXT_PIXEL_DOMAIN_FOUND).text

    def search_input_field(self):
        return self.find(self.locators.SEARCH_INPUT)

    def click_add_pixel_button(self):
        self.click(self.locators.BUTTON_ADD_PIXEL)
