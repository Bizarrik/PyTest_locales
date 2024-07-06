from selenium.webdriver.common.by import By
import time

link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_item_to_basket_button(browser):
    browser.get(link)
    # Визуально проверяем, что язык страницы соответствует заданному параметру запуска теста
    time.sleep(5)
    # Проверяем наличие кнопки добавления в корзину
    assert browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
