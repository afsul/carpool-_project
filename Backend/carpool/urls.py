
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include("accounts.urls")),
    path("payment",include("payments.urls")),
    path("ride/",include('ride.urls'))
]
   