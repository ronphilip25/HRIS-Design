from django.urls import path
from . import views

urlpatterns = [
    
    # Index
    path('', views.index),
    path('base/', views.base, name='base'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Attendance Components
    path('attendance/', views.attendance, name='attendance'),
    path('attendance/monthly', views.monthly, name='monthly'),
    path('attendance/schedule', views.schedule, name='schedule'),
    
    # Team Components
    path('team/', views.team, name='team'),
    path('team/organization', views.organization, name='organization'),
    path('team/employees', views.employees, name='employees'),
]