# Generated by Django 3.0.3 on 2020-07-21 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_availableinventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='availableinventory',
            name='fde80',
            field=models.CharField(default='00/00', max_length=50),
        ),
    ]
