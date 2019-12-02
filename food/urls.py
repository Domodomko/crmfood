from django.urls import path
from food import views

urlpatterns = [
    path('tables', views.TableListView.as_view()),
    path('roles', views.RoleListView.as_view()),
    path('departments', views.DepartmentListView.as_view()),
    path('categories', views.MealCategoryListView.as_view()),
    path('statuses', views.StatusListView.as_view()),
    path('percentage', views.ServicePercentageListView.as_view()),
    path('meals', views.MealListView.as_view()),
]