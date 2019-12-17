from food.serializers import *
from rest_framework import generics, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import RetrieveUpdateAPIView
from .renderers import UserJSONRenderer
import json


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, )
    renderer_classes = (UserJSONRenderer, )
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})

        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class LoginAPIView(APIView):
    permission_classes = (AllowAny, )
    renderer_classes = (UserJSONRenderer, )
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class TableListView(generics.ListAPIView):
    serializer_class = TableSerializer
    queryset = Table.objects.all()

    def get(self, request):
        tables = Table.objects.all()
        serializer = TableSerializer(tables, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        data = json.loads((request.body).decode("utf-8"))
        Table.objects.filter(id=data['id']).delete()
        return Response(status=status.HTTP_201_CREATED)


class RoleListView(APIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def get(self, request):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        data = json.loads((request.body).decode("utf-8"))
        Role.objects.filter(id=data['id']).delete()
        return Response(status=status.HTTP_201_CREATED)


class DepartmentListView(generics.ListAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

    def get(self, request):
        department = Department.objects.all()
        serializer = DepartmentSerializer(department, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        data = json.loads((request.body).decode("utf-8"))
        Department.objects.filter(id=data['id']).delete()
        return Response(status=status.HTTP_201_CREATED)


class MealCategoryListView(generics.ListAPIView):
    serializer_class = MealCategorySerializer
    queryset = MealCategory.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['departmentid__name', ]

    def get(self, request):
        roles = MealCategory.objects.all()
        serializer = MealCategorySerializer(roles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MealCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request):
        data = json.loads((request.body).decode("utf-8"))
        MealCategory.objects.filter(id=data['id']).delete()
        return Response(status=status.HTTP_201_CREATED)


class StatusListView(generics.ListAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()

    def get(self, request):
        roles = Status.objects.all()
        serializer = StatusSerializer(roles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        data = json.loads((request.body).decode("utf-8"))
        Status.objects.filter(id=data['id']).delete()
        return Response(status=status.HTTP_201_CREATED)


class ServicePercentageListView(generics.ListAPIView):
    serializer_class = ServicePercentageSerializer
    queryset = ServicePercentage.objects.all()

    def get(self, request):
        roles = ServicePercentage.objects.all()
        serializer = ServicePercentageSerializer(roles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer =  ServicePercentageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        data = json.loads((request.body).decode("utf-8"))
        ServicePercentage.objects.filter(id=data['id']).delete()
        return Response(status=status.HTTP_201_CREATED)


class MealListView(generics.ListAPIView):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()

    def get(self, request):
        serializer = MealSerializer(Meal.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        data = json.loads((request.body).decode("utf-8"))
        Meal.objects.filter(id=data['id']).delete()

        return Response(status=status.HTTP_201_CREATED)


class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get(self, request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        data = json.loads((request.body).decode("utf-8"))
        Order.objects.filter(id=data['id']).delete()

        return Response(status=status.HTTP_201_CREATED)


class ActiveOrderListView(APIView):
    def get(self, request):
        orders = Order.objects.filter(isitopen=1)
        serializer = OrderSerializer(orders, many=True)

        return Response(serializer.data)


class CheckListView(generics.ListAPIView):
    serializer_class = CheckSerializer
    queryset = Check.objects.all()

    def get(self, request):
        checks = Check.objects.all()
        serializer = CheckSerializer(checks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CheckSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        data = json.loads((request.body).decode("utf-8"))
        Check.objects.filter(id=data['id']).delete()

        return Response(status=status.HTTP_201_CREATED)

class MealsToCheckListView(generics.ListAPIView):
    serializer_class = MealsToCheckSerializer
    queryset = MealsToOrder.objects.all()

