import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from pathlib import Path

class ProfilePage:
    """Класс для представления и взаимодействия со страницей профиля/калькулятора.
    
    Использует паттерн Page Object для инкапсуляции логики UI-элементов 
    и взаимодействия с ними.
    """

    EDIT_WAIT_CALCULATOR = (By.CSS_SELECTOR, "#delay")
    EQUALS = (By.CSS_SELECTOR, "#calculator .keys span.btn.btn-outline-warning") # РАВНО
    RESULT = (By.CLASS_NAME, "screen") # РЕЗУЛЬТАТ
    
    def __init__(self, driver, url):
        """Инициализирует базовые параметры для работы с веб-страницей."""
        self.driver = driver
        self.url = url  
        self.wait = WebDriverWait(self.driver, 10)
        
    @allure.id("Calculator-open")
    @allure.title("Переход на страницу")
    @allure.description("Открывает браузер и загружает целевой URL калькулятора")
    @allure.step("Открытие страницы профиля")
    def open_profile_page(self) -> None:
        """Открывает страницу профиля в браузере по заданному URL."""
        self.driver.get(self.url)
    
    @allure.id("Calculator-save")
    @allure.title("Фиксация экрана")
    @allure.description("Делает снимок текущего состояния UI калькулятора")
    @allure.step("Сохранение скриншота")
    def save_screenshot(self, name_file: str) -> None:
        """Делает скриншот текущего экрана и сохраняет его на диск.
        """
        current_dir = Path(__file__).resolve().parent
        screenshot_dir = current_dir.parent / "shot"
        screenshot_dir.mkdir(parents=True, exist_ok=True)
        path = screenshot_dir / f"{name_file}.png"
        self.driver.save_screenshot(str(path))
        print(f"\n[INFO] Скриншот успешно сохранен: {path}")


    @allure.id("Calculator-wait")
    @allure.title("Настройка задержки")
    @allure.description("Вводит искусственное время ожидания перед выполнением операций")
    @allure.step("Установка задержки калькулятора в {wait_secund} сек.")
    def increase_wait(self, wait_secund: int) -> None:
        """Вводит значение задержки в поле ввода калькулятора."""
        self.wait_secund = wait_secund
        enter_number = self.wait.until(EC.visibility_of_element_located(self.EDIT_WAIT_CALCULATOR))
        enter_number.clear()
        enter_number.send_keys(wait_secund)
        
    @allure.id("Calculator-example")
    @allure.title("Ввод выражения")
    @allure.description("Посимвольно нажимает кнопки калькулятора для ввода математического примера")
    @allure.step("Ввод математического выражения: '{expression}'")
    def primer(self, expression) -> None:
       """Посимвольно вводит математическое выражение в калькулятор и вычисляет результат."""
       for symbol in expression:
            if symbol == '=':
                self.wait.until(EC.visibility_of_element_located(self.EQUALS)).click()
            else:
                xpath = f"//div[@class='keys']/span[text()='{symbol}']"
                self.driver.find_element(By.XPATH, xpath).click()

       self.wait.until(EC.visibility_of_element_located(self.EQUALS)).click()
    
    @allure.id("Calculator-checking-result")  
    @allure.title("Валидация результата")
    @allure.description("Ожидает появления текста на табло и сравнивает его с эталоном")
    @allure.step("Проверка совпадения результата с ожидаемым: '{result_of_the_calculations}'")
    def checking_the_result(self, result_of_the_calculations: str) -> None:
        """Ожидает окончания вычислений калькулятора, округляет результат и проверяет его."""
        locator = (By.XPATH, '//*[@id="calculator"]/div/div')
        
        WebDriverWait(self.driver, 15).until(
            lambda d: not any(op in d.find_element(*locator).text for op in ['+', '-', 'x', '÷', '='])
        )

        element = self.driver.find_element(*locator)
        raw_text = element.text.strip()
        if "." in raw_text:
            float_value = float(raw_text)
            rounded_value = round(float_value, 2)
            actual_result_str = f"{rounded_value:.2f}"
        else:
            actual_result_str = raw_text

        assert result_of_the_calculations == actual_result_str, (
            f"Ошибка! Ожидали '{result_of_the_calculations}', "
            f"но калькулятор показал '{raw_text}' (обработано как '{actual_result_str}')"
        )
       
    @allure.id("Calculator-clear-result")
    @allure.title("Сброс экрана")
    @allure.description("Нажимает кнопку очистки (С) на панели калькулятора")
    @allure.step("Очистка текущего результата вычислений")   
    def clear_result(self) -> None:
       """Очищает текущий результат на калькуляторе, нажимая кнопку сброса."""
       self.wait.until(
           EC.visibility_of_element_located((By.XPATH, "//*[@id='calculator']/div[1]/span"))).click()
       
    


