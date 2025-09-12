from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('create_task/',views.create_task,name='create_task'),
    # path('school/',views.school,name='school',name='school'),
    path('school/',views.SchoolView.as_view(),name='school'),   
    path('school/<pk>/view/',views.school_detail.as_view(),name='school_detail'),
    path('school/create/',views.school_create.as_view(),name='school_create'),
    path('school/<pk>/update/',views.School_Update.as_view(),name='school_update'),
    path('school/<pk>/delete/',views.School_Delete.as_view(),name='school_delete'),
    ]