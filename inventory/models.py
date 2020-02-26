import uuid
from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
import datetime


# Create your models here.
TYPE = (
    ('AR15', "AR15"),
    ('AR308', 'AR308'),
    ('TAC9', 'TAC9'),
    ('80', '80'),
    )

COLOR = (
    ('BLK', "BLK"),
    ('FDE', 'FDE'),
    ('STEALTH', 'STEALTH'),
    ('OD', 'OD'),
    ('RIFLE', 'RIFLE'),
    ('CLEAR', 'CLEAR'),
)

class Inventory(models.Model):
    ''' all serialized and nonserialized inventory by color and type'''
    typemodel = models.CharField(max_length=50, choices = TYPE)
    color = models.CharField(max_length=50, choices = COLOR)
    instock = models.PositiveIntegerField()
    blem = models.BooleanField(default = False)
    
    def get_absolute_url(self):
        return reverse('inventory-detail', kwargs={'pk': self.pk})      

    def __str__(self):
        return f'{self.typemodel} - {self.color} - {self.instock}'