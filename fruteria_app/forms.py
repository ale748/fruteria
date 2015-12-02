from django import forms
from django.forms import ModelForm, DateInput
from models import Product, Order_item, Order
from registration.forms import RegistrationForm



class UserForm(RegistrationForm):
    class Meta:
        model=RegistrationForm.Meta.model
        fields=RegistrationForm.Meta.fields+('first_name','last_name',)

class NewForm(ModelForm):
    class Meta:
        model = Order_item
        fields = {'product','qty'}