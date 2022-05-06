from django.urls import path
from . import views

app_name = "ahc_broker"

urlpatterns = [
    path('', views.index, name='index'),
    path('broker_profile/', views.broker_profile, name='broker_profile'),
]