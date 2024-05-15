from selenium.webdriver.support import expected_conditions as EC


def redirect_window(base_page, redirect_button_locator):
    original_window = base_page.driver.current_window_handle
    base_page.click(redirect_button_locator)

    base_page.wait().until(EC.number_of_windows_to_be(2))

    for window_handle in base_page.driver.window_handles:
        if window_handle != original_window:
            base_page.driver.switch_to.window(window_handle)
            break

    return original_window