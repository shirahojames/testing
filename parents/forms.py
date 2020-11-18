from django import forms
from django.contrib.auth.models import User
from . import models



class ParentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }


class ParentForm(forms.ModelForm):
    #this is the extrafield for linking parent and their assigend doctor
    #this will show dropdown __str__ method doctor model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in Doctor model and return it
    #assignedDoctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Name and Department", to_field_name="user_id")
    class Meta:
        model=models.Parent
        fields=['address','mobile','status','profile_pic']

class DateInput(forms.DateInput):
    input_type='date'

class AddChildForm(forms.ModelForm):
    class Meta:
        model=models.Child
        fields=['first_name','last_name','date_of_birth','age']
        widgets = {
        'date_of_birth': DateInput()
        }

class DateInput(forms.DateInput):
    input_type='date'
