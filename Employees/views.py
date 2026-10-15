from django.shortcuts import get_object_or_404, redirect, render
from . models import Department, Employee
from . forms import EmployeeForm 


def employee_detail(request, id):
    
    employee = get_object_or_404(Employee, id=id, is_deleted=False) 
    
    context = {
        'employee': employee,
    }
    
    return render(request, 'employee_detail.html', context)
    

    
# Add Employee
def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            return redirect('employee_detail', id=employee.id)
    else:
        form = EmployeeForm()

    context = {
        'form': form,
        'page_title': 'Add Employee',
        'button_text': 'Add Employee',
    }

    return render(request, 'employee_form.html', context)


# Edit Employee
def employee_edit(request, id):
    employee = get_object_or_404(Employee, id=id, is_deleted=False)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            return redirect('employee_detail', id=employee.id)
        
    else:
        form = EmployeeForm(instance=employee)

    context = {
        'form': form,
        'employee': employee,
        'page_title': 'Edit Employee',
        'button_text': 'Save Changes',
    }

    return render(request, 'employee_form.html', context)


# Soft Delete Employee
def employee_delete(request, id):
    employee = get_object_or_404(Employee, id=id, is_deleted=False)

    if request.method == 'POST':
        employee.is_deleted = True
        employee.save(update_fields=['is_deleted'])
        return redirect('home')

    return render(request,'employee_confirm_delete.html',{'employee': employee})