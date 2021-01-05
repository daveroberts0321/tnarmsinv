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
    ('TAC9EJT', 'TAC9EJT'),
    ('SERNUM', 'SERNUM')
    )

COLOR = (
    ('BLK', "BLK"),
    ('FDE', 'FDE'),
    ('STEALTH', 'STEALTH'),
    ('OD', 'OD'),
    ('RIFLE', 'RIFLE'),
    ('CLEAR', 'CLEAR'),
    ('PINK', 'PINK'), 
    ('Other', "Other")
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
    od80 = models.CharField(max_length=50, default=0)
    blemblack80 = models.CharField(max_length=50)
    blemfde80 = models.CharField(max_length=50)
    blemstealth80 = models.CharField(max_length=50)
    blemrifle80 = models.CharField(max_length=50,default=0, verbose_name="Blem Rifle 80") 
    blemod80= models.CharField(max_length=50,default=0, verbose_name="Blem OD 80")
    blk980 = models.CharField(max_length=50,default=0, verbose_name="Black TAC-980")
    fde980 =models.CharField(max_length=50,default=0, verbose_name="FDE TAC980")
    od980 =models.CharField(max_length=50,default=0, verbose_name="OD TAC-980")
    rif980 =models.CharField(max_length=50,default=0, verbose_name="Rifle TAC-980")
    stl980 =models.CharField(max_length=50,default=0, verbose_name="Stealth TAC-980")
    blemblk980=models.CharField(max_length=50,default=0, verbose_name="Blem Blk TAC-980")
    blemfde980=models.CharField(max_length=50,default=0, verbose_name="Blem FDE TAC-980")
    blemod980=models.CharField(max_length=50,default=0, verbose_name="Blem OD TAC-980")
    blemrif980=models.CharField(max_length=50,default=0, verbose_name="Blem Rifle TAC-980")
    blemstl980=models.CharField(max_length=50,default=0, verbose_name="Blem Stealth TAC-980")
    blk3080=models.CharField(max_length=50,default=0, verbose_name="Black AR3080")
    fde3080=models.CharField(max_length=50,default=0, verbose_name="FDE AR3080")
    od3080=models.CharField(max_length=50,default=0, verbose_name="OD Ar3080")
    rif3080=models.CharField(max_length=50,default=0, verbose_name="Rifle AR3080")
    stl3080=models.CharField(max_length=50,default=0, verbose_name="Stealth AR3080")
    jig3080=models.CharField(max_length=50,default=0, verbose_name="Jig AR3080")
    blemblk3080=models.CharField(max_length=50,default=0, verbose_name="Blem Black AR3080")
    blemfde3080=models.CharField(max_length=50,default=0, verbose_name="Blem FDE AR3080")
    blemod3080=models.CharField(max_length=50,default=0, verbose_name="Blem OD AR3080")
    blemrif3080=models.CharField(max_length=50,default=0, verbose_name="Blem Rifle AR3080")
    blemstl3080=models.CharField(max_length=50,default=0, verbose_name="Blem Stealth AR3080")

    
    notes = models.TextField()


    def get_absolute_url(self):
        return reverse('inventory-detail', kwargs={'pk': self.pk})      

    def __str__(self):
        return f'Ar15Blk: {self.ar15black} '
class AddInventory(models.Model):
    '''Used to adaa inventory as a running total'''
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
    blemrifle80 = models.CharField(max_length=50,default=0, verbose_name="Blem Rifle 80")  
    blk980 = models.CharField(max_length=50,default=0, verbose_name="Black TAC-980")
    fde980 =models.CharField(max_length=50,default=0, verbose_name="FDE TAC980")
    od980 =models.CharField(max_length=50,default=0, verbose_name="OD TAC-980")
    rif980 =models.CharField(max_length=50,default=0, verbose_name="Rifle TAC-980")
    stl980 =models.CharField(max_length=50,default=0, verbose_name="Stealth TAC-980")
    blemblk980=models.CharField(max_length=50,default=0, verbose_name="Blem Blk TAC-980")
    blemfde980=models.CharField(max_length=50,default=0, verbose_name="Blem FDE TAC-980")
    blemod980=models.CharField(max_length=50,default=0, verbose_name="Blem OD TAC-980")
    blemrif980=models.CharField(max_length=50,default=0, verbose_name="Blem Rifle TAC-980")
    blemstl980=models.CharField(max_length=50,default=0, verbose_name="Blem Stealth TAC-980")
    blk3080=models.CharField(max_length=50,default=0, verbose_name="Black AR3080")
    fde3080=models.CharField(max_length=50,default=0, verbose_name="FDE AR3080")
    od3080=models.CharField(max_length=50,default=0, verbose_name="OD Ar3080")
    rif3080=models.CharField(max_length=50,default=0, verbose_name="Rifle AR3080")
    stl3080=models.CharField(max_length=50,default=0, verbose_name="Stealth AR3080")
    jig3080=models.CharField(max_length=50,default=0, verbose_name="Jig AR3080")
    blemblk3080=models.CharField(max_length=50,default=0, verbose_name="Blem Black AR3080")
    blemfde3080=models.CharField(max_length=50,default=0, verbose_name="Blem FDE AR3080")
    blemod3080=models.CharField(max_length=50,default=0, verbose_name="Blem OD AR3080")
    blemrif3080=models.CharField(max_length=50,default=0, verbose_name="Blem Rifle AR3080")
    blemstl3080=models.CharField(max_length=50,default=0, verbose_name="Blem Stealth AR3080")
class Orders(models.Model):
    '''purchase orders and consumables list'''
    
    orderamount = models.PositiveIntegerField()
    purchase_order_num = models.CharField(max_length=50, default = 000)
    supplier = models.CharField(max_length = 50, blank = True)
    typemodel = models.CharField(max_length=50, default = '80', choices = TYPE)
    color = models.CharField(max_length=50, choices = COLOR, default = 'BLK')
    date = models.DateTimeField(default = timezone.now)
    notes = models.TextField(default = "none")
    
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
    AR308_Buffer_Assembly = models.CharField(default = 0, max_length = 10, verbose_name="AR308 Rifle Buffer")
    pb15=models.CharField(default = 0, max_length = 10, verbose_name="AR15 Pistol Buffer")
    shock15=models.CharField(default = 0, max_length = 10, verbose_name="AR15 Shockwave Pistol Assembly")
    sb15=models.CharField(default = 0, max_length = 10, verbose_name="AR15 Sb Tactical Assembly")
    pb9=models.CharField(default = 0, max_length = 10, verbose_name="TAC9 Pistol Buffer")
    shock9=models.CharField(default = 0, max_length = 10, verbose_name="TAC9 Shockwave Assembly")
    bubble9=models.CharField(default = 0, max_length = 10, verbose_name="TAC9 Bubble Tube")
    sb9=models.CharField(default = 0, max_length = 10, verbose_name="TAC9 SB Tactical Assembly")
    jig308=models.CharField(default = 0, max_length = 10, verbose_name="AR3080 Jig")
    consumablesnotes = models.TextField(blank = True)
    
    
    

    def get_absolute_url(self):
        return reverse('orders-detail', kwargs={'pk': self.pk}) 

    

    def __str__(self):
        return f" Big Brass{self.bigbrass} Little Brass: {self.littlebrass}, Ser#: {self.serialnum}, Tac9 Arm: {self.tac9arm}"  

class Supplier(models.Model):
    '''suppliers of consumables and regular items'''
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    goodsupplied = models.CharField(max_length=50)
    currentprice = models.CharField(max_length=50)
    note = models.TextField()
    

    def __str__(self):
        return f'Name: {self.name}, Email: {self.email}, Supplied: {self.goodsupplied}'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

class AvailableInventory(models.Model):
    ''' all Available Inventory serialized and nonserialized inventory by color and type'''
    ar15black = models.CharField(max_length=50, default= "00/00")
    ar15fde = models.CharField(max_length=50, default= "00/00")
    ar15od = models.CharField(max_length=50, default= "00/00")
    ar15rifle = models.CharField(max_length=50, default= "00/00")
    ar15stealth = models.CharField(max_length=50, default= "00/00")
    ar15clear = models.CharField(max_length=50, default= "00/00")
    ar15pink = models.CharField(max_length=50, default= "00/00")
    blemar15black = models.CharField(max_length=50, default= "00/00")
    blemar15fde = models.CharField(max_length=50, default= "00/00")
    blemar15od = models.CharField(max_length=50, default= "00/00")
    blemar15rifle = models.CharField(max_length=50, default= "00/00")
    blemar15stealth = models.CharField(max_length=50, default= "00/00")
    blemar15clear = models.CharField(max_length=50, default= "00/00")
    blemar15pink = models.CharField(max_length=50, default= "00/00")
    ar308black = models.CharField(max_length=50, default= "00/00")
    ar308fde = models.CharField(max_length=50, default= "00/00")
    ar308od = models.CharField(max_length=50, default= "00/00")
    ar308rifle = models.CharField(max_length=50, default= "00/00")
    ar308stealth = models.CharField(max_length=50, default= "00/00")
    ar308pink = models.CharField(max_length=50, default= "00/00")
    blemar308black = models.CharField(max_length=50, default= "00/00")
    blemar308fde = models.CharField(max_length=50, default= "00/00")
    blemar308od = models.CharField(max_length=50, default= "00/00")
    blemar308rifle = models.CharField(max_length=50, default= "00/00")
    blemar308stealth = models.CharField(max_length=50, default= "00/00")
    blemar308pink = models.CharField(max_length=50, default= "00/00")
    tac9black = models.CharField(max_length=50, default= "00/00")
    tac9fde = models.CharField(max_length=50, default= "00/00")
    tac9od = models.CharField(max_length=50, default= "00/00")
    tac9rifle = models.CharField(max_length=50, default= "00/00")
    tac9stealth = models.CharField(max_length=50, default= "00/00")
    tac9pink = models.CharField(max_length=50, default= "00/00")
    blemtac9black = models.CharField(max_length=50, default= "00/00")
    blemtac9fde = models.CharField(max_length=50, default= "00/00")
    blemtac9od = models.CharField(max_length=50, default= "00/00")
    blemtac9rifle = models.CharField(max_length=50, default= "00/00")
    blemtac9stealth = models.CharField(max_length=50, default= "00/00")
    blemtac9pink = models.CharField(max_length=50, default= "00/00")
    black80 = models.CharField(max_length=50, default= "00/00")
    stealth80 = models.CharField(max_length=50, default= "00/00")
    fde80 = models.CharField(max_length=50, default="00/00")
    rifle80 = models.CharField(max_length=50, default= "00/00")
    jig80 = models.CharField(max_length=50, default="00/00")
    blemblack80 = models.CharField(max_length=50, default= "00/00")
    blemfde80 = models.CharField(max_length=50, default= "00/00")
    blemstealth80 = models.CharField(max_length=50, default= "00/00")
    blemrifle80 = models.CharField(max_length=50, default= "00/00")
    #TAC980 and AR3080
    blk980 = models.CharField(max_length=50, default= "00/00")
    fde980 = models.CharField(max_length=50, default= "00/00")
    od980 = models.CharField(max_length=50, default= "00/00")
    rif980 = models.CharField(max_length=50, default= "00/00")
    stl980 = models.CharField(max_length=50, default= "00/00")
    blkar3080 = models.CharField(max_length=50, default= "00/00")
    fdear3080 = models.CharField(max_length=50, default= "00/00")
    odar3080 = models.CharField(max_length=50, default= "00/00")
    rifar3080 = models.CharField(max_length=50, default= "00/00")
    stlar3080 = models.CharField(max_length=50, default= "00/00")
    
    notes = models.TextField()


    def get_absolute_url(self):
        return reverse('inventory-detail', kwargs={'pk': self.pk})      

    def __str__(self):
        return f'Ar15Blk: {self.ar15black} '