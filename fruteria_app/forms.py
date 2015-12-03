from django import forms
from django.forms import ModelForm, DateInput
from models import *
from registration.forms import RegistrationForm



class UserForm(RegistrationForm):
    class Meta:
        model=RegistrationForm.Meta.model
        fields=RegistrationForm.Meta.fields+('first_name','last_name',)

class OrderForm(ModelForm):
    class Meta:
        model = Order_item
        fields = {'product','qty'}

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = {'name','description','price_per_unit','stock','type','unit'}

class TypeForm(ModelForm):
    class Meta:
        model = ProductType
        fields = {'name'}

class UnitTypeForm(ModelForm):
    class Meta:
        model = Unit_Type
        fields = {'name'}
