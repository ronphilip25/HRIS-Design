from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login/login.html')


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
                "name": "Celvin Nucum",
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
    
    return render(request, 'dashboard/dashboard.html', context=context)

def attendance(request):
    threshold = request.GET.get("threshold")
    if threshold == "weekly":
        return render(request, 'attendance/weekly.html')

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
        ]
        
    }
    return render(request, 'attendance/attendance.html', context=context)

def sidebar(request):
    return render(request, 'sidebar/sidebar.html')

def invited(request):
    context = {
        "invited": [
            {
                "name": "John Andrew Arce",
                "status": "Waiting",
                "contact_number": "123",
                "work_email": "ja@geoproglobal.com",
                "departments": "",
                "tier": "",
                "join_date": "02/24/2024",
                "action": "",
            },
            {
                "name": "John Andrew Arce",
                "status": "Waiting",
                "contact_number": "123",
                "work_email": "ja@geoproglobal.com",
                "departments": "",
                "tier": "",
                "join_date": "02/24/2024",
                "action": "",
            },
            {
                "name": "John Andrew Arce",
                "status": "Active",
                "contact_number": "123",
                "work_email": "12esadaw@gmail.com",
                "departments": "",
                "tier": "",
                "join_date": "02/24/2024",
                "action": "",
            },
            {
                "name": "John Andrew Arce",
                "status": "Active",
                "contact_number": "123",
                "work_email": "12esadaw@gmail.com",
                "departments": "",
                "tier": "",
                "join_date": "02/24/2024",
                "action": "",
            },
            {
                "name": "John Andrew Arce",
                "status": "Active",
                "contact_number": "123",
                "work_email": "12esadaw@gmail.com",
                "departments": "",
                "tier": "",
                "join_date": "02/24/2024",
                "action": "",
            },
            {
                "name": "John Andrew Arce",
                "status": "Active",
                "contact_number": "123",
                "work_email": "12esadaw@gmail.com",
                "departments": "",
                "tier": "",
                "join_date": "02/24/2024",
                "action": "",
            },
            
             
        ]
    }
    return render(request, 'invited/invited.html', context=context)

def employee(request):
    return render(request, 'employee/employee.html')

def active(request):
    context = {
        "active": [
            {
                "name": "John Andrew Arce",
                "status": "Waiting",
                "contact_number": "123",
                "work_email": "ja@geoproglobal.com",
                "tier": "Team Lead",
            },
            {
                "name": "John Andrew Arce",
                "status": "Waiting",
                "contact_number": "123",
                "work_email": "ja@geoproglobal.com",
                "tier": "Team Lead",
            },
            {
                "name": "John Andrew Arce",
                "status": "Active",
                "contact_number": "123",
                "work_email": "12esadaw@gmail.com",
                "tier": "Team Lead",
            },
            {
                "name": "John Andrew Arce",
                "status": "Active",
                "contact_number": "123",
                "work_email": "12esadaw@gmail.com",
                "tier": "Team Lead",
            },
            {
                "name": "John Andrew Arce",
                "status": "Active",
                "contact_number": "123",
                "work_email": "12esadaw@gmail.com",
                "tier": "Team Lead",
            },
            {
                "name": "John Andrew Arce",
                "status": "Active",
                "contact_number": "123",
                "work_email": "12esadaw@gmail.com",
                "tier": "Team Lead",
            },
            {
                "name": "John Andrew Arce",
                "status": "Active",
                "contact_number": "123",
                "work_email": "12esadaw@gmail.com",
                "tier": "Team Lead",
            },
            {
                "name": "John Andrew Arce",
                "status": "Active",
                "contact_number": "123",
                "work_email": "12esadaw@gmail.com",
                "tier": "Team Lead",
            },
            
             
        ]
    }
    return render(request, 'active/active.html', context=context)