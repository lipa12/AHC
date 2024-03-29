"""ahc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from ahc_admin.views import AdminSignUpView
from ahc_app.views import SignUpView
from ahc_broker.views import BrokerSignUpView
from ahc_super_client.views import SuperClientSignUpView,AddNewClient
from ahc_client.views import ClientSignUpView
from ahc_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ahc_app.urls')),
    path('ahc_super_client/', include(('ahc_super_client.urls', 'ahc_super_client'), namespace='ahc_super_client')),
    path('ahc_client/', include(('ahc_client.urls', 'ahc_client'), namespace='ahc_client')),
    path('ahc_broker/', include(('ahc_broker.urls', 'ahc_broker'), namespace='ahc_broker')),
    path('ahc_admin/', include(('ahc_admin.urls', 'ahc_admin'), namespace='ahc_admin')),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/signup/ahc_admin', AdminSignUpView.as_view(), name='ahc_admin_signup'),
    path('accounts/signup/broker/', BrokerSignUpView.as_view(), name='broker_signup'),
    path('accounts/signup/super_client/', SuperClientSignUpView.as_view(), name='super_client_signup'),
    # path('accounts/signup/add_client/', AddNewClient.as_view(), name='add_client_form'),
    path('accounts/signup/client/', ClientSignUpView.as_view(), name='client_signup'),
    # path('', include('ahc_app.urls', LIPSA namespace='ahc_app')),
]
