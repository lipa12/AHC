from rest_framework import *
from rest_framework import serializers

from ahc_client.models import TradeStrategies, TradePayload


class PayLoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeStrategies
        fields = ['strategies', 'symbol', 'expiry_date', 'strike_price', 'ce_pe_fut', 'mis_nrml', 'buy_sell']


class TradePayloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradePayload
        fields = ['exchange', 'asset', 'transtype', 'symbol', 'orderType', 'productType', 'validity', 'days', 'price',
                  'protection', 'quantity', 'discQuantity', 'trigPrice', 'amo', 'instrument', 'expiryDate',
                  'optionType', 'lotSize', 'strikePrice', 'securitysymbol', 'securityseries', 'userRemarks',
                  'exchangeOrderTime', 'expdatevalue', 'orderaction', 'on', 'con', 'gon', 'dl', 'ltp', 'UDRemarks',
                  'SLOrderPrice', 'SLTriggerPrice', 'ProfitOrderPrice', 'SLJumpPrice', 'LTPJumpPrice', 'BracketOrderID',
                  'BracketOrderNo', 'ModifyTerms', 'MarketProtectionPercentage', 'isBracketOrder', 'exchangeorderno']
