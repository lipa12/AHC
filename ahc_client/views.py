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
from ahc_app.forms import ClientSignUpForm
from ahc_app.models import User
from .models import TradeStrategies, NiftyBanknifty


def index(request):
    strategies_number = TradeStrategies.objects.all()
    return render(request, 'ahc_app/index2.html', {'strategies_number': strategies_number})


class ClientSignUpView(CreateView):
    model = User
    form_class = ClientSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'ahc_client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('loginuser')


def trade_strategies(request,strategies):
    strategies_number = TradeStrategies.objects.all()
    strategies_data = TradeStrategies.objects.filter(strategies=strategies)
    return render(request, 'ahc_app/pages/tables/trades.html', {'strategies_number': strategies_number,'strategies_data':strategies_data})


def nifty_banknifty(request):
    data = NiftyBanknifty.objects.all()
    strategies_number = TradeStrategies.objects.all()
    return render(request, 'ahc_app/pages/tables/trades.html', {'data': data, 'strategies_number': strategies_number})


def client_profile(request):
    strategies_number = TradeStrategies.objects.all()
    profile = User.objects.filter(username = request.user.username)
    return render(request, 'ahc_app/pages/profile/client_profile.html', {'strategies_number': strategies_number, 'profile':profile})


def client_profile_update(request):
    strategies_number = TradeStrategies.objects.all()
    return render(request, 'ahc_app/pages/forms/profile_update.html', {'strategies_number': strategies_number})
