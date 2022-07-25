from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from .models import ATMLogin, OBLogin, savingsLogin,Customer_details

class DateInput(forms.DateInput):
    input_type='date'


class savingsLoginform(forms.ModelForm):
    class Meta:
        model=savingsLogin
        fields='__all__'
        widgets={'birthdate':DateInput()}

    def __init__(self,*args,**kwargs):
        super(savingsLoginform,self).__init__(*args,**kwargs)
        self.fields['nameonpassbook'].widget.attrs['placeholder']='Your name on passbook'
        self.fields['accnumber'].widget.attrs['placeholder']='Your account number'
        self.fields['mobnumber'].widget.attrs['placeholder']='Your Mobile number'

class ATMLoginform(forms.ModelForm):
    class Meta:
        model=ATMLogin
        fields='__all__'
        
    def __init__(self,*args,**kwargs):
        super(ATMLoginform,self).__init__(*args,**kwargs)
        self.fields['ATMnumber'].widget.attrs['placeholder']='Your ATM number'
        self.fields['ATMnumber'].widget.attrs['value']='4321 4321 4321'
        self.fields['mobnum'].widget.attrs['placeholder']='Your mobile number'
        self.fields['mobnum'].widget.attrs['value']='9092248685'

class OBLoginform(forms.ModelForm):
    class Meta:
        model=OBLogin
        fields='__all__'
    def __init__(self,*args,**kwargs):
        super(OBLoginform,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['placeholder']='Enter your username'
        self.fields['password'].widget.attrs['placeholder']='Enter your password'

class Customerform(forms.ModelForm):
    class Meta:
        model=Customer_details
        fields='__all__' 
    def __init__(self,*args,**kwargs):
        super(Customerform,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['placeholder']='Enter your username'
        
        
