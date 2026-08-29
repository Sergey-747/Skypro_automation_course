import requests
from functools import cached_property


class Project_api:
    def __init__(self, url):
        self.url = url

    @cached_property
    def token(self):
        return self.get_key()

    def get_key(
        self,
        login="you_login",
        password="you_password",
        companyId="you_ companyId",
    ):
        """Получение ключа авторизации"""

        # Формируем заголовки
        header = {"Content-Type": "application/json"}
        # Формируем тело запроса (JSON-данные)
        data = {"login": login, "password": password, "companyId": companyId}
        # Отправляем POST-запрос
        response = requests.post(self.url + "auth/keys/get", headers=header, json=data)
        return response.json()[-1]["key"]

    def greation_progect(self, data):
        """Создание нового проекта"""
        # Подготавливаем заголовок
        header = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        # Отправляем запрос
        resp = requests.post(self.url + "projects", headers=header, json=data)
        new_project = resp.json()["id"]
        return new_project

    def edit_project(self, data, project_id):
        """Редактирование имеющегося проекта"""
        header = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

        url = f"{self.url}projects/{project_id}"
        resp = requests.put(url, json=data, headers=header)
        # Проеряем статус-код (200 OK или 204 No Content)
        if resp.status_code in [200, 2004]:
            print("Проект успешно изменён!")
        else:
            try:
                error_details = resp.json()
            except Exception:
                error_details = resp.text
            print("Ошибка изменения:", error_details)
        return resp.json()

    # Работает
    def id_last_projects(self):
        """Получение информации об ID последнего проекта"""
        # Подготавливаем заголовок
        header = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        resp = requests.get(self.url + "projects", headers=header)
        resp_data = resp.json()
        last_project_id = resp_data["content"][-1]["id"]
        return last_project_id

    # работает
    def last_project(self, project_id):
        """Получение информации о последнем проекте"""
        header = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        url = f"{self.url}projects/{project_id}"
        resp = requests.get(url, headers=header)
        return resp.json()
