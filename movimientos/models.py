from django.db import models
from django.utils import timezone


class Register(models.Model):
    descriptions =models.CharField(max_length=120,null=True, blank=True)
    income= models.FloatField(max_length=30,null=True, blank=True) 
    expenses = models.FloatField(max_length=30 ,null=True, blank=True)
    balance= models.FloatField(max_length=30 ,null=True, blank=True)
    date = models.DateField(default=timezone.now)
    totall = models.FloatField(max_length=30 ,null=True, blank=True)
 
    def __str__(self):
        return self.date, self.descriptions, self.incomes ,delf.email, self.telefono
       
            
           