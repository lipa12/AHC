from django.urls import path
from . import views

app_name = "ahc_app"

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.ahc_client_signup, name='ahc_client_signup'),
]
