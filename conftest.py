import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

# from selenium import webdriver
# import pytest
#
# # для корректного отображения кириллицы в параметризаторах
# def pytest_make_parametrize_id(config, val): return repr(val)
#
#
# # добавляем параметр запуска тестов в командной строке(чем запускать, хромом или фаерфоксом) По умолчанию хром
# def pytest_addoption(parser):
#     # parser.addoption('--browser_name', action='store', default=None, help="Choose browser: chrome or firefox")
#     # Можно задать значение параметра по умолчанию,
#     # чтобы в командной строке не обязательно было указывать параметр --browser_name, например, так:
#     parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
#
#
# # Запуск браузера(для каждой функции)
# @pytest.fixture(scope="function")  # по умолчанию запускается для каждой функции
# def browser(request):
#     browser_name = request.config.getoption("browser_name")  # получаем параметр командной строки browser_name
#     browser = None
#     if browser_name == "chrome":
#         print("\nstart Сhrome browser for test..")
#         browser = webdriver.Chrome()
#     elif browser_name == "firefox":
#         print("\nstart Firefox browser for test..")
#         browser = webdriver.Firefox()
#     else:
#         raise pytest.UsageError("--browser_name should be chrome or firefox")
#     yield browser
#     print("\nquit browser..")
#     browser.quit()

# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()

# @pytest.fixture
# def click_if_button_exists():
#     def _click_if_button_exists(By, value):
#         againButton = browser.find_elements(By, value)
#         if againButton:
#             againButton[0].click()
#     return _click_if_button_exists
#
# @pytest.fixture
# def confirmAgain():
#     def _confirmAgain(By, value):
#         confirmButton = browser.find_elements(By, value)
#         if confirmButton:
#             confirmButton[0].click()
#     return _confirmAgain



# https://docs.pytest.org/en/latest/example/simple.html?highlight=addoption