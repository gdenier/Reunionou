from django import forms
from django.contrib.admin.import widgets

from .models import Event

class NewForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'description', 'date', 'start-time')

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget = widget.AdminDateWidget()
        self.fields['start_time'].widget = widgets.AdminTimeWidget()

    # titre = forms.CharField(max_length=256, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre'}))
    # description = forms.CharField(max_length=600, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}))
    # date = 
    # adresse = forms.CharField(max_length=256, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse'}))
