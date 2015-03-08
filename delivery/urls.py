#coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

from comidas.views import FoodList

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'login/','django.contrib.auth.views.login',{"template_name":"delivery/login.html"},name='login'),
    url(r'logout/','django.contrib.auth.views.logout_then_login',{'login_url': '/'},name='logout'),

    url(r'^$', TemplateView.as_view(template_name='delivery/site.html'), name = 'site'),
    url(r'^home/$', TemplateView.as_view(template_name='delivery/base.html'), name = 'home'),
    url(r'comidas/', include('comidas.urls')),
    url(r'restaurantes/', include('restaurantes.urls')),
)
