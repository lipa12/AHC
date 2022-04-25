from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe


class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_super_client = models.BooleanField(default=False)
    is_broker = models.BooleanField(default=False)


# import re
# import bcrypt
#
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#
#
# # Create your models here.
# class UserManager(models.Manager):
#     def register_validator(self, postData):
#         errors = {}
#         # Validation Rules for First Name
#         if len(postData['first_name']) < 1:
#             errors["first_name"] = "First name is required"
#         elif len(postData['first_name']) < 2:
#             errors["first_name"] = "First name should be at least 2 characters"
#         elif not postData['first_name'].isalpha():
#             errors["first_name"] = "First Name can only have letters"
#
#         # Validation Rules for Last Name
#         if len(postData['last_name']) < 1:
#             errors["last_name"] = "Last name is required"
#         elif len(postData['last_name']) < 2:
#             errors["last_name"] = "Last name should be at least 2 characters"
#         elif not postData['last_name'].isalpha():
#             errors["last_name"] = "Last name can only have letters"
#
#         # Validation Rules for Email
#         if len(postData['ahc_client_email']) < 1:
#             errors["ahc_client_email"] = "Email is required"
#         elif not EMAIL_REGEX.match(postData['ahc_client_email']):
#             errors["ahc_client_email"] = "Invalid Email Address"
#         if Signup_Ahc_Client.objects.filter(ahc_client_email=postData['ahc_client_email']):
#             errors["ahc_client_email"] = "Sorry, email is already in use"
#
#         # Validation Rules for Password
#         if len(postData['ahc_client_password']) < 1:
#             errors["ahc_client_password"] = "Password is required"
#         elif len(postData['ahc_client_password']) < 8:
#             errors["ahc_client_password"] = "Password should be at least 8 characters"
#
#         # Validation Rules for Confirm Password
#         if postData['ahc_client_password'] != postData['confirm_password']:
#             errors["confirm_password"] = "Password and Password Confirmation did not match"
#
#         return errors
#
#     def login_validator(self, postData):
#         errors = {}
#         # Validation Rules for Login Email
#         if len(postData['ahc_client_email']) < 1:
#             errors["ahc_client_email"] = "Email is required"
#         elif not EMAIL_REGEX.match(postData['ahc_client_email']):
#             errors["ahc_client_email"] = "Invalid Email Address"
#         elif not Signup_Ahc_Client.objects.filter(ahc_client_email=postData['ahc_client_email']):
#             errors["ahc_client_email"] = "This account does not exist. Please register."
#
#         # Validation Rules for Login Password
#         if len(postData['ahc_client_password']) < 1:
#             errors["ahc_client_password"] = "Password is required"
#         else:
#             user = Signup_Ahc_Client.objects.get(ahc_client_email=postData['ahc_client_email'])
#             print(user)
#             # if not bcrypt.checkpw(postData['ahc_client_password'].encode(), user.password.encode()):
#             #     errors["ahc_client_password"] = "Password is not correct"
#
#         return errors
#

# class Signup_Ahc_Client(models.Model):
#     ahc_client_id = models.CharField(max_length=200, blank=True)
#     ahc_client_name = models.CharField(max_length=200)
#     ahc_client_mobile = models.IntegerField()
#     ahc_client_email = models.EmailField()
#     ahc_client_password = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.ahc_client_name
#
#     # objects = UserManager()
