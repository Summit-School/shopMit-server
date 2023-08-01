from django.urls import path
from . import views
urlpatterns = [
    path('user/', views.user_data, name='user_data'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login')
    ]