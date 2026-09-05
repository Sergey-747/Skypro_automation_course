import pytest
import allure
from pages.profile_page import ProfilePage

# Описываем тестовые данные: (выражение, ожидаемый_результат, имя_скриншота)
TEST_DATA = [
    ("5x5=", "25", "multiplication"),
    ("30÷5=", "6", "division"),
    ("10+15=", "25", "addition"),
    ("45-20=", "25", "subtraction"),
    ("45.23-18.56=", "26.67", "subtraction")
]
@allure.epic("UI Тестирование Калькулятора")
@allure.suite("Тесты Калькулятора Boni Garcia") 
@allure.sub_suite("Арифметические операции") 
@allure.feature("Арифметические вычисления")
@allure.story("Параметризованные тесты базовых операций")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка вычисления выражения: {expression}") 
@pytest.mark.parametrize("expression, expected_result, screenshot_name", TEST_DATA)
def test_calculator_operations(driver_authorized, expression, expected_result, screenshot_name):
    """Тест проверяет корректность различных арифметических операций."""
    
    target_url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    page = ProfilePage(driver_authorized, target_url) 

    # Шаг 1. Открываем страницу
    page.open_profile_page()

    # Шаг 2. Задаем время задержки
    wait_secund = 0
    page.increase_wait(wait_secund)

    # Шаг 3. Вводим выражение, переданное из параметров
    page.primer(expression)
    page.save_screenshot(f"primer_{screenshot_name}")
    
    # Шаг 4. Проверяем результат
    page.checking_the_result(expected_result)
