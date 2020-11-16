from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from .views import UserCreateAPIView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r"register/", UserCreateAPIView.as_view(), name="Register-API"),
]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
