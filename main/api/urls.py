from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from .views import (
    PostListAPIView,
    PostDetailAPIView,
    PostDeleteAPIView,
    PostUpdateAPIView,
    PostCreateAPIView,
)

urlpatterns = [
    path(r"", PostListAPIView.as_view(), name="List-API"),
    path("create/", PostCreateAPIView.as_view(), name="Create-API"),
    path("<int:pk>/", PostDetailAPIView.as_view(), name="Detail-API"),
    path("<int:pk>/delete/", PostDeleteAPIView.as_view(), name="Delete-API"),
    path("<int:pk>/update/", PostUpdateAPIView.as_view(), name="Update-API"),
]
