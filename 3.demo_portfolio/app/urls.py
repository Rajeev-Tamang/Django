from django.urls import path,include
from . import views 

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('students/', views.students, name='students'),
    path('students/register/', views.students_register, name='students_register'),

]
