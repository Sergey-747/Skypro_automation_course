from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import allure

 
class ProfilePage:
    """Класс для представления и взаимодействия со страницей магазина Swag Labs.
    
    Использует паттерн Page Object для инкапсуляции логики UI-элементов 
    и взаимодействия с ними.
    """
    
    LOGIN = (By.ID, "user-name") 
    PASSWORD = (By.ID, "password") 
    LOGIN_BTN = (By.ID, "login-button") 
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack") 
    ADD_LABS_BOLT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt") 
    ADD_LABS_ONESIIE = (By.ID, "add-to-cart-sauce-labs-onesie") 
    SHOPPING_CART = (By.CSS_SELECTOR, ".shopping_cart_link") 
    CHECKOUT_BTN = (By.ID, "checkout") 
    FINISH = (By.ID, "finish") 
    #SUMMARY_TOTAL = (By.CSS_SELECTOR, ".summary_total_label") 
    #SUMMARY_TOTAL = (By.XPATH, "//div[contains(@class, 'summary_total_label')]") 
    SUMMARY_TOTAL = (By.CSS_SELECTOR, ".summary_total_label")
    
    def __init__(self, driver, url):
       """Инициализирует базовые параметры для работы с веб-страницей."""
       self.driver = driver
       self.url = url  
       self.wait = WebDriverWait(self.driver, 60)

    @allure.step("Открытие страницы для авторизации")
    def open_page(self):
       """Открывает страницу профиля в браузере по заданному URL."""
       self.driver.get(self.url)

    @allure.step("Открытие страницы для авторизации  на странице")
    def authorization(self):
        login = self.wait.until(EC.visibility_of_element_located(self.LOGIN))
        login.send_keys("standard_user")
        password = self.wait.until(EC.visibility_of_element_located(self.PASSWORD))
        password.send_keys("secret_sauce")
    
    @allure.step("Нажимает кнопку Login")
    def login_to_the_site(self):
        self.wait.until(
            EC.visibility_of_element_located(self.LOGIN_BTN)
        ).click()
        
    @allure.step("Сохранение скриншота напрямую в Allure") 
    def save_screenshot(self, name_file):
       allure.attach(
       self.driver.get_screenshot_as_png(), 
       name=name_file, 
       attachment_type=allure.attachment_type.PNG
    )
    
    @allure.step("""Добавление в корзину товаров: Sauce Labs Backpack, 
                  Sauce Labs Bolt T-Shirt, Sauce Labs Onesie.""")
    def add_product(self):
        self.wait.until(
           EC.visibility_of_element_located(self.ADD_BACKPACK)).click()
        self.wait.until(
           EC.visibility_of_element_located(self.ADD_LABS_BOLT)).click()
        self.wait.until(
           EC.visibility_of_element_located(self.ADD_LABS_ONESIIE)).click()

    @allure.step("Переходит в корзину с выбранными товарами") 
    def go_to_cart(self):
        self.wait.until(
           EC.visibility_of_element_located(self.SHOPPING_CART)).click()

    @allure.step("Прокрутка страницы в самый низ и нажатие Checkout") 
    def checkout(self):
        try:
            link = self.wait.until(
               EC.presence_of_element_located(self.CHECKOUT_BTN))
            self.driver.execute_script(
               "arguments[0].scrollIntoView({block: 'center'});", link)
            self.wait.until(EC.element_to_be_clickable(link)).click()
        finally:
         print("Checkout нажат")

    @allure.step("Заполняем форму для совершения покупок") 
    def filling_fields(self):
        form_data = {
                "first-name": "Sergey",
               "last-name": "Petrov",
               "postal-code": "645789",
              }
     
        for field_name, value in form_data.items():
            field = self.wait.until(
               EC.visibility_of_element_located((By.ID, field_name)))
            field.clear()
            field.send_keys(value)

        #  Нажимаем кнопку Continue
        self.wait.until(
           EC.element_to_be_clickable((By.ID, "continue"))).click()

    @allure.step("Подготовка к проверке итоговой стоимости на странице")
    def check_total_cost(self, expected_cost):
       try:
        link = self.wait.until(EC.presence_of_element_located(self.FINISH))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", link)
        self.wait.until(EC.element_to_be_clickable(link))
        actual_cost = link.text
        assert actual_cost == expected_cost, f"Ожидалось '{expected_cost}', но на странице '{actual_cost}'"
       finally:
         print("Низ страницы достигнут")


    @allure.step("Проверка, что итоговая сумма равна  $58.29.") 
    def total_cost(self):
       summary_info = self.wait.until(
          EC.visibility_of_element_located(self.SUMMARY_TOTAL))
       total = summary_info.text
       print(f"Сумма покупок = {total}")
        # Текстовое сообщение в случае ошибки
       assert total == "Total: $58.29", f"Ошибка! Ожидали $58.29, а на сайте: {total}"
       
    