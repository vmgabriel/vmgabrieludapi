"""Urls of API"""

from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


urlpatterns = [
    path("v1/", include("api.v1.urls")),

    # Auth
    path("auth/",  include("rest_framework.urls")),
    path("auth/jwt/", obtain_jwt_token),
    path("auth/jwt/refresh/", refresh_jwt_token),
    path("auth/jwt/verify/", verify_jwt_token),
]
