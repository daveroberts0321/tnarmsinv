# Generated by Django 3.0.3 on 2020-04-08 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0007_auto_20200408_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='ordernumber',
            field=models.CharField(max_length=25, unique=True, verbose_name='Order Number'),
        ),
    ]
