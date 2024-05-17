import pytest

from cases import LoggedCase
from ui.pages.training_page import TrainingPage
from ui.locators.training_locators import TrainingPageLocators

from selenium.webdriver.support import expected_conditions as EC


class TestTraining(LoggedCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_training(self, driver, config):
        self.training_page = TrainingPage(self.driver)
        self.training_page.open_modal_view(self.training_page.locators.BUTTON_START_TRAINING,
                                           self.training_page.locators_shared.SIGN_OPENING_MODAL_VIEW)

    def test_display(self):
        assert self.training_page.find(self.training_page.locators.TITLE).is_displayed()
        assert self.training_page.find(self.training_page.locators.BUTTON_TRY_LATER).is_displayed()
        assert self.training_page.find(self.training_page.locators.BUTTON_CLOSE).is_displayed()

    @pytest.mark.parametrize('section_name',
        [
            'Сообщество ВКонтакте',
            'Сайт',
            'Каталог товаров',
            'VK Mini Apps'
        ],)
    def test_display_content_list(self, section_name):
        assert self.training_page.find_section_in_content_list(section_name).is_displayed()

    @pytest.mark.parametrize('button_locator',
                             [
                                 TrainingPageLocators.BUTTON_TRY_LATER,
                                 TrainingPageLocators.BUTTON_CLOSE,
                             ],)
    def test_close_by_button(self, button_locator):
        self.training_page.close_modal_view(button_locator, self.training_page.locators_shared.SIGN_OPENING_MODAL_VIEW)

    def test_close_by_click_outside_modal_view(self):
        self.training_page.click_zero_coordinate()

    @pytest.fixture(scope='function')
    def setup_training_site(self, driver, config):
        self.training_page.click(self.training_page.locators.site_locators.BUTTON_SITE)

    def test_display_site_section(self, setup_training_site):
        assert self.training_page.find(self.training_page.locators.site_locators.TITLE).is_displayed()
        assert self.training_page.find(self.training_page.locators.site_locators.BUTTON_VIDEO).is_displayed()
        assert self.training_page.find(self.training_page.locators.site_locators.BUTTON_ARTICLES).is_displayed()
        assert self.training_page.find(self.training_page.locators.site_locators.BUTTON_STEP_BY_STEP_TRAINING).is_displayed()

    def test_site_redirect_article(self, setup_training_site):
        self.training_page.redirect_window(self.training_page.locators.site_locators.BUTTON_ARTICLES)

        assert (self.training_page.wait().
                until(EC.url_matches("https://expert.vk.com/courses/kak-prodvigat-saiti-v-vk-reklame/")))

    def test_site_open_video(self, setup_training_site):
        self.training_page.click(self.training_page.locators.site_locators.BUTTON_VIDEO)

        self.training_page.wait().until(
            EC.visibility_of_element_located(self.training_page.locators.site_locators.SIGN_OPENING_VIDEO))
