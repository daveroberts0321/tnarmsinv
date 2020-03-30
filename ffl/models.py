from django.db import models

# Create your models here.
class FFL(models.Model):

    fflnumber = models.CharField(max_length=50, verbose_name='FFL Number')
    fflexp = models.DateField(default = '1775-11-10', verbose_name='FFL Exp Date xxxx-xx-xx')
    fflimage = models.ImageField(blank = True)
    fflcompanyname = models.CharField(max_length=50, verbose_name='Company Name')
    fflphone = models.CharField(max_length=50,default = 'none', verbose_name='Phone Number')
    fflemail = models.CharField(max_length=50, default = 'none', verbose_name='Email')
    fflcontactname = models.CharField(max_length=50, default = 'none', verbose_name='Contact Name')
    fflmailaddress = models.CharField(max_length=200, verbose_name='Mailing Address')
    notes = models.TextField(blank = True)


    def __str__(self):
        return f'FFL Number: {self.fflnumber}, Company: {self.fflcompanyname}, Exp: {self.fflexp}'

    class Meta:
        verbose_name = 'FFL'
        verbose_name_plural = 'FFLs'