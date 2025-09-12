from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('create_task/',views.create_task,name='create_task'),
    # path('school/',views.school,name='school'),
    path('school/',views.SchoolView.as_view()),   
    path('school/<pk>/view/',views.school_detail.as_view(),name='school_detail')
    ]