"""vmgabrieludapi - Periphepaltype - Test"""

# Modules
from django.test import TestCase
from datetime import datetime
from vmgabrieludapi.models.periphepaltype import Periphepaltype


class PeriphepaltypeTestCase(TestCase):
    """PeriphepalType test cases"""
    fixtures = [ "periphepaltype.json"]

    def test_should_get_datas(self):
        periphepaltype = Periphepaltype.objects.all()
        self.assertEqual(periphepaltype.count(), 3)

    def test_should_get_one_data(self):
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        periphepaltype_name = Periphepaltype.objects.filter(name__icontains="Update")
        self.assertEqual(periphepaltype_name.count(), 3)
        periphepaltype_description = Periphepaltype.objects.filter(description__icontains="Update")
        self.assertEqual(periphepaltype_description.count(), 3)

    def test_should_get_none_data(self):
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        periphepaltype_name = Periphepaltype.objects.filter(name__icontains="2")
        self.assertEqual(periphepaltype_name.count(), 0)
        periphepaltype_description = Periphepaltype.objects.filter(description__icontains="2")
        self.assertEqual(periphepaltype_description.count(), 0)

    def test_get_data(self):
        pk = 2
        periphepaltype = Periphepaltype.objects.get(pk=pk)
        self.assertIsInstance(periphepaltype, (Periphepaltype,))

    def test_put_data(self):
        pk=2
        current_time = datetime.strptime("2020-12-18 3:11:09", "%Y-%m-%d %H:%M:%S")
        data = Periphepaltype.objects.get(pk=pk)
        data.name = "Update"
        data.description = "Update"

        data.save()
        self.assertEqual(data.name, "Update")
        self.assertEqual(data.description, "Update")

    def test_create_data(self):
        new_object = {
            "name": "Update",
            "description": "Update"
        }
        data = Periphepaltype(**new_object)
        data.save()
        pk = data.pk
        datas = Periphepaltype.objects.get(pk=pk)
        self.assertEqual(pk, datas.pk)

    def test_remove_data(self):
        pk = 3
        periphepaltype = Periphepaltype.objects.get(pk=pk)
        periphepaltype.delete()
        datas = Periphepaltype.objects.all().count()
        self.assertEqual(datas, 2)