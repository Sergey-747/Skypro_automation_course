<details>

<summary>🍕🛒 Swag Labs purchase - тестирование интернет магазина UI Automation Project</summary>

[![QA Automation](https://shields.io)](https://github.com)
[![Python](https://shields.io)](https://python.org)
[![Framework](https://shields.io)](https://pytest.org)
[![Reporting](https://shields.io)](https://allurereport.org)
[![Generating ASCII](https://shields.io)](https://gitlab.com/nfriend/tree-online#what-is-this)

Проект содержит автоматизированные UI-тесты для интернет-магазина [Saucedemo (Swag Labs)](https://saucedemo.com). 

В основе проекта лежит паттерн **Page Object Model (POM)**.

---

## 🛠 Используемые технологии
* **Язык программирования:** Python 3.10+
* **Редактор кода:** VS Code (Visual Studio Code)
* **Тест-раннер:** Pytest
* **Автоматизация браузера:** Selenium WebDriver (с явными ожиданиями `WebDriverWait`)
* **Отчетность:** Allure Frameworkk

---

## 📂 Структура проекта

```text
└── Shoping_PageObject/
    ├── pages/                  # Классы Page Object (логика работы со страницами)/
    │   └── profile_page.py     # Страница корзины и оформления заказа
    ├── tests/                  # Тестовые файлы/
    │   └── test_purchase.py    # Тесты сквозного сценария покупки
    ├── conftest.py             # Настройки Pytest (инициализация драйвера, фикстуры)
    └── README.md               # Документация проекта

```

---

## 🛠️ Установка и запуск

### 1. Клонирование репозитория
```bash
git clone https://github.com/Sergey-747/Skypro_automation_course.git
cd Skypro_automation_course
```

### 2. Настройка виртуального окружения (при необходимости)
```bash
python -m venv venv
source venv/bin/activate  # Для Linux/macOS
# или
venv\Scripts\activate     # Для Windows
# после проведения тестирования деактивируйте виртуальное окружение
deactivate                # Для Linux/macOS и Windows
```

### 3. Установка зависимостей (при необходимости)
```bash
pip install -r requirements.txt
```

---

## 🏃 Запуск тестов

### Обычный запуск всех тестов:
```bash
pytest test_purchase.py
```

### Запуск с генерацией результатов для Allure:
```bash
pytest --alluredir=allure-results
```

### Запуск тестов по уровням серьезности (Severity):
```bash
# Только блокирующие тесты (Blocker)
pytest --alluredir=allure-results --allure-severities=blocker
```

---

## 📊 Генерация отчетов Allure

Для локального просмотра красивого веб-отчета со скриншотами и шагами выполните команду (требуется установленный [Allure CLI](https://allurereport.orgdocs/install/)):

```bash
allure serve allure-results
```

### Что проверяется в отчетах:
1. Авторизация под тестовыми учетными данными.
2. Добавление трех выбранных товаров в корзину.
3. Заполнение формы персональных данных покупателя.
4. Проверка корректности итоговой суммы (`Total: $58.29`) на финальном шаге.
5. Автоматическое создание скриншотов на ключевых этапах выполнения.

</details>

<details>

<summary>📰 Boni Garcia Calculator - тестирование калькулятора UI Automation Project</summary>

[![QA Automation](https://shields.io)](https://github.com)
[![Python](https://shields.io)](https://python.org)
[![Framework](https://shields.io)](https://pytest.org)
[![Reporting](https://shields.io)](https://allurereport.org)
[![Generating ASCII](https://shields.io)](https://gitlab.com/nfriend/tree-online#what-is-this)

Проект содержит автоматизированные UI-тесты для калькулятора 
[(Boni Garcia)]([https://saucedemo.com](https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html)). 

В основе проекта лежит паттерн **Page Object Model (POM)**.

---

## 🛠 Используемые технологии
* **Язык программирования:** Python 3.10+
* **Редактор кода:** VS Code (Visual Studio Code)
* **Тест-раннер:** Pytest
* **Автоматизация браузера:** Selenium WebDriver (с явными ожиданиями `WebDriverWait`)
* **Отчетность:** Allure Framework

---

## 📂 Структура проекта

```text
└── Calculator_PageObject/
 ├── pages/                  # Классы Page Object (логика работы со страницами)/
 │       └── profile_page.py # Класс для представления и взаимодействия со страницей 
 ├── tests/                  # Тестовые файлы/
 │       └── test_profile.py # Тесты проверки ввода цифр, арифметических операторов и результатов арифметических операций
 ├── shot                    # Папка со скриншотами операций
 ├── conftest.py             # Настройки Pytest (инициализация драйвера, фикстуры)
 └── README.md               # Документация проекта
```

---

## 🛠️ Установка и запуск

### 1. Клонирование репозитория
```bash
git clone https://github.com/Sergey-747/Skypro_automation_course.git
cd Skypro_automation_course
```

### 2. Настройка виртуального окружения (при необходимости)
```bash
python -m venv venv
source venv/bin/activate  # Для Linux/macOS
# или
venv\Scripts\activate     # Для Windows
# после проведения тестирования деактивируйте виртуальное окружение
deactivate                # Для Linux/macOS и Windows
```

### 3. Установка зависимостей (при необходимости)
```bash
pip install -r requirements.txt
```

---

## 🏃 Запуск тестов

### Обычный запуск всех тестов:
```bash
pytest -v test_profile.py
```

### Запуск с генерацией результатов для Allure:
```bash
pytest --alluredir=allure-results
```

### Запуск тестов по уровням серьезности (Severity):
```bash
# Только блокирующие тесты (Blocker)
pytest --alluredir=allure-results --allure-severities=blocker
```

---

## 📊 Генерация отчетов Allure

Для локального просмотра красивого веб-отчета со скриншотами и шагами выполните команду (требуется установленный [Allure CLI](https://allurereport.orgdocs/install/)):

```bash
allure serve allure-results
```

### Что проверяется в отчетах:
1. Корректность открытия страницы
2. Кликабельность кнопок калькулятора.
3. Точность выполнения арифметических операций
4. Автоматическое создание скриншотов на ключевых этапах выполнения.

</details>
