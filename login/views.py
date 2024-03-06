from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login/login.html')


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def attendance(request):
    return render(request, 'attendance/attendance.html')