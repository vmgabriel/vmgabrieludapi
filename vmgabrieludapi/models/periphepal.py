"""Content Periphepal"""

# Libraries
from django.db import models

 # Modules
from . import periphepaltype


class Periphepal(models.Model):
    name = models.CharField("name", max_length=100, )
    description = models.CharField("description", null=True, blank=True, max_length=200, )
    type_periphepal = models.ForeignKey(periphepaltype.Periphepaltype, on_delete=models.CASCADE)
