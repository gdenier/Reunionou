from django import forms

class SigninForm(forms.Form):
    username = forms.CharField(label="Identifiant", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'}))
    password = forms.CharField(label="Mot de passe", max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}))

class SignupForm(forms.Form):
    username = forms.CharField(label="Identifiant", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'}))
    email = forms.CharField(label="Email", max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Adresse email'}))
    password = forms.CharField(label="Mot de passe", max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}))
    password_conf = forms.CharField(label="Confirmation du mot de passe", max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmation du mot de passe'}))
