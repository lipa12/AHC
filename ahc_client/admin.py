from django.contrib import admin
from .models import NiftyBanknifty, TradeStrategies, TradePayload

admin.site.register(NiftyBanknifty)
admin.site.register(TradeStrategies)
admin.site.register(TradePayload)
