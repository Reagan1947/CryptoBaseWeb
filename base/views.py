from django.shortcuts import render
from CryptoBaseWeb.registration_center import *


# Create your views here.
def register(request):

    return render(request, 'register.html')


def login(request):
    return None


def init(request):
    register = RegistrationCenter()
    register.initation()
    return render(request, 'register.html')
