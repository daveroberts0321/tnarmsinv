# Generated by Django 3.0.3 on 2020-07-20 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_delete_plot'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ar15black', models.CharField(default='00/00', max_length=50)),
                ('ar15fde', models.CharField(default='00/00', max_length=50)),
                ('ar15od', models.CharField(default='00/00', max_length=50)),
                ('ar15rifle', models.CharField(default='00/00', max_length=50)),
                ('ar15stealth', models.CharField(default='00/00', max_length=50)),
                ('ar15clear', models.CharField(default='00/00', max_length=50)),
                ('ar15pink', models.CharField(default='00/00', max_length=50)),
                ('blemar15black', models.CharField(default='00/00', max_length=50)),
                ('blemar15fde', models.CharField(default='00/00', max_length=50)),
                ('blemar15od', models.CharField(default='00/00', max_length=50)),
                ('blemar15rifle', models.CharField(default='00/00', max_length=50)),
                ('blemar15stealth', models.CharField(default='00/00', max_length=50)),
                ('blemar15clear', models.CharField(default='00/00', max_length=50)),
                ('blemar15pink', models.CharField(default='00/00', max_length=50)),
                ('ar308black', models.CharField(default='00/00', max_length=50)),
                ('ar308fde', models.CharField(default='00/00', max_length=50)),
                ('ar308od', models.CharField(default='00/00', max_length=50)),
                ('ar308rifle', models.CharField(default='00/00', max_length=50)),
                ('ar308stealth', models.CharField(default='00/00', max_length=50)),
                ('ar308pink', models.CharField(default='00/00', max_length=50)),
                ('blemar308black', models.CharField(default='00/00', max_length=50)),
                ('blemar308fde', models.CharField(default='00/00', max_length=50)),
                ('blemar308od', models.CharField(default='00/00', max_length=50)),
                ('blemar308rifle', models.CharField(default='00/00', max_length=50)),
                ('blemar308stealth', models.CharField(default='00/00', max_length=50)),
                ('blemar308pink', models.CharField(default='00/00', max_length=50)),
                ('tac9black', models.CharField(default='00/00', max_length=50)),
                ('tac9fde', models.CharField(default='00/00', max_length=50)),
                ('tac9od', models.CharField(default='00/00', max_length=50)),
                ('tac9rifle', models.CharField(default='00/00', max_length=50)),
                ('tac9stealth', models.CharField(default='00/00', max_length=50)),
                ('tac9pink', models.CharField(default='00/00', max_length=50)),
                ('blemtac9black', models.CharField(default='00/00', max_length=50)),
                ('blemtac9fde', models.CharField(default='00/00', max_length=50)),
                ('blemtac9od', models.CharField(default='00/00', max_length=50)),
                ('blemtac9rifle', models.CharField(default='00/00', max_length=50)),
                ('blemtac9stealth', models.CharField(default='00/00', max_length=50)),
                ('blemtac9pink', models.CharField(default='00/00', max_length=50)),
                ('black80', models.CharField(default='00/00', max_length=50)),
                ('stealth80', models.CharField(default='00/00', max_length=50)),
                ('rifle80', models.CharField(default='00/00', max_length=50)),
                ('blemblack80', models.CharField(default='00/00', max_length=50)),
                ('blemfde80', models.CharField(default='00/00', max_length=50)),
                ('blemstealth80', models.CharField(default='00/00', max_length=50)),
                ('blemrifle80', models.CharField(default='00/00', max_length=50)),
                ('notes', models.TextField()),
            ],
        ),
    ]
