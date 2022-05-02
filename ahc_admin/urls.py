from django.urls import path
from . import views
from .views import AddNewClient

app_name = "ahc_admin"

urlpatterns = [
    path('', views.index, name='index'),
    path('add_client/', AddNewClient.as_view(), name='add_client_form'),
    path('client_list/', views.client_list, name='client_list'),
    path('trade/', views.trade, name='trade'),
    path('client_profile/', views.client_profile, name='client_profile'),
    path('broker_profile/', views.broker_profile, name='broker_profile'),
]