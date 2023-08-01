# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def test1(request):
    return HttpResponse("<h1> Server Runing.....")


def homepage(request):
    return render(request, 'index.html')
