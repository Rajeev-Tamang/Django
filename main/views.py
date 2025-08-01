from django.shortcuts import render
from django.http import HttpResponse

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
    task =[
            {
                "title": "This is our task1 title",
                 "des": "This is task1 des"
            },
            {
                "title": "This is our task 2 title", 
                "des" : "This is the task 2 desc"
            }
        ]
    
    context = {
       
        "task" : task  
       
    }
    return render(request,"main/task.html",context)

def createTask(request):
    return render(request,"main/create_task.html")