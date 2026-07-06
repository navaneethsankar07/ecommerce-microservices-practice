from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json
from users.models import User

class HealthCheckTests(APITestCase):
    def test_health_endpoint_returns_success(self):
        response = self.client.get("/health/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = json.loads(response.content)

        self.assertEqual(data["status"], "healthy")

class UserTests(APITestCase):
    def test_create_user(self):
        payload = {
            "name": "Navaneeth",
            "email": "navaneeth@example.com",
        }

        response = self.client.post(
            reverse("user-list"),
            payload,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

    def test_get_user(self):
        user = User.objects.create(
            name="Navaneeth",
            email="navaneeth@example.com",
        )

        response = self.client.get(
            reverse("user-detail", args=[user.id])
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], user.email)