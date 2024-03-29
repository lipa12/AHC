from django.urls import path
from . import views
from .views import AddNewClient

app_name = "ahc_admin"

urlpatterns = [
    path('', views.index, name='index'),
    path('add_client/', AddNewClient.as_view(), name='add_client_form'),
    path('client_list/', views.client_list, name='client_list'),
    path('master_client_list/', views.master_client_list, name='master_client_list'),
    path('trade/<int:strategies>/', views.trade, name='trade'),
    path('profile/', views.admin_profile, name = 'admin_profile'),
    path('client_profile/<int:profile_id>', views.client_profile, name='client_profile'),
    path('master_client_profile/<int:profile_id>', views.master_client_profile, name='master_client_profile'),
    path('save_profile_data/', views.save_profile_data, name='save_profile_data'),
    path('profile_update/<int:profile_id>', views.profile_update, name='profile_update'),
    path('broker_profile/', views.broker_profile, name='broker_profile'),
    path('profile_update/', views.admin_profile_update, name='admin_profile_update'),
    path('trade_data/', views.trade_data, name='trade_data'),
    path('trade_save_data/', views.trade_save_data, name='trade_save_data'),
]
