"""Content Periphepaltype"""

# Libraries
from django.db import models

 # Modules


class Periphepaltype(models.Model):
    name = models.CharField("name", max_length=120, )
    description = models.CharField("description", max_length=200, )
