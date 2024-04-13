import pytest
from selenium import webdriver

import helpers
from pages.login_page import LoginPage


@pytest.fixture(params=['chrome', 'firefox'], scope='function')
def driver(request):
    driver = None
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    if request.param == 'firefox':
        driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture
def user():
    user = helpers.create_user()
    yield user
    helpers.delete_user(user)


@pytest.fixture
def login(driver, user):
    login_page = LoginPage(driver)
    login_page.open_url(login_page.login_url)
    login_page.log_in_account(user)
    yield login_page
