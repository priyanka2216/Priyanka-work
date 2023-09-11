from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Designation ,CustomUser,Employee,Session_year ,Employee_Notification,Employee_leave
from django.contrib import messages
from django.db.models import Count


@login_required(login_url='/')
def Home(request):
    employee_count = Employee.objects.all().count()
    designation_count = Designation.objects.all().count()

    employee_gender_male =Employee.objects.filter(gender = 'Male').count()
    employee_gender_female = Employee.objects.filter(gender = 'Female').count()
    print(employee_gender_male)
    print(employee_gender_female)

    context = {
        'employee_count':employee_count,
        'designation_count':designation_count,
        'employee_gender_male':employee_gender_male,
        'employee_gender_female':employee_gender_female,
    }
    return render(request, 'Admin/home.html',context)

@login_required(login_url='/')
def Add_Employee(request):
    designation_list = Designation.objects.all()  # Rename the variable to avoid confusion
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        designation_id = request.POST.get('designation_id')
        gender = request.POST.get('gender')
        print(designation_id)

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "Email Is Already Taken")
            return redirect('add_employeepage')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "Username Is Already Taken")
            return redirect('add_employeepage')
        else:
                user = CustomUser(
                    first_name = first_name,
                    last_name = last_name,
                    username = username,
                    email = email,
                    profile_pic = profile_pic,
                    user_type = 2,
                )
                user.set_password(password)
                user.save()
                
                selected_designation = Designation.objects.get(id=designation_id)
                
                employee = Employee(
                    admin = user,
                    address = address,
                    designation_id = selected_designation,  # Assign the selected designation instance
                    gender = gender,
                )
                employee.save()

                messages.success(request, user.first_name + " " +user.last_name + " are successfully add!!")
                return redirect('add_employeepage')

    context = {
        'designation_list': designation_list,  # Update the context variable name
    }
    return render(request, "Admin/add_employee.html", context)

#fetch all data in employee dashbord
def View_Employee(request):
    employee=Employee.objects.all()
    print(employee)
    context = {
        'employee': employee,  # Update the context variable name
    }
    return render(request, "Admin/view_employee.html",context)

# create function for edit  Employee Records
def Edit_Employee(request,id):
    employee =Employee.objects.filter(id=id)
    designation_list = Designation.objects.all()
    context = {
        'employee' : employee,
        'designation_list': designation_list,


    }
    return render(request,"Admin/edit_employee.html",context)


def Update_Employee(request):
    #get a post request value
    if request.method =="POST":
        employee_id = request.POST.get('employee_id')
        print(employee_id)
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        designation_id = request.POST.get('designation_id')
        gender = request.POST.get('gender')
        # print(profile_pic,first_name,last_name,email,username,password,address,designation_id,gender)
        # this id use for update data
        user=CustomUser.objects.get(id=employee_id)
        # this user.profile_pic = profile_pic use for save data
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        if password != None and password != '':
            user.set_password(password)

        if profile_pic != None and profile_pic != '':
            user.profile_pic = profile_pic
        user.save()

        employee =Employee.objects.get(admin=employee_id)
        employee.address = address
        employee.gender = gender
        designation = Designation.objects.get(id =designation_id)
        employee.designation_id = designation
        employee.save()
        messages.success(request,"Record Are Successfully updated!!")
        return redirect('view_employeepage')

    return render(request,"Admin/edit_employee.html")


def Delete_Employee(request,admin):
    employee =CustomUser.objects.get(id=admin)
    employee.delete()
    messages.success(request,"Record Successfully Delete!!")
    return redirect('view_employeepage')


def Add_Designation(request):
    if request.method == "POST":
        designation_name = request.POST.get('designation_name')
        designation =Designation(
            name = designation_name,
        )
        designation.save()
        messages.success(request, "Designation Are Successfully Created!!")
        return redirect('add_designationpage')
    return render(request, "Admin/add_designation.html")

def View_Designation(request):
    designation =Designation.objects.all()
    context = {
        'designation': designation,
    }

    return render(request, "Admin/view_designation.html",context)


def Edit_Designation(request,id):
    designation = Designation.objects.get(id = id)
    context = {
        'designation': designation,
    }
    return render(request, "Admin/edit_designation.html", context)


def Update_Designation(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        designation_id = request.POST.get('designation_id')
        # use for update
        designation = Designation.objects.get(id=designation_id)
        designation.name = name
        designation.save()
        messages.success(request, "Record Are Successfully Updated!!")
        return redirect('view_designationpage')

    return render(request, "Admin/edit_designation.html")


def Delete_Designation(request, id):
    designation = Designation.objects.get(id=id)
    designation.delete()
    messages.success(request, "Record Successfully Deleted!!")
    return redirect('view_designationpage')


def Add_Session(request):
    if request.method == "POST":
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')
        print (session_year_start,session_year_end)
        session = Session_year(
            session_start = session_year_start,
            session_end  = session_year_end,
        )
        session.save()
        messages.success(request,"Session Are Successfull Add")
        return redirect('add_session')
    return render(request,  "Admin/add_session.html")


def View_Session(request):
    session = Session_year.objects.all()
    context = {
      'session' : session,
    }
    return render(request, 'Admin/view_session.html', context)


def Edit_Session(request, id):
    session = Session_year.objects.filter(id=id)
    context={
            'session': session,
        }
    return render(request, 'Admin/edit_session.html', context)


def Update_Session(request):
    if request.method == "POST":
        session_id = request.POST.get('session_id')
        session_year_start=request.POST.get('session_year_start')
        session_year_end =request.POST.get('session_year_end')

        session = Session_year(
            id = session_id,
            session_start = session_year_start,
            session_end = session_year_end,
        )
        session.save()
        messages.success(request, "Record Has Been Successfully Updated")
        return redirect("view_session")
    return render(request, "Admin/edit_session.html")

def Delete_Session(request,id):
    session = Session_year.objects.get(id=id)
    session.delete()
    messages.success(request, "Record Successfully Deleted!!")
    return redirect('view_session')

def Employee_Send_Notification(request):
    employee = Employee.objects.all()
    #.order_by use for show message serial wise [0:5] use for leatest 5 message show onle
    see_notification =  Employee_Notification.objects.all().order_by('-id')[0:5]
    context = {
        'employee': employee,
        'see_notification':see_notification,
    }
    return render(request,"Admin/employee_notification.html", context)


def Employee_Save_Notification(request):
    if request.method == "POST":
        employee_id = request.POST.get('employee_id')
        message = request.POST.get('message')

        employee = Employee.objects.get(admin=employee_id)
        notification = Employee_Notification(
            employee_id = employee,
            message = message,
        )
        notification.save()
        messages.success(request, "Send Notification Successfully!!")
        return redirect('employee_send_notification')


def Employee_Leave_View(request):
    employee_leave = Employee_leave.objects.all()
    context = {
        'employee_leave': employee_leave,
    }
    return render(request, "Admin/employee_leave.html", context)


def Employee_Approve_leave(request, id):
    leave = Employee_leave.objects.get(id=id)
    leave.status = 1
    leave.save()
    return redirect('leave_view')


def Employee_Disapprove_leave(request,id):
    leave = Employee_leave.objects.get(id=id)
    leave.status = 2
    leave.save()
    return redirect('leave_view')
