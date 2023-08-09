from django.shortcuts import render,redirect
def Home(request):
    return render(request, 'Employee/home.html')