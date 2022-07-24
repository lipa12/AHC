from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from rest_framework import generics

from ahc_app.models import User

# from django.shortcuts import render, redirect, get_object_or_404
# from .models import *
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import auth
# from django.contrib import messages
# from django.core.exceptions import ObjectDoesNotExist,FieldDoesNotExist
#
#
# # Create your views here.
#
from ahc_app.serializer import PayLoadSerializer, TradePayloadSerializer
from ahc_client.models import TradeStrategies, TradePayload


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_super_client:
            return redirect('super_client/')
        elif request.user.is_ahc_admin:
            return redirect('ahc_admin/')
        elif request.user.is_client:
            return redirect('ahc_client/')
        elif request.user.is_broker:
            return redirect('ahc_broker/')
        else:
            return redirect('loginuser')
    return render(request, 'ahc_app/index4.html')


def index(request):
    return render(request, 'ahc_app/index.html')


def dashboard(request):
    return render(request, 'ahc_app/index.html')


#
#
def dashboard2(request):
    return render(request, 'ahc_app/index2.html')


def dashboard3(request):
    return render(request, 'ahc_app/index3.html')


#
def user_login(request):
    return render(request, 'ahc_app/pages/forms/login-v2.html')


# def user_signup(request):
#     return render(request, 'ahc_app/pages/forms/register-v2.html')
#
#
# def ahc_client_signup(request):
#     if request.method == 'POST':
#         if request.POST.get('ahc_client_name') and request.POST.get('ahc_client_mobile') and request.POST.get(
#                 'ahc_client_email') and request.POST.get('ahc_client_password'):
#             ahc_client_signup = Signup_Ahc_Client()
#             ahc_client_signup.ahc_client_name = request.POST.get('ahc_client_name')
#             ahc_client_signup.ahc_client_mobile = request.POST.get('ahc_client_mobile')
#             ahc_client_signup.ahc_client_email = request.POST.get('ahc_client_email')
#             ahc_client_signup.ahc_client_password = request.POST.get('ahc_client_password')
#
#             ahc_client_signup.save()
#
#             return redirect('ahc_app:dashboard')
#         else:
#             return render(request, 'ahc_app/pages/forms/client_signup.html')
#
#
# def ahc_client_signin(request):
#     if request.method == "POST":
#         errors = Signup_Ahc_Client.objects.login_validator(request.POST)
#         if len(errors):
#             for key, value in errors.items():
#                 messages.add_message(request, messages.ERROR, value, extra_tags='login')
#             return redirect('/')
#         try:
#             user = Signup_Ahc_Client.objects.all()
#             user_email = Signup_Ahc_Client.objects.get(ahc_client_email=request.POST['ahc_client_email'])
#             if user_email:
#                 for user in user:
#                     if user.ahc_client_email == request.POST['ahc_client_email'] and user.ahc_client_password==request.POST['ahc_client_password']:
#                         return redirect('ahc_app:dashboard2')
#                     elif user.ahc_client_email != request.POST['ahc_client_email'] and user.ahc_client_password==request.POST['ahc_client_password']:
#                         return redirect('ahc_app:user_signup')
#                     else:
#                         return redirect('ahc_app:user_login')
#             else:
#                 return redirect('ahc_app:user_signup')
#             # user = Signup_Ahc_Client.objects.filter(
#             #     ahc_client_email=request.POST['ahc_client_email']).first() and Signup_Ahc_Client.objects.filter(
#             #     ahc_client_password=request.POST['ahc_client_password']).first()
#             # request.session['ahc_client_email'] = user.ahc_client_email
#             # return redirect('ahc_app:dashboard2')
#         except user.DoesNotExist :
#             print("error")


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'registration/login.html',
                          {'form': AuthenticationForm(), 'error': 'Username or Password did not match'})
        else:
            login(request, user)
            if request.user.is_authenticated:
                if request.user.is_super_client:
                    return redirect('ahc_super_client:index')
                elif request.user.is_ahc_admin:
                    return redirect('ahc_admin:index')
                elif request.user.is_client:
                    return redirect('ahc_client:index')
                elif request.user.is_broker:
                    return redirect('ahc_broker:index')
                else:
                    return redirect('loginuser')
            return redirect('ahc_app:dashboard')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('loginuser')


def save_data(request):
    if request.method == 'POST':
        trade_startegies = TradeStrategies.objects.create()
        trade_startegies.strategies = request.POST.get('strategies')
        trade_startegies.symbol = request.POST.get('symbol')
        trade_startegies.expiry_date = request.POST.get('expiry_date')
        trade_startegies.strike_price = request.POST.get('strike_price')
        trade_startegies.ce_pe_fut = request.POST.get('ce_pe_fut')
        trade_startegies.mis_nrml = request.POST.get('mis_nrml')
        trade_startegies.buy_sell = request.POST.get('buy_sell')
        trade_startegies.order_quantity = request.POST.get('order_quantity')
        trade_startegies.partial_exit_quantity = request.POST.get('partial_exit_quantity')
        trade_startegies.target = request.POST.get('target')
        trade_startegies.buy_sell_spotprice = request.POST.get('buy_sell_spotprice')
        trade_startegies.stop_loss = request.POST.get('stop_loss')
        trade_startegies.profit_trailing = request.POST.get('profit_trailing')
        trade_startegies.trailing_sl_points = request.POST.get('trailing_sl_points')
        trade_startegies.m_ma_mb = request.POST.get('m_ma_mb')
        trade_startegies.current_sl_position = request.POST.get('current_sl_position')
        trade_startegies.trade_status = request.POST.get('trade_status')
        trade_startegies.executed_price = request.POST.get('executed_price')
        trade_startegies.live_ltp = request.POST.get('live_ltp')
        trade_startegies.vwap = request.POST.get('vwap')
        trade_startegies.mtm = request.POST.get('mtm')
        trade_startegies.iv = request.POST.get('iv')
        trade_startegies.delta = request.POST.get('delta')
        trade_startegies.gamma = request.POST.get('gamma')
        trade_startegies.rho = request.POST.get('rho')
        trade_startegies.theta = request.POST.get('theta')
        trade_startegies.vega = request.POST.get('vega')
        trade_startegies.volume = request.POST.get('volume')
        trade_startegies.lot_size = request.POST.get('lot_size')
        trade_startegies.capital_required_to_buy = request.POST.get('capital_required_to_buy')
        trade_startegies.order_id = request.POST.get('order_id')
        trade_startegies.current_profit_position = request.POST.get('current_profit_position')
        trade_startegies.entry_time = request.POST.get('entry_time')
        trade_startegies.exit_time = request.POST.get('exit_time')

        trade_startegies.save()

        return redirect('AHC_App:index')


class Payload(generics.ListAPIView):
    queryset = TradeStrategies.objects.all()
    serializer_class = PayLoadSerializer


class PayloadTrade(generics.ListAPIView):
    queryset =  TradePayload.objects.all()
    serializer_class = TradePayloadSerializer
