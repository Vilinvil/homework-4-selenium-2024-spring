import time

from ui.locators import basic_locators
from utils.timeout import BASIC_TIMEOUT

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):
    locators = basic_locators.BasePageLocators()
    url = 'https://ads.vk.com/'

    def is_opened(self, url=url, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == url:
                return True
        raise PageNotOpenedExeption(f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = BASIC_TIMEOUT
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    def hover_wrapper(self, locator, timeout=None):
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.presence_of_element_located(locator))
        actions = AC(self.driver)
        actions.move_to_element(elem).perform()

    def write_input(self, locator, message, timeout=None):
        input = self.find(locator, timeout)
        input = self.wait().until(EC.visibility_of(input))
        input.clear()
        input.send_keys(message)
