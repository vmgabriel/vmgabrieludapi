"""vmgabrieludapi - Cameraperiphepal - Test"""

# Modules
from django.test import TestCase
from datetime import datetime
from vmgabrieludapi.models.cameraperiphepal import Cameraperiphepal


class CameraperiphepalTestCase(TestCase):
    """CameraPeriphepal test cases"""
    fixtures = ["camera.json","periphepal.json","periphepaltype.json", "cameraperiphepal.json"]

    def test_should_get_datas(self):
        cameraperiphepal = Cameraperiphepal.objects.all()
        self.assertEqual(cameraperiphepal.count(), 3)

    def test_should_get_one_data(self):
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")

    def test_should_get_none_data(self):
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")

    def test_get_data(self):
        pk = 2
        cameraperiphepal = Cameraperiphepal.objects.get(pk=pk)
        self.assertIsInstance(cameraperiphepal, (Cameraperiphepal,))

    def test_put_data(self):
        pk=2
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        data = Cameraperiphepal.objects.get(pk=pk)

        data.save()

    def test_create_data(self):
        new_object = {
            "camera_id": 1,
            "periphepal_id": 1
        }
        data = Cameraperiphepal(**new_object)
        data.save()
        pk = data.pk
        datas = Cameraperiphepal.objects.get(pk=pk)
        self.assertEqual(pk, datas.pk)

    def test_remove_data(self):
        pk = 3
        cameraperiphepal = Cameraperiphepal.objects.get(pk=pk)
        cameraperiphepal.delete()
        datas = Cameraperiphepal.objects.all().count()
        self.assertEqual(datas, 2)