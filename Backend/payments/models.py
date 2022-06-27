
from django.db import models
from accounts.models import User

# Create your models here.



class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    payer = models.CharField(max_length=200)
    payment_id = models.CharField(max_length=200)
    price = models.IntegerField()
    status = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)





