import re
from urllib import response
from webbrowser import get
from requests import request

from accounts.models import User
from .models import Ride
from .serializers import GetRiderInfo, RideSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from ride import models
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView

# Create your views here.

# create ride


class Ride_create(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RideSerializer

    def post(self, request):
        user = User.objects.get(id=request.user.id)
        
        create_ride = RideSerializer(data=request.data)
        if create_ride.is_valid():
            create_ride.save(user= user)
            return Response(data = create_ride.data)
        else:
            data = create_ride.errors
            return Response(data)
    
    


        
        



   
  
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_rides(request):
        print("Entered the function=============>")
        print(request.data)
        get_list = Ride.objects.filter(source_city=request.data["source_city"],destination_city=request.data["destination_city"],date=request.data["date"])
        # get_list = Ride.objects.all()
        print(get_list.count())
        serializer_class = GetRiderInfo(get_list, many=True)
        
        return Response(serializer_class.data,status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_rides_object(request,id):
        print("Entered the -----Get function=============>")
        print(request.data)
        get_list = Ride.objects.get(id=id)
        # get_list = Ride.objects.all()
        print(get_list)
        serializer_class = GetRiderInfo(get_list)
        
        return Response(serializer_class.data,status=status.HTTP_200_OK)

