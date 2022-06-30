from . import views
from django.urls import path

urlpatterns = [
       path("create_ride",views.Ride.as_view(),name="create_ride"),
    

]   