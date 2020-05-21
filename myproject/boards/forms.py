from django import forms
from .models import Topic
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_forms.layout import Field

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'A quoi pensez-vous?'}
        ),
        max_length=4000,
        help_text='La taille maximale du texte est de 4000 mots.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, label="Name")
    contact_email = forms.EmailField(required=True, label="Email")
    content = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label="Message"
    )

