# Generated by Django 2.1.2 on 2018-11-05 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0024_auto_20181105_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='APP',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='CG',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='GS',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='SV',
            field=models.IntegerField(default=0),
        ),
    ]