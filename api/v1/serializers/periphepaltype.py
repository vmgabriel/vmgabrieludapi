"""Serializer Api vmgabrieludapi - Periphepaltype"""

# Libraries
from rest_framework import serializers

# Modules
from vmgabrieludapi.models.periphepaltype import Periphepaltype

# Serializers


class PeriphepaltypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Periphepaltype
        fields = ["id", "name", "description", ]