from django.db import models
from django.utils import formats
from django.utils import timezone
from datetime import datetime, date
from qr_code.qrcode.utils import ContactDetail


''' .CSV files will be uploaded using https://medium.com/@simathapa111/how-to-upload-a-csv-file-in-django-3a0d6295f624'''
# Create your models here.
TYPE = (
    ('TNARMS15', "TNARMS15"),
    ('AR308', 'AR308'),
    ('TAC9', 'TAC9')
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

class Serialized(models.Model):
    """fields for serialized equipment to be used with QR codes. using qr_code: https://django-qr-code.readthedocs.io/en/latest/pages/README.html#usage """
    serialnumber = models.CharField(max_length=20,null=True, default = 'none')
    gunmasterid = models.CharField(max_length=50,unique = True, null=True, blank = True)
    modeltype = models.CharField(max_length=50,null=True, default = 'AR15')
    color = models.CharField(max_length=50,null=True, default = 'BLK')
    dateaquired = models.CharField(max_length=15,null=True, default='01-01-2020')
    datedeposed = models.CharField(max_length=15,null=True, default='01-01-2020')
    ininventory = models.BooleanField(default = True, null=True,)
    ordernumber = models.CharField(max_length=50,null=True, default = '0000', blank = True)
    notes = models.TextField(blank = True, null=True,)
    

    
    def __str__(self):
        """Unicode representation of Serialized."""
        return f"In Stock: {self.ininventory},SerNum: {self.serialnumber}, DateAqu: {self.dateaquired}, DateDep: {self.datedeposed}"


    def get_absolute_url(self):
        """Return absolute url for Serialized."""
        return ('')


