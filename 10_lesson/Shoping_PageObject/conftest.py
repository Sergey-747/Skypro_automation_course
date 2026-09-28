import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Фикстура возвращает драйвер, предварительно выполнив логику входа
@pytest.fixture(scope="module", autouse=False)
def driver_authorized():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 200)

    # Открываем сайт магазина
    target_url = "https://www.saucedemo.com/"
    driver.get(target_url)
    driver.maximize_window()
    wait.until(EC.url_to_be(target_url))

    # Передаем готовый драйвер в тест
    yield driver

    # Закрываем драйвер после завершения тестов модуля
    driver.quit()
