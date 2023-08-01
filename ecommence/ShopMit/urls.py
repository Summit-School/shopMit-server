from django.urls import path
from . import views
urlpatterns = [
    path('index.html/', views.homepage, name='home'),
    path('test/', views.index, name='index'),
]