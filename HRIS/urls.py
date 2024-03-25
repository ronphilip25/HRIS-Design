from django.urls import path
from . import views

urlpatterns = [
    
    # Index/Dashboard
    path('', views.index),
    path('base/', views.base, name='base'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Attendance Components
    path('attendance/', views.attendance, name='attendance'),
    path('attendance/daily', views.daily, name='daily'),
    path('attendance/monthly', views.monthly, name='monthly'),
    path('attendance/schedule', views.schedule, name='schedule'),
    
    # Leave Components
    path('leaves/', views.leaves, name='leaves'),
    path('leaves/leave_usage', views.leave_usage, name='leave_usage'),
    path('leaves/manual_grant', views.manual_grant, name='manual_grant'),
    path('leaves/leave_settings', views.leave_settings, name='leave_settings'),
    
    
    # Team Components
    path('team/', views.team, name='team'),
    path('team/organization/', views.organization, name='organization'),
    
    # Settings Copmponents
    path('settings/', views.settings, name='settings'),
    path('settings/company_info/', views.company_info, name='company_info'),
    path('settings/work_place/', views.work_place, name='work_place'),
    path('settings/setup_work_sched/', views.setup_work_sched, name='setup_work_sched'),
    path('settings/setup_work_sched/company_work_sched/', views.company_work_sched, name='company_work_sched'),
    path('settings/holiday', views.holiday, name='holiday'),
]