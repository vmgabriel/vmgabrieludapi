"""Content Cameraperiphepal"""

# Libraries
from django.db import models

 # Modules
from . import camera
from . import periphepal


class Cameraperiphepal(models.Model):
    camera = models.ForeignKey(camera.Camera, on_delete=models.CASCADE)
    periphepal = models.ForeignKey(periphepal.Periphepal, on_delete=models.CASCADE)
