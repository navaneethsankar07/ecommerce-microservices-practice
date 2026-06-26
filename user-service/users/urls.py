from django.urls import path

from .views import (
    health,
    UserListCreateView,
    UserDetailView
)

urlpatterns = [
    path("health/", health),

    path(
        "users/",
        UserListCreateView.as_view()
    ),

    path(
        "users/<int:pk>/",
        UserDetailView.as_view()
    ),
]