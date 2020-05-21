from django import forms
from .models import Home
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_forms.layout import Field

class HomeForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(HomeForm, self).__init__(*args, **kwargs)
		self.fields['products'].label = 'Produits de premières nécessités'
		self.fields['quantity'].label = 'Quantité'
		self.fields['extra_needs'].label = 'Allergies - Besoins particuliers'
		self.fields['extra_needs'].required = False
		self.fields['validate'].label = 'Accepter les termes et conditions préscrites par Remedy'
		self.fields['validate'].required = True

	class Meta :
		model = Home
		fields = '__all__'

