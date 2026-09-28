import allure
from pages.profile_page import ProfilePage

@allure.feature("Оформление заказа")
@allure.story("Сквозной сценарий покупки")
@allure.title("Полный цикл покупки 3-х товаров в магазине Swag Labs")
@allure.description("""Тест проверяет вход на сайт по логину и паролю,
                    добавление товаров в корзину и переход в нее, 
                    инициализацию заказа и заполнение персональных данных,
                    проводит проверку финальной стоимости покупки""")
@allure.title("Сквозной сценарий покупки товаров в магазине Swag Labs")
def test_magzin(driver_authorized):
    target_url = "https://www.saucedemo.com/"
    page = ProfilePage(driver_authorized, target_url) 
    
    with allure.step("Этап 1: Авторизация на сайте"):
        page.open_page()
        page.authorization()
        page.login_to_the_site()
        page.save_screenshot("profil")

    with allure.step("Этап 2: Добавление товаров в корзину и переход в нее"):
        page.add_product()
        page.save_screenshot("add_product")
        page.go_to_cart()
        page.save_screenshot("cart")

    with allure.step("Этап 3: Инициация заказа и заполнение персональных данных"):
        page.checkout()
        page.filling_fields()
        page.save_screenshot("filling_form")

    with allure.step("Этап 4: Проверка финальной стоимости (Total) и завершение"):
        # Передаем ожидаемую строку в метод. 
        # Обратите внимание: на Saucedemo текст обычно выглядит как "Total: $58.29"
        page.total_cost()
        page.save_screenshot("total_cost")
        
