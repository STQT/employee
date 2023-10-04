from django.shortcuts import render
from django.http import JsonResponse
from .models import Department


def department_list(request):
    root_department = Department.objects.get(name='Company')
    return render(request, 'employees/department_list.html', {'root_department': root_department})


def load_department(request, department_id):
    department = Department.objects.get(pk=department_id)
    children = Department.objects.filter(parent=department)
    data = [{'id': child.id, 'name': child.name} for child in children]
    return JsonResponse({'data': data})
