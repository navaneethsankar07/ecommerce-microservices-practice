from django.http import JsonResponse
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


def health(request):
    return JsonResponse({
        "service": "product-service",
        "status": "healthy"
    })


class ProductListCreateView(
    generics.ListCreateAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(
    generics.RetrieveAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer