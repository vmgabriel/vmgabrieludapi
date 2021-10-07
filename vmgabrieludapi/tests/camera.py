"""vmgabrieludapi - Camera - Test"""

# Modules
from django.test import TestCase
from datetime import datetime
from vmgabrieludapi.models.camera import Camera


class CameraTestCase(TestCase):
    """Camera test cases"""
    fixtures = [ "camera.json"]

    def test_should_get_datas(self):
        camera = Camera.objects.all()
        self.assertEqual(camera.count(), 3)

    def test_should_get_one_data(self):
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        camera_name = Camera.objects.filter(name__icontains="Update")
        self.assertEqual(camera_name.count(), 3)

    def test_should_get_none_data(self):
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        camera_name = Camera.objects.filter(name__icontains="2")
        self.assertEqual(camera_name.count(), 0)

    def test_get_data(self):
        pk = 2
        camera = Camera.objects.get(pk=pk)
        self.assertIsInstance(camera, (Camera,))

    def test_put_data(self):
        pk=2
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        data = Camera.objects.get(pk=pk)
        data.name = "Update"

        data.save()
        self.assertEqual(data.name, "Update")

    def test_create_data(self):
        new_object = {
            "name": "Update"
        }
        data = Camera(**new_object)
        data.save()
        pk = data.pk
        datas = Camera.objects.get(pk=pk)
        self.assertEqual(pk, datas.pk)

    def test_remove_data(self):
        pk = 3
        camera = Camera.objects.get(pk=pk)
        camera.delete()
        datas = Camera.objects.all().count()
        self.assertEqual(datas, 2)