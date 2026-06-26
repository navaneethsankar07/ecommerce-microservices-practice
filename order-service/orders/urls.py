from django.urls import path

from .views import (
    health,
    OrderListCreateView
)

urlpatterns = [

    path(
        "health/",
        health
    ),

    path(
        "orders/",
        OrderListCreateView.as_view()
    ),
]