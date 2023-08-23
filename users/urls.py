from django.urls import path
from .views import *

urlpatterns = [
    path('user-data/', UserData.as_view(), name='user-data'),
    path('forgot-password/', ForgotPassword.as_view(), name='forgot-password'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
]
