from django import forms

class ChangeForm(forms.Form):
    """
        The Form to change user's information
    """
    username = forms.CharField(label="Identifiant", max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nom d\'utilisateur'}))
    password = forms.CharField(label="Mot de passe", max_length=100, widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Mot de passe'}, render_value=True))
    password_conf = forms.CharField(label="Confirmer le mot de passe", max_length=100, widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Mot de passe'}, render_value=True))
    last_name = forms.CharField(label="Nom", max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nom de famille'}))
    first_name = forms.CharField(label="Prénom", max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Prénom'}))
    email = forms.CharField(label="Email", max_length=100, widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}))
