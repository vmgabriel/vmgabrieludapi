"""View API"""

# Libraries
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions

# Models
from vmgabrieludapi.models.cameraperiphepal import Cameraperiphepal

# Serializers
from ..serializers.cameraperiphepal import CameraperiphepalSerializer


class CameraperiphepalViewSet(viewsets.ModelViewSet):
    queryset = Cameraperiphepal.objects.all()
    serializer_class = CameraperiphepalSerializer
    permission_classes = [permissions.IsAuthenticated]