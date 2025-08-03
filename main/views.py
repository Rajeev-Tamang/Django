from django.shortcuts import render , redirect
from django.http import HttpResponse 
from .models import Task
# tasks =[
#             {
#                 "title": "This is our task1 title",
#                  "des": "This is task1 des"
#             },
#             {
#                 "title": "This is our task 2 title", 
#                 "des" : "This is the task 2 desc"
#             }
#         ]


def home(request):
    # print("This is a home page")
    # return HttpResponse("<h1>Welcome to the home page</h1>")
    return render(request, "main/home.html")

def contact(request):
    pass
    return HttpResponse("<p>This is a contact page</p>")
def about(request):
    #if hamlai variable send garnu xa vanhe
    user_name = "User1"
    context = {"user" : user_name} # context data banhaunu parne hunxa & context must be dict 
    return render(request, "main/about.html",context)

def task(request):
    # task =[
    #             {
    #                 "title": "This is our task1 title",
    #                 "des": "This is task1 des"
    #             },
    #             {
    #                 "title": "This is our task 2 title", 
    #                 "des" : "This is the task 2 desc"
    #             }
    #         ]
    # global tasks
    tasks=Task.objects.all()    
    context = {
       
        "task" : tasks  
       
    }
    return render(request,"main/task.html",context)

def createTask(request):
    if request.method=="POST":
        data = request.POST
        task_title = data.get("title")
        task_decs = data.get("des")
        # new_task= {"title":task_title, "des":task_decs}
        # global tasks
        # tasks.append(new_task)
        Task.objects.create(title=task_title,des=task_decs)

        return redirect(task)
    return render(request,"main/create_task.html")

# def pic(request):
#     redirect ("/media/student_profile")