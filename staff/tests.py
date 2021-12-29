from django.test import TestCase
from staff.models import Department, Employee


class StaffTestCase(TestCase):

    def setUp(self):
        self.d = Department.objects.create(name="Sales", manager="Emp11")
        print("d:", self.d)
        self.e = Employee.objects.create(name="Rohan", depart=self.d, email="test11@gmail.com")
        print("e:", self.e)

    def test_get_data(self):
        try:
            self.assertEqual(self.d.name, 'Sales')
            self.assertEqual(self.e.name, 'Rohan')
        except Exception as e:
            print("ERROR:", repr(e))


