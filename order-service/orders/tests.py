from unittest.mock import Mock, patch

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from orders.models import Order


class HealthCheckTests(APITestCase):
    def test_health_endpoint_returns_success(self):
        response = self.client.get("/health/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "healthy")


class OrderTests(APITestCase):
    @patch("orders.views.requests.get")
    def test_create_order(self, mock_get):
        user_response = Mock()
        user_response.status_code = 200

        product_response = Mock()
        product_response.status_code = 200
        product_response.json.return_value = {
            "quantity": 10,
        }

        mock_get.side_effect = [
            user_response,
            product_response,
        ]

        payload = {
            "user_id": 1,
            "product_id": 1,
            "quantity": 2,
        }

        response = self.client.post(
            reverse("order-list"),
            payload,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)