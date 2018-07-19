from django import forms

class ChangeForm(forms.Form):
    """
        The Form to change user's information
    """
    username = forms.CharField(label="Identifiant", max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nom d\'utilisateur'}))
    email = forms.CharField(label="Email", max_length=100, widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}))
    password = forms.CharField(label="Mot de passe", max_length=100, widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Mot de passe'}, render_value=True))
    password_conf = forms.CharField(label="Confirmer le mot de passe", max_length=100, widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Mot de passe'}, render_value=True))
    first_name = forms.CharField(label="Prénom", max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Prénom'}))
    last_name = forms.CharField(label="Nom", max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nom'}))

class SendMessageForm(forms.Form):
    """
        The form to send a message to an other user or multiple user
    """
    target = forms.CharField(label="Nom du contact", max_length=200, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nom du contact'}))
    content = forms.CharField(label="Message", max_length=600, widget=forms.Textarea(attrs={'class': 'input', 'placeholder': 'Message...'}))
