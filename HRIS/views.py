from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def dashboard(request):
    context = {
        "dashboard": [
            {
                "name": "Jane Nicole",
                "department": "Teaching",
                "tardiness": "0",
                "absences": "0",
            },
            {
                "name": "NIGGA",
                "department": "IT",
                "tardiness": "0",
                "absences": "0",
            },
            {
                "name": "Louis Dizon",
                "department": "IT",
                "tardiness": "0",
                "absences": "0",
            },
            {
                "name": "Sean Owen Turner",
                "department": "IT",
                "tardiness": "0",
                "absences": "0",
            },
            {
                "name": "Ivan Magtite",
                "department": "IT",
                "tardiness": "0",
                "absences": "0",
            },
            {
                "name": "Carlo Pingol",
                "department": "IT",
                "tardiness": "0",
                "absences": "0",
            },
            {
                "name": "Cleavant",
                "department": "IT",
                "tardiness": "0",
                "absences": "0",
            },
            {
                "name": "Jim manese",
                "department": "IT",
                "tardiness": "0",
                "absences": "0",
            },
            {
                "name": "John Doe",
                "department": "IT",
                "tardiness": "0",
                "absences": "0",
            },
            {
                "name": "John Doe",
                "department": "IT",
                "tardiness": "0",
                "absences": "0",
            },
            {
                "name": "John Doe",
                "department": "IT",
                "tardiness": "0",
                "absences": "0",
            },
            {
                "name": "John Doe",
                "department": "IT",
                "tardiness": "0",
                "absences": "0",
            },
            {
                "name": "John Doe",
                "department": "IT",
                "tardiness": "0",
                "absences": "0",
            },
            
        ],
        
        "approvals": [
            {
                "name": "John Doe",
                "department": "IT",
                "type": "Leave",
                "request_date": "02/24/2024",
            },
            {
                "name": "John Doe",
                "department": "IT",
                "type": "Leave",
                "request_date": "02/24/2024",
            },
            {
                "name": "John Doe",
                "department": "IT",
                "type": "Leave",
                "request_date": "02/24/2024",
            },
            {
                "name": "John Doe",
                "department": "IT",
                "type": "Leave",
                "request_date": "02/24/2024",
            },
            {
                "name": "John Doe",
                "department": "IT",
                "type": "Leave",
                "request_date": "02/24/2024",
            },
        ],
    }
    return render(request, '_components/dashboard.html',context=context)

def attendance(request):
    threshold = request.GET.get("threshold")
    if threshold == "weekly":
        return render(request, 'attendance/weekly.html')
    # if threshold == "monthly":
    #     return render(request, 'attendance/monthly.html')
        
    context = {
        "attendance": [
            {
                "date": "02/24/2024",
                "day": "Tuesday",
                "total_working_hrs": "8hrs",
                "in_out": "9:00 AM - 6:00 PM",
                "break": "12:00 NN - 1:00 PM",
                "overtime": "2hrs",
                "notes": "Hello",
            },
            {
                "date": "02/24/2024",
                "day": "Tuesday",
                "total_working_hrs": "8hrs",
                "in_out": "9:00 AM - 6:00 PM",
                "break": "12:00 NN - 1:00 PM",
                "overtime": "2hrs",
                "notes": "Hello",
            },
            {
                "date": "02/24/2024",
                "day": "Tuesday",
                "total_working_hrs": "8hrs",
                "in_out": "9:00 AM - 6:00 PM",
                "break": "12:00 NN - 1:00 PM",
                "overtime": "2hrs",
                "notes": "Hello",
            },
            {
                "date": "02/24/2024",
                "day": "Tuesday",
                "total_working_hrs": "8hrs",
                "in_out": "9:00 AM - 6:00 PM",
                "break": "12:00 NN - 1:00 PM",
                "overtime": "2hrs",
                "notes": "Hello",
            },
            {
                "date": "02/24/2024",
                "day": "Tuesday",
                "total_working_hrs": "8hrs",
                "in_out": "9:00 AM - 6:00 PM",
                "break": "12:00 NN - 1:00 PM",
                "overtime": "2hrs",
                "notes": "Hello",
                "action": "",
            },
            {
                "date": "02/24/2024",
                "day": "Tuesday",
                "total_working_hrs": "8hrs",
                "in_out": "9:00 AM - 6:00 PM",
                "break": "12:00 NN - 1:00 PM",
                "overtime": "2hrs",
                "notes": "Hello",
                "action": "",
            },
        ],
        
        "user": [
            {
                "name": "Patricia Kim Rosauro",
            }
        ],
        
        
    }
    return render(request, '_components/attendance.html', context=context)

def monthly(request):
    context = {
        "monthly": [
            {
                "department": "IT",
                "work_schedule": "Day shift",
                "work_hour": "8:00am - 6:00pm",
                "overtime": "-",
                "holiday_work": "-",
                "holiday_overtime": "-",
                "leave": "-",
                "tardiness": "-",
                "under_time": "-",
                "absences": "-",
                "custom_policy": "-",
            },
            {
                "department": "IT",
                "work_schedule": "Day shift",
                "work_hour": "8:00am - 6:00pm",
                "overtime": "-",
                "holiday_work": "-",
                "holiday_overtime": "-",
                "leave": "-",
                "tardiness": "-",
                "under_time": "-",
                "absences": "-",
                "custom_policy": "-",
            },
            {
                "department": "IT",
                "work_schedule": "Day shift",
                "work_hour": "8:00am - 6:00pm",
                "overtime": "-",
                "holiday_work": "-",
                "holiday_overtime": "-",
                "leave": "-",
                "tardiness": "-",
                "under_time": "-",
                "absences": "-",
                "custom_policy": "-",
            },
            {
                "department": "IT",
                "work_schedule": "Day shift",
                "work_hour": "8:00am - 6:00pm",
                "overtime": "-",
                "holiday_work": "-",
                "holiday_overtime": "-",
                "leave": "-",
                "tardiness": "-",
                "under_time": "-",
                "absences": "-",
                "custom_policy": "-",
            },
            {
                "department": "IT",
                "work_schedule": "Day shift",
                "work_hour": "8:00am - 6:00pm",
                "overtime": "-",
                "holiday_work": "-",
                "holiday_overtime": "-",
                "leave": "-",
                "tardiness": "-",
                "under_time": "-",
                "absences": "-",
                "custom_policy": "-",
            },
            {
                "department": "IT",
                "work_schedule": "Day shift",
                "work_hour": "8:00am - 6:00pm",
                "overtime": "-",
                "holiday_work": "-",
                "holiday_overtime": "-",
                "leave": "-",
                "tardiness": "-",
                "under_time": "-",
                "absences": "-",
                "custom_policy": "-",
            },
            {
                "department": "IT",
                "work_schedule": "Day shift",
                "work_hour": "8:00am - 6:00pm",
                "overtime": "-",
                "holiday_work": "-",
                "holiday_overtime": "-",
                "leave": "-",
                "tardiness": "-",
                "under_time": "-",
                "absences": "-",
                "custom_policy": "-",
            },
            {
                "department": "IT",
                "work_schedule": "Day shift",
                "work_hour": "8:00am - 6:00pm",
                "overtime": "-",
                "holiday_work": "-",
                "holiday_overtime": "-",
                "leave": "-",
                "tardiness": "-",
                "under_time": "-",
                "absences": "-",
                "custom_policy": "-",
            },
            {
                "department": "IT",
                "work_schedule": "Day shift",
                "work_hour": "8:00am - 6:00pm",
                "overtime": "-",
                "holiday_work": "-",
                "holiday_overtime": "-",
                "leave": "-",
                "tardiness": "-",
                "under_time": "-",
                "absences": "-",
                "custom_policy": "-",
            },
        ],
    }
    
    return render(request, '_components/_attendance[components]/monthly.html', context=context)


def schedule(request):
    return render(request, '_components/_attendance[components]/schedule.html')
