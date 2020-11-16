from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
)


from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
)
from django.contrib.auth import get_user_model

from .serializers import UserCreateSerializer

User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
