from django.db import models


class NiftyBanknifty(models.Model):
    nifty_spot = models.FloatField(null=True, blank=True)
    nifty_future = models.FloatField(null=True, blank=True)
    bank_nifty_spot = models.FloatField(null=True, blank=True)
    bank_nifty_future = models.FloatField(null=True, blank=True)
    profit = models.FloatField(null=True, blank=True)
    loss = models.FloatField(null=True, blank=True)
    mtm = models.FloatField(null=True, blank=True)
    vt = models.FloatField(null=True, blank=True)
    lt = models.FloatField(null=True, blank=True)


class TradeStrategies(models.Model):
    strategies = models.IntegerField(null=True, blank=True)
    symbol = models.IntegerField(null=True, blank=True)
    expiry_date = models.DateTimeField(null=True, blank=True)
    strike_price = models.FloatField(null=True, blank=True)
    ce_pe_fut = models.FloatField(null=True, blank=True)
    mis_nrml = models.FloatField(null=True, blank=True)
    buy_sell = models.FloatField(null=True, blank=True)
    order_quantity = models.IntegerField(null=True, blank=True)
    partial_exit_quantity = models.IntegerField(null=True, blank=True)
    target = models.FloatField(null=True, blank=True)
    buy_sell_spotprice = models.FloatField(null=True, blank=True)
    stop_loss = models.FloatField(null=True, blank=True)
    profit_trailing = models.FloatField(null=True, blank=True)
    trailing_sl_points = models.IntegerField(null=True, blank=True)
    m_ma_mb = models.FloatField(null=True, blank=True)
    current_sl_position = models.CharField(max_length=50)
    trade_status = models.CharField(max_length=50)
    executed_price = models.FloatField(null=True, blank=True)
    live_ltp = models.FloatField(null=True, blank=True)
    vwap = models.FloatField(null=True, blank=True)
    mtm = models.FloatField(null=True, blank=True)
    iv = models.FloatField(null=True, blank=True)
    delta = models.FloatField(null=True, blank=True)
    gamma = models.FloatField(null=True, blank=True)
    rho = models.FloatField(null=True, blank=True)
    theta = models.FloatField(null=True, blank=True)
    vega = models.FloatField(null=True, blank=True)
    volume = models.FloatField(null=True, blank=True)
    lot_size = models.FloatField(null=True, blank=True)
    capital_required_to_buy = models.FloatField(null=True, blank=True)
    order_id = models.IntegerField(null=True, blank=True)
    current_profit_position = models.FloatField(null=True, blank=True)
    entry_time = models.DateTimeField(null=True, blank=True)
    exit_time = models.DateTimeField(null=True, blank=True)

    def __int__(self):
        return self.strategies
