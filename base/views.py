from django.shortcuts import render
from CryptoBaseWeb.registration_center import *
from CryptoBaseWeb.mobile_user_register import *
from CryptoBaseWeb.mobile_user_login import *
from CryptoBaseWeb.cloud_service_provider import *
import pickle


# change the object register to register_init
# Create your views here.

def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def do_login(request):
    user_id = ''
    password = ''

    if request.method == "POST":
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
    mobile_login = MobileUserLogin(int(user_id), password)
    data_name_str = 'data' + user_id + '.pkl'
    with open(data_name_str, 'rb') as f:
        smart_car = pickle.load(f)

    log_in_result = mobile_login.log_in(smart_car, 1)

    cloudProvider = CloudServiceProvider()
    PK = smart_car[9]
    au_result = cloudProvider.authentication(log_in_result, 1, register, PK)
    mobile_login.monile_authentiation(au_result, smart_car, 1)
    return None


def init(request):
    global register_init
    register_init = RegistrationCenter()
    register_init.initation()

    return render(request, 'register.html')


def do_register(request):
    user_id = ''
    password = ''

    if request.method == "POST":
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')

    mobile_register = MobileUserRegister(user_id, str(password))
    NBPW_result = mobile_register.NBPW_gen()
    user_id = NBPW_result[0]
    NBPW = NBPW_result[1]
    smart_car_result = register_init.smart_car(user_id, NBPW)
    smart_car = mobile_register.smart_car_save(smart_car_result)

    data_name_str = 'data' + user_id + '.pkl'
    output = open(data_name_str, 'wb')
    pickle.dump(smart_car, output)

    return render(request, 'smart_car.html')
