from django import forms
from django.forms import ModelForm
from .models import Customer,ServiceStation,Service
from django.contrib.auth import get_user_model

#for User model
User = get_user_model

#CustomerRegistration form
class CustomerRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())

#CustomerInfo form
class CustomerInfoForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.TextInput())
    cust_phone = forms.CharField(widget=forms.TextInput(),label='PhoneNumber')
    address = forms.CharField(widget=forms.Textarea(),label='Address')

#ServiceStationRegistration form
class ServiceStationRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())

#ServiceStationInfo form
class ServiceStationInfoForm(forms.Form):
    station_name = forms.CharField(widget=forms.TextInput(), label='ServiceCenter Name')
    email = forms.CharField(widget=forms.TextInput())
    ss_phone = forms.CharField(widget=forms.TextInput(),label='PhoneNumber')
    address = forms.CharField(widget=forms.Textarea(),label='Address')

# CustomerLogin form
class CustomerLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

#ServiceStationLogin form
class ServiceStationLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

#Booking form
class VBooking(forms.Form):
    choice = (('Car','Car'),('Bike','Bike'),('Scooter','Scooter'))
    schoice = (('Wash','Wash'),('Denting','Denting'),('Full Service','Full Service'))
    vehicle_reg_no = forms.CharField(widget=forms.TextInput())
    vehicle_name = forms.CharField(widget=forms.TextInput())
    vehicle_type = forms.CharField(widget=forms.TextInput())
    type_of_service = forms.CharField(widget=forms.TextInput())
    service_desc = forms.CharField(widget=forms.Textarea())





