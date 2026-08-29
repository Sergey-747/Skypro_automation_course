import pytest
from selenium import webdriver


# Фикстура возвращает и драйвер, и объект ожидания
@pytest.fixture(scope="module", autouse=False)
def driver_authorized():
    # Инициализация драйвера
    driver = webdriver.Chrome()  

    # Открытие страницы калькулятора
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")  
    driver.maximize_window()
    
    # Возвращаем авторизованный драйвер
    yield driver

    # Закрываем драйвер после завершения тестов
    driver.quit()