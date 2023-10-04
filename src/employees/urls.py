from django.urls import path

from src.employees.views import department_list, load_department

app_name = "employees"
urlpatterns = [
    path("", department_list, name="department-list"),
    path("<int:department_id>/", load_department, name="employees-list"),
]
