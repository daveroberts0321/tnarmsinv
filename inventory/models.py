import uuid
from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from django.utils import timezone
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

class Orders(models.Model):
    '''purchase orders and consumables list'''
    
    orderamount = models.PositiveIntegerField()
    typemodel = models.CharField(max_length=50, default = '80', choices = TYPE)
    color = models.CharField(max_length=50, choices = COLOR, default = 'BLK')
    date = models.DateTimeField(default = timezone.now)
    
    def get_absolute_url(self):
        return reverse('orders-detail', kwargs={'pk': self.pk}) 

    

    def __str__(self):
        return f" {self.date} Model: {self.typemodel}, Color: {self.color}, Amount: {self.orderamount}"     

class Consumables(models.Model):
    '''brass and other consumables'''
    bigbrass = models.PositiveIntegerField()
    littlebrass = models.PositiveIntegerField() 
    sernum = models.PositiveIntegerField()
    tac9arm = models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse('orders-detail', kwargs={'pk': self.pk}) 

    

    def __str__(self):
        return f" Big Brass{self.bigbrass} Little Brass: {self.littlebrass}, Ser#: {self.sernum}, Tac9 Arm: {self.tac9arm}"  

