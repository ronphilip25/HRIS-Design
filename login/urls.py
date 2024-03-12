from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('attendance/', views.attendance, name="attendance"),
    path('attendance/monthly', views.monthly, name="monthly"),
    path('attendance/schedule', views.schedule, name="schedule"),
]
