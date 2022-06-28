from .models import Ride
from .serializers import RideSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


from ride import models


# Create your views here.

#create ride
class Ride(generics.ListCreateAPIView):
    print("Hello entreed to function")
    permission_classes = [IsAuthenticated]
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
