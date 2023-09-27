from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Employee , Employee_Notification , Employee_leave ,Attendance

@login_required(login_url='/')
def Home(request):
    employee = Employee.objects.filter(admin=request.user.id)
    for i in employee:
        employee_id = i.id
        employee_attendance = Attendance.objects.filter(employee_id=employee_id)
        context = {
            'employee_attendance': employee_attendance,
        }
        return render(request, 'Employee/home.html', context)

@login_required(login_url='/')
def Notification(request):
    employee = Employee.objects.filter(admin=request.user.id)
    for i in employee:
        employee_id = i.id
        notification = Employee_Notification.objects.filter(employee_id=employee_id)
        context = {
            'notification':notification,
        }
        return render(request, 'Employee/notification.html' , context)

@login_required(login_url='/')
def Mark_As_Done(request,status):
    notification = Employee_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('notification')

@login_required(login_url='/')
def Employee_Leave(request):
    employee = Employee.objects.filter(admin=request.user.id)
    for i in employee:
        employee_id = i.id
        employee_leave_history = Employee_leave.objects.filter(employee_id=employee_id)
        context = {
            'employee_leave_history': employee_leave_history,
        }
        return render(request, 'Employee/leave.html', context)

@login_required(login_url='/')
def Employee_Save_Leave(request):
    if request.method == "POST":
        leave_type = request.POST.get('leave_type')
        leave_date = request.POST.get('leave_date')
        message = request.POST.get('message')

        employee = Employee.objects.get(admin=request.user.id)
        leave = Employee_leave(
            employee_id=employee,
            data=leave_date,
            message=message,
        )
        leave.save()
        messages.success(request, "Employee Leave Successfully Submit!!")
        return redirect('apply_leave')

@login_required(login_url='/')
def Attendance_Sheet(request):
    employee_id = request.user.employee
    today_date = timezone.now().date()
    has_logged_in_today = Attendance.objects.filter(
        employee_id=employee_id,
        date=today_date,
        logout_time__isnull=True  # Check if there is no logout time for today
    ).exists()

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'login':
            if not has_logged_in_today:
                login_time = timezone.now().time()
                attendance = Attendance(
                    employee_id=employee_id,
                    date=today_date,
                    login_time=login_time,
                )
                attendance.save()
        elif action == 'logout':
            if has_logged_in_today:
                logout_time = timezone.now().time()
                print(logout_time)
                latest_login = Attendance.objects.filter(
                    employee_id=employee_id,
                    date=today_date,
                    logout_time__isnull=True
                ).order_by('-id').first()
                if latest_login:
                    latest_login.logout_time = logout_time
                    latest_login.save()

    employee_attendance = Attendance.objects.filter(employee_id=employee_id)

    return render(request, 'Employee/attendance_sheet.html', {'employee_attendance': employee_attendance, 'loggedIn': has_logged_in_today})
