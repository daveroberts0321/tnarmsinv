# Generated by Django 3.0.3 on 2020-04-01 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ffl', '0004_auto_20200331_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ffl',
            name='fflexp',
            field=models.DateField(default='2020-01-01', verbose_name='FFL Exp Date xxxx-xx-xx'),
        ),
    ]