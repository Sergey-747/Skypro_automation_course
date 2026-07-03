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
    links = driver.find_elements(By.TAG_NAME, "a")
    print(f"Найдено ссылок на странице: {len(links)}")
        # Проверьте, что количество ссылок равно 9.
    assert len(links) == 9, "Ссылок не 9"
      # Проверяем, что все ссылки отображаются
    for link in links:
        assert link.is_displayed(), "Не все ссылки отображаются"
      # Проверяем текст первой ссылки
    assert "1" in links[0].text, "Это не Первая ссылка "

test_paig()
driver.quit()
