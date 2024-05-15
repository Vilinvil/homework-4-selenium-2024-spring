import pytest

from cases import LoggedCase
from ui.pages.training_page import TrainingPage


class TestTraining(LoggedCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_training(self, driver, config):
        self.training_page = TrainingPage(self.driver)
        self.training_page.open_modal_view(self.training_page.locators.BUTTON_START_TRAINING,
                                           self.training_page.locators_shared.MODAL_PAGE)

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
