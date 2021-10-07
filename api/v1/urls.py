"""Urls V1 API"""

from django.urls import path, include
from rest_framework import routers

# Modules
from .router import router


urlpatterns = [
    path("", include(router.urls))
]
