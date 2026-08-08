from pages.profile_page import ProfilePage


def test_magzin(driver_authorized):
    target_url = "https://www.saucedemo.com/"
    page = ProfilePage(driver_authorized, target_url) 
        # Открываем сайт
    page.open_page()
        # Вводим логин и пароль
    page.authorization()
        # Нажимаем кнопку Войти
    page.login_to_the_site()
    page.save_screenshot("profil")
        # Добавляем в корзину товары:Sauce Labs Backpack. Sauce Labs Bolt T-Shirt. 
        # Sauce Labs Onesie.
    page.add_product()
    page.save_screenshot("add_product")
        # Переходим в корзину.
    page.go_to_cart()
    page.save_screenshot("cart")
        # Нажимаем кнопку Checkout.
    page.checkout()
        # Заполняем форму своими данными: Имя. Фамилия. Почтовый индекс.
    page.filling_fields()
    page.save_screenshot("filling_form")
        # Читаем со страницы итоговую стоимость (Total).
    page.total_cost()
    page.save_screenshot("total_cost")
        # Проверяем (assert), что итоговая сумма равна $58.29.
    page.assert_total()
        