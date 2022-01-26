from django.forms import TextInput
from accounts.models import *
from django import forms
from.models import CustomUser,  Reception1, Reception2, Reception3
# modelフォーム


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['patient_id', 'patient_name', 'last_name', 'first_name', 'birthday',
                  'email', 'email_2', 'tel', 'postal_code', 'address', 'relationship1']


class Reception1Form(forms.ModelForm):
    class Meta:
        model = Reception1
        fields = ['bt1', 'bt2', 'InHospital']


class Reception2Form(forms.ModelForm):
    class Meta:
        model = Reception2
        fields = ['purpose',
                  'accompany', 'companion_last_name',
                  'companion_first_name', 'relationship2', 'bt1', 'bt2', 'InHospital']


class Reception3Form(forms.ModelForm):
    class Meta:
        model = Reception3
        fields = ['OutHospital']
