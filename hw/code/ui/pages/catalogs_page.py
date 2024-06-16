from selenium.common import TimeoutException
from ui.pages.base_page_functionality import BasePageFunctionality, add_write, add_get_value, add_hover, add_clicks
from ui.locators.catalogs_locators import CatalogLocators
from utils.expected_conditions import element_has_background

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.alert import Alert
from os import path


class CatalogsPage(BasePageFunctionality):
    url = "https://ads.vk.com/hq/ecomm/catalogs"
    locators = CatalogLocators()


    @property
    @add_clicks
    def BUTTON_CREATE_CATALOG(self):
        return self.find(self.locators.BUTTON_CREATE_CATALOG, until_EC=EC.visibility_of_element_located) 
    

    @property
    @add_clicks
    def BUTTON_BY_HAND(self):
        return self.find(self.locators.BUTTON_BY_HAND, until_EC=EC.visibility_of_element_located)
    

    @property
    @add_clicks
    def BUTTON_SELECT_FEED_TYPE(self):
        return self.find(self.locators.INPUT_TYPE_FEED)
    

    @property
    @add_clicks
    def OPTION_AUTO(self):
        return self.find(self.locators.OPTION_AUTO, until_EC=EC.visibility_of_element_located)


    def close_training_if_shown(self):
        try:
            self.find(self.locators.MODAL_VIEW_TRAINING, until_EC=EC.visibility_of_element_located)
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
        return self.find(self.locators.BUTTON_CONFIRM_CREATE_CATALOG, until_EC=EC.visibility_of_element_located) 
    

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
        return self.find(self.locators.FEED_OR_COMMUNITY, until_EC=EC.visibility_of_element_located)
    

    @property
    @add_clicks
    def BUTTON_SETTINGS(self):
        return self.find(self.locators.BUTTON_SETTINGS, until_EC=EC.visibility_of_element_located)
    

    @property
    @add_clicks
    def BUTTON_DELETE(self):
        return self.find(self.locators.BUTTON_DELETE, until_EC=EC.visibility_of_element_located)
    

    @property
    @add_clicks
    def BUTTON_CONFIRM_DELETE(self):
        return self.find(self.locators.BUTTON_CONFIRM_DELETE)
    

    @add_clicks
    def BUTTON_OPEN_GOOD(self, name):
        return self.find(self.locators.BUTTON_OPEN_GOOD(name), timeout=120, until_EC=EC.visibility_of_element_located)


    def INFO_FIELD(self, i):
        return self.find(self.locators.INFO_FIELD(i), until_EC=EC.visibility_of_element_located).text
    

    @property
    def NOT_FOUND_MESSAGE(self):
        return self.find(self.locators.TEXT_NOT_FOUND, timeout=120, until_EC=EC.visibility_of_element_located)
    

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
        return self.find(self.locators.CHOOSE_PERIOD(period=period), until_EC=EC.visibility_of_element_located)
    
    

    @property
    def UPDATE_PERIOD_SPAN(self):
        return self.find(self.locators.UPDATE_PERIOD_SPAN, until_EC=EC.visibility_of_element_located).text
    

    @property
    @add_write
    def SEARCH_FIELD(self):
        return self.find(self.locators.SEARCH_FIELD)
    

    def GOODS_NAME(self, i=1):
        return self.find(self.locators.ITEM_NAME(i), until_EC=EC.visibility_of_element_located).text
    

    def GOODS_ID(self, i=1):
        return self.find(self.locators.ITEM_ID(i), until_EC=EC.visibility_of_element_located).text

