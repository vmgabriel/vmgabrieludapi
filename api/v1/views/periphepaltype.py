"""View API"""

# Libraries
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions

# Models
from vmgabrieludapi.models.periphepaltype import Periphepaltype

# Serializers
from ..serializers.periphepaltype import PeriphepaltypeSerializer


class PeriphepaltypeViewSet(viewsets.ModelViewSet):
    queryset = Periphepaltype.objects.all()
    serializer_class = PeriphepaltypeSerializer
    permission_classes = [permissions.IsAuthenticated]