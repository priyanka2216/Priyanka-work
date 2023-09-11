from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Employee , Employee_Notification , Employee_leave

def Home(request):
    return render(request, 'Employee/home.html')


def Notification(request):
    employee = Employee.objects.filter(admin=request.user.id)
    for i in employee:
        employee_id = i.id

        notification = Employee_Notification.objects.filter(employee_id=employee_id)
        context = {
            'notification':notification,
        }
        return render(request, 'Employee/notification.html' , context)


def Mark_As_Done(request,status):
    notification = Employee_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('notification')


def Employee_Leave(request):
    employee = Employee.objects.filter(admin=request.user.id)
    for i in employee:
        employee_id = i.id
        employee_leave_history = Employee_leave.objects.filter(employee_id=employee_id)
        context = {
            'employee_leave_history': employee_leave_history,
        }
        return render(request, 'Employee/leave.html', context)

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