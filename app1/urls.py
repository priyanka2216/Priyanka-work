from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf .urls.static import static
from . import views,Admin_Views,Employee_Views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name="basepage"),
    path('', views.Login, name="login_page"),
    path('dologin', views.doLogin, name="dologin_page"),
    path('dologout', views.doLogout, name="dologout_page"),

    #profile update
    path('profile/', views.PROFILE, name="profile_page"),
    path('profile/update', views.PROFILE_UPDATE, name="profile_updatepage"),

    #Admin urls
    path('Admin/home',Admin_Views.Home, name="Admin/homepage"),

    path('Admin/Add/Employee',Admin_Views.Add_Employee, name="add_employeepage"),
    path('Admin/Employee/View',Admin_Views.View_Employee, name="view_employeepage"),
    path('Admin/Employee/Edit/<str:id>',Admin_Views.Edit_Employee, name="edit_employeepage"),
    path('Admin/Employee/Update' ,Admin_Views.Update_Employee, name="update_employeepage"),
    path('Admin/Employee/Delete/<str:admin>' ,Admin_Views.Delete_Employee, name="delete_employeepage"),

    path('Admin/Add/Designation',Admin_Views.Add_Designation, name="add_designationpage"),
    path('Admin/View/Designation',Admin_Views.View_Designation, name="view_designationpage"),
    path('Admin/Edit/Designation/<str:id>',Admin_Views.Edit_Designation, name="edit_designationpage"),

    path('Admin/Update/Designation/<int:id>/', Admin_Views.Update_Designation, name="update_designationpage"),
    path('Admin/Delete/Designation/<int:id>/', Admin_Views.Delete_Designation, name="delete_designationpage"),
    #Middleware urls
    path('redirecttohome', views.redirectToHome, name="redirectToHome_page"),

    #Employee Ur̥ls
path('Employee/home',Employee_Views.Home, name="employee/homepage"),




]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)