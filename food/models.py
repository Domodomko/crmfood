from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=100, default='')


class Role(models.Model):
    name = models.CharField(max_length=100, default='')


class Department(models.Model):
    name = models.CharField(max_length=100, default='')


class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    roleid = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='user')
    dateofadd = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)


class MealCategory(models.Model):
    name = models.CharField(max_length=100, default='')
    departmentid = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department')


class Status(models.Model):
    name = models.CharField(max_length=100, default='')


class ServicePercentage(models.Model):
    percentage = models.IntegerField(default=0)


class Order(models.Model):
    waiterid = models.IntegerField(default=0)
    tableid = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='table', null=True)
    isitopen = models.BooleanField(default=0)
    date = models.CharField(max_length=200, default='')

    def get_total_sum(self):
        return sum(item.get_sum() for item in self.orderid.all())


class Meal(models.Model):
    name = models.CharField(max_length=100, default='')
    categoryid = models.ForeignKey(MealCategory, on_delete=models.CASCADE, related_name='category')
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='mealsid')


class MealsToOrder(models.Model):
    orderid = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name='orderid')
    mealsid = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True)
    count = models.IntegerField(default=1)

    def get_sum(self):
        return self.mealsid.price * self.count


class Check(models.Model):
    orderid = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    servicefee = models.ForeignKey(ServicePercentage, on_delete=None, related_name='servicefee')
    date = models.CharField(max_length=100, default='')

    def get_total(self):
        return self.orderid.get_total_sum() * (1+(self.servicefee.percentage/100))
