# Generated by Django 3.0.3 on 2020-03-03 18:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_remove_inventory_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bigbrass', models.PositiveIntegerField()),
                ('littlebrass', models.PositiveIntegerField()),
                ('sernum', models.PositiveIntegerField()),
                ('tac9arm', models.PositiveIntegerField()),
                ('orderamount', models.PositiveIntegerField()),
                ('typemodel', models.CharField(choices=[('AR15', 'AR15'), ('AR308', 'AR308'), ('TAC9', 'TAC9'), ('80', '80')], default='80', max_length=50)),
                ('color', models.CharField(choices=[('BLK', 'BLK'), ('FDE', 'FDE'), ('STEALTH', 'STEALTH'), ('OD', 'OD'), ('RIFLE', 'RIFLE'), ('CLEAR', 'CLEAR')], default='BLK', max_length=50)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
