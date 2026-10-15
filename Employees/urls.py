from django.urls import include, path
from . import views 


urlpatterns = [
    path('<int:id>/', views.employee_detail, name = 'employee_detail'),
    path('add/', views.employee_add, name = 'employee_add'),
    path('<int:id>/edit/', views.employee_edit, name='employee_edit'),
    path('<int:id>/delete/', views.employee_delete, name='employee_delete'),
]