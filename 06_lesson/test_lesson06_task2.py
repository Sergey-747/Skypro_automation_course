from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def test_session_storage_auth():
    driver = webdriver.Chrome()
#Откройте страницу https://gitflic.ru/.
    driver.get("https://gitflic.ru/")
    driver.maximize_window()

# Установите cookie пользователя 1.
    driver.add_cookie({
        "name": "SESSION",
        "value": "NzFjNWE3MDAtMGJjYy00MjBmLWI3NmQtMjVjZmU5MDY5Nzc2",
        "domain": ".gitflic.ru",
        "path": "/"
    })

    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

# Обновите страницу.
    driver.refresh()
# Перейдите на страницу пользователя 1.
    driver.get("https://gitflic.ru/user/treeburo")
    sleep(5)

# Сохраните текущий URL.
    # Получаем текущий URL
    current_url_user1 = driver.current_url

    # Провереряем совпадение
    assert current_url_user1 == "https://gitflic.ru/user/treeburo"

# Разлогиньтесь (очистите куки).
    driver.delete_all_cookies()
# Обновите страницу.
    driver.refresh()
    driver.get("https://gitflic.ru")
    print("Страница обновлена до ", driver.current_url)
    sleep(3)

# Установите cookie пользователя 2.
    driver.add_cookie({
        "name": "SESSION",
        "value": "ZDhjMjEzMjgtMGQwZC00ZDhiLTkzMWQtNTQ2Y2M4YTBlYzY3",
        "domain": ".gitflic.ru",
        "path": "/"
    })

    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

# Перейдите на страницу пользователя 2.
    driver.refresh()
    driver.get("https://gitflic.ru/user/serfre13")

# Сохраните текущий URL.
    current_url_user2 = driver.current_url
    assert current_url_user2 == "https://gitflic.ru/user/serfre13"

# Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    assert current_url_user1 != current_url_user2
    print(f"Пользователь1: {current_url_user1} Пользователь2: {current_url_user2}")
    sleep(3)
    driver.quit()

test_session_storage_auth()