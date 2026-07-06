from django.urls import path

from .views import (
    health,
    ProductListCreateView,
    ProductDetailView,
)

urlpatterns = [
    path(
        "health/",
        health,
        name="health",
    ),
    path(
        "products/",
        ProductListCreateView.as_view(),
        name="product-list",
    ),
    path(
        "products/<int:pk>/",
        ProductDetailView.as_view(),
        name="product-detail",
    ),
]