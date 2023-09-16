from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from.models import Leave_apply
 
class CustomUserForm(UserCreationForm):
  username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
  email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}))
  password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
  password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password'}))
  class Meta:
    model=User
    fields=['username','email','password1','password2']

class DateInput(forms.DateInput):
   input_type='date'

class Leaveapplication(forms.ModelForm):
  class Meta:
       model=Leave_apply
       fields='__all__'

       widgets={
        'apply_date':DateInput()
       } 

       labels={
          'std_id':"student rollno:",
          'apply_date':"Applying date:",
       }
      