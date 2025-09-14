from django.shortcuts import render
class demo:
    def __init__(self):
        self.value='default value'


# Create your views here.
def home(request):
    # Creating Dictionaty
    user= {
        'firstName':'Rajeev',
        'lastName':'Tamang',
        'Address':'Birtanagar',
        }
    # Creating List
    Certificates=['CCNA','CCNP','CCIE']

    #Object
    demo_obj=demo()
    context={
        'cuser':user,
        'Certificates':Certificates,
        'demo_obj':demo_obj
    }
    return render(request,'app/home.html',context)


def posts(request):

    data=[
        {
            'title':'Happy Birthday',
            'wish':'Wishing you the Happiest Bday ',
            'tags':["rajeev","jeshis","nabin"]
         },
            {
            'title':'Happy Dashai',
            'wish':'Wishing you the Happiest Dashai ',
            'tags':["rajeev","jeshis","nabin"]

         }
         ,
            {
            'title':'Happy Tihar',
            'wish':'Wishing you the Happiest Tihar ',
            'tags':["rajeev","jeshis","nabin"]

         }
    ]
    user=" "
    context={
        'data':data,
        'user':user
    }
    return render(request,'app/posts.html',context)