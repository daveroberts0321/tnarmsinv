# Generated by Django 3.0.3 on 2020-04-01 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ffl', '0007_auto_20200401_0958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ffl',
            name='fflimage',
        ),
    ]