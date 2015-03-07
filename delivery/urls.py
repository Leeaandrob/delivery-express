#coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

from comidas.views import FoodList

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='delivery/base.html'), name = 'base'),
    url(r'comidas/', include('comidas.urls')),
)
