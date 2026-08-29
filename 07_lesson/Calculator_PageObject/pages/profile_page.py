from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class ProfilePage:

    EDIT_WAIT_CALCULATOR = (By.CSS_SELECTOR, "#delay")
    NUMBER_SEVET = (By.CSS_SELECTOR, "#calculator .keys span:nth-child(1)")
    NUMBER_EIGHT = (By.CSS_SELECTOR, "#calculator .keys span:nth-child(2)")
    ACTION_PLUS = (By.CSS_SELECTOR, "#calculator .keys span:nth-child(4)")
    EQUALS = (By.CSS_SELECTOR, "#calculator .keys span.btn.btn-outline-warning")
    RESULT = (By.CLASS_NAME, "screen")
    
    # ProfilePage будет знать, с каким драйвером работать и какой URL у страницы.
    def __init__(self, driver, url):
       self.driver = driver
       self.url = url  # Теперь сюда запишется target_url из теста
       self.wait = WebDriverWait(self.driver, 10)

    def open_profile_page(self):
       self.driver.get(self.url)

    # Делаем скриншот страницы 
    def save_screenshot(self, name_file):
        current_dir = os.getcwd()
        path = os.path.join(current_dir, f"{name_file}.png")
        self.driver.save_screenshot(path)
        print(f"\n[INFO] Скриншот успешно сохранен: {path}")

    # В поле ввода по локатору #delay  введите значение 45.
    def increase_wait(self, wait_secund):
        self.wait_secund = wait_secund
        enter_number = self.wait.until(
            EC.visibility_of_element_located(self.EDIT_WAIT_CALCULATOR))
        enter_number.clear()
        enter_number.send_keys(wait_secund)

    def primer(self):
    # Нажмите на кнопки:7+8=
        self.wait.until(
            EC.visibility_of_element_located(self.NUMBER_SEVET)).click()
        self.wait.until(
            EC.visibility_of_element_located(self.ACTION_PLUS)).click()
        self.wait.until(
            EC.visibility_of_element_located(self.NUMBER_EIGHT)).click()
        self.wait.until(
        EC.visibility_of_element_located(self.EQUALS)).click()

    # Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.
    def checking_the_result(self):
        wait = WebDriverWait(self.driver, 50)
        result_found = wait.until(
           EC.text_to_be_present_in_element(self.RESULT, "15")
    )
        assert result_found, "Результат '15' не отобразился на экране калькулятора через 45 секунд!"
     