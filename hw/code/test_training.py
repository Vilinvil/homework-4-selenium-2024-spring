import pytest

from cases import LoggedCase
from ui.pages.training_page import TrainingPage


class TestTraining(LoggedCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_training(self, driver):
        self.training_page = TrainingPage(self.driver)
        self.main_page.open_training()

    def test_display(self):
        assert self.training_page.TITLE
        assert self.training_page.BUTTON_TRY_LATER
        assert self.training_page.BUTTON_CLOSE

    @pytest.mark.parametrize('section_name',
                             [
                                 'Сообщество ВКонтакте',
                                 'Сайт',
                                 'Каталог товаров',
                                 'VK Mini Apps'
                             ], )
    def test_display_content_list(self, section_name):
        assert self.training_page.SECTION_IN_CONTENT_LIST_BY_NAME(section_name)

    @pytest.fixture(scope='function')
    def setup_training_site(self):
        self.training_page.BUTTON_SITE.open_view()

    def test_display_site_section(self, setup_training_site):
        assert self.training_page.SITE_TITLE
        assert self.training_page.SITE_BUTTON_VIDEO
        assert self.training_page.BUTTON_ARTICLES
        assert self.training_page.SITE_BUTTON_STEP_BY_STEP_TRAINING

    @pytest.fixture(scope="function")
    def setup_step_by_step(self, setup_training_site):
        self.training_page.click(self.training_page.SITE_BUTTON_STEP_BY_STEP_TRAINING)

    def test_full_way_step_by_step(self, setup_step_by_step):
        campaign_shared_page = self.training_page.step1_full_way_step_by_step()

        campaign_shared_page = self.training_page.step2_of_full_way_step_by_step(campaign_shared_page)

        campaign_shared_page = self.training_page.step3_of_full_way_step_by_step(campaign_shared_page)

        self.training_page.step4_of_full_way_step_by_step(campaign_shared_page)
