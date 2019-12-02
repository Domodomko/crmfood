from rest_framework import serializers
from food.models import Table, Role, Department, User, MealCategory, Status, ServicePercentage, Meal


class TableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Table
        fields = ('name',)


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ('name',)


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('name',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'surname', 'login', 'password', 'email', 'roleid', 'dateofadd', 'phone')


class MealCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MealCategory
        fields = ('name', 'departmentid')


class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ('name',)


class ServicePercentageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServicePercentage
        fields = ('percentage',)


class MealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'name', 'categoryid', 'price', 'description')