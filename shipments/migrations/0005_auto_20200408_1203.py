# Generated by Django 3.0.3 on 2020-04-08 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0004_auto_20200408_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='customernotes',
            field=models.TextField(blank=True, null=True, verbose_name='Customer Notes'),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='staffnotes',
            field=models.TextField(blank=True, null=True, verbose_name='Staff Notes'),
        ),
    ]
