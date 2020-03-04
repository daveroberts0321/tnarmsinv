# Generated by Django 3.0.3 on 2020-03-03 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bigbrass', models.PositiveIntegerField()),
                ('littlebrass', models.PositiveIntegerField()),
                ('sernum', models.PositiveIntegerField()),
                ('tac9arm', models.PositiveIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='orders',
            name='bigbrass',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='littlebrass',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='sernum',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='tac9arm',
        ),
    ]