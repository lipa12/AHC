from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from ahc_app.decorators import broker_required
from ahc_app.forms import AdminSignUpForm
from ahc_client.models import NiftyBanknifty, TradeStrategies
from ahc_super_client.forms import AddClientForm
from ahc_app.models import User
from rest_framework import generics



@login_required(login_url="loginuser")
def index(request):
    strategies_number = TradeStrategies.objects.all().exclude(strategies=None)
    # return render(request, 'ahc_app/pages/forms/add_client.html')
    return render(request, 'ahc_app/ahc_admin.html', {'strategies_number': strategies_number})


@login_required(login_url="loginuser")
def admin_profile(request):
    profile = User.objects.filter(username=request.user.username)
    strategies_number = TradeStrategies.objects.all().exclude(strategies=None)
    return render(request, 'ahc_app/pages/profile/admin_profile.html',
                  {'profile': profile, 'strategies_number': strategies_number})


@login_required(login_url="loginuser")
def admin_profile_update(request):
    profile = User.objects.filter(username=request.user.username)
    strategies_number = TradeStrategies.objects.all().exclude(strategies=None)
    if request.method == "POST":
        user = User.objects.get(username=request.user.username)
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.email = request.POST.get('email')
        user.mobile_number = request.POST.get('mobile_number')

        user.save()

        return redirect('ahc_admin:index')
    return render(request, 'ahc_app/pages/forms/admin_profile_update.html',
                  {'profile': profile, 'strategies_number': strategies_number})


@login_required(login_url="loginuser")
def trade_data(request):
    data = NiftyBanknifty.objects.filter()[1:]
    return JsonResponse({'stock_data': list(data.values())})


@login_required(login_url="loginuser")
def add_client(request):
    user = request.user.username
    strategies_number = TradeStrategies.objects.all().exclude(strategies=None)
    return render(request, 'ahc_app/pages/forms/add_client.html', {'strategies_number': strategies_number})


@login_required(login_url="loginuser")
def client_list(request):
    client_list = User.objects.filter(is_client=True)
    strategies_number = TradeStrategies.objects.all().exclude(strategies=None)
    return render(request, 'ahc_app/pages/tables/admin_client_list.html',
                  {'client_list': client_list, 'strategies_number': strategies_number})


@login_required(login_url="loginuser")
def master_client_list(request):
    master_client_list = User.objects.filter(is_super_client=True)
    strategies_number = TradeStrategies.objects.all().exclude(strategies=None)
    return render(request, 'ahc_app/pages/tables/master_client_list.html',
                  {'master_client_list': master_client_list, 'strategies_number': strategies_number})


@login_required(login_url="loginuser")
def trade(request, strategies):
    data = NiftyBanknifty.objects.filter()[1:]
    strategies_number = TradeStrategies.objects.all().exclude(strategies=None)
    strategies_data = TradeStrategies.objects.filter(strategies=strategies)
    return render(request, 'ahc_app/pages/tables/trades.html',
                  {'stock_data': list(data.values()), 'strategies_number': strategies_number,
                   'strategies_data': strategies_data})


@login_required(login_url="loginuser")
def client_profile(request, profile_id):
    profile = User.objects.filter(id=profile_id)
    strategies_number = TradeStrategies.objects.all().exclude(strategies=None)
    return render(request, 'ahc_app/pages/profile/profile_details.html',
                  {'profile': profile, 'strategies_number': strategies_number})


@login_required(login_url="loginuser")
def master_client_profile(request, profile_id):
    profile = User.objects.filter(id=profile_id)
    strategies_number = TradeStrategies.objects.all().exclude(strategies=None)
    return render(request, 'ahc_app/pages/profile/profile_details.html',
                  {'profile': profile, 'strategies_number': strategies_number})


def profile_update(request, profile_id):
    profile = User.objects.filter(id=profile_id)
    strategies_number = TradeStrategies.objects.all().exclude(strategies=None)
    return render(request, 'ahc_app/pages/forms/client_profile_update.html',
                  {'profile': profile, 'strategies_number': strategies_number})


def save_profile_data(request):
    if request.method == "POST":
        print(request.POST.get('username'))
        user = User.objects.get(username=request.POST.get('username'))
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.email = request.POST.get('email')
        user.mobile_number = request.POST.get('mobile_number')

        user.save()

        return redirect('ahc_admin:index')


@login_required(login_url="loginuser")
def broker_profile(request):
    strategies_number = TradeStrategies.objects.all().exclude(strategies=None)
    return render(request, 'ahc_app/pages/profile/broker_profile.html', {'strategies_number': strategies_number})


class AddNewClient(CreateView):
    model = User
    form_class = AddClientForm
    template_name = 'ahc_app/pages/forms/add_client.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'ahc_client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('ahc_admin:index')


class AdminSignUpView(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'ahc_admin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('loginuser')


def trade_save_data(request):
    if request.method == 'POST':
        trade_startegies = TradeStrategies.objects.create()
        trade_startegies.strategies = request.POST.get('strategies')
        print(request.POST.get('strategies'))
        trade_startegies.symbol = request.POST.get('symbol')
        print(request.POST.get('symbol'))
        #trade_startegies.expiry_date = request.POST.get('expiry_date')
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
        #trade_startegies.entry_time = request.POST.get('entry_time')
        #trade_startegies.exit_time = request.POST.get('exit_time')

        trade_startegies.save()

        return redirect("/")


