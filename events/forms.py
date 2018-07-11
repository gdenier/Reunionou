from django.forms import ModelForm, Textarea
from django.contrib.admin.widgets import AdminDateWidget
from django.utils.translation import gettext_lazy as _

from .models import Event

class NewForm(ModelForm):

    class Meta:
        model = Event
        fields = ['titre', 'description', 'date', 'adresse']
        widgets = {
            'description': Textarea(attrs={'cols':80, 'rows':20, 'placeholder': 'ceci est la description'}), #faire apparaitre ce bloc de texte avec un editeur genre tinyMCE
        }
        help_texts = {
            'description': _("Some useful help text"),
        }
        error_messages = {
            'date': {
                'invalid_date': _("This is an invalid date"),
            }
        }

