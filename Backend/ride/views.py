from requests import request

from accounts.models import User
from .models import Ride
from .serializers import RideSerializer
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


class Ride(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RideSerializer

    def post(self, request):
        # data = request.data
        user = User.objects.get(id=request.user.id)
        # source_city = data['origin']
        # destination_city = data['destination']
        # date = data['date']
        # time = data['time']
        # seat = data['seat']
        # amount = data['amount']
        # smoking = data['smoking']
        # pets = data['pets']
        # music = data['music'] 
        # print(data, '--------------------------------')

        seri = RideSerializer(data=request.data)
        # print(seri)
        if seri.is_valid():
            seri.save(user= user)
            return Response(data = seri.data)
        else:
            data = seri.errors
            return Response(data)

        # Ride.objects.create(user=user,source_city=str(source_city),destination_city=str(destination_city),date="10-1-1-1",time=time,seat=seat,amount=int(amount))

  
            
