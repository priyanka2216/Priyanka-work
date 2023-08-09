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




