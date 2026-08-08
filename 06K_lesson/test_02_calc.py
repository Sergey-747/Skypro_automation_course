from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture(scope="module", autouse=False)
def browser():
    driver = webdriver.Chrome() 
    wait = WebDriverWait(driver, 10)
    yield driver, wait  
    driver.quit()

# Открываем страницу: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html в Google Chrome.
def test_open_url(browser):
    driver, wait = browser
    target_url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    driver.get(target_url)
    driver.maximize_window()
# В поле ввода по локатору #delay  введите значение 45.
    enter_number = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#delay")))
    enter_number.clear()
    enter_number.send_keys(45)
# Нажмите на кнопки:7+8=
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#calculator .keys span:nth-child(1)"))).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#calculator .keys span:nth-child(4)"))).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#calculator .keys span:nth-child(2)"))).click()
    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#calculator .keys span.btn.btn-outline-warning"))).click()
        
# Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.
    wait = WebDriverWait(driver, 50)
    result_found = wait.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )
    assert result_found, "Результат '15' не отобразился на экране калькулятора через 45 секунд!"
     