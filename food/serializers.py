from rest_framework import serializers
from food.models import *
from django.contrib.auth import authenticate


class RegistrationSerializer(serializers.ModelSerializer):
    roleid = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(),
        source='role.id'
    )
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['roleid', 'name', 'surname', 'email', 'created_at', 'token', 'phone']
        read_only_fields = ('create_at', 'token')

    def create(self, validated_data):
        username = validated_data['name'] + "_user"
        password = validated_data['phone']
        return User.objects.create_user(
            role=validated_data.pop('role')['id'],
            username=username,
            password=password,
            **validated_data
        )


class LoginSerializer(serializers.Serializer):
    role_id = serializers.IntegerField(
        source='role.id',
        read_only=True
    )
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in'
            )
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                "A user with this email and password was not found."
            )

        if not user.is_active:
            raise serializers.ValidationError(
                "This user has been deactivated."
            )

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('role', 'name', 'surname', 'email', 'username', 'created_at', 'password', 'token')
        read_only_fields = ('token',)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance


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


class MealCategorySerializer(serializers.HyperlinkedModelSerializer):
    departmentid = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())

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
    categoryid = serializers.PrimaryKeyRelatedField(queryset=MealCategory.objects.all())

    class Meta:
        model = Meal
        fields = ('id', 'name', 'categoryid', 'price', 'description')


class MealsToOrderSerializer(serializers.ModelSerializer):
    mealsid = serializers.PrimaryKeyRelatedField(queryset=Meal.objects.all(), source='mealsid.id')
    name = serializers.CharField(source='mealsid.name', read_only=True)

    class Meta:
        model = MealsToOrder
        fields = ('mealsid', 'name', 'count')


class MealsToCheckSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='mealsid.name', read_only=True)
    price = serializers.CharField(source='mealsid.price', read_only=True)
    total = serializers.FloatField(source='get_sum', read_only=True)

    class Meta:
        model = MealsToOrder
        fields = ('name', 'count', 'price', 'total')


class OrderSerializer(serializers.ModelSerializer):
    mealsid = MealsToOrderSerializer(many=True, required=False, source='orderid')
    tableid = serializers.PrimaryKeyRelatedField(queryset=MealCategory.objects.all())
    tablename = serializers.CharField(source='tableid.name', read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'waiterid', 'tableid', 'tablename', 'isitopen', 'date', 'mealsid')


class CheckSerializer(serializers.ModelSerializer):
    orderid = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all(), source='orderid.id')
    servicefee = serializers.FloatField(source='servicefee.percentage', read_only=True)
    meals = MealsToCheckSerializer(many=True, required=False)
    totalsum = serializers.FloatField(source='get_total', read_only=True)

    class Meta:
        model = Check
        fields = ['id', 'orderid', 'date', 'servicefee', 'totalsum', 'meals']
