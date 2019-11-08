# Generated by Django 2.2.6 on 2019-11-07 09:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaving_from', models.CharField(max_length=150)),
                ('going_to', models.CharField(max_length=150)),
                ('total_distance', models.FloatField()),
                ('ride_fair', models.FloatField()),
                ('ride_booked_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('cabs_driver', models.CharField(max_length=150)),
            ],
        ),
    ]
