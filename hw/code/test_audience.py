import pytest

from cases import LoggedCase
from ui.pages.audience_page import AudiencePage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


class TestAudience(LoggedCase):
    @pytest.fixture(scope='function', autouse=True)
    def setup_training(self, driver, config):
        self.main_page.click(self.main_page.locators.NAV_BUTTON_AUDIENCE_SECTION)
        self.audience_page = AudiencePage(self.driver)

    @pytest.mark.parametrize('source_items', [
        'Существующая аудитория',
        'Список пользователей',
        'Ключевые фразы',
        'События в рекламной компании',
        'События в мобильном приложении',
        'События в лид-форме',
        'События на сайте',
        'Подписчики сообществ',
        'Музыканты'
    ])
    @pytest.mark.parametrize('tab_items', [
            'audience',
            'audience.users_list'
    ])
    def test_display_start(self, tab_items, source_items):
        assert self.audience_page.find_tabs_in_subnav(tab_items)
        self.audience_page.click_create_audience()
        assert self.audience_page.find(self.audience_page.locators.INPUT_NAME_GROUP,
                                       until_EC=EC.visibility_of_element_located)
        assert self.audience_page.find(self.audience_page.locators.BUTTON_SAVE_GROUP,
                                       until_EC=EC.visibility_of_element_located)
        assert self.audience_page.find(self.audience_page.locators.BUTTON_CANCEL_GROUP,
                                       until_EC=EC.visibility_of_element_located)
        self.audience_page.click(self.audience_page.locators.BUTTON_ADD_SOURCE)
        assert self.audience_page.find_source_items(source_items)
        assert self.audience_page.find(self.audience_page.locators.BUTTON_SAVE_GROUP,
                                       until_EC=EC.visibility_of_element_located)
        assert self.audience_page.find(self.audience_page.locators.BUTTON_CANCEL_GROUP,
                                       until_EC=EC.visibility_of_element_located)

    def test_create(self):
        self.audience_page.click_create_audience()
        self.audience_page.click(self.audience_page.locators.BUTTON_ADD_SOURCE)
        self.audience_page.click(self.audience_page.locators.SUBSCRIBERS_SOURCE)
        self.audience_page.click(self.audience_page.locators.ADD_LIST)
        self.audience_page.click(self.audience_page.locators.VK_COMMUNITY)
        self.audience_page.write_input(self.audience_page.locators.TEXTAREA, 'https://vk.com/vk_ads')
        self.audience_page.click(self.audience_page.locators.ADD)
        self.audience_page.click(self.audience_page.locators.BUTTON_SAVE_GROUP)
        self.audience_page.click(self.audience_page.locators.BUTTON_SAVE_GROUP)
