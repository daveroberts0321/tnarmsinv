# Generated by Django 3.0.3 on 2020-03-12 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_auto_20200312_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='notes',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
