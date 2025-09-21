from django import forms
from .models import studentReg

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
    
class studentReg(forms.ModelForm):
    class Meta:
        model=studentReg
        fields="__all__"
        widgets={
            'first_name': forms.TextInput(attrs={'class':'input', 'placeholder':'eg. John'}),
            'last_name': forms.TextInput(attrs={'placeholder':'eg. Doe','class':'input'}),
            'email': forms.EmailInput(attrs={'placeholder':'eg. 8K9bI@example.com','class':'input'}),
            'address': forms.TextInput(attrs={'placeholder':'eg. kathmandu','class':'input'}),
            'phone': forms.TextInput(attrs={'placeholder':'eg. 98******','class':'input'}), }
    def clean_phone(self):
        phone=self.cleaned_data['phone']
        
        try:
            int(phone)
        except ValueError:
            raise forms.ValidationError("Phone number muus be numeric")
        if not phone[:2] in ('98','97'):
            raise forms.ValidationError("Phone number must start with 98 or 97")
        
        return phone