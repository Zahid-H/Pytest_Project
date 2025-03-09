import pytest
from selenium import webdriver
# for defining browser commandline input
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Specify the browser: chrome or firefox or edge")
#Created two fixture setup and browser fixture
@pytest.fixture()
#receiving command line input from browser
def browser(request):
    return request.config.getoption("--browser")
# Value received from the
@pytest.fixture()
def setup(browser):
    #diver instance variable
    global driver
    if browser == "chrome":
        return webdriver.Chrome()
    elif browser == "firefox":
        return webdriver.Firefox()
    elif browser == "edge":
        return webdriver.Edge()
    else:
        raise Exception("Browser not supported")

    return driver


