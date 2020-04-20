# Generated by Django 3.0.3 on 2020-04-06 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordernumber', models.IntegerField(max_length=20, unique=True, verbose_name='Order Number')),
                ('lastname', models.CharField(max_length=50, verbose_name='Last Name')),
                ('firstname', models.CharField(max_length=50, verbose_name='First Name')),
                ('billingaddress', models.CharField(max_length=200, verbose_name='Billing Address')),
                ('phonenumber', models.CharField(max_length=50, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('salestotal', models.CharField(max_length=50, verbose_name='Total Sale')),
                ('orderdate', models.DateTimeField(verbose_name='Order Date and Time')),
                ('shippingaddress', models.CharField(max_length=200, verbose_name='Shipping Address')),
                ('ffl', models.CharField(blank=True, max_length=100, verbose_name='FFL')),
            ],
            options={
                'verbose_name': 'CustomerOrder',
                'verbose_name_plural': 'CustomerOrders',
                'ordering': ['orderdate', 'ordernumber'],
            },
        ),
    ]