from django.shortcuts import render
# Create your views here.
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import JsonResponse
from .model import CustomUser
from django.core.mail import send_mail
from django.conf import settings
import random
import string


# Function for the forgot password (You may need to implement this using Django's built-in password reset functionality)

#@login_required
def user_data(request):
    user = request.user
    data = {
        'username': user.username,
        'email': user.email,
        'phone_number': user.phone_number,
        'user_validation': user.user_validation,
    }
    if request.method == 'POST':
        # Update user data based on POST data
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        user.email = email
        user.phone_number = phone_number
        user.save()
        return JsonResponse({'message': 'User data updated successfully.'})
    else:
        return JsonResponse(data)


def forgot_password(request):
    if request.method == 'POST':
        # Implement your forgot password logic here
        email = request.POST.get('email')
        user = CustomUser.objects.get(email=email)
        if user:
            # Generate a random verification code
            verification_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            user.user_validation_code = verification_code
            user.save()

            # Send an email to the user with the verification code
            subject = 'Forgot Password Verification Code'
            message = f'Your verification code is: {verification_code}'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            return JsonResponse({'message': 'Verification code sent to your email.'})
        else:
            return JsonResponse({'error': 'User not found.'}, status=404)
    else:
        return JsonResponse({'error': 'POST request required.'}, status=400)

# Function for user registration
def signup(request):
    if request.method == 'POST':
        # Implement your user registration logic here
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')

        # Generate a random verification code
        verification_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

        user = CustomUser.objects.create_user(username=username, email=email, phone_number=phone_number, password=password, user_validation_code=verification_code)

        # Send an email to the user with the verification code
        subject = 'Registration Verification Code'
        message = f'Your verification code is: {verification_code}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        return JsonResponse({'message': 'User registered successfully. Please verify your email.'})
    else:
        return render(request, 'signup.html')  # Provide the signup template

# Function for user login
def login(request):
    if request.method == 'POST':
        # Implement your user login logic here
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.user_validation:
                login(request, user)
                return JsonResponse({'message': 'User logged in successfully.'})
            else:
                return JsonResponse({'error': 'Please verify your email first.'}, status=403)
        else:
            return JsonResponse({'error': 'Invalid credentials.'}, status=401)
    else:
        return render(request, 'login.html')  # Provide the login template


