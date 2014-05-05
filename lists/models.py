from django.db import models

# Create your models here.



class List(models.Model):
    pass


class Item(models.Model):
    #blank=True or blank=Flase 
    #if blank=Flase with is by deault , you can not save blank data
    text = models.TextField(default='',blank=False)
    list = models.ForeignKey(List,default=None)
    
    