from django.urls import path
from food import views
from .views import *

urlpatterns = [
    path('tables', views.TableListView.as_view()),
    path('roles', views.RoleListView.as_view()),
    path('departments', views.DepartmentListView.as_view()),
    path('categories', views.MealCategoryListView.as_view()),
    path('statuses', views.StatusListView.as_view()),
    path('percentage', views.ServicePercentageListView.as_view()),
    path('meals', views.MealListView.as_view()),
    path('orders', views.OrderListView.as_view()),
    path('checks', views.CheckListView.as_view()),
    path('mealstoorder', views.MealsToOrderListView.as_view()),
    path('activeorders', views.ActiveOrderListView.as_view()),
    path('users', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
    path('user', UserRetrieveUpdateAPIView.as_view()),
]