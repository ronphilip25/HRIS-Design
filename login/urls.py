from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('attendance/', views.attendance, name="attendance"),
    path('sidebar/', views.sidebar, name="sidebar"),
    path('invited/', views.invited, name="invited"),
    path('employees/', views.employee, name="employees"),
    path('active/', views.active, name="active"),
    
]

