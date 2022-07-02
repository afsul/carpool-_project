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

    def __str__(self):
        return str(self.source_city) + "  --->  " + str(self.destination_city) 
