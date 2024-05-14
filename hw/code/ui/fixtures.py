import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from ui.pages.base_page import BasePage
from utils.credentials import Credentials


@pytest.fixture()
def driver(config):
    browser = config['browser']
    url = config['url']
    options = Options()
    if browser == 'chrome':
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


def get_driver(browser_name):
    if browser_name == 'chrome':
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    else:
        raise RuntimeError(f'Unsupported browser: "{browser_name}"')
    browser.maximize_window()
    return browser


@pytest.fixture(scope='session', params=['chrome'])
def all_drivers(config, request):
    url = config['url']
    browser = get_driver(request.param)
    browser.get(url)
    yield browser
    browser.quit()


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)

@pytest.fixture(scope='session')
def credentials():
        login = os.getenv('LOGIN')
        password = os.getenv('PASSWORD')

        assert login 
        assert password 

        return Credentials(login, password)

@pytest.fixture(scope='session')
def credentials_new_user():
    login = os.getenv('LOGIN_NEW_USER')
    password = os.getenv('PASSWORD_NEW_USER')

    assert login
    print(password)
    assert password

    return Credentials(login, password)
