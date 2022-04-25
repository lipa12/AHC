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
from ahc_app.models import User


def index(request):
    # return render(request, 'ahc_app/pages/forms/add_client.html')
    return render(request, 'ahc_app/index.html')


def add_client(request):
    return render(request, 'ahc_app/pages/forms/add_client.html')


def client_list(request):
    return render(request, 'ahc_app/pages/tables/client_list.html')


def client_profile(request):
    return render(request, 'ahc_app/pages/profile/client_profile.html')


def broker_profile(request):
    return render(request, 'ahc_app/pages/profile/broker_profile.html')


class SuperClientSignUpView(CreateView):
    model = User
    form_class = SuperClientSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'ahc_super_client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
