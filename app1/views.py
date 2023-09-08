from django.shortcuts import render, HttpResponse, redirect
from .EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomUser


def BASE(request):
    return render(request, 'base.html')


def Login(request):
    if request.session.get('is_logged_in'):
        return redirect('Admin/homepage')  # Redirect to the home page if already logged in
    return render(request, 'login.html')


def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(
            request,
            username=request.POST.get('email'),
            password=request.POST.get('password')
        )
        if user is not None:
            login(request, user)
            request.session['is_logged_in'] = True  # Set the session variable to indicate the user is logged in
            user_type = user.user_type
            if user_type == '1':
                return redirect('Admin/homepage')  # Redirect to the home page for admin
            elif user_type == '2':
                return redirect('employee/homepage')
            else:
                messages.error(request, 'Email And Password Are Invalid!!')
                return redirect('login_page')
        else:
            messages.error(request, 'Email And Password Are Invalid!!')
            return redirect('login_page')


def doLogout(request):
    logout(request)
    #request.session.clear()
    return redirect('login_page')


@login_required(login_url='login_page')
def redirectToHome(request):
    return redirect('Admin/homepage')

#Create function for update Profile
def PROFILE(request):
    user = CustomUser.objects.get(id=request.user.id)
    context = {
        "user": user
    }
    return render(request, 'profile.html', context)

#Create function for fetch data in database
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(profile_pic)
        try:
            # this code for get id
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            customuser.profile_pic = profile_pic



            if password != None and password != '':
                customuser.set_password(password)

            if profile_pic != None and profile_pic != '':
                customuser.profile_pic = profile_pic

            customuser.save()
            messages.success(request, "Your Profile Updtaed Successfull")
            return redirect('profile_page')

        except:
            messages.error(request, "Your Profile Updated Filed!!")

    return render(request, 'profile.html')

# *************************************
# from django.shortcuts import render,HttpResponse,redirect
# from .EmailBackEnd import EmailBackEnd
# from django.contrib.auth import authenticate,logout,login
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# # from app1.models import CustomUser
# from .models import CustomUser
#
#
#
# def BASE(request):
#     return render(request,'base.html')
#
# def Login(request):
#     return render(request,'login.html')
#
# def doLogin(request):
#     if request.method == "POST":
#         user = EmailBackEnd.authenticate( request, username=request.POST.get('email'),
#                                          password=request.POST.get('password'))
#         if user != None:
#             login(request, user)
#             user_type = user.user_type
#             if user_type == '1':
#                 return redirect('Admin/home')
#             elif user_type == '2':
#                 return HttpResponse("This is user penel")
#             else:
#                 messages.error(request,'Email And Password Are Invailid!!')
#                 return redirect('login_page')
#
#         else:
#             messages.error(request, 'Email And Password Are Invailid!!')
#             return redirect('login_page')
#
#
# def doLogout(request):
#     logout(request)
#     return render('login_page')
#
#
# def PROFILE(request):
#     user =CustomUser.objects.get(id=request.user.id)
#     context={
#         "user":user
#     }
#     return render(request,'profile.html',context)
#
#
# def PROFILE_UPDATE(request):
#     if request.method =="POST":
#         profile_pic = request.FILES.get('profile.pic')
#         first_name =request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print(profile_pic)
#
#
#         try:
#             # this code for get id
#             customuser =CustomUser.objects.get(id=request.user.id)
#             customuser.first_name= first_name
#             customuser.last_name= last_name
#
#             if password!=None and password!= '':
#                 customuser.set_password(password)
#
#             if password!=None and password!= '':
#                 customuser.profile_pic = profile_pic
#
#             customuser.save()
#             messages.success(request,"Your Profile Updtaed Successfull")
#             return redirect('profile_page')
#
#         except:
#              messages.error(request,"Your Profile Updated Filed!!")
#
#     return render(request,'profile.html')
#
