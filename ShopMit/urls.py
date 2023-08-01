from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage),
    path('test/', views.test1, name='index'),
]