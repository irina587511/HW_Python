import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://ru.yougile.com/api-v2"
TOKEN = os.getenv("YOUGILE_API_TOKEN")
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}


class ProjectsPage:

    @staticmethod
    def create_project(name: str) -> requests.Response:
        payload = {"title": name}
        response = requests.post(f"{BASE_URL}/projects", json=payload, headers=HEADERS)
        return response

    @staticmethod
    def update_project(project_id: str, name: str) -> requests.Response:
        payload = {"title": name}
        response = requests.put(f"{BASE_URL}/projects/{project_id}", json=payload, headers=HEADERS)
        return response

    @staticmethod
    def get_project(project_id: str) -> requests.Response:
        response = requests.get(f"{BASE_URL}/projects/{project_id}", headers=HEADERS)
        return response

    @staticmethod
    def delete_project(project_id: str) -> requests.Response:
        response = requests.delete(f"{BASE_URL}/projects/{project_id}", headers=HEADERS)
        return response
