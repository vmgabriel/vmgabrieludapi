"""Serializer Api vmgabrieludapi - Camera"""

# Libraries
from rest_framework import serializers

# Modules
from vmgabrieludapi.models.camera import Camera

# Serializers


class CameraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Camera
        fields = ["id", "name", ]