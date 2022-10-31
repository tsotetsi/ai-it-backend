import unittest
from fastapi.testclient import TestClient
from fastapi import status

from app import app, API_VERSION, API_ENV


client = TestClient(app=app)


class TestApplicationRoot(unittest.TestCase):

    """
    Test application root url.
    """
    def test_app_route(self) -> None:
        response = client.get(
            "/"
        )
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["api_version"], API_VERSION)
        self.assertEqual(data["environment"], API_ENV)
