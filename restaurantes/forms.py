# coding: utf-8

from django import forms
from restaurantes.models import Restaurant
from django.core.exceptions import ValidationError

class RestaurantForm(forms.ModelForm):
    password2 = forms.CharField(label='Repita sua senha',error_messages={'required': 'Preenchimento Obrigatório'},)
    class Meta:
        model = Restaurant
        fields = ('name','email','phone','address','neighborhood','city','state','cnpj','foods','password')

class RestaurantFormEdit(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('name','email','phone','address','neighborhood','city','state','cnpj','foods')