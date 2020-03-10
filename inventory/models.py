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
    ('PINK', 'PINK')
)

class Inventory(models.Model):
    ''' all serialized and nonserialized inventory by color and type'''
    typemodel = models.CharField(max_length=50, choices = TYPE)
    color = models.CharField(max_length=50, choices = COLOR)
    instock = models.IntegerField()
    blem = models.BooleanField(default = False)
    
    def get_absolute_url(self):
        return reverse('inventory-detail', kwargs={'pk': self.pk})      

    def __str__(self):
        return f'{self.typemodel} - {self.color} - {self.instock}'

class Orders(models.Model):
    '''purchase orders and consumables list'''
    
    orderamount = models.PositiveIntegerField()
    purchase_order_num = models.CharField(max_length=50, default = 000)
    typemodel = models.CharField(max_length=50, default = '80', choices = TYPE)
    color = models.CharField(max_length=50, choices = COLOR, default = 'BLK')
    date = models.DateTimeField(default = timezone.now)
    
    def get_absolute_url(self):
        return reverse('orders-detail', kwargs={'pk': self.pk}) 

    

    def __str__(self):
        return f" {self.date} Model: {self.typemodel}, Color: {self.color}, Amount: {self.orderamount}"     

class Consumables(models.Model):
    '''brass and other consumables'''
    bigbrass = models.PositiveIntegerField(default = 0)
    littlebrass = models.PositiveIntegerField(default = 0) 
    serialnum = models.PositiveIntegerField(default = 0)
    tac9arm = models.PositiveIntegerField(default = 0)
    tac9ejector = models.PositiveIntegerField(default = 0)
    ar15kit = models.PositiveIntegerField(default = 0)
    AR308kit = models.PositiveIntegerField(default = 0)
    jigs = models.PositiveIntegerField(default = 0)
    drillbits = models.PositiveIntegerField(default = 0)
    jigscrew = models.PositiveIntegerField(default = 0)
    pistolgripscrew = models.PositiveIntegerField(default = 0)
    AR15_Buffer_Assembly = models.PositiveIntegerField(default = 0)
    AR308_Buffer_Assembly = models.PositiveIntegerField(default = 0)
    consumablesnotes = models.TextField(blank = True)
    
    

    def get_absolute_url(self):
        return reverse('orders-detail', kwargs={'pk': self.pk}) 

    

    def __str__(self):
        return f" Big Brass{self.bigbrass} Little Brass: {self.littlebrass}, Ser#: {self.sernum}, Tac9 Arm: {self.tac9arm}"  

