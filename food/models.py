from django.db import models


# Create your models here.

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
    roleid = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='User')
    dateofadd = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)


class MealCategory(models.Model):
    name = models.CharField(max_length=100, default='')
    departmentid = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='Department')


class Status(models.Model):
    name = models.CharField(max_length=100, default='')


class ServicePercentage(models.Model):
    percentage = models.IntegerField(default=0)


class Meal(models.Model):
    name = models.CharField(max_length=100, default='')
    categoryid = models.ForeignKey(MealCategory, on_delete=models.CASCADE, related_name='Category')
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='')
