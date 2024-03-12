from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('attendance/', views.attendance, name="attendance"),
    
    
    
    # LEONARD FORMS AND MODALS
    path("AddWorkSchedule/", views.AddWorkSchedule, name="AddWorkSchedule"),
    path("InviteEmployees/", views.InviteEmployees, name="InviteEmployees"),
    path("EmployeeInformation/", views.EmployeeInformation, name="EmployeeInformation"),
    path("sample/", views.sample, name="sample"),
    
    path("", views.home, name="home"),
]
