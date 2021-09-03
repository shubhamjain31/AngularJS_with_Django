from django.urls import path
from App import views

urlpatterns = [
    path('add/employee/', views.employee_add,name='employee_add'),
    path('edit/employee/<int:id>', views.employee_edit,name='employee_edit'),
    path('delete/employee/',views.employee_delete,name='employee_delete'),
    path('', views.employee_list, name='employee_list'),
    path('search/', views.search, name='search')
]