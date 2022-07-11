from django.db import models
from accounts.models import User
# Create your models here.

  

     
class Ride(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    source_city = models.CharField(max_length=200)
    destination_city = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField(unique=True)
    seat = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    smoking = models.BooleanField(default=False)
    pets = models.BooleanField(default=False)
    music = models.BooleanField(default=True) 
    # companion = models.ManyToManyField("User", blank=True)
    

    def __str__(self):
        return str(self.source_city) + "  --->  " + str(self.destination_city) 


class Ride_Request(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE) 
    ride_id = models.ForeignKey(Ride, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.from_user) + "  --->  " + str(self.to_user) 


class Copassengers(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.passenger_name)
