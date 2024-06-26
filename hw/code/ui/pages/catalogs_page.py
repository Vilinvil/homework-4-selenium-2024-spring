from os import path

from ui.pages.base_page_functionality import BasePageFunctionality, add_write, add_clicks
from ui.locators.catalogs_locators import CatalogLocators

from selenium.common import TimeoutException


class CatalogsPage(BasePageFunctionality):
    url = "https://ads.vk.com/hq/ecomm/catalogs"
    locators = CatalogLocators()

    @property
    @add_clicks
    def BUTTON_CREATE_CATALOG(self):
        return self.find_with_check_visibility(self.locators.BUTTON_CREATE_CATALOG)

    @property
    @add_clicks
    def BUTTON_BY_HAND(self):
        return self.find_with_check_visibility(self.locators.BUTTON_BY_HAND)

    @property
    @add_clicks
    def BUTTON_SELECT_FEED_TYPE(self):
        return self.find(self.locators.INPUT_TYPE_FEED)

    @property
    @add_clicks
    def OPTION_AUTO(self):
        return self.find_with_check_visibility(self.locators.OPTION_AUTO)

    def close_training_if_shown(self):
        try:
            self.find_with_check_visibility(self.locators.MODAL_VIEW_TRAINING)
            self.click(self.find(self.locators.CHOOSE_NO))
        except TimeoutException:
            pass

    def select_feed_auto(self):
        self.BUTTON_SELECT_FEED_TYPE.clicks()
        self.OPTION_AUTO.clicks()

    def load_feed_file(self, filepath):
        abspath = path.abspath(filepath)
        self.find(self.locators.FILE_INPUT).send_keys(abspath)

    @property
    @add_clicks
    def BUTTON_CONFIRM_CREATE_CATALOG(self):
        return self.find_with_check_visibility(self.locators.BUTTON_CONFIRM_CREATE_CATALOG)

    @property
    @add_write
    def INPUT_CATALOG_NAME(self):
        return self.find(self.locators.INPUT_CATALOG_NAME)

    @property
    @add_clicks
    def BUTTON_TO_GOODS(self):
        return self.find(self.locators.BUTTON_GOODS)

    @property
    def CATALOG_HEADER_NAME(self):
        return self.find(self.locators.CATALOG_NAME_HEADER).text

    @property
    @add_clicks
    def BUTTON_FEED_OR_COMMUNITY(self):
        return self.find_with_check_visibility(self.locators.FEED_OR_COMMUNITY)

    @property
    @add_clicks
    def BUTTON_SETTINGS(self):
        return self.find_with_check_visibility(self.locators.BUTTON_SETTINGS)

    @property
    @add_clicks
    def BUTTON_DELETE(self):
        return self.find_with_check_visibility(self.locators.BUTTON_DELETE)

    @property
    @add_clicks
    def BUTTON_CONFIRM_DELETE(self):
        return self.find(self.locators.BUTTON_CONFIRM_DELETE)

    @add_clicks
    def BUTTON_OPEN_GOOD(self, name):
        return self.find_with_check_visibility(self.locators.BUTTON_OPEN_GOOD(name), timeout=120)

    def INFO_FIELD(self, i):
        return self.find_with_check_visibility(self.locators.INFO_FIELD(i)).text

    @property
    def NOT_FOUND_MESSAGE(self):
        return self.find_with_check_visibility(self.locators.TEXT_NOT_FOUND, timeout=120)

    @property
    @add_clicks
    def BUTTON_TO_EVENTS(self):
        return self.find(self.locators.TO_EVENTS)

    @property
    @add_clicks
    def CLOSE_GOOD(self):
        return self.find(self.locators.CLOSE_GOOD)

    @property
    @add_write
    def INPUT_LINKS(self):
        return self.find(self.locators.INPUT_LINKS)

    @property
    @add_clicks
    def SELECT_UPDATE_PERIOD(self):
        return self.find(self.locators.SELECT_UPDATE_PERIOD)

    @add_clicks
    def UPDATE_PERIOD_OPTION(self, period='1 час'):
        return self.find_with_check_visibility(self.locators.CHOOSE_PERIOD(period=period))

    @property
    def UPDATE_PERIOD_SPAN(self):
        return self.find_with_check_visibility(self.locators.UPDATE_PERIOD_SPAN).text

    @property
    @add_write
    def SEARCH_FIELD(self):
        return self.find(self.locators.SEARCH_FIELD)

    def GOODS_NAME(self, i=1):
        return self.find_with_check_visibility(self.locators.ITEM_NAME(i)).text

    def GOODS_ID(self, i=1):
        return self.find_with_check_visibility(self.locators.ITEM_ID(i)).text
