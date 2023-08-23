from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
import random
import string
from django.contrib.auth import authenticate
from .model import CustomUser
from rest_framework.permissions import IsAuthenticated
from .serializers import UserDataSerializer, ForgotPasswordSerializer, SignupSerializer, LoginSerializer
from drf_spectacular.utils import extend_schema


class UserData(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(description="View user data and update", responses={200: UserDataSerializer})
    def get(self, request):
        user = request.user
        serializer = UserDataSerializer(user)
        return Response(serializer.data)

    @extend_schema(description="Update user data", responses={200: "User data updated successfully."})
    def post(self, request):
        user = request.user
        serializer = UserDataSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User data updated successfully.'})
        return Response(serializer.errors, status=400)

class ForgotPassword(APIView):
    @extend_schema(description="Request password reset", responses={200: "Verification code sent to your email."})
    def post(self, request):
        email = request.data.get('email')
        user = CustomUser.objects.filter(email=email).first()
        if user:
            verification_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            user.user_validation_code = verification_code
            user.save()

            subject = 'Forgot Password Verification Code'
            message = f'Your verification code is: {verification_code}'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            return Response({'message': 'Verification code sent to your email.'})
        else:
            return Response({'error': 'User not found.'}, status=404)

class Signup(APIView):
    @extend_schema(description="User registration", responses={200: "User registered successfully. Please verify your email."})
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            verification_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            user.user_validation_code = verification_code
            user.save()

            subject = 'Registration Verification Code'
            message = f'Your verification code is: {verification_code}'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            return Response({'message': 'User registered successfully. Please verify your email.'})
        return Response(serializer.errors, status=400)

class Login(APIView):
    @extend_schema(description="User login", responses={200: "User logged in successfully."})
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            if user is not None:
                if user.user_validation:
                    return Response({'message': 'User logged in successfully.'})
                else:
                    return Response({'error': 'Please verify your email first.'}, status=403)
            else:
                return Response({'error': 'Invalid credentials.'}, status=401)
        return Response(serializer.errors, status=400)
