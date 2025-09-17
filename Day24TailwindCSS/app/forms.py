from django import forms

class Studentregistration(forms.Form):
    first_name = forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    phone = forms.CharField(min_length=10,max_length=10)

    def clean_phone(self):
        phone=self.cleaned_data['phone']
        
        try:
            int(phone)
        except ValueError:
            raise forms.ValidationError("Phone number muus be numeric")
        if not phone[:2] in ('98','97'):
            raise forms.ValidationError("Phone number must start with 98 or 97")
        
        return phone
    
