from django.forms import ModelForm, Textarea
from django.contrib.admin.widgets import AdminDateWidget
from django.utils.translation import gettext_lazy as _

from .models import Event, Guest

class NewForm(ModelForm):

    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'addresse']
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

class InvitForm(ModelForm):
    class Meta:
        model = Guest
        fields = ['last_name', 'first_name', 'age', 'email', 'password']
