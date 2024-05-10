from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.

# Index
def index(request):
    return render(request, 'index.html')

# def base(request):
#     return render(request, 'base.html')


# End of Index

# Dashboard
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
                "name": "Drew Garcia",
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

# End of Dashboard

# Attendance
# def attendance(request):
#     threshold = request.GET.get("threshold")
#     if threshold == "weekly":
#         return render(request, 'attendance/weekly.html')
#     # if threshold == "monthly":
#     #     return render(request, 'attendance/monthly.html')
        
    return render(request, '_components/attendance.html')

def daily(request):
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
    return render(request, '_components/_attendance[components]/daily.html', context=context)

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
# End Attendance Components


# Leaves Components
def leaves(request):
    return render(request, '_components/leaves.html')

def leave_usage(request):
    return render(request, '_components/_leaves[components]/leave_usage.html')

def manual_grant(request):
    return render(request, '_components/_leaves[components]/manual_grant.html')

def leave_setting(request):
    return render(request, '_components/_leaves[components]/leave_setting.html')
# End Leaves Components




# Team Components
def employees(request):
    return render(request, '_components/_team[components]/employees.html')

def active(request):
    return render(request, '_components/_team[components]/_submenus/active.html')

def invited(request):
    return render(request, '_components/_team[components]/_submenus/invited.html')

def resigned(request):
    return render(request, '_components/_team[components]/_submenus/resigned.html')

def deleted(request):
    return render(request, '_components/_team[components]/_submenus/deleted.html')

def organization(request):
    return render(request, '_components/_team[components]/organization.html')

def department(request):
    return render(request, '_components/_team[components]/_submenus/department.html')

def tier(request):
    return render(request, '_components/_team[components]/_submenus/tier.html')

# End Team Components


# Filing Components
def approval_management(request):
    return render(request, '_components/_filing[components]/approval_management.html')

def approved(request):
    return render(request, '_components/_filing[components]/_submenus/approved.html')

def pending_approval(request):
    return render(request, '_components/_filing[components]/_submenus/pending_approval.html')

def filing_settings(request):
    return render(request, '_components/_filing[components]/filing_settings.html')




# Settings Components
def company_settings(request):
    return render(request, '_components/_settings[components]/company_settings.html')

def company_info(request):
    return render(request, '_components/_settings[components]/_submenus/company_info.html')

def work_place(request):
    return render(request, '_components/_settings[components]/_submenus/work_place.html')

def setup_work_sched(request):
    return render(request, '_components/_settings[components]/_submenus/setup_work_sched.html')

def company_work_sched(request):
    return render(request, '_components/_settings[components]/_submenus/_schedule[setup_work]/company_work_sched.html')

def holiday(request):
    return render(request, '_components/_settings[components]/_submenus/holiday.html')

def admin_settings(request):
    return render(request, '_components/_settings[components]/admin_settings.html')

def master_admin2(request):
    return render(request, '_components/_settings[components]/_submenus/master_admin2.html')

def head_group(request):
    return render(request, '_components/_settings[components]/_submenus/head_group.html')

def testers(request):
    return render(request, '_components/_settings[components]/_submenus/testers.html')
# End Settings Components