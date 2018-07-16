from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from django.contrib.auth import  logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from events.models import Event
from .forms import ChangeForm

# Create your views here.

@login_required
def home_view(request):
    events = request.user.event_set.all()

    event_exist = True if len(events) >= 0 else False

    return render(request, 'members/home.html', locals())

@login_required(login_url='')
def logout_view(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès")
    return HttpResponseRedirect(reverse('index:login'))

@login_required
def change_view(request):
    if request.method == 'POST':
        form = ChangeForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_conf']:
                request.user.username = form.cleaned_data['username']
                if form.cleaned_data['password'] != '******':
                    request.user.password = form.cleaned_data['password']
                request.user.last_name = form.cleaned_data['last_name']
                request.user.first_name = form.cleaned_data['first_name']
                request.user.email = form.cleaned_data['email']

                request.user.save()

                messages.success(request, "Vos informations ont bien été mise à jour")
                return HttpResponseRedirect(reverse('members:home'))
    else:
        form = ChangeForm(initial={
            'username': request.user.username,
            'password': "******",
            'password_conf': "******",
            'last_name': request.user.last_name,
            'first_name': request.user.first_name,
            'email': request.user.email,
        })

    return render(request, 'members/change.html', locals())
        error = False
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                if form.cleaned_data['password'] == form.cleaned_data['password_conf']:
                    user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
                    # login(request, user)
                    messages.success(request, "Votre compte a bien été crée")
                    return HttpResponseRedirect(reverse('members:login'))
                else:
                    error = True
            else:
                error = True
                messages.error(request, "Votre compte n'a pas pu être crée")
        else:
            form = SignupForm()
    
    return render(request, 'members/register.html', locals())

@login_required
def profil_view(request):
    return render(request, 'members/profil.html', locals())
