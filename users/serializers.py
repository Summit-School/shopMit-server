from rest_framework import serializers
from .model import CustomUser


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'password')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()



class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'  # Or specify the fields you want to include
