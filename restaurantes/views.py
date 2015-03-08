from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from .models import Restaurant
from .forms import RestaurantForm,RestaurantFormEdit


class RestaurantList(ListView):
    model = Restaurant
    template_name = "restaurantes/restaurant_list.html"

class RestaurantCreate(CreateView):
    template_name = "restaurantes/createrestaurant.html"
    form_class = RestaurantForm
    #success_url = reverse_lazy('restaurantlist')

    def post(self, request, *args, **kwargs):
        form = RestaurantForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.username = f.email
            f.set_password(f.password)
            f.save()

            #user = authenticate(username=f.username, nopass=f.password)
            #login(request, user)

            return HttpResponseRedirect('/home/')
        else:
            return render(request,'restaurantes/createrestaurant.html',{'form':form})

class RestaurantUpdate(UpdateView):
    model = Restaurant
    template_name = "restaurantes/updaterestaurant.html"
    form_class = RestaurantFormEdit
    success_url = reverse_lazy('restaurantlist')