from django.contrib import admin
from food.models import Table, Role, Department, User, MealCategory, Status, ServicePercentage, Meal

admin.site.register(Table)
admin.site.register(Role)
admin.site.register(Department)
admin.site.register(User)
admin.site.register(MealCategory)
admin.site.register(Status)
admin.site.register(ServicePercentage)
admin.site.register(Meal)