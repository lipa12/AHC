from django.urls import path
from . import views

app_name = "ahc_client"

urlpatterns = [
    path('', views.index, name='index'),
    path('trade/', views.trade_strategies, name='trade_strategies'),
    ]