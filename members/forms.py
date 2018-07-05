from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Identifiant", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'}))
    password = forms.CharField(label="Mot de passe", max_length=100, widget=forms.PasswordInput)

class SigninForm(forms.Form):
    username = forms.CharField(label="Identifiant", max_length=100)
    email = forms.CharField(label="Email", max_length=100, widget=forms.EmailInput)
    password = forms.CharField(label="Mot de passe", max_length=100, widget=forms.PasswordInput)