"""vmgabrieludapi - Periphepal - Test"""

# Modules
from django.test import TestCase
from datetime import datetime
from vmgabrieludapi.models.periphepal import Periphepal


class PeriphepalTestCase(TestCase):
    """Periphepal test cases"""
    fixtures = ["periphepaltype.json", "periphepal.json"]

    def test_should_get_datas(self):
        periphepal = Periphepal.objects.all()
        self.assertEqual(periphepal.count(), 3)

    def test_should_get_one_data(self):
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        periphepal_name = Periphepal.objects.filter(name__icontains="Update")
        self.assertEqual(periphepal_name.count(), 3)
        periphepal_description = Periphepal.objects.filter(description__icontains="Update")
        self.assertEqual(periphepal_description.count(), 3)

    def test_should_get_none_data(self):
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        periphepal_name = Periphepal.objects.filter(name__icontains="2")
        self.assertEqual(periphepal_name.count(), 0)
        periphepal_description = Periphepal.objects.filter(description__icontains="2")
        self.assertEqual(periphepal_description.count(), 0)

    def test_get_data(self):
        pk = 2
        periphepal = Periphepal.objects.get(pk=pk)
        self.assertIsInstance(periphepal, (Periphepal,))

    def test_put_data(self):
        pk=2
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        data = Periphepal.objects.get(pk=pk)
        data.name = "Update"
        data.description = "Update"

        data.save()
        self.assertEqual(data.name, "Update")
        self.assertEqual(data.description, "Update")

    def test_create_data(self):
        new_object = {
            "name": "Update",
            "description": "Update",
            "type_periphepal_id": 1
        }
        data = Periphepal(**new_object)
        data.save()
        pk = data.pk
        datas = Periphepal.objects.get(pk=pk)
        self.assertEqual(pk, datas.pk)

    def test_remove_data(self):
        pk = 3
        periphepal = Periphepal.objects.get(pk=pk)
        periphepal.delete()
        datas = Periphepal.objects.all().count()
        self.assertEqual(datas, 2)