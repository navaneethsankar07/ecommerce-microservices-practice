from django.http import JsonResponse

from rest_framework import generics

from .models import User
from .serializers import UserSerializer


def health(request):
    return JsonResponse({
        "service": "user-service",
        "status": "healthy"
    })


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer