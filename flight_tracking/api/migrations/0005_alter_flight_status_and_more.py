# Generated by Django 4.0 on 2022-10-15 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_airline_country_remove_airport_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='flighttracking',
            name='tracking_status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
