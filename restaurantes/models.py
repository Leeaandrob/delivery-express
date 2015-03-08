from django.db import models
from pessoas.models import Person
from comidas.models import Food

class Restaurant(Person):
    cnpj = models.CharField(max_length=14,blank=True,null=True)
    foods = models.ManyToManyField(Food)

    def __unicode__(self):
        return self.cnpj

