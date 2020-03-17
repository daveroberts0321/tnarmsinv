from django.db import models
from datetime import date
from qr_code.qrcode.utils import ContactDetail


''' .CSV files will be uploaded using https://medium.com/@simathapa111/how-to-upload-a-csv-file-in-django-3a0d6295f624'''
# Create your models here.
class Serialized(models.Model):
    """fields for serialized equipment to be used with QR codes. using qr_code: https://django-qr-code.readthedocs.io/en/latest/pages/README.html#usage """
    serialnumber = models.CharField(max_length=20)
    dateaquired = models.DateField( auto_now_add=True)
    datedeposed = models.DateField(blank = True, auto_now_add=False)
    ordernumber = models.CharField(max_length=50, blank = True)
    notes = models.TextField(blank = True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Serialized."""

        verbose_name = 'Serialized'
        verbose_name_plural = 'Serializeds'

    def __str__(self):
        """Unicode representation of Serialized."""
        return f"SerNum: {self.serialnumber}, DateAqu: {self.dateaquired}, DateDep: {self.datedeposed}"

    def save(self):
        """Save method for Serialized."""
        pass

    def get_absolute_url(self):
        """Return absolute url for Serialized."""
        return ('')

    # TODO: Define custom methods here
