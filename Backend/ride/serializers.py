from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from accounts.models import User
from .models import  Ride



class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        exclude = ['user']
        

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'
    
class GetRiderInfo(serializers.ModelSerializer):
    user = UserInfoSerializer()
    class Meta:
        model = Ride
        fields = '__all__'