import pytest

from cases import LoggedCase
from ui.pages.training_page import TrainingPage
from ui.locators.training_locators import TrainingPageLocators

from selenium.webdriver.support import expected_conditions as EC


class TestTraining(LoggedCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_training(self, driver):
        self.training_page = TrainingPage(self.driver)
        self.training_page.open_modal_view(self.training_page.locators.BUTTON_START_TRAINING,
                                           self.training_page.locators_shared.SIGN_OPENING_MODAL_VIEW)

    def test_display(self):
        assert self.training_page.find(self.training_page.locators.TITLE,
                                       until_EC=EC.visibility_of_element_located)
        assert self.training_page.find(self.training_page.locators.BUTTON_TRY_LATER,
                                       until_EC=EC.visibility_of_element_located)
        assert self.training_page.find(self.training_page.locators.BUTTON_CLOSE,
                                       until_EC=EC.visibility_of_element_located)

    @pytest.mark.parametrize('section_name',
                             [
                                 'Сообщество ВКонтакте',
                                 'Сайт',
                                 'Каталог товаров',
                                 'VK Mini Apps'
                             ], )
    def test_display_content_list(self, section_name):
        assert self.training_page.find_section_in_content_list(section_name)

    @pytest.mark.parametrize('button_locator',
                             [
                                 TrainingPageLocators.BUTTON_TRY_LATER,
                                 TrainingPageLocators.BUTTON_CLOSE,
                             ], )
    def test_close_by_button(self, button_locator):
        self.training_page.close_modal_view(button_locator, self.training_page.locators_shared.SIGN_OPENING_MODAL_VIEW)

    def test_close_by_click_outside_modal_view(self):
        self.training_page.click_zero_coordinate()

    @pytest.fixture(scope='function')
    def setup_training_site(self):
        self.training_page.click(self.training_page.locators.site_locators.BUTTON_SITE)

    def test_display_site_section(self, setup_training_site):
        assert self.training_page.find(self.training_page.locators.site_locators.TITLE,
                                       until_EC=EC.visibility_of_element_located)
        assert self.training_page.find(self.training_page.locators.site_locators.BUTTON_VIDEO,
                                       until_EC=EC.visibility_of_element_located)
        assert self.training_page.find(self.training_page.locators.site_locators.BUTTON_ARTICLES,
                                       until_EC=EC.visibility_of_element_located)
        assert self.training_page.find(
            self.training_page.locators.site_locators.BUTTON_STEP_BY_STEP_TRAINING,
            until_EC=EC.visibility_of_element_located)

    def test_site_redirect_article(self, setup_training_site):
        self.training_page.redirect_window(self.training_page.locators.site_locators.BUTTON_ARTICLES)

        assert (self.training_page.wait().
                until(EC.url_matches("https://expert.vk.com/courses/kak-prodvigat-saiti-v-vk-reklame/")))

    def test_site_open_video(self, setup_training_site):
        self.training_page.click(self.training_page.locators.site_locators.BUTTON_VIDEO)

        self.training_page.wait().until(
            EC.visibility_of_element_located(self.training_page.locators.site_locators.SIGN_OPENING_VIDEO))

    @pytest.fixture(scope="function")
    def setup_step_by_step(self, setup_training_site):
        self.training_page.click(self.training_page.locators.site_locators.BUTTON_STEP_BY_STEP_TRAINING)

    def test_open_step_by_step(self, setup_step_by_step):
        assert self.training_page.find(self.training_page.locators.campaign_page_shared_locators.
                                       STEP1_BUTTON_CREATE_CAMPAIGN, until_EC=EC.visibility_of_element_located)
        assert self.training_page.find(self.training_page.locators.step_by_step_locators.
                                       STEP1_TOOLTIP_CREATE_CAMPAIGN, until_EC=EC.visibility_of_element_located)

    def test_interrupt_step_by_step(self, setup_step_by_step):
        self.training_page.click(self.training_page.locators.step_by_step_locators.STEP1_BUTTON_TOOLTIP_CLOSE)
        self.training_page.close_modal_view(self.training_page.locators.step_by_step_locators.
                                            STEP1_BUTTON_CLOSE_TRAINING,
                                            self.training_page.locators.step_by_step_locators.
                                            STEP1_TOOLTIP_CREATE_CAMPAIGN)

    def test_full_way_step_by_step(self, setup_step_by_step):
        campaign_shared_page = self.training_page.test_step1_of_full_way_step_by_step()

        campaign_shared_page = self.training_page.test_step2_of_full_way_step_by_step(campaign_shared_page)

        campaign_shared_page = self.training_page.test_step3_of_full_way_step_by_step(campaign_shared_page)

        self.training_page.test_step4_of_full_way_step_by_step(campaign_shared_page)
