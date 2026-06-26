from django.urls import path

from .views import (
    health,
    ProductListCreateView,
    ProductDetailView
)

urlpatterns = [

    path(
        "health/",
        health
    ),

    path(
        "products/",
        ProductListCreateView.as_view()
    ),

    path(
        "products/<int:pk>/",
        ProductDetailView.as_view()
    ),
]