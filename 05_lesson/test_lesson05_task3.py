import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()

#Открываем страницу https://httpbin.org/links/10.
def test_paig():
    driver.get("https://httpbin.org/links/10")
    #Находим все ссылки на странице (тег <a>).
    link = driver.find_elements(By.TAG_NAME, "a")
    print(f"Найдено ссылок на странице: {len(link)}")

test_paig()
driver.quit()