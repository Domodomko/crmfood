from django.test import TestCase
from food.models import *


class OrderModelTest(TestCase):
    def setUp(self):
        role = Role.objects.create(name='AFFICIANT')
        table = Table.objects.create(name='STOL')
        order = Order.objects.create(waiterid=1, tableid=table, isitopen = 1, date='10.12.2019')
        department = Department.objects.create(name='DEPARTAMENT PO BEZOPASNOSTI TVOEI VIRGINOSTI')
        mealcategory = MealCategory.objects.create(name='VERY HOT',departmentid = department)
        status = Status.objects.create(name='READY')
        servicepercentage = ServicePercentage.objects.create(percentage = 22)
        meal = Meal.objects.create(name='PLOV', categoryid = mealcategory, price = 228, description = 'kekeke', order = order)

    def test_role(self):
        role = Role.objects.get(name='AFFICIANT')
        self.assertEqual(role.name, 'AFFICIANT')

    def test_table(self):
        table = Table.objects.get(name='STOL')
        self.assertEqual(table.name, 'STOL')

    def test_order(self):
        order = Order.objects.get(waiterid=1, isitopen = 1)
        self.assertEqual(order.waiterid, 1)
        self.assertEqual(order.isitopen, 1)

    def test_department(self):
        department = Department.objects.get(name='DEPARTAMENT PO BEZOPASNOSTI TVOEI VIRGINOSTI')
        self.assertEqual(department.name, 'DEPARTAMENT PO BEZOPASNOSTI TVOEI VIRGINOSTI')

    def test_department(self):
        department = Department.objects.get(name='DEPARTAMENT PO BEZOPASNOSTI TVOEI VIRGINOSTI')
        self.assertEqual(department.name, 'DEPARTAMENT PO BEZOPASNOSTI TVOEI VIRGINOSTI')

    def test_mealcategory(self):
        mealcategory = MealCategory.objects.get(name='VERY HOT')
        self.assertEqual(mealcategory.name, 'VERY HOT')

    def test_status(self):
        status = Status.objects.get(name='READY')
        self.assertEqual(status.name, 'READY')

    def test_meal(self):
        meal = Meal.objects.get(name='PLOV', price=228, description='kekeke')
        self.assertEqual(meal.name, 'PLOV')
        self.assertEqual(meal.price, 228)







