"""Router API"""

# Libraries
from rest_framework import routers

# Modules
from .views.periphepaltype import PeriphepaltypeViewSet
from .views.periphepal import PeriphepalViewSet
from .views.camera import CameraViewSet
from .views.cameraperiphepal import CameraperiphepalViewSet


router = routers.DefaultRouter()
router.register(r"periphepaltypes", PeriphepaltypeViewSet)
router.register(r"periphepals", PeriphepalViewSet)
router.register(r"cameras", CameraViewSet)
router.register(r"cameraperiphepals", CameraperiphepalViewSet)
