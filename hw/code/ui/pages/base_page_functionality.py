import time
from functools import wraps

from utils.timeout import BASIC_TIMEOUT

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC


class PageNotOpenedException(Exception):
    pass


class BasePageFunctionality(object):
    def is_opened(self, timeout=BASIC_TIMEOUT):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url.find(self.url) >= 0:
                return True
        raise PageNotOpenedException(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def wait(self, timeout=BASIC_TIMEOUT) -> WebDriverWait:
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=BASIC_TIMEOUT, until_EC=EC.presence_of_element_located) -> WebElement:
        return self.wait(timeout).until(until_EC(locator))

    def find_with_check_visibility(self, locator, timeout=BASIC_TIMEOUT) -> WebElement:
        return self.find(locator, timeout, until_EC=EC.visibility_of_element_located)

    def click(self, locator, timeout=BASIC_TIMEOUT) -> WebElement:
        elem = self.find(locator, timeout=timeout, until_EC=EC.element_to_be_clickable)
        elem.click()

        return elem

    def hover_to_element(self, element):
        AC(self.driver).move_to_element(element).perform()

        return element

    def hover_wrapper(self, locator, timeout=BASIC_TIMEOUT) -> WebElement:
        elem = self.find(locator, timeout=timeout)

        return self.hover_to_element(elem)

    @staticmethod
    def write_input_to_element(element, message) -> WebElement:
        element.clear()
        element.send_keys(message)

        return element

    def write_input(self, locator, message, timeout=BASIC_TIMEOUT) -> WebElement:
        input_element = self.find_with_check_visibility(locator, timeout)
        return self.write_input_to_element(input_element, message)

    def write_input_without_clearing(self, locator, message, timeout=BASIC_TIMEOUT):
        input_element = self.find_with_check_visibility(locator, timeout)
        input_element.send_keys(message)

    @staticmethod
    def get_value_from_elem(element):
        return element.get_attribute('value')

    def get_value(self, locator, timeout=BASIC_TIMEOUT):
        element = self.find(locator, timeout)

        return self.get_value_from_elem(element)

    def check_url(self, expected_url, timeout=BASIC_TIMEOUT):
        return self.wait(timeout).until(EC.url_matches(expected_url))


# add_write add method write() to input field
def add_write(input_field_getter):
    @wraps(input_field_getter)
    def functionality(self, *args, **kwargs):
        input_field_result = input_field_getter(self, *args, **kwargs)

        def write(message):
            return self.write_input_to_element(input_field_result, message=message)

        input_field_result.write = write

        return input_field_result

    return functionality


# add_hover add method hover() to element
def add_hover(elem_getter):
    @wraps(elem_getter)
    def functionality(self, *args, **kwargs):
        hoverable_elem_result = elem_getter(self, *args, **kwargs)

        def hover():
            return self.hover_to_element(hoverable_elem_result)

        hoverable_elem_result.hover = hover

        return hoverable_elem_result

    return functionality


# add_get_value add method get_value() to element
def add_get_value(elem_getter):
    @wraps(elem_getter)
    def functionality(self, timeout=BASIC_TIMEOUT, *args, **kwargs):
        value_elem_result = elem_getter(self, *args, **kwargs)

        def get_value():
            return self.get_value_from_elem(value_elem_result)

        value_elem_result.get_value = get_value

        return value_elem_result

    return functionality
