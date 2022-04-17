from django.db import models


# Create your models here.

class Signup_Ahc_Client(models.Model):
    ahc_client_id = models.ImageField(auto_created=True)
    ahc_client_name = models.CharField(max_length=200)
    ahc_client_mobile = models.IntegerField()
    ahc_client_email = models.EmailField()
    ahc_client_password = models.CharField(max_length=100)

    def __str__(self):
        return self.ahc_client_name
