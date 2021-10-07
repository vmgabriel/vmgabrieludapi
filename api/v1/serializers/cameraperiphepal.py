"""Serializer Api vmgabrieludapi - Cameraperiphepal"""

# Libraries
from rest_framework import serializers

# Modules
from vmgabrieludapi.models.cameraperiphepal import Cameraperiphepal

# Serializers
from ..serializers.camera import CameraSerializer
from ..serializers.periphepal import PeriphepalSerializer


class CameraperiphepalSerializer(serializers.ModelSerializer):
    camera = CameraSerializer(many=True)
    periphepal = PeriphepalSerializer(many=True)

    class Meta:
        model = Cameraperiphepal
        fields = ["id", "camera", "periphepal", ]