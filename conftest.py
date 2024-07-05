# Создайте GitHub-репозиторий, в котором будут лежать файлы conftest.py и test_items.py.
# Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр language.
# Реализуйте в файле conftest.py логику запуска браузера с указанным языком пользователя. Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.
# В файл test_items.py напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину. Например, можно проверять товар, доступный по http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.
# Тест должен запускаться с параметром language следующей командой:
# pytest --language=es test_items.py
# и проходить успешно. Достаточно, чтобы код работал только для браузера Сhrome.
# Отправить ссылку на данный репозиторий в качестве ответа на данное задание.
# Отправить решение на рецензирование другим учащимся. Не забудьте, что решение на рецензирование можно отправить только один раз.
# Проверьте решения минимум трех других учащихся, чтобы получить баллы за задание.

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

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

options = Options()
language = browser.find_element(By.TAG_NAME, 'language')
options.add_experimental_option('prefs', {'intl.accept_languages': language})
browser = webdriver.Chrome(options=options)