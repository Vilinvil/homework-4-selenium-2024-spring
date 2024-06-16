from cases import LoggedCase
from ui.pages.site_page import SitePage
import pytest
import random


class TestSitePage(LoggedCase):
    INVALID_DOMAIN = "INVALID_DOMAIN"
    ERROR_MSG_INVALID_DOMAIN = "Введите корректный адрес сайта (вида: example.ru)"
    NOTHING_FIND_TEXT = "Ничего не найдено"

    EXISTED_DOMAIN = f"my-kopilka.ru"

    NEW_DOMAIN = f"my-kopilka{random.randint(100, 1000)}.ru"
    UPDATE_DOMAIN = "update-domain.ru"
    STATUS_DONT_ARRIVE = "Данные не поступают"
    STATUS_ACCESS_REQUESTED = "Доступ запрошен"

    ID = "3518620"
    EMAIL = "sachatarba@rambler.ru"

    ONE_EXISTED_DOMAIN = "my-kopilka100.ru"
    TWO_EXISTED_DOMAIN = "etotopchel.com"

    @pytest.fixture(scope='function', autouse=True)
    def setup_site_page(self):
        self.main_page.click_redirect_to_site_page()
        self.site_page = SitePage(self.driver)

    # @pytest.mark.skip
    def test_pixel_create_delete(self):
        self.site_page.click_create_pixel_button()
        self.site_page.enter_in_domain_name_field(self.NEW_DOMAIN)
        self.site_page.click_frame_button()
        self.site_page.close_modal()
        self.site_page.enter_in_search_field(self.NEW_DOMAIN)
        raw = self.site_page.get_pixel_raw()
        
        assert raw != None
        assert self.site_page.get_span_pixel_name(raw, self.NEW_DOMAIN) != None
        assert self.site_page.get_span_pixel_status(raw, self.STATUS_DONT_ARRIVE) != None
        
        self.site_page.open_delete_modal()
        self.site_page.click_delete_button()


    # @pytest.mark.skip
    def test_input_existed_domain(self):
        self.site_page.click_create_pixel_button()
        self.site_page.enter_in_domain_name_field(self.ONE_EXISTED_DOMAIN)

        self.site_page.click_frame_button()
        self.site_page.get_access_button().clicks()
        self.site_page.get_input_email_owner_input().write(self.EMAIL)
        self.site_page.get_confirm_access_button().clicks()
        self.site_page.close_modal()

        self.site_page.enter_in_search_field(self.ONE_EXISTED_DOMAIN)
        raw = self.site_page.get_pixel_raw()
        
        assert raw != None
        assert self.site_page.get_span_pixel_name(raw, self.ONE_EXISTED_DOMAIN) != None
        assert self.site_page.get_span_pixel_status(raw, self.STATUS_ACCESS_REQUESTED) != None
        
        self.site_page.open_delete_modal()
        self.site_page.click_delete_button()

    # @pytest.mark.skip
    def test_input_two_existed_domain(self):
        self.site_page.click_create_pixel_button()
        self.site_page.enter_in_domain_name_field(self.TWO_EXISTED_DOMAIN)

        self.site_page.click_frame_button()
        self.site_page.get_access_button().clicks()
        self.site_page.get_input_email_owner_input().write(self.EMAIL)
        self.site_page.get_confirm_access_button().clicks()
        self.site_page.close_modal()

        self.site_page.enter_in_search_field(self.TWO_EXISTED_DOMAIN)
        raw = self.site_page.get_pixel_raw()
        
        assert raw != None
        assert self.site_page.get_span_pixel_name(raw, self.TWO_EXISTED_DOMAIN) != None
        assert self.site_page.get_span_pixel_status(raw, self.STATUS_ACCESS_REQUESTED) != None
        
        self.site_page.open_delete_modal()
        self.site_page.click_delete_button()
        


    # @pytest.mark.skip
    def test_create_delete_pixel_by_id(self):
        self.site_page.click_create_pixel_button()
        self.site_page.click_create_pixel_by_id()
        self.site_page.get_input_email_owner().write(self.EMAIL)
        self.site_page.get_input_field_pixel_id().write(self.ID)
        self.site_page.click_frame_button()
        self.site_page.close_modal()
        self.site_page.enter_in_search_field(self.ID)
        raw = self.site_page.get_pixel_raw()

        assert raw != None
        assert self.site_page.get_div_pixel_id(raw, self.ID) != None
        assert self.site_page.get_span_pixel_status(raw, self.STATUS_ACCESS_REQUESTED) != None
        
        self.site_page.open_delete_modal()
        self.site_page.click_delete_button()

    
    

    # @pytest.mark.skip
    def test_pixel_search(self):
        self.site_page.click_create_pixel_button()
        self.site_page.enter_in_domain_name_field(self.NEW_DOMAIN)
        self.site_page.click_frame_button()
        self.site_page.close_modal()

        search = self.site_page.get_search_input_field()
        search.write(self.NEW_DOMAIN)
        raw = self.site_page.get_pixel_raw()
        
        assert raw != None
        assert self.site_page.get_span_pixel_name(raw, self.NEW_DOMAIN) != None
        assert self.site_page.get_span_pixel_status(raw, self.STATUS_DONT_ARRIVE) != None

        search.write("")
        self.site_page.clear_search()
        search.write(self.NEW_DOMAIN[:2])
        raw = self.site_page.get_pixel_raw()

        assert raw != None
        assert self.site_page.get_span_pixel_name(raw, self.NEW_DOMAIN) != None
        assert self.site_page.get_span_pixel_status(raw, self.STATUS_DONT_ARRIVE) != None

        search.write("")
        self.site_page.clear_search()
        search.write(self.INVALID_DOMAIN)
        assert self.site_page.get_not_found_pixel_message() == self.NOTHING_FIND_TEXT

        search.write("")
        self.site_page.clear_search()
        search.write("")
        self.site_page.open_delete_modal()
        self.site_page.click_delete_button()
