# Generated by Django 3.0.3 on 2020-03-30 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ffl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ffl',
            name='fflexp',
            field=models.DateField(default='1775/11/10', verbose_name='FFL Exp Date xxxx/xx/xx'),
        ),
    ]
