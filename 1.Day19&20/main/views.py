from django.shortcuts import render,redirect
from .models import Task,School
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy


task=[
    {"title":"CCNA", "desc":"Cisco certifie Network Asso"},
    {"title":"CCNP", "desc":"Cisco Certification Network Professional"}
]
# Create your views here.
def home(request):
    # global task
    task=Task.objects.all()
    context={
        'task': task
    }
    return render(request,"main/home.html",context)

def create_task(request):
    if request.method=="POST":
        data=request.POST
        print(data)
        Task_title=data.get('title')
        Task_desc=data.get('desc')
        Task.objects.create(title=Task_title,desc=Task_desc)
        return redirect(home)
    return render(request,"main/create_task.html")

# def school(request):
#     print("-------------School detail")


# def school_detail(request, school_id):
#     print("------------------------This is School Page", school_id,"----------------------------")

class SchoolView(ListView):
    model=School

class school_detail(DetailView):
    model=School

class school_create(CreateView):
    model=School
    fields="__all__"
    success_url=reverse_lazy("school")

class School_Update(UpdateView):
    model=School
    fields="__all__"
    success_url=reverse_lazy("school")

class School_Delete(DeleteView):
    model=School
    success_url=reverse_lazy("school")  