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

    def write_input_without_clearing(self, locator, message, timeout=BASIC_TIMEOUT):
        input_element = self.find_with_check_visibility(locator, timeout)
        input_element.send_keys(message)

    def check_url(self, expected_url, timeout=BASIC_TIMEOUT):
        return self.wait(timeout).until(EC.url_matches(expected_url))


class BasePage(BasePageFunctionality):
    locators = basic_locators.BasePageLocators()
    url = 'https://ads.vk.com/'

    def find_nav_button_help(self):
        return self.find_with_check_visibility(self.locators.NAV_BUTTON_HELP)

    def find_nav_button_monetization(self):
        return self.find_with_check_visibility(self.locators.NAV_BUTTON_MONETIZATION)

    def find_nav_button_ideas(self):
        return self.find_with_check_visibility(self.locators.NAV_BUTTON_IDEAS)

    def find_nav_button_cases(self):
        return self.find_with_check_visibility(self.locators.NAV_BUTTON_CASES)

    def find_nav_button_news(self):
        return self.find_with_check_visibility(self.locators.NAV_BUTTON_NEWS)

    def find_nav_button_cabinet(self):
        return self.find_with_check_visibility(self.locators.NAV_BUTTON_CABINET_LOCATOR)

    def find_nav_wrapper_education(self):
        return self.find_with_check_visibility(self.locators.NAV_WRAPPER_EDUCATION)

    def find_nav_wrapped_button_insights(self):
        return self.find_with_check_visibility(self.locators.NAV_WRAPPED_BUTTON_INSIGHTS)

    def find_nav_wrapped_button_events(self):
        return self.find_with_check_visibility(self.locators.NAV_WRAPPED_BUTTON_EVENTS)

    def find_nav_wrapped_button_video_courses(self):
        return self.find_with_check_visibility(self.locators.NAV_WRAPPED_BUTTON_VIDEO_COURSES)

    def find_nav_wrapped_button_certification(self):
        return self.find_with_check_visibility(self.locators.NAV_WRAPPED_BUTTON_CERTIFICATION)

    def find_footer_wrapper_language(self):
        return self.find_with_check_visibility(self.locators.FOOTER_WRAPPER_LANGUAGE)

    def find_footer_logo_ok(self):
        return self.find_with_check_visibility(self.locators.FOOTER_LOGO_OK)

    def find_footer_logo_tg(self):
        return self.find_with_check_visibility(self.locators.FOOTER_LOGO_TG)

    def find_footer_logo_vk(self):
        return self.find_with_check_visibility(self.locators.FOOTER_LOGO_VK)

    def find_footer_button_cases(self):
        return self.find_with_check_visibility(self.locators.FOOTER_BUTTON_CASES)

    def find_footer_about_company(self):
        return self.find_with_check_visibility(self.locators.FOOTER_ABOUT_COMPANY)

    def find_footer_button_cabinet(self):
        return self.find_with_check_visibility(self.locators.FOOTER_BUTTON_CABINET)

    def find_footer_button_documents(self):
        return self.find_with_check_visibility(self.locators.FOOTER_BUTTON_DOCUMENTS)

    def find_footer_button_events(self):
        return self.find_with_check_visibility(self.locators.FOOTER_BUTTON_EVENTS)

    def find_footer_button_experts(self):
        return self.find_with_check_visibility(self.locators.FOOTER_BUTTON_EXPERTS)

    def find_footer_button_help(self):
        return self.find_with_check_visibility(self.locators.FOOTER_BUTTON_HELP)

    def find_footer_button_insights(self):
        return self.find_with_check_visibility(self.locators.FOOTER_BUTTON_INSIGHTS)

    def find_footer_button_monetization(self):
        return self.find_with_check_visibility(self.locators.FOOTER_BUTTON_MONETIZATION)

    def find_footer_button_news(self):
        return self.find_with_check_visibility(self.locators.FOOTER_BUTTON_NEWS)

    def find_footer_logo_vk_business(self):
        return self.find_with_check_visibility(self.locators.FOOTER_LOGO_VK_BUSINESS)

    def hover_nav_wrapper_education(self):
        self.hover_wrapper(self.locators.NAV_WRAPPER_EDUCATION)

    def hover_footer(self):
        self.hover_wrapper(self.locators.FOOTER_LOCATOR)

    def click_nav_button_help(self):
        self.click(self.locators.NAV_BUTTON_HELP)

    def click_nav_button_ideas(self):
        self.click(self.locators.NAV_BUTTON_IDEAS)

    def click_nav_button_cases(self):
        self.click(self.locators.NAV_BUTTON_CASES)

    def click_nav_button_news(self):
        self.click(self.locators.NAV_BUTTON_NEWS)

    def click_nav_button_cabinet(self):
        self.click(self.locators.NAV_BUTTON_CABINET_LOCATOR)

    def click_nav_wrapped_button_insights(self):
        self.click(self.locators.NAV_WRAPPED_BUTTON_INSIGHTS)

    def click_nav_wrapped_button_events(self):
        self.click(self.locators.NAV_WRAPPED_BUTTON_EVENTS)

    def click_footer_button(self, locator):
        elem = self.find(locator)
        AC(self.driver).move_to_element(elem).click(elem).perform()

    def click_footer_button_news(self):
        self.click_footer_button(self.locators.FOOTER_BUTTON_NEWS)

    def click_footer_button_insights(self):
        self.click_footer_button(self.locators.FOOTER_BUTTON_INSIGHTS)

    def click_footer_button_events(self):
        self.click_footer_button(self.locators.FOOTER_BUTTON_EVENTS)

    def click_footer_button_documents(self):
        self.click_footer_button(self.locators.FOOTER_BUTTON_DOCUMENTS)

    def click_footer_button_cases(self):
        self.click_footer_button(self.locators.FOOTER_BUTTON_CASES)

    def click_footer_button_help(self):
        self.click_footer_button(self.locators.FOOTER_BUTTON_HELP)

    def click_footer_button_cabinet(self):
        self.click_footer_button(self.locators.FOOTER_BUTTON_CABINET)

    def click_footer_wrapper_language(self):
        self.click_footer_button(self.locators.FOOTER_WRAPPER_LANGUAGE)

    def click_footer_button_language_ru(self):
        self.click_footer_button(self.locators.FOOTER_LANGUAGE_BUTTON_RUSSIAN)

    def click_footer_button_language_en(self):
        self.click_footer_button(self.locators.FOOTER_LANGUAGE_BUTTON_ENGLISH)

    def redirect_nav_monetization(self, redirect_page):
        redirect_page.redirect_window(self.locators.NAV_BUTTON_MONETIZATION)

    def redirect_nav_wrapped_button_video_courses(self, redirect_page):
        redirect_page.redirect_window(self.locators.NAV_WRAPPED_BUTTON_VIDEO_COURSES)

    def redirect_nav_wrapped_button_certification(self, redirect_page):
        redirect_page.redirect_window(self.locators.NAV_WRAPPED_BUTTON_CERTIFICATION)

    def redirect_footer_button_experts(self, redirect_page):
        redirect_page.redirect_window_with_scroll(self.locators.FOOTER_BUTTON_EXPERTS)

    def redirect_footer_button_monetization(self, redirect_page):
        redirect_page.redirect_window_with_scroll(self.locators.FOOTER_BUTTON_MONETIZATION)

    def redirect_footer_button_vk_business(self, redirect_page):
        redirect_page.redirect_window_with_scroll(self.locators.FOOTER_LOGO_VK_BUSINESS)

    def redirect_footer_button_logo_vk(self, redirect_page):
        redirect_page.redirect_window_with_scroll(self.locators.FOOTER_LOGO_VK)

    def redirect_footer_button_logo_tg(self, redirect_page):
        redirect_page.redirect_window_with_scroll(self.locators.FOOTER_LOGO_TG)

    def redirect_footer_button_logo_ok(self, redirect_page):
        redirect_page.redirect_window_with_scroll(self.locators.FOOTER_LOGO_OK)

    def redirect_footer_button_about_company(self, redirect_page):
        redirect_page.redirect_window_with_scroll(self.locators.FOOTER_ABOUT_COMPANY)

    def get_footer_language(self):
        return self.find_with_check_visibility(self.locators.FOOTER_WRAPPER_LANGUAGE).text


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
