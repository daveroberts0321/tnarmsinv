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
    ('JIGS', 'JIGS'), 
    ('BRASS', 'BRASS'),
    ('LPK15', 'LPK15'),
    ('LPK308','LPK308'),
    ('TAC9ARM', 'TAC9ARM'),
    ('TAC9BUT', 'TAC9BUT'),
    ('TAC9EJT', 'TAC9EJT')
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
    ar15black = models.CharField(max_length=50)
    ar15fde = models.CharField(max_length=50)
    ar15od = models.CharField(max_length=50)
    ar15rifle = models.CharField(max_length=50)
    ar15stealth = models.CharField(max_length=50)
    ar15clear = models.CharField(max_length=50)
    ar15pink = models.CharField(max_length=50)
    blemar15black = models.CharField(max_length=50)
    blemar15fde = models.CharField(max_length=50)
    blemar15od = models.CharField(max_length=50)
    blemar15rifle = models.CharField(max_length=50)
    blemar15stealth = models.CharField(max_length=50)
    blemar15clear = models.CharField(max_length=50)
    blemar15pink = models.CharField(max_length=50)
    ar308black = models.CharField(max_length=50)
    ar308fde = models.CharField(max_length=50)
    ar308od = models.CharField(max_length=50)
    ar308rifle = models.CharField(max_length=50)
    ar308stealth = models.CharField(max_length=50)
    ar308pink = models.CharField(max_length=50)
    blemar308black = models.CharField(max_length=50)
    blemar308fde = models.CharField(max_length=50)
    blemar308od = models.CharField(max_length=50)
    blemar308rifle = models.CharField(max_length=50)
    blemar308stealth = models.CharField(max_length=50)
    blemar308pink = models.CharField(max_length=50)
    tac9black = models.CharField(max_length=50)
    tac9fde = models.CharField(max_length=50)
    tac9od = models.CharField(max_length=50)
    tac9rifle = models.CharField(max_length=50)
    tac9stealth = models.CharField(max_length=50)
    tac9pink = models.CharField(max_length=50)
    blemtac9black = models.CharField(max_length=50)
    blemtac9fde = models.CharField(max_length=50)
    blemtac9od = models.CharField(max_length=50)
    blemtac9rifle = models.CharField(max_length=50)
    blemtac9stealth = models.CharField(max_length=50)
    blemtac9pink = models.CharField(max_length=50)
    black80 = models.CharField(max_length=50)
    fde80 = models.CharField(max_length=50)
    stealth80 = models.CharField(max_length=50)
    rifle80 = models.CharField(max_length=50)
    blemblack80 = models.CharField(max_length=50)
    blemfde80 = models.CharField(max_length=50)
    blemstealth80 = models.CharField(max_length=50)
    blemrifle80 = models.CharField(max_length=50)
    
    notes = models.TextField()


    def get_absolute_url(self):
        return reverse('inventory-detail', kwargs={'pk': self.pk})      

    def __str__(self):
        return f'Ar15Blk: {self.ar15black} '

class Orders(models.Model):
    '''purchase orders and consumables list'''
    
    orderamount = models.PositiveIntegerField()
    purchase_order_num = models.CharField(max_length=50, default = 000)
    supplier = models.CharField(max_length = 50, blank = True)
    typemodel = models.CharField(max_length=50, default = '80', choices = TYPE)
    color = models.CharField(max_length=50, choices = COLOR, default = 'BLK')
    date = models.DateTimeField(default = timezone.now)
    
    def get_absolute_url(self):
        return reverse('orders-detail', kwargs={'pk': self.pk}) 

    

    def __str__(self):
        return f" {self.date} Model: {self.typemodel}, Color: {self.color}, Amount: {self.orderamount}"     

class Consumables(models.Model):
    '''brass and other consumables'''
    bigbrass = models.CharField(default = 0, max_length = 10)
    littlebrass = models.CharField(default = 0, max_length = 10) 
    serialnum = models.CharField(default = 0, max_length = 10)
    tac9arm = models.CharField(default = 0, max_length = 10)
    tac9button = models.CharField(default = 0, max_length = 10)
    tac9ejector = models.CharField(default = 0, max_length = 10)
    ar15kit = models.CharField(default = 0, max_length = 10)
    AR308kit = models.CharField(default = 0, max_length = 10)
    tac9bufferkit = models.CharField(default = 0, max_length = 50)
    extendedmagrelease = models.CharField(default = 0, max_length = 10)
    jigs = models.CharField(default = 0, max_length = 10)
    drillbits = models.CharField(default = 0, max_length = 10)
    jigscrew = models.CharField(default = 0, max_length = 10)
    pistolgripscrew = models.CharField(default = 0, max_length = 10)
    AR15_Buffer_Assembly = models.CharField(default = 0, max_length = 10)
    AR308_Buffer_Assembly = models.CharField(default = 0, max_length = 10)
    consumablesnotes = models.TextField(blank = True)
    updatedby = models.CharField( max_length = 30, default = 'Amy' , help_text = 'Example: Amy on xx/xx')
    
    

    def get_absolute_url(self):
        return reverse('orders-detail', kwargs={'pk': self.pk}) 

    

    def __str__(self):
        return f" Big Brass{self.bigbrass} Little Brass: {self.littlebrass}, Ser#: {self.sernum}, Tac9 Arm: {self.tac9arm}"  

class Supplier(models.Model):
    '''suppliers of consumables and regular items'''
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    goodsupplied = models.CharField(max_length=50)
    currentprice = models.CharField(max_length=50)
    note = models.TextField()
    updatedby = models.CharField( max_length = 30, default = 'Amy' , help_text = 'Example: Amy on xx/xx')

    def __str__(self):
        return f'Name: {self.name}, Email: {self.email}, Supplied: {self.goodsupplied}'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'