from django.urls import path
from . import views

app_name = "ahc_client"

urlpatterns = [
    path('', views.index, name='index'),
    path('trade/', views.trade_strategies, name='trade_strategies'),
    path('client_profile/', views.client_profile, name='client_profile'),
    path('client_profile_update/', views.client_profile_update, name='client_profile_update'),
    ]