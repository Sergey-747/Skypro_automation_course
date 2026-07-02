import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

def test_page_title():
    driver.get("https://httpbin.org")
    link_form = driver.find_element(By.XPATH, "//a[@href='/forms/post']")
    link_form.click()
    new_title = driver.current_url
    print("Новый URL:", new_title)
        # Проверка, что URL изменился на /forms/post.
        # assert "https://httpbin.org/forms/post" == new_title
    assert "forms/post" in new_title, "URL не изменился!"
    print(f'URL изменился! на {new_title}')
        
    # Вернитесь назад на главную страницу.
    # Проверьте, что вернулись на исходный URL.
def page_back():
    page = "https://httpbin.org/"
    driver.back()
    old_page = driver.current_url
    assert page == old_page, "Ошибка перехода"
    print(f"Вернулись назад на: {old_page}")
    
test_page_title()
driver.quit()