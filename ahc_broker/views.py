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
from ahc_app.forms import BrokerSignUpForm
from ahc_app.models import User
from ahc_broker.models import BrokerDetails


@login_required(login_url="loginuser")
def index(request):
    return render(request, 'ahc_app/index3.html')


@login_required(login_url="loginuser")
def broker_profile(request):
    profile = User.objects.filter(username=request.user.username)
    return render(request, 'ahc_app/pages/profile/broker_profile.html', {'profile': profile})


@login_required(login_url="loginuser")
def broker_profile_update(request):
    profile = User.objects.filter(username=request.user.username)
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.email = request.POST.get('email')
        user.mobile_number = request.POST.get('mobile_number')

        user.save()
        return redirect('ahc_broker:index')
    elif request.method == 'POST':
        broker = BrokerDetails.objects.get(username=request.user.username)
        if broker:
            broker.login_id = request.POST.get('loginid')
            broker.password = request.POST.get('password')
            broker.question = request.POST.get('question')
            broker.secret_key = request.POST.get('secretkey')
            broker.secret_id = request.POST.get('secretid')
            broker.save()

            return redirect('ahc_broker:index')
        else:
            broker_details = BrokerDetails()
            broker_details.username = request.user.username
            broker_details.login_id = request.POST.get('loginid')
            broker_details.password = request.POST.get('password')
            broker_details.question = request.POST.get('question')
            broker_details.secret_key = request.POST.get('secretkey')
            broker_details.secret_id = request.POST.get('secretid')
            broker_details.save()

            return redirect('ahc_broker:index')

    return render(request, 'ahc_app/pages/forms/broker_profile_update.html', {'profile': profile})


class BrokerSignUpView(CreateView):
    model = User
    form_class = BrokerSignUpForm
    template_name = './registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'ahc_broker'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('ahc_brker:index')
