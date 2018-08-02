from django.forms import ModelForm, Textarea
from django.contrib.admin.widgets import AdminDateWidget
from django.utils.translation import gettext_lazy as _

from .models import Event, Guest, Comment

class NewForm(ModelForm):

    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'address']
        widgets = {
            'description': Textarea(attrs={'cols':80, 'rows':20, 'placeholder': 'ceci est la description'}), #tinyMCE
        }
        help_texts = {
            'description': _("Some useful help text"),
        }
        error_messages = {
            'date': {
                'invalid_date': _("This is an invalid date"),
            }
        }

    NATURE_CHOICES = (
        ('1', u'Public'),
        ('0', u'Privé'),
    )
    nature = forms.ChoiceField(label="Nature", choices=NATURE_CHOICES, widget=forms.RadioSelect())
    street = forms.CharField(label="Rue", max_length=80, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nom de la rue'}))
    street_number = forms.IntegerField(label="N° de rue", widget=forms.TextInput(attrs={'class':'input', 'placeholder': 'N° de rue'}))
    postcode = forms.IntegerField(label="Code Postal", widget=forms.TextInput(attrs={'class':'input', 'placeholder': 'Code Postal'}))
    country = forms.CharField(label="Pays", max_length=20, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Pays'}))
    TYPE_CHOICES = (
        ('rue', u'rue'),
        ('avenue', u'avenue'),
    )
    type_street = forms.ChoiceField(label="type de rue", choices=TYPE_CHOICES)

    INVIT_CHOICES = (
        ('1', u'Lancer des invitation'),
        ('0', u'Ne pas lancer d\'invitation'),
    )
    invit = forms.ChoiceField(label="Invitation", choices=INVIT_CHOICES, widget=forms.RadioSelect())

class InvitForm(ModelForm):
  
    class Meta:
        model = Guest
        fields = ['last_name', 'first_name', 'age', 'email', 'password']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['core']