import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")

# def test_guest_should_see_login_link_fail(browser):
#     browser.get(link)
#     browser.find_element(By.CSS_SELECTOR, "#magic_link")
# def test_task_locales(browser):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     browser.get(link)

    button = browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    assert "Ajouter au panier" in button.text
    # button.click()



