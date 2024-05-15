import time

from ui.locators import basic_locators
from utils.timeout import BASIC_TIMEOUT

from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):
    locators = basic_locators.BasePageLocators()
    url = 'https://ads.vk.com/'

    def is_opened(self, timeout=BASIC_TIMEOUT):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedExeption(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def wait(self, timeout=BASIC_TIMEOUT):
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=BASIC_TIMEOUT):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=BASIC_TIMEOUT):
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    def hover_wrapper(self, locator, timeout=BASIC_TIMEOUT):
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.presence_of_element_located(locator))
        actions = AC(self.driver)
        actions.move_to_element(elem).perform()

    def write_input(self, locator, message, timeout=BASIC_TIMEOUT):
        input_element = self.find(locator, timeout)
        input_element = self.wait().until(EC.visibility_of(input_element))
        input_element.clear()
        input_element.send_keys(message)


class PageWithModalView(BasePage):
    def open_modal_view(self, button_open_locator, sign_opening_locator):
        self.click(button_open_locator)
        assert self.find(sign_opening_locator).is_displayed()

    def close_modal_view(self, button_close_locator, sign_opening_locator):
        self.click(button_close_locator)
        self.wait().until(EC.invisibility_of_element_located(sign_opening_locator))
