# Generated by Django 4.0 on 2022-10-14 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_flight_country_arrival_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='airport',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='airport',
            name='iata',
            field=models.CharField(blank=True, max_length=3, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='airport',
            name='icao',
            field=models.CharField(blank=True, max_length=4, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='airport',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]