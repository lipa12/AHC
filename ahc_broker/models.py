from django.db import models
from ahc_app .models import User


class BrokerDetails(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    login_id = models.IntegerField()
    password = models.CharField(max_length=50)
    question = models.CharField(max_length=200)
    secret_key = models.CharField(max_length=200)
    secret_id = models.CharField(max_length=200)
