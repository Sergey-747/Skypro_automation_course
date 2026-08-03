from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

# Фикстура возвращает и драйвер, и объект ожидания
@pytest.fixture(scope="module", autouse=False)
def browser():
    driver = webdriver.Edge() 
    wait = WebDriverWait(driver, 10)
    yield driver, wait  # Передаем кортеж в тесты
    driver.quit()

# Открываем страницу в Edge
def test_open_url(browser):
    driver, wait = browser  
    target_url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    driver.get(target_url)
    driver.maximize_window()

def test_filling_out_the_form(browser):
    driver, wait = browser  
# Убедимся, что мы на нужной странице
    if driver.current_url == "data:,":
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        
 # Составляем словарь данных для заполнения
    form_data = {
         "first-name": "Иван",
         "last-name": "Петров",
         "address": "Ленина, 55-3",
         "e-mail": "test@skypro.com",
         "phone": "+7985899998787",
         "city": "Москва",
         "country": "Россия",
         "job-position": "QA",
         "company": "SkyPro"
     }
 # Заполняем все поля в цикле по нашему словарю
    for field_name, value in form_data.items():
         field = wait.until(EC.visibility_of_element_located((By.NAME, field_name)))
         field.clear()
         field.send_keys(value)
 
     #  Нажимаем кнопку Submit
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

# Проверьте (assert), что поле Zip code подсвечено красным
def test_zip_code_red(browser):
    driver, wait = browser
       
    # Находим поле Zip code
    zip_code_field = wait.until(EC.visibility_of_element_located((By.ID, "zip-code")))
    
    # Получаем значение цвета его рамки через CSS
    border_color = zip_code_field.value_of_css_property("border-color")
        
    # Для отладки 
    #print(f"\n---> ТОЧНОЕ ЗНАЧЕНИЕ CSS: {border_color} <---")
    
    # Проверяем, что в rgb-коде преобладает красный компонент
    assert "245" in border_color, f"Поле не подсвечено красным! Цвет: {border_color}"

#  Проверяем что остальные поля подсвечены зеленым.
def test_other_fields_green(browser):
    driver, wait = browser
       
    # Список имен, которые должны быть зелеными
    valid_fields_names = [
        "first-name", "last-name", "address", 
        "e-mail", "phone", "city", "country", 
        "job-position", "company"
    ]
    
    #  Проверяем в цикле каждое поле
    for field_name in valid_fields_names:
        # Передаем переменную field_name
        field = wait.until(EC.visibility_of_element_located((By.ID, field_name)))
        # Получаем цвет рамки
        border_color = field.value_of_css_property("border-color")
        # Для отладки
        #print(f"\n---> Поле: {field_name} | CSS border-color: {border_color} <---")
    # Проверяем, что в rgb-коде преобладает зеленый компонент (число 186)
        assert "186" in border_color, f"Поле {field_name} НЕ подсвечено зеленым! Текущий цвет: {border_color}"


    
