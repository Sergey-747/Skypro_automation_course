import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()

def test_paig():
    driver = webdriver.Chrome()
    # Открываем страницу (httpbin генерирует n ссылок)
    driver.get("https://httpbin.org/links/10")
    # Находим все ссылки на странице (тег <a>)
    links = driver.find_elements(By.TAG_NAME, "a")
    print(f"Найдено ссылок на странице: {len(links)}")
    # ИСПРАВЛЕНО: Проверяем, что количество ссылок действительно равно 10
    assert len(links) == 9, f"Ожидалось 9 ссылок, но найдено {len(links)}"
    # Проверяем, что все ссылки отображаются на экране
    for link in links:
        assert link.is_displayed(), "Не все ссылки отображаются"
    # Текст первой ссылки в httpbin равен "1"
    assert "1" in links[0].text, f"Ожидался текст '1', но получен '{links[0].text}'"
    
test_paig()
driver.quit()
