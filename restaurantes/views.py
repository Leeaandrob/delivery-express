from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse, reverse_lazy

from .models import Restaurant
from .forms import RestaurantForm,RestaurantFormEdit


class RestaurantList(ListView):
    model = Restaurant
    template_name = "restaurantes/restaurant_list.html"

class RestaurantCreate(CreateView):
    #model = Restaurant
    template_name = "restaurantes/createrestaurant.html"
    form_class = RestaurantForm
    success_url = reverse_lazy('restaurantlist')

class RestaurantUpdate(UpdateView):
    model = Restaurant
    template_name = "restaurantes/updaterestaurant.html"
    form_class = RestaurantFormEdit
    success_url = reverse_lazy('restaurantlist')