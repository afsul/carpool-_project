from django.contrib import admin

from .models import Copassengers, Ride
from .models import Ride_Request
# Register your models here.
admin.site.register(Ride)
admin.site.register(Ride_Request)
admin.site.register(Copassengers)
# admin.site.register(Preferences)  