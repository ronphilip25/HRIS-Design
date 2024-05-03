from django.urls import path
from . import views

urlpatterns = [
    
    # Index/Dashboard
    path('', views.index),
    # path('base/', views.base, name='base'),
    path('dashboard', views.dashboard, name='dashboard'),
    
    # Attendance Components
    path('attendance/daily', views.daily, name='daily'),
    path('attendance/monthly', views.monthly, name='monthly'),
    path('attendance/schedule', views.schedule, name='schedule'),
    
    # Leave Components
    path('leaves', views.leaves, name='leaves'),
    path('leaves/leave_usage', views.leave_usage, name='leave_usage'),
    path('leaves/manual_grant', views.manual_grant, name='manual_grant'),
    path('leaves/leave_setting', views.leave_setting, name='leave_setting'),
    
    
    # Team Components
    path('team/', views.team, name='team'),
    path('team/organization/', views.organization, name='organization'),
    
    # Settings Copmponents
    path('company_settings', views.company_settings, name='company_settings'),
    path('company_settings/company_info/', views.company_info, name='company_info'),
    path('company_settings/work_place/', views.work_place, name='work_place'),
    path('company_settings/setup_work_sched/', views.setup_work_sched, name='setup_work_sched'),
    path('company_settings/setup_work_sched/company_work_sched/', views.company_work_sched, name='company_work_sched'),
    path('company_settings/holiday', views.holiday, name='holiday'),
    
    path('admin_settings', views.admin_settings, name='admin_settings'),
    path('admin_settings/master_admin2', views.master_admin2, name='master_admin2'),
    path('admin_settings/head_group', views.head_group, name='head_group'),
    path('admin_settings/testers', views.testers, name='testers'),
]