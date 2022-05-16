from django.urls import path
from . import views
from .views import AddNewClient

app_name = "ahc_super_client"

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.super_client_profile, name='super_client_profile'),
    path('profile_update/', views.super_client_profile_update, name='super_client_profile_update'),
    path('add_client/', AddNewClient.as_view(), name='add_client_form'),
    path('client_list/', views.client_list, name='client_list'),
    path('trade/<int:strategies>/', views.trade, name='trade'),
    path('trade_data/', views.trade_data, name='trade_data'),
    path('client_profile/', views.client_profile, name='client_profile'),
    path('broker_profile/', views.broker_profile, name='broker_profile'),
]
