from functools import wraps

from ui.locators import basic_locators
from ui.pages.base_page_functionality import BasePageFunctionality

from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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


# add_open_view add method open_view() to button by locator
def add_open_view(sign_opening_locator):
    def add_open_view_decorator(elem_getter):
        @wraps(elem_getter)
        def functionality(self, *args, **kwargs):
            openable_elem_result = elem_getter(self, *args, **kwargs)

            def open_view():
                return self.open_view(openable_elem_result,
                                      sign_opening_locator=sign_opening_locator)

            openable_elem_result.open_view = open_view

            return openable_elem_result

        return functionality

    return add_open_view_decorator


# add_close_view add method close_view() to button by locator
def add_close_view(sign_opening_locator):
    def add_close_view_decorator(elem_getter):
        @wraps(elem_getter)
        def functionality(self, *args, **kwargs):
            closable_elem_result = elem_getter(self, *args, **kwargs)

            def close_view():
                return self.close_view(closable_elem_result,
                                       sign_opening_locator=sign_opening_locator)

            closable_elem_result.close_view = close_view

            return closable_elem_result

        return functionality

    return add_close_view_decorator


class PageWithRedirectWindow(BasePageFunctionality):
    def redirect_window_by_element(self, element, expected_number_of_windows_to_be=2):
        original_window = self.driver.current_window_handle
        self.click(redirect_button_locator)

        self.wait().until(EC.number_of_windows_to_be(expected_number_of_windows_to_be))

        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)

        return original_window

    def redirect_window(self, redirect_button_locator, expected_number_of_windows_to_be=2):
        element = self.find(redirect_button_locator, EC.element_to_be_clickable)

        return self.redirect_window_by_element(element,
                                               expected_number_of_windows_to_be=expected_number_of_windows_to_be)

    def redirect_window_with_scroll_by_element(self, element, expected_number_of_windows_to_be=2):
        original_window = self.driver.current_window_handle
        AC(self.driver).move_to_element(element).click(element).perform()

        self.wait().until(EC.number_of_windows_to_be(expected_number_of_windows_to_be))

        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)

        return original_window

    def redirect_window_with_scroll(self, redirect_button_locator, expected_number_of_windows_to_be=2):
        element = self.find(redirect_button_locator)
        return self.redirect_window_with_scroll_by_element(element, expected_number_of_windows_to_be)


# add_redirect add method redirect() to button
def add_redirect(elem_getter):
    @wraps(elem_getter)
    def functionality(self, expected_number_of_windows_to_be=2, *args, **kwargs):
        redirectable_elem_result = elem_getter(self, *args, **kwargs)

        def redirect(expected_number_of_windows_to_be=expected_number_of_windows_to_be):
            return self.redirect_window_by_element(redirectable_elem_result,
                                                   expected_number_of_windows_to_be=
                                                   expected_number_of_windows_to_be)

        redirectable_elem_result.redirect = redirect

        return redirectable_elem_result

    return functionality


# add_redirect_with_scroll add method redirect_with_scroll() to button
def add_redirect_with_scroll(elem_getter):
    @wraps(elem_getter)
    def functionality(self, expected_number_of_windows_to_be=2, *args, **kwargs):
        redirectable_elem_result = elem_getter(self, *args, **kwargs)

        def redirect_with_scroll(expected_number_of_windows_to_be=expected_number_of_windows_to_be):
            return self.redirect_window_with_scroll_by_element(redirectable_elem_result,
                                                               expected_number_of_windows_to_be=
                                                               expected_number_of_windows_to_be)

        redirectable_elem_result.redirect_with_scroll = redirect_with_scroll

        return redirectable_elem_result

    return functionality
