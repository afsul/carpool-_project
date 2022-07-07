# Generated by Django 4.0.5 on 2022-07-07 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0007_remove_ride_preferences_ride_music_ride_pets_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='companion',
            field=models.ManyToManyField(blank=True, to='ride.ride'),
        ),
        migrations.CreateModel(
            name='Ride_Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='ride.ride')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='ride.ride')),
            ],
        ),
    ]