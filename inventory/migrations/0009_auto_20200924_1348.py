# Generated by Django 3.0.3 on 2020-09-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_availableinventory_jig80'),
    ]

    operations = [
        migrations.AddField(
            model_name='availableinventory',
            name='blk980',
            field=models.CharField(default='00/00', max_length=50),
        ),
        migrations.AddField(
            model_name='availableinventory',
            name='blkar3080',
            field=models.CharField(default='00/00', max_length=50),
        ),
        migrations.AddField(
            model_name='availableinventory',
            name='fde980',
            field=models.CharField(default='00/00', max_length=50),
        ),
        migrations.AddField(
            model_name='availableinventory',
            name='fdear3080',
            field=models.CharField(default='00/00', max_length=50),
        ),
        migrations.AddField(
            model_name='availableinventory',
            name='od980',
            field=models.CharField(default='00/00', max_length=50),
        ),
        migrations.AddField(
            model_name='availableinventory',
            name='odar3080',
            field=models.CharField(default='00/00', max_length=50),
        ),
        migrations.AddField(
            model_name='availableinventory',
            name='rif980',
            field=models.CharField(default='00/00', max_length=50),
        ),
        migrations.AddField(
            model_name='availableinventory',
            name='rifar3080',
            field=models.CharField(default='00/00', max_length=50),
        ),
        migrations.AddField(
            model_name='availableinventory',
            name='stl980',
            field=models.CharField(default='00/00', max_length=50),
        ),
        migrations.AddField(
            model_name='availableinventory',
            name='stlar3080',
            field=models.CharField(default='00/00', max_length=50),
        ),
    ]
