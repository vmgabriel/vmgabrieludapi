"""View API"""

# Libraries
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions

# Models
from vmgabrieludapi.models.camera import Camera

# Serializers
from ..serializers.camera import CameraSerializer


class CameraViewSet(viewsets.ModelViewSet):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer
    permission_classes = [permissions.IsAuthenticated]