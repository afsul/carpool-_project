# Generated by Django 4.0.5 on 2022-07-09 00:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_city', models.CharField(max_length=200)),
                ('destination_city', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('time', models.TimeField(unique=True)),
                ('seat', models.PositiveIntegerField()),
                ('amount', models.PositiveIntegerField()),
                ('smoking', models.BooleanField(default=False)),
                ('pets', models.BooleanField(default=False)),
                ('music', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ride_Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL)),
                ('ride_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ride.ride')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Copassengers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ride.ride_request')),
                ('ride', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ride.ride')),
            ],
        ),
    ]
