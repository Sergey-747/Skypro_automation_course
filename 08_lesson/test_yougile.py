import pytest
from functools import cached_property
from Project_Api_test import Project_api

api = Project_api("https://ru.yougile.com/api-v2/")

"""Позитивные тесты"""


def test_greation_progect():
    """Тест на создание нового проекта"""
    new_name_project = "Наше дело"
    data = {
        "title": new_name_project,
        "users": {"a5209aa5-d070-4077-8a37-2c3bb04ad6ee": "admin"},
    }
    project_id = api.greation_progect(data)
    assert project_id


"""Изменить данные в проекте"""


def test_edit_progect():
    edit_tittle = "Бизнес"
    data = {"title": edit_tittle}
    project_id = api.id_last_projects()
    project = api.edit_project(data, project_id)
    id_last_project = api.id_last_projects()
    last_project = api.last_project(id_last_project)
    new_title = last_project["title"]
    assert edit_tittle == new_title, f"Получена {new_title}"


"""Получить проект по ID"""


def test_get_project_by_ID():
    project_id = api.id_last_projects()
    project = api.last_project(project_id)
    assert isinstance(project, dict)


"""Негативные тесты"""


def test_negative_greation_progect():
    """Тест на создание нового проекта"""
    new_name_project = ""  # новое имя проекта
    data = {
        "title": new_name_project,
        "users": {"a5209aa5-d070-4077-8a37-2c3bb04ad6ee": "admin"},
    }
    project_id = api.greation_progect(data)
    assert type(project_id) is str
    assert project_id


"""Изменить данные в проекте"""


def test_negative_edit_progect():
    edit_tittle = "😊 процессы"
    data = {"deleted": True, "title": edit_tittle}
    project_id = api.id_last_projects()
    project = api.edit_project(data, project_id)
    id_last_project = api.id_last_projects()
    last_project = api.last_project(id_last_project)
    new_title = last_project["title"]
    assert edit_tittle == new_title, f"Получена {new_title}"


"""Получить проект по ID"""


def test_negative_get_project_by_ID():
    project_id = ""
    project = api.last_project(project_id)
    assert project == "", f"Ожидалась пустая строка, но получено: '{project}'"
