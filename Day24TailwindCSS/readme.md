# Day24 Tailwind CSS

- Install Tailwind

- {% extends 'base.html' %}->more like copy and paste

- {% block content %} {% endblock content %}->makeing block block in base.html and when we extend base.html we can modify the block content.

- components-{% include 'app/components/basic-card.html' with stat=stat %}- small small components


_______________________________________________________________

- request.method
- request.POST
- request.get
- request.POST.get('exactly name define in form')
- return redirect('dashboard'), after form handels its post request , redirect to other page as without it when reloading the page , it will be submit the last hold form data

----------------------------------------------------------
## Django Forms
- create forms.py
- import form of form.py
- use it/call the class form=studentregistartion()
- use validation/cleaning method 

----------------------------------------------------------

- create modeles in model.py 
- use that in forms.py with forms.modelform 
- use wigits and cleaning 
- use that form in views 
- use that context in html page

---------------------------------------------------------

#  Pratice OrM in Shell/address is model/class name

## get all data

- address = address.objects.all() &#8629; <!-- ↵ -->
- address &#8629; <!-- ↵ -->

## Add new data in DB

- new_address=Address(name="Biratnagar") &#8629; <!-- ↵ -->
- new_address &#8629; <!-- ↵ -->
- new_address.save() &#8629; <!-- ↵ -->
- verify in DB

## Add new data in DB in sinlge step 

- address.objects.create("Chitwan) &#8629; <!-- ↵ -->

## Access via PK or ID

- ktm=address.objects.get(pk=1)/(id=1) &#8629; <!-- ↵ -->
- ktm &#8629; <!-- ↵ -->

## Get first and last item.

- new_address=address.object.get(last) &#8629; <!-- ↵ -->
- new_address &#8629; <!-- ↵ -->

## Update in DB

- ktm = address.object.get(last) &#8629; <!-- ↵ -->
- ktm &#8629; <!-- ↵ -->
- ktm.name = "New Kathmandu" &#8629; <!-- ↵ -->
- ktm.save()


