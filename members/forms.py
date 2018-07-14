from django import forms

class SigninForm(forms.Form):
    username = forms.CharField(label="Identifiant", max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nom d\'utilisateur'}))
    password = forms.CharField(label="Mot de passe", max_length=100, widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Mot de passe'}))

class SignupForm(forms.Form):
    username = forms.CharField(label="Identifiant", max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nom d\'utilisateur'}))
    # first_name= forms.CharField(label="Prénom", max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Prénom'}))
    # last_name = forms.CharField(label="Nom", max_length=100, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nom'}))
    email = forms.CharField(label="Email", max_length=100, widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Adresse email'}))
    password = forms.CharField(label="Mot de passe", max_length=100, widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Mot de passe'}))
    password_conf = forms.CharField(label="Confirmation du mot de passe", max_length=100, widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Confirmation du mot de passe'}))
