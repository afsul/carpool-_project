# Generated by Django 4.0.5 on 2022-06-27 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0003_alter_ride_seat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferences',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]