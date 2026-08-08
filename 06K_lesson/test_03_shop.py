from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture(scope="module", autouse=False)
def browser():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    yield driver, wait  
    # Закрыть браузер.
    driver.quit()

#Откройте сайт магазина: https://www.saucedemo.com/ в FireFox.
def test_open_url(browser):
    driver, wait = browser
    target_url = "https://www.saucedemo.com/"
    driver.get(target_url)
    driver.maximize_window()
    wait.until(EC.url_to_be(target_url))

    #  Авторизация как пользователь standard_user
    login = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    login.send_keys("standard_user")
    password= wait.until(EC.visibility_of_element_located((By.ID, "password")))
    password.send_keys("secret_sauce")
    wait.until(EC.visibility_of_element_located((By.ID, "login-button"))).click()

    # Добавление в корзину товаров: Sauce Labs Backpack, Sauce Labs Bolt T-Shirt, Sauce Labs Onesie.
    add_backpack = wait.until(EC.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    add_labs_bolt = wait.until(
        EC.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()
    add_labs_onesie = wait.until(EC.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-onesie"))).click()

    # Перейдите в корзину.
    basket = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping_cart_link"))).click()

    # Прокрутка страницы в самый низ
    try:
        link = wait.until(EC.presence_of_element_located((By.ID, "checkout")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", link)
        wait.until(EC.element_to_be_clickable(link)).click()
    finally:
        print("Checkout нажат")

    # Заполняем все поля в цикле по нашему словарю
    form_data = {
             "first-name": "Sergey",
             "last-name": "Petrov",
             "postal-code": "645789",
            }
     
    for field_name, value in form_data.items():
        field = wait.until(EC.visibility_of_element_located((By.ID, field_name)))
        field.clear()
        field.send_keys(value)

    #  Нажимаем кнопку Continue
    wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

    # Прочитайте со страницы итоговую стоимость ( Total ).
        # Прокрутка страницы в самый низ
    try:
        link = wait.until(EC.presence_of_element_located((By.ID, "finish")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", link)
        wait.until(EC.element_to_be_clickable(link))
    finally:
        print("Низ страницы, достигнут")

    # Проверка, что итоговая сумма равна  $58.29.
    summary_info = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_total_label")))
    total = summary_info.text
    print(f"Сумма покупок = {total}")
    # Текстовое сообщение в случае ошибки
    assert total == "Total: $58.29", f"Ошибка! Ожидали $58.29, а на сайте: {total}"
   