"""Content Camera"""

# Libraries
from django.db import models

 # Modules


class Camera(models.Model):
    name = models.CharField("name", max_length=100, )
