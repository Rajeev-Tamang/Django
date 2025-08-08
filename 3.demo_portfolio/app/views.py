from django.shortcuts import render, redirect

# Create your views here.

def dashboard(request):
    # stats = {
    #     'Total_Students': 100,
    #     'Total_Payments': 50000,
    #     'pending_payments': 30000,
    #     'Active_Classes': 5000,
    # }

    stats = [
        {
            "title": "Total_Students",
            "value": 100,
            "tex_color":"text-primary"
        },
                {
            "title": "Total_Payments",
            "value": 500000,
            "tex_color":"text-green-600"
        },
          {
            "title": "pending_payments",
            "value": 10000,
            "tex_color":"text-red-600"
        },       
        {
            "title": "Active_Classes",
            "value": 30,
            "tex_color":"text-secondary"
        }
    ]

    context = {
        'stats': stats
    }
    return render(request, 'app/dashboard.html',context)

def students(request):
    return render(request, 'app/students.html')


def students_register(request):

    print("----------------------",request.method,"--------------------------------")

    if request.method == 'POST':
        print(request.POST)
        print(request.POST.get('first_name'))
        print(request.POST.get('last_name'))
        print(request.POST.get('address'))
        print(request.POST.get('contact_no'))

        return redirect('dashboard')    

    return render(request, 'app/students_register.html' )