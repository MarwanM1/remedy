from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Listing(models.Model):
    nom = models.CharField(max_length=80)
    prenom = models.CharField(max_length=80)
    email = models.EmailField()
    address_1 = models.CharField(max_length=80)    
    address_2 = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    zip_code = models.CharField(max_length=80)
    nbrpersonnes = models.IntegerField()
    phonenumber = models.CharField(max_length=80)
    profession = models.CharField(max_length=80)
    check_me_out = models.BooleanField()