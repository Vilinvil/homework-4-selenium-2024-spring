from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from utils.timeout import BASIC_TIMEOUT


def redirect_window(base_page, redirect_button_locator, expected_number_of_windows_to_be=2):
    original_window = base_page.driver.current_window_handle
    base_page.click(redirect_button_locator)

    base_page.wait().until(EC.number_of_windows_to_be(expected_number_of_windows_to_be))

    new_window = [window for window in base_page.driver.window_handles if window != original_window][-1]
    base_page.driver.switch_to.window(new_window)

    return original_window


def redirect_window_with_scroll(base_page, redirect_button_locator, expected_number_of_windows_to_be=2):
    original_window = base_page.driver.current_window_handle
    elem = base_page.wait(BASIC_TIMEOUT).until(EC.presence_of_element_located(redirect_button_locator))
    AC(base_page.driver).move_to_element(elem).click(elem).perform()

    base_page.wait().until(EC.number_of_windows_to_be(expected_number_of_windows_to_be))

    new_window = [window for window in base_page.driver.window_handles if window != original_window][-1]
    base_page.driver.switch_to.window(new_window)

    return original_window
