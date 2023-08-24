import pytest
from selenium import webdriver

from Utilities.Read_Config_File import Read_Confi_File


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        Edge_options = webdriver.EdgeOptions()
        Edge_options.add_argument("headless")
        driver = webdriver.Edge(options=Edge_options)

    r = Read_Confi_File()
    # driver.get("https://testautomationpractice.blogspot.com")
    driver.get(r.get_URL())
    driver.maximize_window()
    return driver
