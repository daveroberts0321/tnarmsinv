# Generated by Django 3.0.3 on 2020-04-20 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serialized', '0002_auto_20200402_1348'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='serialized',
            options={'ordering': ['modeltype', 'color']},
        ),
        migrations.AlterField(
            model_name='serialized',
            name='gunmasterid',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
