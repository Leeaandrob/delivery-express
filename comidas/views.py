from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.core.urlresolvers import reverse, reverse_lazy

from .models import Food

class FoodList(ListView):
    model = Food
    template_name = "comidas/foodlist.html"


class FoodCreate(CreateView):
    model = Food
    template_name = "comidas/createfood.html"
    success_url = reverse_lazy('foodlist')


class FoodUpdate(UpdateView):
    model = Food
    success_url = reverse_lazy('foodlist')


