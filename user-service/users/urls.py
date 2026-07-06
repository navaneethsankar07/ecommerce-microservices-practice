from django.urls import path

from .views import (
    health,
    UserListCreateView,
    UserDetailView,
)

urlpatterns = [
    path(
        "health/",
        health,
        name="health",
    ),
    path(
        "users/",
        UserListCreateView.as_view(),
        name="user-list",
    ),
    path(
        "users/<int:pk>/",
        UserDetailView.as_view(),
        name="user-detail",
    ),
]