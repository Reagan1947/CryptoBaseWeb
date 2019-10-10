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


def do_register(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')

        print(user_id)
        print(password)
    return None
