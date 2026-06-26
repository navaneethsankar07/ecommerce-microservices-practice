from django.http import JsonResponse

import requests

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serializers import OrderSerializer


def health(request):
    return JsonResponse({
        "service": "order-service",
        "status": "healthy"
    })


class OrderListCreateView(APIView):

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(
            orders,
            many=True
        )
        return Response(serializer.data)

    def post(self, request):

        user_id = request.data.get("user_id")
        product_id = request.data.get("product_id")
        quantity = request.data.get("quantity")

        try:

            user_response = requests.get(
                f"http://127.0.0.1:8001/users/{user_id}/"
            )

            if user_response.status_code != 200:
                return Response(
                    {"error": "User not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            product_response = requests.get(
                f"http://127.0.0.1:8002/products/{product_id}/"
            )

            if product_response.status_code != 200:
                return Response(
                    {"error": "Product not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            product_data = product_response.json()

            available_stock = product_data["stock"]

            if int(quantity) > available_stock:
                return Response(
                    {
                        "error": "Insufficient stock"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

        except requests.exceptions.ConnectionError:

            return Response(
                {
                    "error": "Unable to communicate with other services"
                },
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )

        serializer = OrderSerializer(data=request.data)

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )