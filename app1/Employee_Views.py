from django.shortcuts import render,redirect
from app1.models import Employee , Employee_Notification

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
    return render(request,'Employee/leave.html')