import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

def test_page_title():
    driver.get("https://httpbin.org/forms/post")
    
    # 1. Вводим даннеы в поле ввода по атрибуту name  = custname
    cust_name = driver.find_element(By.NAME, "custname")
    # 2. Очищаем поле перед вводом 
    cust_name.clear()
    # 3. Передаем значение
    cust_name.send_keys("Зябликов")
    
        # Телефон: name="custtel"
    cust_tel = driver.find_element(By.NAME, "custtel")
    cust_tel.clear
    cust_tel.send_keys("+79132143589")
    
        #Адрес электронной почты: name="custemail"
    cust_email = driver.find_element(By.NAME, "custemail")
    cust_email.clear
    cust_email.send_keys("sergey@gmail.com")
    time.sleep(3)
    title = driver.current_url
    print("Страница до нажатия Submit order", title)
    
        #Нажать кнопку Submit order
    button = driver.find_element(By.XPATH, "//*[text()='Submit order']")
    button.click()
    print("Мы на странице:", driver.current_url)
    print("Кнопка успешно нажата!")
         #прверить, что URL изменился
    title_new = driver.current_url
    assert title != title_new, 'Ошибка перехода'   

test_page_title()
driver.quit()