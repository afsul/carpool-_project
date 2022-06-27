from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from payments.models import Payment
from accounts.models import User
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def payment(request):

    payment_details = request.data['details']
    print(request.data)
    user = User.objects.get(id=request.user.id)
    name = payment_details['payer']
    payer = payment_details['purchase_units']
    
    full_name = str(name["name"]['given_name']) +  " " +str(name["name"]['surname'])
    price = request.data["price"]

    Payment.objects.create(
         user=user, payer=full_name, payment_id=payment_details['id'], price=price, status=True)

    return Response(status=status.HTTP_201_CREATED)
