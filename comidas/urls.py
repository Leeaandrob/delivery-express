#coding: utf-8
from django.conf.urls import patterns, include, url

from .views import FoodList, CreateFood

urlpatterns = patterns('',
    url(r'^$', FoodList.as_view(), name='foodlist'),
    url(r'^createfood/$', CreateFood.as_view(), name='createfood'),
)
