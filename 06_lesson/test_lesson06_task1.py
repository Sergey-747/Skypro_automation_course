from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    logging.basicConfig(level=logging.INFO)

# Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2.
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    driver.maximize_window()

# Найдите и нажмите на кнопку Start.
    start_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='start']/button")))
    logging.info("Найдена кнопка START")
    start_btn.click()

# Дождитесь появления текста Hello World!
    visible_text = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='finish']/h4")))
    logging.info("Текст Hello World! появился на стрнице")

# Сделайте скриншот страницы.
    driver.save_screenshot(r"C:\Users\se.engineer\Desktop\Tests\Page_HW.png")

# Проверьте, что появившийся текст равен Hello World!
    assert visible_text.text == "Hello World!"

    driver.quit()

test_dynamic_loading()
