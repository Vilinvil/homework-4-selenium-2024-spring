from cases import LoggedCase
from ui.pages.site_page import SitePage
import pytest
# from selenium.webdriver.common.keys import Keys
import random
# import time

class TestSitePage(LoggedCase):
    INVALID_DOMAIN = "INVALID_DOMAIN"
    ERROR_MSG_INVALID_DOMAIN = "Введите корректный адрес сайта (вида: example.ru)"
    NOTHING_FIND_TEXT = "Ничего не найдено"

    EXISTED_DOMAIN = f"my-kopilka.ru"
    # CORRECT_DOMAIN = f"https://vk{random.randint(10, 20)}.ru"
    
    # DELETE_DOMAIN = f"https://not-my-kopilka{random.randint(5, 100)}.ru"
    # FIND_TEXT = "Нашли пиксели, привязанные к сайту"
    # CREATE_PIXEL_ID = "Создан ID пикселя"
    # SEARCH_KOPILKA = "Kopilka"

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

    @pytest.mark.skip
    def test_create_delete_pixel(self):
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


    @pytest.mark.skip
    def test_open_add_pixel_modal(self):
        self.site_page.click_create_pixel_button()
        text_add_pixel = self.site_page.get_add_pixel_message()
        assert text_add_pixel != None

    @pytest.mark.skip
    def test_input_invalid_domain(self):
        self.site_page.click_create_pixel_button()

        self.site_page.enter_in_domain_name_field(self.INVALID_DOMAIN)

        self.site_page.click_frame_button()
        error_text = self.site_page.get_error_message()
        
        assert error_text == self.ERROR_MSG_INVALID_DOMAIN

    @pytest.mark.skip
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

    @pytest.mark.skip
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
        


    @pytest.mark.skip
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

    @pytest.mark.skip
    def test_create_and_delete_pixel(self):
        self.site_page.click_create_pixel_button()
        self.site_page.enter_in_domain_name_field(self.EXISTED_DOMAIN)
        self.site_page.click_frame_button()
        self.site_page.click_create_pixel_copy()

        # странное поведение сайта: если ввести несуществующий сайт и сразу закрыть окно, 
        # то пиксель создастся и добавиться в список, при этом если не закрывать окно,
        # то домен не создается и появлется сообщение об ошибке

        # при этом без автотестов не получается отловить данную ситуацию
        assert self.site_page.get_pixel_create_message().startswith("Создан ID пикселя")
        self.site_page.close_modal()
        self.site_page.open_delete_modal()
        self.site_page.click_delete_button()


    @pytest.mark.skip
    def test_remove_pixel(self):
        self.site_page.click_create_pixel_button()
        self.site_page.enter_in_domain_name_field(self.DELETE_DOMAIN)
        self.site_page.click_frame_button()
        self.site_page.close_modal()
        self.site_page.open_delete_modal()
        self.site_page.click_delete_button()

    @pytest.mark.skip
    def test_rename_pixel(self):
        self.site_page.click_create_pixel_button()
        self.site_page.enter_in_domain_name_field(self.NEW_DOMAIN)
        self.site_page.click_frame_button()
        self.site_page.close_modal()
   

        self.site_page.open_update_modal()
        
        self.site_page.enter_in_update_modal_new_domain(self.UPDATE_DOMAIN)
        self.site_page.submit_update_button()
        # self.site_page.refresh()
        # while 1:
        #     pass
        # self.site_page.enter_in_search_field(self.UPDATE_DOMAIN)
        # # while 1:
        # #     pass
        # raw = self.site_page.get_pixel_raw()

        # assert raw != None
        # assert self.site_page.get_span_pixel_name(raw, self.UPDATE_DOMAIN) != None
        # assert self.site_page.get_span_pixel_status(raw, self.STATUS_DONT_ARRIVE) != None

        # self.site_page.open_delete_modal()
        # self.site_page.click_delete_button()

    @pytest.mark.skip
    def test_find_no_results(self):
        self.site_page.click_create_pixel_button()
        self.site_page.enter_in_domain_name_field(self.NEW_DOMAIN)
        self.site_page.click_frame_button()
        self.site_page.close_modal()
        self.site_page.enter_in_search_field(self.INVALID_DOMAIN)
        assert self.site_page.get_not_found_pixel_message() == self.NOTHING_FIND_TEXT

    @pytest.mark.skip
    def test_find_pixel(self):
        self.site_page.enter_in_search_field(self.EXISTED_DOMAIN)

        assert self.site_page.verify_domain_found() == self.SEARCH_KOPILKA

    @pytest.mark.skip
    def test_create_delete_pixel(self):
        self.site_page.click_create_pixel_button()
        self.site_page.enter_in_domain_name_field(self.NEW_DOMAIN)
        self.site_page.click_frame_button()
        self.site_page.close_modal()
        self.site_page.enter_in_search_field(self.NEW_DOMAIN)
        raw = self.site_page.get_pixel_raw()
        
        assert raw != None
        assert self.site_page.get_span_pixel_name(raw, self.NEW_DOMAIN) != None
        assert self.site_page.get_span_pixel_status(raw, self.STATUS_DONT_ARRIVE) != None

        self.site_page.enter_in_search_field("".join([self.NEW_DOMAIN[i] for i in range(2)]))

        assert raw != None
        assert self.site_page.get_span_pixel_name(raw, self.NEW_DOMAIN) != None
        assert self.site_page.get_span_pixel_status(raw, self.STATUS_DONT_ARRIVE) != None

        self.site_page.enter_in_search_field(self.INVALID_DOMAIN)
        assert self.site_page.get_not_found_pixel_message() == self.NOTHING_FIND_TEXT

        self.site_page.enter_in_search_field("")
        
        self.site_page.open_delete_modal()
        self.site_page.click_delete_button()
