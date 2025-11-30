import pytest
from pages.projects_page import ProjectsPage


class TestProjectsAPI:

    @pytest.fixture
    def projects_page(self):
        return ProjectsPage()

    def test_create_project_positive(self, projects_page):
        # позитивный: создание с корректными данными
        response = projects_page.create_project("Test Project", "API Test")
        assert response.status_code == 201
        data = response.json()
        assert "id" in data
        assert data["name"] == "Test Project"

    def test_create_project_negative_empty_name(self, projects_page):
        # негативный: создание без имени
        response = projects_page.create_project("", "Only description")
        assert response.status_code == 400
        data = response.json()
        assert "error" in data or "message" in data

    def test_update_project_positive(self, projects_page):
        # позитивный: редактирование проекта
        # Создание проекта
        create_resp = projects_page.create_project("Temp Project", "Temp")
        assert create_resp.status_code == 201
        project_id = create_resp.json()["id"]

        # Редактирование
        update_resp = projects_page.update_project(project_id, "Updated Name!")
        assert update_resp.status_code == 200
        data = update_resp.json()
        assert data["name"] == "Updated Name!"

    def test_update_project_negative_nonexistent_id(self, projects_page):
        # негативный: редактирование несуществующего проекта
        response = projects_page.update_project("999999", "Invalid")
        assert response.status_code in [404, 400]

    def test_get_project_positive(self, projects_page):
        # позитивный: получение проекта
        # Создание проекта
        create_resp = projects_page.create_project("Get Test", "")
        assert create_resp.status_code == 201
        project_id = create_resp.json()["id"]

        # Получение проекта
        response = projects_page.get_project(project_id)
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == project_id

    def test_get_project_negative_nonexistent_id(self, projects_page):
         # негативный: получение несуществующего проекта
        response = projects_page.get_project("999999")
        assert response.status_code in [404, 400]
