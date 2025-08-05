from django.urls import path 
from .views import *

urlpatterns = [
    path('', home, name="home"),
    # path('contact/'contact)
    path('about/', about),
    path('test/', test.as_view(), name="SchoolList"),
    path('task/', task),
    path('task/create/',createTask),
    # path('school/<int:school_id>/view', school_details)
    # path("SchoolViews",SchoolViews.as_view())
    # path('student_profile/PP.jpg', pic),
    path('test/<pk>/SchoolViews/', test_view.as_view(), name="SchoolDetail"),
    path('create/',  create.as_view(), name="create"),
    path('update/<int:pk>/', update.as_view(), name="update"),
    path('delete/<int:pk>/', delete.as_view(), name="delete")
]