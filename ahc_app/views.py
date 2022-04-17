from django.shortcuts import render, redirect, get_object_or_404
from .models import *


# Create your views here.

def index(request):
    return render(request, 'ahc_app/pages/forms/client_signup.html')


def dashboard(request):
    return render(request, 'ahc_app/index.html')


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
