from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf .urls.static import static
from . import views,Admin_Views,Employee_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name="basepage"),
    path('', views.Login, name="login_page"),
    # path('', views.Login, name="login_page"),
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

    path('Admin/Add/Session', Admin_Views.Add_Session , name = "add_session"),
    path('Admin/View/Session', Admin_Views.View_Session , name = "view_session"),
    path('Admin/Edit/Session/<str:id>',Admin_Views.Edit_Session, name="edit_session"),
    path('Admin/Update/Session' ,Admin_Views.Update_Session, name="update_session"),
    path('Admin/Delete/Session/<int:id>/', Admin_Views.Delete_Session, name="delete_session"),

    path('Admin/Employee/Send_Notification', Admin_Views.Employee_Send_Notification, name= "employee_send_notification"),
    path('Admin/Employee/Save_Notification', Admin_Views.Employee_Save_Notification, name= "employee_save_notification"),
    path('Admin/Leave_View', Admin_Views.Employee_Leave_View, name="leave_view"),
    path('Admin/Employee_approve_leave/<str:id>', Admin_Views.Employee_Approve_leave,name="approve_leave"),
    path('Admin/Employee_disapprove_leave/<str:id>', Admin_Views.Employee_Disapprove_leave, name="disapprove_leave"),
    path('Admin/Attendance_View', Admin_Views.Admin_Attendance_View, name="attendance_view"),

    #Middleware urls
    path('redirecttohome', views.redirectToHome, name="redirectToHome_page"),

    #Employee Ur̥ls
    path('Employee/home',Employee_Views.Home, name="employee/homepage"),
    path('Employee/Notification', Employee_Views.Notification, name="notification"),
    path('Employee/mark_as_done/<str:status>/', Employee_Views.Mark_As_Done, name="mark_as_done"),
    path('Employee/employee_leave',Employee_Views.Employee_Leave, name="apply_leave" ),
    path('Emplyee/employee_save_leave', Employee_Views.Employee_Save_Leave, name="employee_leave_save"),
    path('Employee/Attendance/Sheet', Employee_Views.Attendance_Sheet, name="attendance_sheet"),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)