from django.urls import path

from .views import (
    health,
    OrderListCreateView,
)

urlpatterns = [
    path(
        "health/",
        health,
        name="health",
    ),
    path(
        "orders/",
        OrderListCreateView.as_view(),
        name="order-list",
    ),
]