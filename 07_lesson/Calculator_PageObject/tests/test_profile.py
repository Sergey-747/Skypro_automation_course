from pages.profile_page import ProfilePage


def test_change_profile_name(driver_authorized):

# Явно передаем и драйвер, и ссылку, которую требует __init__
    target_url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    page = ProfilePage(driver_authorized, target_url) 

# Шаг 1. Передаем все пораметры в page
    page.open_profile_page()

# Шаг 2. Задаем время появления ответа в переменной - time_wait      
    wait_secund = 45
    page.increase_wait(wait_secund)
    time_wait_str = str(wait_secund)
    # print(f"время ожидания = {time_wait_str}")
    page.save_screenshot(f"wait_{time_wait_str}_sek")

# Шаг 3. Вводим 7 + 8 =
    page.primer()
    page.save_screenshot("primer")

# Шаг 4. Проверьте (assert), что в окне отобразится 
# результат 15 через 45 секунд.
    page.checking_the_result()
    page.save_screenshot("result")