from cases import LoggedCase
from ui.pages.site_page import SitePage
import pytest
from selenium.webdriver.common.keys import Keys
import random
import time

class TestSitePage(LoggedCase):
    INVALID_DOMAIN = "INVALID_DOMAIN"
    ERROR_MSG_INVALID_DOMAIN = "Введите корректный адрес сайта (вида: example.ru)"

    EXISTED_DOMAIN = f"my-kopilka.ru"
    CORRECT_DOMAIN = f"https://vk{random.randint(10, 20)}.ru"
    UPDATE_DOMAIN = "UPDATE_DOMAIN"
    DELETE_DOMAIN = f"https://not-my-kopilka{random.randint(5, 100)}.ru"
    FIND_TEXT = "Нашли пиксели, привязанные к сайту"
    CREATE_PIXEL_ID = "Создан ID пикселя"
    NOTHING_FIND_TEXT = "Ничего не найдено"
    SEARCH_Kopilka = "Kopilka"

    @pytest.fixture(scope='function', autouse=True)
    def setup_site_page(self):
        self.main_page.click_redirect_to_site_page()
        self.site_page = SitePage(self.driver)

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
        self.site_page.enter_in_domain_name_field(self.EXISTED_DOMAIN)

        self.site_page.click_frame_button()

        find_text = self.site_page.get_pixel_found_message()
        assert find_text == self.FIND_TEXT

    @pytest.mark.skip
    def test_verify_pixel_id_input(self):
        self.site_page.click_create_pixel_button()
        self.site_page.click_create_pixel_by_id()

        # button = self.site_page.get_input_field_pixel_id()
        # button.send_keys(Keys.RIGHT)
        assert self.site_page.get_input_email_owner() != None
        assert self.site_page.get_input_field_pixel_id() != None

    @pytest.mark.skip
    def test_create_and_delete_pixel(self):
        self.site_page.click_create_pixel_button()
        self.site_page.enter_in_domain_name_field(self.EXISTED_DOMAIN)
        self.site_page.click_frame_button()
        self.site_page.click_create_pixel_copy()

        # странное поведение сайта: если ввести несуществующий сайт и сразу закрыть окно, 
        # то пиксель создастся и добавиться в список, при этом если не закрывать окно,
        # то домен не здается и появлется сообщение об ошибке

        # при этом в без автотестов не получается отловить данную ситуацию
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
        self.site_page.enter_in_domain_name_field(self.CORRECT_DOMAIN)
        self.site_page.click_frame_button()
        self.site_page.close_modal()

        self.site_page.open_update_modal()
        
        self.site_page.enter_in_update_modal_new_domain(self.UPDATE_DOMAIN)
        self.site_page.submit_update_button()

        self.site_page.close_modal()
        self.site_page.open_delete_modal()
        self.site_page.click_delete_button()

    @pytest.mark.skip
    def test_find_no_results(self):
        self.site_page.click_create_pixel_button()
        self.site_page.enter_in_domain_name_field(self.CORRECT_DOMAIN)
        self.site_page.click_frame_button()
        self.site_page.close_modal()
        self.site_page.enter_in_search_field(self.INVALID_DOMAIN)
        assert self.site_page.get_not_found_pixel_message() == self.NOTHING_FIND_TEXT

    @pytest.mark.skip
    def test_find_pixel(self):
        self.site_page.enter_in_search_field(self.EXISTED_DOMAIN)

        assert self.site_page.verify_domain_found() == self.SEARCH_Kopilka
