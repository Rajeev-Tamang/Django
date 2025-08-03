from django.urls import path 
from .views import *

urlpatterns = [
    path('', home),
    # path('contact/'contact)
    path('about/', about),
    path('task/', task),
    path('task/create/',createTask),
    # path('student_profile/PP.jpg', pic),
]