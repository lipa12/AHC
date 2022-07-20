from rest_framework import *
from rest_framework import serializers

from ahc_client.models import TradeStrategies


class PayLoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeStrategies
        fields = ['strategies','symbol','expiry_date','strike_price','ce_pe_fut','mis_nrml','buy_sell']
