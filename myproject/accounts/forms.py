from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_forms.layout import Field

STATES = (
    ('', 'Choisissez...'),
    ('92', 'Haut de Seine'),
    ('75', 'Ile de France '),
    ('44', 'Loire-Atlantique')
)

class SignUpForm(UserCreationForm):
    nom = forms.CharField()
    prenom = forms.CharField(label='Prénom')
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    address_1 = forms.CharField(
        label='Adresse',
        widget=forms.TextInput(attrs={'placeholder': '5, rue des Lilas'})
    )
    address_2 = forms.CharField(
    	label='Complément d\'adresse',
        widget=forms.TextInput(attrs={'placeholder': 'Appartement, N°, Etage, Immeuble'}),
        required=False
    )

    city = forms.CharField(label='Ville')
    state = forms.ChoiceField(label='Département',choices=STATES)
    zip_code = forms.CharField(label='Code Postal')
    nbrpersonnes = forms.IntegerField(label='Nombre de personnes dans votre foyer')
    phonenumber = forms.CharField(label='Téléphone')
    profession = forms.CharField(label='Profession')
    check_me_out = forms.BooleanField(label='Je suis volontaire',required=False)

    class Meta:
        model = User
        fields = ('nom','prenom','username', 'email', 'password1', 'password2','address_1','address_2','city','state','zip_code','nbrpersonnes', 'phonenumber','profession','check_me_out')

# PRODUITS = (
#     ('', 'Choisissez...'),
#     ('1', 'Paquet 1'),
#     ('2', 'Paquet 2'),
#     ('3', 'Paquet 3'),
#     ('4', 'Paquet 4'),
#     ('5', 'Paquet 5'),
#     ('6', 'Paquet 6'),
# )

# QUANTITE = (
#     ('', 'Choisissez...'),
#     ('1', '1'),
#     ('2', '2'),
#     ('3', '3')
# )

# class HomeForm(forms.Form):

#     products = forms.ChoiceField(label='Produits de premières nécessités',choices=PRODUITS)
#     quantity = forms.ChoiceField(label='Quantité',choices=QUANTITE)
#     zip_code = forms.CharField(label='Code Postal')
#     extra_needs = forms.CharField(label='Nombre de personnes dans votre foyer')
#     validate = forms.BooleanField(label='J\'accepte les termes et conditions du contrat',required=True)

#     class Meta:
#         #model = Order
#         fields = ('products','quantity','extra_needs', 'validate')
