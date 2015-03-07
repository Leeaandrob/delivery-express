from django.shortcuts import render
from django.views.generic import ListView

from .models import Food

class FoodList(ListView):
    model = Food
    template_name = "comidas/foodlist.html"
