from django.contrib import admin
from .models import Department, Employee

# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("dept_name", "dept_location")
    search_fields = ("dept_name",)
    
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "fullname", "email", "designation", "created_at", "department"]
    search_fields = ["fullname", "email"]
    list_display_links = ["id", "fullname"]
    ordering = ["-id"]
        