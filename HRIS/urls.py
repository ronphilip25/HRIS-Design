from django.urls import path
from . import views

urlpatterns = [
    
    # Index/Dashboard
    path('', views.index),
    path('base/', views.base, name='base'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Attendance Components
    path('attendance/', views.attendance, name='attendance'),
    path('attendance/monthly', views.monthly, name='monthly'),
    path('attendance/schedule', views.schedule, name='schedule'),
    
    # Team Components
    path('team/', views.team, name='team'),
    path('team/organization/', views.organization, name='organization'),
    
    # Settings Copmponents
    path('settings/', views.settings, name='settings'),
    path('settings/company_info/', views.company_info, name='company_info'),
    path('settings/work_place/', views.work_place, name='work_place'),
    path('settings/setup_work_sched/', views.setup_work_sched, name='setup_work_sched'),
    path('settings/setup_work_sched/company_work_sched/', views.company_work_sched, name='company_work_sched'),
]