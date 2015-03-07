#coding: utf-8
from django.conf.urls import patterns, include, url

from .views import FoodList, FoodCreate

urlpatterns = patterns('',
    url(r'^$', FoodList.as_view(), name='foodlist'),
    url(r'^createfood/$', FoodCreate.as_view(), name='createfood'),
)
