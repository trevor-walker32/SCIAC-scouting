# Generated by Django 2.1.2 on 2018-11-03 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20181102_2106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Position', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='Team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Team'),
        ),
    ]
