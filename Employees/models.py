from django.db import models

# Create your models here.

class Department(models.Model):
    dept_name = models.CharField(max_length=30)
    dept_location = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.dept_name} - {self.dept_location}"
    
    
class Employee(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    designation = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)  # Soft delete flag
        
    def __str__(self):
        return f"{self.fullname} ({self.designation})"

    def full_name(self):
        return f"{self.fullname}"