
from django.http import HttpResponse
from Employees.models import Employee
from django.shortcuts import render

def home(request):
    employees = Employee.objects.filter(is_deleted=False) 
    context = {
        'employees': employees,
    }
    # print(employees)   # for debugging purposes
    return render(request, 'home.html', context)