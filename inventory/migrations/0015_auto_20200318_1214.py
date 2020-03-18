# Generated by Django 3.0.3 on 2020-03-18 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_auto_20200317_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumables',
            name='tac9button',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='consumables',
            name='AR15_Buffer_Assembly',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='consumables',
            name='AR308_Buffer_Assembly',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='consumables',
            name='AR308kit',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='consumables',
            name='ar15kit',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='consumables',
            name='bigbrass',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='consumables',
            name='drillbits',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='consumables',
            name='jigs',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='consumables',
            name='jigscrew',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='consumables',
            name='littlebrass',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='consumables',
            name='pistolgripscrew',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='consumables',
            name='serialnum',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='consumables',
            name='tac9arm',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='consumables',
            name='tac9ejector',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
