# Generated by Django 3.0.3 on 2020-03-26 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20200326_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='updatedby',
        ),
    ]
