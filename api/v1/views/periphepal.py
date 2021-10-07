"""View API"""

# Libraries
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions

# Models
from vmgabrieludapi.models.periphepal import Periphepal

# Serializers
from ..serializers.periphepal import PeriphepalSerializer


class PeriphepalViewSet(viewsets.ModelViewSet):
    queryset = Periphepal.objects.all()
    serializer_class = PeriphepalSerializer
    permission_classes = [permissions.IsAuthenticated]