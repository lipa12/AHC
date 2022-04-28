from django.db import models


class Broker(models.Model):
    broker_name = models.CharField(max_length=50)
    broker_id = models.CharField(max_length=50)
    login_id = models.IntegerField()
    password = models.CharField(max_length=50)
    question = models.CharField(max_length=200)
    secret_key = models.CharField(max_length=100)
    secret_id = models.CharField(max_length=50)
