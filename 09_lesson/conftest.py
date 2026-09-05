import pytest
from sqlalchemy import create_engine


# Создаем один общий engine для тестов
DATABASE_URL = "postgresql://postgres:12345@localhost:5432/MyPostgreSQL"  
engine = create_engine(DATABASE_URL)

@pytest.fixture(scope="function")
def db_connection():
    """Фикстура для тестов на чистом SQL. Откатывает все INSERT/UPDATE/DELETE."""
    # Открываем соединение
    connection = engine.connect()
    # Запускаем транзакцию 
    transaction = connection.begin()

    # Передаем соединение в функцию теста
    yield connection

    # ПОСЛЕ ТЕСТА: откатываем абсолютно все изменения
    transaction.rollback()
    connection.close()
