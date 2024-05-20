from cases import LoggedCase
from ui.pages.site_page import SitePage
import pytest
from selenium.webdriver.common.keys import Keys

class TestSitePage(LoggedCase):
    NON_EXISTENT_DOMAIN = "NON_EXISTENT"
    CORRECT_DOMAIN = "https://my-kopilka.ru"
    UPDATE_DOMAIN = "UPDATE_DOMAIN"
    DELETE_DOMAIN = "https://delete.com"
    FIND_TEXT = "Нашли пиксели, привязанные к сайту"
    CREATE_PIXEL_ID = "Создан ID пикселя"
    NOTHING_PIXEL_TEXT = "Нет привязанных пикселей трекинга"
    SEARCH_TEXT = "Example Domain"
    NOTHING_FIND_TEXT = "Ничего не найдено"

    @pytest.fixture(scope='function', autouse=True)
    def setup_site_page(self, driver):
        self.site_page = SitePage(self.driver)

    def test_open_add_pixel_modal(self):
        self.site_page.click_create_pixel_button()
        text_add_pixel = self.site_page.find_add_pixel_header()
        assert text_add_pixel != None

    def test_input_invalid_domain(self):
        self.site_page.click_create_pixel_button()

        domain_input = self.site_page.enter_domain_name()
        domain_input.clear()
        domain_input.send_keys(self.NON_EXISTENT_DOMAIN)

        self.site_page.click_frame_button()

        error_text = self.site_page.get_error_message()
        assert error_text == 'Введите корректный адрес сайта (вида: example.ru)'

    def test_input_valid_domain(self):
        self.site_page.click_create_pixel_button()

        domain_input = self.site_page.enter_domain_name()
        domain_input.clear()
        domain_input.send_keys(self.CORRECT_DOMAIN)

        self.site_page.click_frame_button()

        find_text = self.site_page.get_pixel_found_message()
        assert find_text == self.FIND_TEXT

    def test_verify_pixel_id_input(self):
        self.site_page.click_create_pixel_button()

        button = self.site_page.enter_pixel_id()
        button.send_keys(Keys.RIGHT)
        assert self.site_page.input_email_owner() != None
        assert self.site_page.enter_pixel_id() != None

    def test_create_and_delete_pixel(self):
        self.site_page.click_create_pixel_button()

        domain_input = self.site_page.enter_domain_name()
        domain_input.clear()
        domain_input.send_keys(self.CORRECT_DOMAIN)

        self.site_page.click_frame_button()
        self.site_page.click_create_pixel_button()
        assert self.site_page.find_text_create_ID_pixel().startswith(self.CREATE_PIXEL_ID)
        self.site_page.click(self.locators.BUTTON_CLOSE_MODAL)
        self.site_page.delete_pixel()

    def test_remove_pixel(self):
        self.site_page.create_new_pixel(self.DELETE_DOMAIN)
        self.site_page.open_delete_modal()
        self.site_page.click_delete_button()

        assert self.site_page.verify_no_pixels_message() == self.NOTHING_PIXEL_TEXT

    def test_rename_pixel(self):
        self.site_page.create_new_pixel(self.CORRECT_DOMAIN)
        self.site_page.open_update_modal()

        update_input = self.site_page.update_name_input()
        update_input.clear()
        update_input.send_keys(self.UPDATE_DOMAIN)
        self.site_page.submit_update_button()

        assert self.site_page.verify_update_successful() == self.UPDATE_DOMAIN
        self.site_page.click(self.locators.BUTTON_CLOSE_MODAL)
        self.site_page.delete_pixel()

    def test_find_no_results(self):
        self.site_page.create_new_pixel(self.CORRECT_DOMAIN)
        search_input = self.site_page.search_input_field()
        search_input.clear()
        search_input.send_keys(self.NON_EXISTENT_DOMAIN)

        assert self.site_page.verify_nothing_found() == self.NOTHING_FIND_TEXT
        self.site_page.delete_pixel()

    def test_find_pixel(self):
        self.site_page.create_new_pixel(self.CORRECT_DOMAIN)
        search_input = self.site_page.search_input_field()
        search_input.clear()
        search_input.send_keys(self.SEARCH_TEXT)

        assert self.site_page.verify_domain_found() == self.SEARCH_TEXT
        self.site_page.delete_pixel()
