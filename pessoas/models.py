from django.db import models
from django.contrib.auth.models import User,Group

class Person(User):
    name            = models.CharField(max_length=100)
    phone           = models.CharField(max_length=11,blank=True,null=True)
    address         = models.CharField(max_length=30,blank=True,null=True)
    neighborhood    = models.CharField(max_length=20,blank=True,null=True)
    city            = models.CharField(max_length=20,blank=True,null=True)
    state           = models.CharField(max_length=20,blank=True,null=True)