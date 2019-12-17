from django.db import models
import jwt

from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)


class UserManager(BaseUserManager):
    def create_user(self, role, name, surname, username, email, phone=None, password=None):
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(
            role=role,
            username=username,
            email=self.normalize_email(email),
            name=name,
            surname=surname,
            phone=phone
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')
        role = Role.objects.get(id=1)
        user = self.create_user(username=username,
        email=email, password=password, phone="077777777",
        role=role, name=username, surname=username)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class Role(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL)
    name = models.CharField(db_index=True, max_length=255)
    surname = models.CharField(db_index=True, max_length=255)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    phone = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_short_name(self):
        return self.name

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')


class Table(models.Model):
    name = models.CharField(max_length=100, default='')


class Department(models.Model):
    name = models.CharField(max_length=100, default='')


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
