from ui.pages.base_page import PageWithView, PageWithRedirectWindow
from ui.locators.site_locators import SitePageLocators

from selenium.webdriver.support import expected_conditions as EC
from ui.pages.base_page_functionality import BasePageFunctionality, add_write, add_click

class SitePage(PageWithView, PageWithRedirectWindow):
    url = "https://ads.vk.com/hq/pixels"
    locators = SitePageLocators()

    def click_create_pixel_by_id(self):
        self.click(self.locators.LABEL_ID_PIXEL)

    def click_create_pixel_button(self):
        self.click(self.locators.BUTTON_CREATE_NEW_PIXEL)

    def click_create_pixel_copy(self):
        self.click(self.locators.BUTTON_CREATE_COPY_PIXEL)

    def get_error_message(self):
        return self.find(self.locators.ERROR_DOMAIN_INPUT).text

    @add_write
    def get_input_field_pixel_id(self):
        return self.find(self.locators.PIXEL_ID_INPUT)
    
    def enter_pixel_id(self, input_id):
        domain_input = self.get_input_field_pixel_id()
        domain_input.clear()
        domain_input.send_keys(input_id)

    def enter_in_domain_name_field(self, input_domain):
        domain_input = self.get_input_field_domain_name()
        domain_input.clear()
        domain_input.send_keys(input_domain)

    def enter_in_update_modal_new_domain(self, new_domain):
        update_input = self.get_update_name_input()
        update_input.clear()
        update_input.send_keys(new_domain)

    def enter_in_search_field(self, domain_name):
        domain_input = self.get_search_input_field()
        domain_input.clear()
        domain_input.send_keys(domain_name)

    @add_write
    def get_input_email_owner(self):
        return self.find(self.locators.EMAIL_INPUT, 3)
    
    @add_write
    def get_input_email_owner_input(self):
        return self.find(self.locators.INPUT_EMAIL_INPUT, 3)

    def click_frame_button(self):
        self.click(self.locators.BUTTON_GROUP_IFRAME, 5)

    def get_pixel_create_message(self):
        return self.find(self.locators.TEXT_CREATE_PIXEL_ID_CONFIRM).text

    def get_pixel_found_message(self):
        return self.find(self.locators.MESSAGE_PIXEL_FOUND).text

    def get_input_field_domain_name(self):
        return self.find(self.locators.DOMAIN_INPUT)

    def get_add_pixel_message(self):
        return self.find(self.locators.TEXT_ADD_PIXEL_HEADER).text
    
    def get_not_found_pixel_message(self):
        return self.find(self.locators.TEXT_NOTHING_FOUND).text

    def open_more_menu(self):
        self.hover_wrapper(self.locators.BUTTON_MENU_MORE)
        self.click(self.locators.BUTTON_MENU_MORE)

    def submit_update_button(self):
        self.click(self.locators.BUTTON_SUBMIT_UPDATE)

    def get_update_name_input(self):
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

        domain_input = self.get_input_field_domain_name()
        domain_input.clear()
        domain_input.send_keys(domain_name)

        self.click_frame_button()
        self.click_create_pixel_button()
        self.click(self.locators.BUTTON_CLOSE_MODAL)

    # def search_for_pixel(self, domain_name):
    #     return self.find(self.locators.find_element(domain_name))

    def verify_nothing_found(self):
        return self.find(self.locators.TEXT_NOTHING_FOUND).text

    def verify_domain_found(self):
        return self.find(self.locators.TEXT_PIXEL_DOMAIN_FOUND).text

    def get_search_input_field(self):
        return self.find(self.locators.SEARCH_INPUT)

    def click_add_pixel_button(self):
        self.click(self.locators.BUTTON_ADD_PIXEL)

    def close_modal(self):
        self.click(self.locators.BUTTON_CLOSE_MODAL)

    # def check_new_pixel(self, name):
    #     self.find(self.locators.PIXEL_NAME(name))

    def get_pixel_raw(self):
        return self.find(self.locators.PIXEL_ROW)
    
    def get_span_pixel_name(self, pixel_raw, name):
        return self.find_child(pixel_raw, self.locators.PIXEL_NAME(name))
    
    def get_div_pixel_id(self, pixel_raw, id):
        return self.find_child(pixel_raw, self.locators.PIXEL_ID(id))
    
    def get_span_pixel_status(self, pixel_raw, status):
        return self.find_child(pixel_raw, self.locators.PIXEL_STATUS(status))
    
    @add_click
    def get_access_button(self):
        return self.find(self.locators.BUTTON_REQUEST_ACCESS)
    
    @add_click
    def get_confirm_access_button(self):
        return self.find(self.locators.BUTTON_REQUEST)
    
    def refresh(self):
        self.driver.refresh()
        self.close_alert_if_shown()
