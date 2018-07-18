from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.utils.translation import gettext_lazy as _

from .models import Event, Guest, Comment

class NewForm(forms.ModelForm):
    """
        Form to creat or change an event
    """
    class Meta:
        model = Event
        fields = ['title', 'description', 'date']
        widgets = {
            'description': forms.Textarea(attrs={'cols':80, 'rows':20, 'placeholder': 'ceci est la description'}), #tinyMCE
        }
        help_texts = {
            'description': _("Some useful help text"),
        }
        error_messages = {
            'date': {
                'invalid_date': _("This is an invalid date"),
            }
        }

    street = forms.CharField(label="Rue", max_length=80, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nom de la rue'}))
    street_number = forms.IntegerField(label="N° de rue")
    postcode = forms.IntegerField(label="Code postal")
    country = forms.CharField(label="Pays", max_length=20, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Pays'}))
    TYPE_CHOICES = (
        ('rue', u'rue'),
        ('avenur', u'avenue'),
    )
    type_street = forms.MultipleChoiceField(label="type de rue", choices=TYPE_CHOICES)

class InvitForm(forms.ModelForm):
    """
        Form to creat a guest for an event
    """
    class Meta:
        model = Guest
        fields = ['last_name', 'first_name', 'age', 'email', 'password']

class CommentForm(forms.ModelForm):
    """
        Form to write a comment for an event
    """
    class Meta:
        model = Comment
        fields = ['core']