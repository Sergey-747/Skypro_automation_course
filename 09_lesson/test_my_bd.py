from sqlalchemy import text

def test_add_users(db_connection):
    """Добавление пользователя и студента"""
    user_id = 50
    subject_id = 15
    email_to_check = "director@mail.ru"

    sql_user = text(
        "INSERT INTO users (user_id, user_email, subject_id) VALUES (:user_id, :new_user_email, :subject_id)"
    )
    sql_student = text(
        "INSERT INTO student (user_id, level, education_form, subject_id) VALUES (:user_id, :level, :education_form, :subject_id)"
    )
    
    # Сначала родитель (users)
    db_connection.execute(
        sql_user,
        {
            "user_id": user_id,
            "new_user_email": email_to_check,
            "subject_id": subject_id,
        },
    )
    # Затем потомок (student)
    db_connection.execute(
        sql_student,
        {
            "user_id": user_id,
            "level": "Beginner",
            "education_form": "group",
            "subject_id": subject_id,
        },
    )

    # Проверяем пользователя
    check_user_query = text("SELECT user_email FROM users WHERE user_id = :user_id;")
    db_email = db_connection.execute(check_user_query, {"user_id": user_id}).scalar()
    assert db_email == email_to_check, f"Ожидали {email_to_check}, но в БД сохранено: {db_email}"

    # Проверяем студента
    check_student_query = text("SELECT level FROM student WHERE user_id = :user_id;")
    db_level = db_connection.execute(check_student_query, {"user_id": user_id}).scalar()
    assert db_level == "Beginner", f"Ожидали уровень Beginner, но получили {db_level}"


def test_change_user(db_connection):
    """Изменение email пользователя"""
    user_id = 60
    old_email = "director@mail.ru"
    new_email = "new_director@mail.ru"

    # Подготовка данных: создаем пользователя для этого изолированного теста
    db_connection.execute(
        text("INSERT INTO users (user_id, user_email, subject_id) VALUES (:id, :email, 1)"),
        {"id": user_id, "email": old_email}
    )

    # Действие: обновляем email
    sql_update = text(
        """
        UPDATE users 
        SET user_email = :new_email 
        WHERE user_email = :old_email
        """
    )
    result = db_connection.execute(
        sql_update,
        {
            "new_email": new_email,
            "old_email": old_email,
        },
    )
    
    assert result.rowcount == 1, "Пользователь не найден или не был обновлен"

    # Проверяем, что старый email исчез
    check_old = db_connection.execute(
        text("SELECT * FROM users WHERE user_email = :email"),
        {"email": old_email},
    )
    assert check_old.fetchone() is None, "Старый email всё еще существует!"

    # Проверяем, что новый email успешно записан
    check_new = db_connection.execute(
        text("SELECT * FROM users WHERE user_email = :email"),
        {"email": new_email},
    )
    assert check_new.fetchone() is not None, "Новый email не был найден!"


def test_del_user_id(db_connection):
    """Удаление пользователя и его данных студента по ID"""
    user_id = 70

    # Подготовка данных: создаем изолированного пользователя и студента
    db_connection.execute(
        text("INSERT INTO users (user_id, user_email, subject_id) VALUES (:id, 'to_delete@mail.ru', 1)"),
        {"id": user_id}
    )
    db_connection.execute(
        text("INSERT INTO student (user_id, level) VALUES (:id, 'Intermediate')"),
        {"id": user_id}
    )

    # Действие: удаляем в правильном порядке (сначала дочерний student, затем родитель users)
    sql_student = text("DELETE FROM student WHERE user_id = :user_id")
    sql_user = text("DELETE FROM users WHERE user_id = :user_id")
    
    res_student = db_connection.execute(sql_student, {"user_id": user_id})
    res_user = db_connection.execute(sql_user, {"user_id": user_id})

    # Проверка с помощью rowcount
    assert res_student.rowcount == 1, "Запись студента не была удалена"
    assert res_user.rowcount == 1, "Запись пользователя не была удалена"
