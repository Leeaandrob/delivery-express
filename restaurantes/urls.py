#coding: utf-8
from django.conf.urls import patterns, include, url

from .views import RestaurantList,RestaurantCreate,RestaurantUpdate

urlpatterns = patterns('',
    url(r'^$', RestaurantList.as_view(), name='restaurantlist'),
    url(r'^createrestaurant/$', RestaurantCreate.as_view(), name='createrestaurant'),
    url(r'^updaterestaurant/(?P<pk>\d+)$', RestaurantUpdate.as_view(), name='updaterestaurant'),
)
