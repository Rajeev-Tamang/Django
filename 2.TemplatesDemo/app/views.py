from django.shortcuts import render,redirect

# Create your views here.

class demo:
    def __init__(self):
        self.value = "defaut_value"


def home(request):
    # print("this is home page")
    var1 = "this is string variable & to use variable we need to define context, context should be dict"

    users = {"first_name": "Rajeev", "last_name": "Tamang"}
    intrests = ["coding", "learning", "writting"]
    demo_obj=demo()

    context = {
        "variable" : var1,
        "users": users,
        "users_intrests": intrests,
        "demo_obj": demo_obj
    }
    return render(request,"app/home.html",context)

def post(request):
    role = "admin"
    post_data= [
        {
            "title":"Happy Bday",
            "caption": "Many many happy returns of the day",
            "tags":["ram","shyam"]
        },

                {
            "title":"Happy Anniverseiry",
            "caption": "Many many happy Anniverseiry",
            "tags":["nabin","jeshis"]
        },

                {
            "title":"Happy father's day",
            "caption": "Many many happy father's day",
            "tags":["rajeev","dipak"]
        }
    ]

    context= {
        "data": post_data,
        "role": role
    }

    return render(request, "app/post.html", context)