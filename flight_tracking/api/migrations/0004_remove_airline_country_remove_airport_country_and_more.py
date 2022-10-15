# Generated by Django 4.0 on 2022-10-14 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_airport_city_airport_iata_airport_icao_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airline',
            name='country',
        ),
        migrations.RemoveField(
            model_name='airport',
            name='country',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='country',
        ),
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
        migrations.AddField(
            model_name='airline',
            name='country_ip',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='airport',
            name='country_ip',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='country_ip',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]