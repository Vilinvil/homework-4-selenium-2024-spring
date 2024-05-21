import time

from ui.locators import basic_locators
from utils.timeout import BASIC_TIMEOUT

from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def wait(self, timeout=BASIC_TIMEOUT):
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=BASIC_TIMEOUT, until_EC=EC.presence_of_element_located):
        return self.wait(timeout).until(until_EC(locator))

    def find_with_check_visibility(self, locator, timeout=BASIC_TIMEOUT):
        return self.find(locator, timeout, until_EC=EC.visibility_of_element_located)

    def click(self, locator, timeout=BASIC_TIMEOUT):
        elem = self.find(locator, timeout=timeout, until_EC=EC.element_to_be_clickable)
        elem.click()

    def hover_wrapper(self, locator, timeout=BASIC_TIMEOUT):
        elem = self.find(locator, timeout=timeout)
        AC(self.driver).move_to_element(elem).perform()

    def write_input(self, locator, message, timeout=BASIC_TIMEOUT):
        input_element = self.find_with_check_visibility(locator, timeout)
        input_element.clear()
        input_element.send_keys(message)

    def check_url(self, expected_url, timeout=BASIC_TIMEOUT):
        return self.wait(timeout).until(EC.url_matches(expected_url))


class BasePage(BasePageFunctionality):
    locators = basic_locators.BasePageLocators()
    url = 'https://ads.vk.com/'

    def click_nav_button_help(self):
        self.click(self.locators.NAV_BUTTON_HELP)


class PageWithView(BasePage):
    def open_view(self, button_open_locator, sign_opening_locator):
        self.click(button_open_locator)
        self.find_with_check_visibility(sign_opening_locator)

    def close_view(self, button_close_locator, sign_opening_locator):
        self.click(button_close_locator)
        self.find(sign_opening_locator, until_EC=EC.invisibility_of_element_located)


class PageWithRedirectWindow(BasePage):
    def redirect_window(self, redirect_button_locator, expected_number_of_windows_to_be=2):
        original_window = self.driver.current_window_handle
        self.click(redirect_button_locator)

        self.wait().until(EC.number_of_windows_to_be(expected_number_of_windows_to_be))

        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)

        return original_window

    def redirect_window_with_scroll(self, redirect_button_locator, expected_number_of_windows_to_be=2):
        original_window = self.driver.current_window_handle
        elem = self.wait(BASIC_TIMEOUT).until(EC.presence_of_element_located(redirect_button_locator))
        AC(self.driver).move_to_element(elem).click(elem).perform()

        self.wait().until(EC.number_of_windows_to_be(expected_number_of_windows_to_be))

        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)

        return original_window
