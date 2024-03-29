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
from ahc_app.forms import SuperClientSignUpForm
from ahc_super_client.forms import AddClientForm
from ahc_app.models import User
from ahc_client.models import NiftyBanknifty, TradeStrategies


@login_required(login_url="loginuser")
def index(request):
    strategies_number = TradeStrategies.objects.all()
    return render(request, 'ahc_app/index.html', {'strategies_number': strategies_number})


@login_required(login_url="loginuser")
def test(request):
    user = request.user.username
    username = str(user)
    print(username)
    # return render(request, 'ahc_app/pages/forms/add_client.html')
    return render(request, 'ahc_app/index.html')


@login_required(login_url="loginuser")
def add_client(request):
    strategies_number = TradeStrategies.objects.all()
    return render(request, 'ahc_app/pages/forms/add_client.html', {'strategies_number': strategies_number})


@login_required(login_url="loginuser")
def client_list(request):
    user = request.user.username
    client_list = User.objects.filter(super_client_username=user)
    strategies_number = TradeStrategies.objects.all()
    return render(request, 'ahc_app/pages/tables/client_list.html',
                  {'client_list': client_list, 'strategies_number': strategies_number})


@login_required(login_url="loginuser")
def trade(request, strategies):
    data = NiftyBanknifty.objects.filter()[1:]
    strategies_number = TradeStrategies.objects.all()
    strategies_data = TradeStrategies.objects.filter(strategies=strategies)
    return render(request, 'ahc_app/pages/tables/trades.html',
                  {'stock_data': list(data.values()), 'strategies_number': strategies_number,
                   'strategies_data': strategies_data})


@login_required(login_url="loginuser")
def trade_data(request):
    data = NiftyBanknifty.objects.filter()[1:]
    return JsonResponse({'stock_data': list(data.values())})


@login_required(login_url="loginuser")
def super_client_profile(request):
    strategies_number = TradeStrategies.objects.all()
    profile = User.objects.filter(username=request.user.username)
    return render(request, 'ahc_app/pages/profile/super_client_profile.html',
                  {'strategies_number': strategies_number, 'profile': profile})


@login_required(login_url="loginuser")
def super_client_profile_update(request):
    strategies_number = TradeStrategies.objects.all()
    profile = User.objects.filter(username=request.user.username)
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.email = request.POST.get('email')
        user.mobile_number = request.POST.get('mobile_number')

        user.save()

        return redirect('ahc_super_client:index')

    return render(request, 'ahc_app/pages/forms/super_client_profile_update.html',
                  {'strategies_number': strategies_number, 'profile': profile})


@login_required(login_url="loginuser")
def client_profile(request):
    strategies_number = TradeStrategies.objects.all()
    return render(request, 'ahc_app/pages/profile/client_profile.html', {'strategies_number': strategies_number})


@login_required(login_url="loginuser")
def broker_profile(request):
    strategies_number = TradeStrategies.objects.all()
    return render(request, 'ahc_app/pages/profile/broker_profile.html', {'strategies_number': strategies_number})


class SuperClientSignUpView(CreateView):
    model = User
    form_class = SuperClientSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'ahc_super_client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('loginuser')


class AddNewClient(CreateView):
    model = User
    form_class = AddClientForm
    template_name = 'ahc_app/pages/forms/add_client.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'ahc_client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('ahc_super_client:index')


@login_required(login_url="loginuser")
def nifty_banknifty(request):
    data = NiftyBanknifty.objects.all()
    strategies_number = TradeStrategies.objects.all()
    return render(request, 'ahc_app/pages/tables/trades.html', {'data': data, 'strategies_number': strategies_number})
