from django.db import models
from datetime import datetime, date


# Create your models here.
class CustomerOrder(models.Model):
    '''customer orders updated from Google Sheets populated from Big Commerce '''


    ordernumber = models.CharField(max_length = 25, unique = True, verbose_name='Order Number')
    lastname = models.CharField(max_length=50, verbose_name='Last Name')
    firstname = models.CharField(max_length=50, verbose_name='First Name')
    billingaddress = models.TextField(verbose_name='Billing Address')
    phonenumber = models.CharField(max_length=50, verbose_name='Phone Number')
    email = models.EmailField(verbose_name='Email')
    salestotal = models.CharField(max_length=50, verbose_name='Total Sale')
    orderdate = models.CharField(max_length = 200, verbose_name='Order Date and Time')
    shippingaddress = models.TextField(verbose_name='Shipping Address')
    ffl = models.CharField(max_length=100, blank = True, verbose_name='FFL')
    customernotes = models.TextField(blank = True,null = True,  verbose_name= 'Customer Notes')
    staffnotes = models.TextField(blank = True, null = True, verbose_name='Staff Notes')

    class Meta:
        verbose_name = 'CustomerOrder'
        verbose_name_plural = 'CustomerOrders'
        ordering = ['orderdate', 'ordernumber']



