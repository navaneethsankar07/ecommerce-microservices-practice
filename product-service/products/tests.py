from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from products.models import Product


class HealthCheckTests(APITestCase):
    def test_health_endpoint_returns_success(self):
        response = self.client.get("/health/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "healthy")


class ProductTests(APITestCase):
    def test_create_product(self):
        payload = {
            "name": "Laptop",
            "price": "50000.00",
            "quantity": 20,
        }

        response = self.client.post(
            reverse("product-list"),
            payload,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)

    def test_get_product(self):
        product = Product.objects.create(
            name="Laptop",
            price=50000,
            quantity=20,
        )

        response = self.client.get(
            reverse("product-detail", args=[product.id])
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], product.name)