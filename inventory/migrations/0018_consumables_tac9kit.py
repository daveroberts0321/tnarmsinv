# Generated by Django 3.0.3 on 2020-03-19 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0017_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumables',
            name='tac9kit',
            field=models.CharField(default=0, max_length=50),
        ),
    ]