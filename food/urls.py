from django.urls import path
from food import views

urlpatterns = [
    path('tables', views.TableListView),
    path('roles', views.RoleListView),
    path('departments', views.DepartmentListView),
    path('categories', views.MealCategoryListView),
    path('statuses', views.StatusListView),
    path('percentage', views.ServicePercentageListView),
    path('meals', views.MealListView),
]