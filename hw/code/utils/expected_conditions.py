class element_has_background(object):
    def __init__(self, locator, expected_background):
        self.locator = locator
        self.expected_background = expected_background

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        if element.value_of_css_property('background').startswith(self.expected_background):
            return element
        else:
            return False
