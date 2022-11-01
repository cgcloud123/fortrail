
from wsgiref import validate
from django import forms
from .models import Userdetails


class CustForm(forms.ModelForm):
    name = forms.CharField(max_length=500,label='', widget=forms.TextInput(attrs={'placeholder':'Full Name*','size': '10', 'class':'form-control no-border'}))
    email = forms.CharField(max_length=500,label='', widget=forms.EmailInput(attrs={'placeholder':'Email*','size': '10','class':'form-control no-border'}))
    contact_no = forms.CharField(label='', widget=forms.NumberInput(attrs={'placeholder':'Contact No*','size': '10','class':'form-control no-border'}))
    description = forms.CharField(max_length=500,label='', widget=forms.TextInput(attrs={'placeholder':'Description*','size': '10','class':'form-control no-border'}))

    class Meta:
        model = Userdetails
        fields = "__all__"
      
    # this function will be used for the validation
    def clean(self):
 
        super(CustForm, self).clean()

        contact_no = self.cleaned_data.get('contact_no')
        
        if len(contact_no) >10 or len(contact_no) <10:
            self._errors['contact_no'] = self.error_class([
                'Contact Number must be in 10 digit'])

        
        return self.cleaned_data        

   