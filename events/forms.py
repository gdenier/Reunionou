from django.forms import ModelForm, Textarea
from django.contrib.admin.widgets import AdminDateWidget

from .models import Event

class NewForm(ModelForm):

    class Meta:
        model = Event
        fields = ['titre', 'description', 'date', 'adresse']
        widgets = {
            'description': Textarea(attrs={'cols':80, 'rows':20}),
        }

