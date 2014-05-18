from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.



class List(models.Model):
    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])


class Item(models.Model):
    #blank=True or blank=Flase 
    #if blank=Flase with is by deault , you can not save blank data
    text = models.TextField(default='',blank=False)
    list = models.ForeignKey(List,default=None)
    
    class Meta:
        ordering = ('id',)
        unique_together = ('list','text')
    
    def __str__(self):
        return self.text