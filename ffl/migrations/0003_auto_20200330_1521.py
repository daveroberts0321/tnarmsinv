# Generated by Django 3.0.3 on 2020-03-30 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ffl', '0002_auto_20200330_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ffl',
            name='fflexp',
            field=models.DateField(default='1775-11-10', verbose_name='FFL Exp Date xxxx-xx-xx'),
        ),
    ]
