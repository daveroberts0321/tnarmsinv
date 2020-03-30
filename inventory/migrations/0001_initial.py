# Generated by Django 3.0.3 on 2020-03-30 20:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bigbrass', models.CharField(default=0, max_length=10)),
                ('littlebrass', models.CharField(default=0, max_length=10)),
                ('serialnum', models.CharField(default=0, max_length=10)),
                ('tac9arm', models.CharField(default=0, max_length=10)),
                ('tac9button', models.CharField(default=0, max_length=10)),
                ('tac9ejector', models.CharField(default=0, max_length=10)),
                ('ar15kit', models.CharField(default=0, max_length=10)),
                ('AR308kit', models.CharField(default=0, max_length=10)),
                ('tac9bufferkit', models.CharField(default=0, max_length=50)),
                ('extendedmagrelease', models.CharField(default=0, max_length=10)),
                ('jigs', models.CharField(default=0, max_length=10)),
                ('drillbits', models.CharField(default=0, max_length=10)),
                ('jigscrew', models.CharField(default=0, max_length=10)),
                ('pistolgripscrew', models.CharField(default=0, max_length=10)),
                ('AR15_Buffer_Assembly', models.CharField(default=0, max_length=10)),
                ('AR308_Buffer_Assembly', models.CharField(default=0, max_length=10)),
                ('consumablesnotes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ar15black', models.CharField(max_length=50)),
                ('ar15fde', models.CharField(max_length=50)),
                ('ar15od', models.CharField(max_length=50)),
                ('ar15rifle', models.CharField(max_length=50)),
                ('ar15stealth', models.CharField(max_length=50)),
                ('ar15clear', models.CharField(max_length=50)),
                ('ar15pink', models.CharField(max_length=50)),
                ('blemar15black', models.CharField(max_length=50)),
                ('blemar15fde', models.CharField(max_length=50)),
                ('blemar15od', models.CharField(max_length=50)),
                ('blemar15rifle', models.CharField(max_length=50)),
                ('blemar15stealth', models.CharField(max_length=50)),
                ('blemar15clear', models.CharField(max_length=50)),
                ('blemar15pink', models.CharField(max_length=50)),
                ('ar308black', models.CharField(max_length=50)),
                ('ar308fde', models.CharField(max_length=50)),
                ('ar308od', models.CharField(max_length=50)),
                ('ar308rifle', models.CharField(max_length=50)),
                ('ar308stealth', models.CharField(max_length=50)),
                ('ar308pink', models.CharField(max_length=50)),
                ('blemar308black', models.CharField(max_length=50)),
                ('blemar308fde', models.CharField(max_length=50)),
                ('blemar308od', models.CharField(max_length=50)),
                ('blemar308rifle', models.CharField(max_length=50)),
                ('blemar308stealth', models.CharField(max_length=50)),
                ('blemar308pink', models.CharField(max_length=50)),
                ('tac9black', models.CharField(max_length=50)),
                ('tac9fde', models.CharField(max_length=50)),
                ('tac9od', models.CharField(max_length=50)),
                ('tac9rifle', models.CharField(max_length=50)),
                ('tac9stealth', models.CharField(max_length=50)),
                ('tac9pink', models.CharField(max_length=50)),
                ('blemtac9black', models.CharField(max_length=50)),
                ('blemtac9fde', models.CharField(max_length=50)),
                ('blemtac9od', models.CharField(max_length=50)),
                ('blemtac9rifle', models.CharField(max_length=50)),
                ('blemtac9stealth', models.CharField(max_length=50)),
                ('blemtac9pink', models.CharField(max_length=50)),
                ('black80', models.CharField(max_length=50)),
                ('fde80', models.CharField(max_length=50)),
                ('stealth80', models.CharField(max_length=50)),
                ('rifle80', models.CharField(max_length=50)),
                ('blemblack80', models.CharField(max_length=50)),
                ('blemfde80', models.CharField(max_length=50)),
                ('blemstealth80', models.CharField(max_length=50)),
                ('blemrifle80', models.CharField(max_length=50)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderamount', models.PositiveIntegerField()),
                ('purchase_order_num', models.CharField(default=0, max_length=50)),
                ('supplier', models.CharField(blank=True, max_length=50)),
                ('typemodel', models.CharField(choices=[('AR15', 'AR15'), ('AR308', 'AR308'), ('TAC9', 'TAC9'), ('80', '80'), ('JIGS', 'JIGS'), ('BRASS', 'BRASS'), ('LPK15', 'LPK15'), ('LPK308', 'LPK308'), ('TAC9ARM', 'TAC9ARM'), ('TAC9BUT', 'TAC9BUT'), ('TAC9EJT', 'TAC9EJT')], default='80', max_length=50)),
                ('color', models.CharField(choices=[('BLK', 'BLK'), ('FDE', 'FDE'), ('STEALTH', 'STEALTH'), ('OD', 'OD'), ('RIFLE', 'RIFLE'), ('CLEAR', 'CLEAR'), ('PINK', 'PINK')], default='BLK', max_length=50)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('goodsupplied', models.CharField(max_length=50)),
                ('currentprice', models.CharField(max_length=50)),
                ('note', models.TextField()),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Suppliers',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
