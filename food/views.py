from food.serializers import *
from rest_framework import generics, filters


class TableListView(generics.ListAPIView):
    serializer_class = TableSerializer
    queryset = Table.objects.all()


class RoleListView(generics.ListAPIView):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()


class DepartmentListView(generics.ListAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class MealCategoryListView(generics.ListAPIView):
    serializer_class = MealCategorySerializer
    queryset = MealCategory.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['departmentid__name',]


class StatusListView(generics.ListAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()


class ServicePercentageListView(generics.ListAPIView):
    serializer_class = ServicePercentageSerializer
    queryset = ServicePercentage.objects.all()


class MealListView(generics.ListAPIView):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()