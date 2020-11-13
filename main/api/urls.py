from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from .views import (
    PostListAPIView,
    PostDetailAPIView,
    PostDeleteAPIView,
    PostUpdateAPIView,
)

urlpatterns = [
    path(r"", PostListAPIView.as_view(), name="List-API"),
    url(r"(?P<pk>\d+)/$", PostDetailAPIView.as_view(), name="Detail-API"),
    url(r"(?P<pk>\d+)/delete/$", PostDeleteAPIView.as_view(), name="Delete-API"),
    url(r"(?P<pk>\d+)/update/$", PostUpdateAPIView.as_view(), name="Update-API"),
]
