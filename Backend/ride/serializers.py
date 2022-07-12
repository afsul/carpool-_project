from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from accounts.models import User
from .models import  Ride, Ride_Request



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

class RideRequestSerializers(serializers.ModelSerializer):
    to_user = UserInfoSerializer()
    class Meta:
        model= Ride_Request
        fields = '__all__'
        depth = 2