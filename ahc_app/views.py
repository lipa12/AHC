from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'ahc_app/index4.html')


def dashboard(request):
    return render(request, 'ahc_app/index.html')


def dashboard2(request):
    return render(request, 'ahc_app/index2.html')

def user_login(request):
    return render(request, 'ahc_app/pages/forms/client_login.html')

def signup(request):
    return render(request, 'ahc_app/pages/forms/client_signup.html')


def ahc_client_signup(request):
    if request.method == 'POST':
        if request.POST.get('ahc_client_name') and request.POST.get('ahc_client_mobile') and request.POST.get(
                'ahc_client_email') and request.POST.get('ahc_client_password'):
            ahc_client_signup = Signup_Ahc_Client()
            ahc_client_signup.ahc_client_name = request.POST.get('ahc_client_name')
            ahc_client_signup.ahc_client_mobile = request.POST.get('ahc_client_mobile')
            ahc_client_signup.ahc_client_email = request.POST.get('ahc_client_email')
            ahc_client_signup.ahc_client_password = request.POST.get('ahc_client_password')

            ahc_client_signup.save()

            return redirect('ahc_app:dashboard')
        else:
            return render(request, 'ahc_app/pages/forms/client_signup.html')


def ahc_client_signin(request):
    if request.method == "POST":
        errors = Signup_Ahc_Client.objects.login_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.add_message(request, messages.ERROR, value, extra_tags='login')
            return redirect('/')
        else:
            user = Signup_Ahc_Client.objects.get(
                ahc_client_email=request.POST['ahc_client_email']) and Signup_Ahc_Client.objects.get(
                ahc_client_password=request.POST['ahc_client_password'])
            request.session['ahc_client_email'] = user.ahc_client_email
            return redirect('ahc_app:dashboard2')
