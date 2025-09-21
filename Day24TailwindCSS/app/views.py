from django.shortcuts import render,redirect
from .forms import Studentregistration,studentReg
# Create your views here.

def dashboard(request):
    
    # stats = {
    #     'Total Students': 1250,
    #     'Total Payments': "Rs. 300000",
    #     'Pending Payments': "Rs. 55000",
    #     'Active Classes': 34
    # }
    
    stats = [
        {
            'title': 'Total Students',
            'value': 1250,
            'text_color':"text-primary"
        },
        {
            'title': 'Total Payments',
            'value': "Rs. 300000",
            'text_color':"text-green-600"
        },
        {
            'title': 'Pending Payments',
            'value': "Rs. 55000",
            'text_color':"text-red-600"
        },
        {
            'title': 'Active classes',
            'value': 34,
            'text_color':"text-secondary"
        },
        
        {
            'title': 'Total Students',
            'value': 34000,
            'text_color':"text-primary"
        },
        
    ]
    
    context = {
        'stats':stats
    }
        
    return render(request, "app/dashboard.html", context)
#def register(request):
#     print(f"...........{request.method}...........")
#     if request.method == 'POST':
#         print(f"-----{request.POST}-------") 
#         # lets get the data of form to process
#         user_data={
#             'firtsname':request.POST.get('first_name'),
#             'lastname':request.POST.get('last_name'),
#             "address":request.POST.get('address'),
#             "phone":request.POST.get('phone'),
#         }
#         print(f"-----{user_data}-------")
#         firstname=request.POST.get('first_name')
#         lastname=request.POST.get('last_name')
#         address=request.POST.get('address')
#         phone=request.POST.get('phone')
#         print(f"""
#                 name = {firstname} {lastname}
#                 address = {address}
#                 phone = {phone}

#                 """)
#         errors = {}
#         if not len(phone) == 10:
#             errors['phone'] = 'The phone number must be exactly 10 digits number'

#         if len(errors.keys())>0:
#             form_data={
#                 'first_name' : firstname,
#                 'last_name': lastname,
#                 'address' : address,
#                 'phone' : phone,
                
#             }
#             context = {
#                 'form_data':form_data,
#                 'errors':errors
#             }
#             return render(request, "app/register.html",context) 

#             print(errors)
#         return redirect ("dashboard")
#     return render(request, "app/register.html") 
# def register(request):
    # if request.method == 'POST':
    #     first_name=request.POST.get('first_name')
    #     last_name=request.POST.get('last_name')
    #     address=request.POST.get('address')
    #     phone=request.POST.get('phone')
    #     print('name: ',first_name,last_name)
    #     print('adress: ',address)
    #     print('phone: ',phone)
    #     form = Studentregistration(request.POST)
    #     if not form.is_valid():
    #         context={
    #             'form':form
    #         }
    #         return render(request,'app/register.html',context)
    #     return redirect('dashboard')

    # form = Studentregistration()
    # context={
    #     'form':form
    # }
    # return render(request,'app/register.html',context)


def register(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        print('name: ',first_name,last_name)
        print('adress: ',address)
        print('phone: ',phone)
        form = studentReg(request.POST)
        if not form.is_valid():
            context={
                'form':form
            }
            return render(request,'app/register.html',context)
        form.save() #save the user
        return redirect('dashboard')

    form = studentReg()
    context={
        'form':form
    }
    return render(request,'app/register.html',context)