from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    USER =(
        (1, 'Admin'),
        (2,'Employee'),
    )

    user_type =models.CharField(choices=USER,max_length=50,default=1)
    profile_pic=models.ImageField(upload_to='media/profile_pic')

# create class for designation
class Designation(models.Model):
    name= models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Session_year(models.Model):
    session_start = models.CharField(max_length=100)
    session_end = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.session_start} to {self.session_end}"

#craete class for Employee
class Employee(models.Model):
    admin= models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.TextField()
    gender=models.CharField(max_length=100)
    designation_id=models.ForeignKey(Designation,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    # def __init__(self):
        # return self.admin.first_name + " " + self.admin.last_name
    def __str__(self):
        return f"{self.admin.first_name} {self.admin.last_name}"


class Employee_Notification(models.Model):
    employee_id = models.ForeignKey(Employee,on_delete=models.CASCADE)
    message=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.employee_id.admin.first_name

class Employee_leave(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    data = models.CharField(max_length=100)
    message = models.TextField(max_length=100)
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee_id.admin.first_name} {self.employee_id.admin.last_name}"

class Attendance(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    login_time = models.TimeField()
    logout_time = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=10, default='Present')  # Add this line

    def __str__(self):
        return f"{self.employee_id} - {self.date.strftime('%Y-%m-%d')}"


