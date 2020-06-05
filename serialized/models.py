from django.db import models
from django.utils import formats
from django.utils import timezone
from datetime import datetime, date
from qr_code.qrcode.utils import ContactDetail


''' .CSV files will be uploaded using https://medium.com/@simathapa111/how-to-upload-a-csv-file-in-django-3a0d6295f624'''


class Serialized(models.Model):
    """fields for serialized equipment to be used with QR codes. using qr_code: https://django-qr-code.readthedocs.io/en/latest/pages/README.html#usage """
    serialnumber = models.CharField(max_length=20,null=True, default = 'none', verbose_name='Serial Number')
    gunmasterid = models.CharField(max_length=50, null=True, blank = True, verbose_name='Gunmaster ID Number')
    modeltype = models.CharField(max_length=50,null=True, default = 'AR15', verbose_name='Model Type')
    color = models.CharField(max_length=50,null=True, default = 'BLK', verbose_name='Color')
    dateaquired = models.CharField(max_length=15,null=True, default='01-01-2020', verbose_name='Date Aquired')
    datedeposed = models.CharField(max_length=15,null=True, default='01-01-2020', verbose_name='Date Deposed')
    ininventory = models.BooleanField(default = True, null=True, verbose_name='In Inventory')
    ordernumber = models.CharField(max_length=50,null=True, default = '0000', blank = True, verbose_name="Order Number")
    notes = models.TextField(blank = True, null=True, verbose_name='Notes')
    
    class Meta:
        ordering = ['modeltype', 'color']
    
    def __str__(self):
        """Unicode representation of Serialized."""
        return f"In Stock: {self.ininventory},SerNum: {self.serialnumber}, DateAqu: {self.dateaquired}, DateDep: {self.datedeposed}"


    def get_absolute_url(self):
        """Return absolute url for Serialized."""
        return ('')


