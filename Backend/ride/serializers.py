
from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import  Ride



class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        exclude = ['user']