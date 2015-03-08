#coding: utf-8
from mock import Mock
from django.test import TestCase
from django.test.client import RequestFactory, Client
from django.views.generic import ListView

from restaurantes.views import RestaurantList
from restaurantes.models import Restaurant

class RestaurantListTest(TestCase):

    def setUp(self):
        self.request = RequestFactory()

    def test_template_used(self):
        self.assertEqual(RestaurantList.template_name,
                         'restaurantes/restaurant_list.html')

    def test_deve_ser_um_list_view(self):
        self.assertTrue(issubclass(RestaurantList, ListView))

    def test_get(self):
        request = self.request.get('/restaurantes/restaurantlist')
        response = RestaurantList.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_restaurant_context_data_sem_restaurantes(self):
        request = self.request.get('/')
        response = RestaurantList.as_view()(request)
        self.assertFalse(response.context_data['restaurant_list'])

    def test_restaurant_context_data_com_restaurantes(self):
        request = self.request.get('/')
        Restaurant.objects.create(cnpj='Foo')
        response = RestaurantList.as_view()(request)
        resposta = Restaurant.objects.all()
        self.assertEqual(type(response.context_data['restaurant_list']), type(resposta))
        self.assertEqual(response.context_data['restaurant_list'].count(), 1)


