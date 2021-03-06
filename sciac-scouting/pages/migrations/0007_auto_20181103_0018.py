# Generated by Django 2.1.2 on 2018-11-03 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20181102_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='AVG',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='player',
            name='OBP',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='player',
            name='SLG',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=3),
        ),
    ]
