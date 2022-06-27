

from .serializers import MyTokenObtainPairSerializer, SignUpSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt




def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class SignupView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save() 
            user =User.objects.get(username = data['username']) #to create a token 
            token = get_tokens_for_user(user)
            response = {
                "message": "User Created Successfully",
                "data": serializer.data,
                "token":token
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    



  
class LoginView(APIView):
    permission_classes = []

    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)
        print(user,'============================')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                response = {"message": "Login Successfull",
                            "token": user.auth_token.key}
                return Response(data=response, status=status.HTTP_200_OK)
            else:
                return Response(data={"message": "Invalid email or password,,,,,,"})
        # if user is not None:

        #     # tokens = create_jwt_pair_for_user(user)

        #     response = {"message": "Login Successfull", "token": user.auth_token.key}
        #     return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(data={"message": "Invalid email or password///////////"})

    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}

        return Response(data=content, status=status.HTTP_200_OK)


class Mytoken_view(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


def otp_send_to_number(num):
    number = str(num)
    user_mobile = "+91" + number
    account_sid = 'AC9ad5789bb469edf6397e6ac8e75824cd'
    auth_token = 'c5c28c0d3203bf5b1521dbac7a42b661'
    client = Client(account_sid, auth_token)
    verification = client.verify.services(
        'VA1a1f91b803dcb3d0015b179ac89b4ed3').verifications.create(to=user_mobile, channel="sms")

    print(verification.status)
    return Response(status=status.HTTP_200_OK)


def otp_verification(otp, numb):
    print(otp, numb, "==============================")
    number = str(numb)
    user_mobile = "+91" + number
    account_sid = 'AC9ad5789bb469edf6397e6ac8e75824cd'
    auth_token = 'c5c28c0d3203bf5b1521dbac7a42b661'
    client = Client(account_sid, auth_token)

    verification_check = client.verify \
        .services('VA1a1f91b803dcb3d0015b179ac89b4ed3') \
        .verification_checks \
        .create(to=user_mobile, code=otp)
    print(verification_check.status)

    # checking otp is valid or not. If valid redirect home
    return Response(status=status.HTTP_200_OK)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def otp_verify(request):
    otp = request.data['otp']
    print(request.user, "=======================")
    user = User.objects.get(id=request.user.id)
    phone = user.phone
    if(otp_verification(otp, phone)):
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def otp_send(request):
    print(request.user)
    user = User.objects.get(id=request.user.id)
    if(otp_send_to_number(user.phone)):
        return Response(status=status.HTTP_201_CREATED)
