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
from ahc_client.models import NiftyBanknifty
from ahc_super_client.forms import AddClientForm
from ahc_app.models import User


@login_required(login_url="loginuser")
def index(request):
    # return render(request, 'ahc_app/pages/forms/add_client.html')
    return render(request, 'ahc_app/ahc_admin.html')


@login_required(login_url="loginuser")
def admin_profile(request):
    profile = User.objects.filter(username=request.user.username)
    return render(request, 'ahc_app/pages/profile/admin_profile.html', {'profile': profile})


@login_required(login_url="loginuser")
def admin_profile_update(request):
    profile = User.objects.filter(username=request.user.username)
    if request.method == "POST":
        user = User.objects.get(username=request.user.username)
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.email = request.POST.get('email')
        user.mobile_number = request.POST.get('mobile_number')

        user.save()

        return redirect('ahc_admin:index')
    return render(request, 'ahc_app/pages/forms/admin_profile_update.html', {'profile': profile})


@login_required(login_url="loginuser")
def trade_data(request):
    data = NiftyBanknifty.objects.filter()[1:]
    return JsonResponse({'stock_data': list(data.values())})


@login_required(login_url="loginuser")
def add_client(request):
    user = request.user.username
    return render(request, 'ahc_app/pages/forms/add_client.html')


@login_required(login_url="loginuser")
def client_list(request):
    client_list = User.objects.filter(is_client=True)
    return render(request, 'ahc_app/pages/tables/admin_client_list.html', {'client_list': client_list})


@login_required(login_url="loginuser")
def master_client_list(request):
    master_client_list = User.objects.filter(is_super_client=True)
    return render(request, 'ahc_app/pages/tables/master_client_list.html', {'master_client_list': master_client_list})


@login_required(login_url="loginuser")
def trade(request):
    return render(request, 'ahc_app/pages/tables/trades.html')


@login_required(login_url="loginuser")
def client_profile(request, profile_id):
    profile = User.objects.filter(id=profile_id)
    return render(request, 'ahc_app/pages/profile/client_profile.html', {'profile': profile})


@login_required(login_url="loginuser")
def master_client_profile(request, profile_id):
    profile = User.objects.filter(id=profile_id)
    return render(request, 'ahc_app/pages/profile/client_profile.html', {'profile': profile})

@login_required(login_url="loginuser")
def broker_profile(request):
    return render(request, 'ahc_app/pages/profile/broker_profile.html')


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
