from . import views
from django.urls import path

urlpatterns = [
       path("create_ride",views.Ride_create.as_view(),name="ride"),
       path("get_rides",views.get_rides,name="get_rides"),
       
    

]   