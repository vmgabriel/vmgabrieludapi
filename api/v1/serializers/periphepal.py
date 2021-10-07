"""Serializer Api vmgabrieludapi - Periphepal"""

# Libraries
from rest_framework import serializers

# Modules
from vmgabrieludapi.models.periphepal import Periphepal

# Serializers
from ..serializers.periphepaltype import PeriphepaltypeSerializer


class PeriphepalSerializer(serializers.ModelSerializer):
    type_periphepal = PeriphepaltypeSerializer(many=True)

    class Meta:
        model = Periphepal
        fields = ["id", "name", "description", "type_periphepal", ]