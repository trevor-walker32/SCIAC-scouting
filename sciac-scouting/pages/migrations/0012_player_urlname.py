# Generated by Django 2.1.2 on 2018-11-04 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_team_urlname'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='urlname',
            field=models.CharField(default='', max_length=50),
        ),
    ]
