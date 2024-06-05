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

    def hover_wrapper(self, locator, timeout=BASIC_TIMEOUT) -> WebElement:
        elem = self.find(locator, timeout=timeout)
        AC(self.driver).move_to_element(elem).perform()

        return elem

    def write_input(self, locator, message, timeout=BASIC_TIMEOUT) -> WebElement:
        input_element = self.find_with_check_visibility(locator, timeout)
        input_element.clear()
        input_element.send_keys(message)

        return input_element

    def check_url(self, expected_url, timeout=BASIC_TIMEOUT):
        return self.wait(timeout).until(EC.url_matches(expected_url))


# add_click add method click() to button by locator
def add_click(locator):
    def add_click_decorator(button_getter):
        @wraps(button_getter)
        def functionality(self, timeout=BASIC_TIMEOUT):
            def click(locator=locator, timeout=timeout):
                return self.click(locator=locator, timeout=timeout)

            button_result = button_getter(self)
            button_result.click = click

            return button_result

        return functionality

    return add_click_decorator


# add_write add method write() to input field by locator
def add_write(locator):
    def add_write_decorator(input_field_getter):
        @wraps(input_field_getter)
        def functionality(self, timeout=BASIC_TIMEOUT):
            def write(message, timeout=timeout):
                return self.write_input(locator=locator, message=message, timeout=timeout)

            input_field_result = input_field_getter(self)
            input_field_result.write = write

            return input_field_result

        return functionality

    return add_write_decorator


# add_hover add method hover() to element by locator
def add_hover(locator):
    def add_hover_decorator(elem_getter):
        @wraps(elem_getter)
        def functionality(self, timeout=BASIC_TIMEOUT):
            def hover(timeout=timeout):
                return self.hover_wrapper(locator=locator, timeout=timeout)

            hoverable_elem_result = elem_getter(self)
            hoverable_elem_result.hover = hover

            return hoverable_elem_result

        return functionality

    return add_hover_decorator
