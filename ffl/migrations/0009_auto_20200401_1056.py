# Generated by Django 3.0.3 on 2020-04-01 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ffl', '0008_remove_ffl_fflimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ffl',
            options={'ordering': ['fflstate'], 'verbose_name': 'FFL', 'verbose_name_plural': 'FFLs'},
        ),
        migrations.AddField(
            model_name='ffl',
            name='ffldontship',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ffl',
            name='fflshiptomail',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ffl',
            name='fflcfd',
            field=models.CharField(default='none', max_length=50, verbose_name='CFD'),
        ),
    ]