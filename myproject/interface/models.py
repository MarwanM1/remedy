from django.db import models
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_forms.layout import Field
from django import forms
# Create your models here.


PRODUITS = (
    ('', 'Choisissez...'),
    ('1', 'Paquet 1'),
    ('2', 'Paquet 2'),
    ('3', 'Paquet 3'),
    ('4', 'Paquet 4'),
    ('5', 'Paquet 5'),
    ('6', 'Paquet 6'),
)

QUANTITE = (
    ('', 'Choisissez...'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3')
)

class Home(models.Model):
	
    products = models.CharField(choices=PRODUITS, max_length = 1,default='Non défini')
    quantity = models.CharField(choices=QUANTITE, max_length = 1,default='0')
    extra_needs = models.CharField(max_length = 200)
    validate = models.BooleanField()

