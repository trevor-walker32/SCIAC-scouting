# Generated by Django 2.1.2 on 2018-11-04 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20181104_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='OPS',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=3),
        ),
        migrations.AddField(
            model_name='team',
            name='OPS',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=3),
        ),
    ]
